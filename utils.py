import subprocess

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
    flag = -1

    if (msg['photo']):
      file = bot.getFile(msg['photo'][-1]['file_id'])
      path = file['file_path']
      subprocess.call(['mkdir', 'message_files/pics'])
      subprocess.call(['wget', path, '-P', 'message_files/pics/'])
      flag = 0

    if ('voice' in msg.keys()):
      file = bot.getFile(msg['voice']['file_id'])
      path = file['file_path']
      subprocess.call(['mkdir', 'message_files/voice'])
      subprocess.call(['wget', path, '-P', 'message_files/voice/'])
      flag = 1

    if ('document' in msg.keys()):
      file = bot.getFile(msg['document']['file_id'])
      path = file['file_path']
      subprocess.call(['mkdir', 'message_files/document'])
      subprocess.call(['wget', path, '-P', 'message_files/document/'])
      flag = 2

    # Post
    # Channel
    chat_id = '@TyteKa_Channel'
    if (flag == -1):
      bot.send_message(chat_id=chat_id, text=msg['text'])
    elif (flag == 0):
      bot.send_photo(chat_id=chat_id, photo=msg['photo'][-1]['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)
    elif (flag == 1):
      bot.send_voice(chat_id=chat_id, voice=msg['voice']['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)
    elif (flag == 2):
      bot.send_document(chat_id=chat_id, document=msg['document']['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)

    bot.send_message(chat_id=msg['chat']['id'], text='Posted.', reply_to_message_id=msg['message_id'])
