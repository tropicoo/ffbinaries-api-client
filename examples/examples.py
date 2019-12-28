from ffbinaries import FFBinariesAPIClient

# API client can optionally cache ffbinaries.com json response with defined cache age in seconds.
# By default caching is turned off; Default cache age time is 300 seconds.
client = FFBinariesAPIClient(use_caching=True, cache_age=60)

print(client.get_latest_version())
# '4.2'

print(client.get_latest_metadata())
# {'bin': {'linux-32': {
#     'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-32.zip',
#     'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-32.zip'},
#     'linux-64': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-64.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-64.zip'},
#     'linux-arm64': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-arm-64.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-arm-64.zip'},
#     'linux-armel': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-armel-32.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-armel-32.zip'},
#     'linux-armhf': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-armhf-32.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-armhf-32.zip'},
#     'osx-64': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-osx-64.zip',
#         'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-osx-64.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-osx-64.zip'},
#     'windows-32': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-32.zip',
#         'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-32.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-32.zip'},
#     'windows-64': {
#         'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-64.zip',
#         'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-64.zip',
#         'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-64.zip'}},
#     'permalink': 'http://ffbinaries.com/api/v1/version/4.2',
#     'version': '4.2'}

print(client.get_available_versions())
# ['3.2', '3.3', '3.4', '4.0', '4.1', '4.2']

print(client.get_available_versions_metadata())
# {'versions': {'3.2': 'http://ffbinaries.com/api/v1/version/3.2',
#               '3.3': 'http://ffbinaries.com/api/v1/version/3.3',
#               '3.4': 'http://ffbinaries.com/api/v1/version/3.4',
#               '4.0': 'http://ffbinaries.com/api/v1/version/4.0',
#               '4.1': 'http://ffbinaries.com/api/v1/version/4.1',
#               '4.2': 'http://ffbinaries.com/api/v1/version/4.2',
#               'latest': 'http://ffbinaries.com/api/v1/version/latest'}}

print(client.get_exact_version_metadata('3.3'))
# {'bin': {'linux-32': {
#     'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-32.zip',
#     'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-32.zip',
#     'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-32.zip'},
#          'linux-64': {
#              'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-64.zip',
#              'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-64.zip',
#              'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-64.zip'},
#          'linux-armel': {
#              'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-armel.zip',
#              'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-armel.zip',
#              'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-armel.zip'},
#          'linux-armhf': {
#              'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-armhf.zip',
#              'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-armhf.zip',
#              'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-armhf.zip'},
#          'osx-64': {
#              'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-osx-64.zip',
#              'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffplay-3.3.4-osx-64.zip',
#              'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-osx-64.zip',
#              'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-osx-64.zip'},
#          'windows-32': {
#              'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-win-32.zip',
#              'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffplay-3.3.4-win-32.zip',
#              'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-win-32.zip'},
#          'windows-64': {
#              'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-win-64.zip',
#              'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffplay-3.3.4-win-64.zip',
#              'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-win-64.zip'}},
#  'permalink': 'http://ffbinaries.com/api/v1/version/3.3',
#  'version': '3.3'}

x = client.download_latest_version('ffmpeg', 'windows-64', stream=True)
print(type(x))
# <class 'requests.models.Response'>

x = client.download_exact_version('ffmpeg', '3.3', 'windows-64', stream=True)
print(type(x))
# <class 'requests.models.Response'>

print(client.show_cache())
# {'https://ffbinaries.com/api/v1/version/3.3': (1571426154,
#                                                {'bin': {'linux-32': {
#                                                    'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-32.zip',
#                                                    'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-32.zip',
#                                                    'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-32.zip'},
#                                                         'linux-64': {
#                                                             'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-64.zip',
#                                                             'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-64.zip',
#                                                             'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-64.zip'},
#                                                         'linux-armel': {
#                                                             'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-armel.zip',
#                                                             'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-armel.zip',
#                                                             'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-armel.zip'},
#                                                         'linux-armhf': {
#                                                             'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-linux-armhf.zip',
#                                                             'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-linux-armhf.zip',
#                                                             'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-linux-armhf.zip'},
#                                                         'osx-64': {
#                                                             'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-osx-64.zip',
#                                                             'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffplay-3.3.4-osx-64.zip',
#                                                             'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-osx-64.zip',
#                                                             'ffserver': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffserver-3.3.4-osx-64.zip'},
#                                                         'windows-32': {
#                                                             'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-win-32.zip',
#                                                             'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffplay-3.3.4-win-32.zip',
#                                                             'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-win-32.zip'},
#                                                         'windows-64': {
#                                                             'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffmpeg-3.3.4-win-64.zip',
#                                                             'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffplay-3.3.4-win-64.zip',
#                                                             'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v3.3/ffprobe-3.3.4-win-64.zip'}},
#                                                 'permalink': 'http://ffbinaries.com/api/v1/version/3.3',
#                                                 'version': '3.3'}),
#  'https://ffbinaries.com/api/v1/version/latest': (1571426154,
#                                                   {'bin': {'linux-32': {
#                                                       'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-32.zip',
#                                                       'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-32.zip'},
#                                                            'linux-64': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-64.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-64.zip'},
#                                                            'linux-arm64': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-arm-64.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-arm-64.zip'},
#                                                            'linux-armel': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-armel-32.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-armel-32.zip'},
#                                                            'linux-armhf': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-linux-armhf-32.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-linux-armhf-32.zip'},
#                                                            'osx-64': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-osx-64.zip',
#                                                                'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-osx-64.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-osx-64.zip'},
#                                                            'windows-32': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-32.zip',
#                                                                'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-32.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-32.zip'},
#                                                            'windows-64': {
#                                                                'ffmpeg': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-64.zip',
#                                                                'ffplay': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-64.zip',
#                                                                'ffprobe': 'https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-64.zip'}},
#                                                    'permalink': 'http://ffbinaries.com/api/v1/version/4.2',
#                                                    'version': '4.2'}),
#  'https://ffbinaries.com/api/v1/versions': (1571426154,
#                                             {'versions': {
#                                                 '3.2': 'http://ffbinaries.com/api/v1/version/3.2',
#                                                 '3.3': 'http://ffbinaries.com/api/v1/version/3.3',
#                                                 '3.4': 'http://ffbinaries.com/api/v1/version/3.4',
#                                                 '4.0': 'http://ffbinaries.com/api/v1/version/4.0',
#                                                 '4.1': 'http://ffbinaries.com/api/v1/version/4.1',
#                                                 '4.2': 'http://ffbinaries.com/api/v1/version/4.2',
#                                                 'latest': 'http://ffbinaries.com/api/v1/version/latest'}})}
