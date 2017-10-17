import subprocess, facebook
from ids import *

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu[0]

def save_message(bot, msg):
    flag = 'text'

    if (msg['photo']):
      file = bot.getFile(msg['photo'][-1]['file_id'])
      path = file['file_path']
      subprocess.call(['mkdir', 'message_files/pics'])
      subprocess.call(['wget', path, '-P', 'message_files/pics/'])
      flag = 'pic'

    if ('voice' in msg.keys()):
      file = bot.getFile(msg['voice']['file_id'])
      path = file['file_path']
      subprocess.call(['mkdir', 'message_files/voice'])
      subprocess.call(['wget', path, '-P', 'message_files/voice/'])
      flag = 'voice'

    if ('document' in msg.keys()):
      file = bot.getFile(msg['document']['file_id'])
      path = file['file_path']
      subprocess.call(['mkdir', 'message_files/document'])
      subprocess.call(['wget', path, '-P', 'message_files/document/'])
      flag = 'docu'

    # Post
    # Channel
    graph = facebook.GraphAPI(access_token=facebook_auth_token, version="2.1")

    # chat_id = '@TyteKa_Channel'
    chat_id = -1001103536115
    if (flag == 'text'):
      # On channel
      bot.send_message(chat_id=chat_id, text=msg['text'])
      # On facebook
      graph.put_object(
         parent_object="me",
         connection_name="feed",
         message=msg['text'])
    elif (flag == 'pic'):
      bot.send_photo(chat_id=chat_id, photo=msg['photo'][-1]['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)

      graph.put_photo(image=open('message_files/pics/' + path.split('/')[-1], 'rb'),
                message=msg['caption'] if 'caption' in msg.keys() else 'Post a picture.')
    elif (flag == 'voice'):
      bot.send_voice(chat_id=chat_id, voice=msg['voice']['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)
    elif (flag == 'docu'):
      bot.send_document(chat_id=chat_id, document=msg['document']['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)

    bot.send_message(chat_id=msg['chat']['id'], text='Posted.', reply_to_message_id=msg['message_id'])

