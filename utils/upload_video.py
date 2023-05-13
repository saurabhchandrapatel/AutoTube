import httplib2
import os
import random
import sys
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from yt_config import *
 
class UploadVedioBase(object):
  ...

class UploadVedio(UploadVedioBase):
  def __init__(self):
    ...

  def get_authenticated_service(self, args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
      scope=YOUTUBE_UPLOAD_SCOPE,
      message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage(os.path.join(CURRENT_DIR, "%s-oauth2.json" % sys.argv[0]) )
    credentials = storage.get()

    if credentials is None or credentials.invalid:
      credentials = run_flow(flow, storage, args)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      http=credentials.authorize(httplib2.Http()))

  def initialize_upload(self,youtube, options):
    tags = None
    #if options['keywords']:
    #  tags = options['keywords'].split(",")

    body=dict(
      snippet=dict(
        title=options['title'],
        description=options['description'],
      ),
      status=dict(
        privacyStatus=options['privacyStatus']
      )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
      part=",".join(body.keys()),
      body=body,
      media_body=MediaFileUpload(options['file'], chunksize=-1, resumable=True)
    )
    return self.resumable_upload(insert_request)

  def resumable_upload(self,insert_request):
    response = None
    error = None
    retry = 0
    response_id = None
    while response is None:
      try:
        print("Uploading file...")
        status, response = insert_request.next_chunk()
        if response is not None:
          if 'id' in response:
            print("Video id '%s' was successfully uploaded." % response['id'])
            response_id = response['id']
          else:
            exit("The upload failed with an unexpected response: %s" % response)
      except HttpError as e:
        if e.resp.status in RETRIABLE_STATUS_CODES:
          error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                               e.content)
        else:
          raise
      except RETRIABLE_EXCEPTIONS as e:
        error = "A retriable error occurred: %s" % e

      if error is not None:
        print(error)
        retry += 1
        if retry > MAX_RETRIES:
          exit("No longer attempting to retry.")

        max_sleep = 2 ** retry
        sleep_seconds = random.random() * max_sleep
        print("Sleeping %f seconds and then retrying..." % sleep_seconds)
        time.sleep(sleep_seconds)
        return None
      else:
        return response_id

  def upload(self,video_data): 
    args = argparser.parse_args()
    if not os.path.exists(video_data['file']):
      exit("Please specify a valid file using the --file= parameter.")

    youtube = self.get_authenticated_service(args)
    try:
      return self.initialize_upload(youtube, video_data)
    except HttpError as e:
      print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
      return None