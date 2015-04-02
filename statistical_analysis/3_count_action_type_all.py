filename = 'act_type/action_type'

norm_action_type = {'CREATE_DOCUMENT' : 0 , 'GUEST' : 0, 'LINK_CLICK' : 0, 
                    'LIKE' : 0, 'VOTE' : 0, 'DOCUMENT_DELETED' : 0, 'MARK_PHOTO' : 0,
                    'PHOTO_TEXT' : 0, 'RE_SHARE' : 0, 'VIDEO_CALL_INCOMING' : 0,
                    'VIDEO_CALL' : 0, 'VOTE_PHOTO' : 0, 'SEND_PRESENT' : 0, 'PHOTOPIN' : 0}

bot_action_type = {'CREATE_DOCUMENT' : 0 , 'GUEST' : 0, 'LINK_CLICK' : 0, 
                   'LIKE' : 0, 'VOTE' : 0, 'DOCUMENT_DELETED' : 0, 'MARK_PHOTO' : 0,
                   'PHOTO_TEXT' : 0, 'RE_SHARE' : 0, 'VIDEO_CALL_INCOMING' : 0,
                   'VIDEO_CALL' : 0, 'VOTE_PHOTO' : 0, 'SEND_PRESENT' : 0, 'PHOTOPIN' : 0}

norm = 0
bot = 0

for i in range(0,10):
    filename = 'act_type/action_type' + str(i) + 'b'
    f = open(filename)
    data = f.readlines()
    bot += int(data[0])
    for line in data[1:]:
        value = line.split()
        bot_action_type[value[0]] += int(value[1])
    

for i in range(0,10):
    filename = 'act_type/action_type' + str(i) + 'n'
    f = open(filename)
    data = f.readlines()
    norm += int(data[0])
    for line in data[1:]:
        value = line.split()
        norm_action_type[value[0]] += int(value[1])


print 'NORM'
fn = open('action_type_n','w')
fn.write(str(norm) + '\n')
print str(norm)
for t in norm_action_type:
    print t, norm_action_type[t]
    fn.write(' '.join([t, str((norm_action_type[t]*1000000)/norm), '\n']))
fn.close()


print 'BOT'
fb = open('action_type_b','w')
fb.write(str(bot) + '\n')
print str(bot)
for t in bot_action_type:
    print t, bot_action_type[t]
    fb.write(' '.join([t, str((bot_action_type[t]*1000000)/bot), '\n']))
fb.close()

