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

filename = 'data/part-r-00000'
#filename = 'data/part-r-00001'
#filename = 'data/part-r-00002'
#filename = 'data/part-r-00003'
#filename = 'data/part-r-00004'
#filename = 'data/part-r-00005'
#filename = 'data/part-r-00006'
#filename = 'data/part-r-00007'
#filename = 'data/part-r-00008'
#filename = 'data/part-r-00009'

print(filename)
f = open(filename)
for line in f:
    data = line.split(",")
    if data[0] == '1':
        bot += 1
        bot_action_type[data[3]] +=1
    elif data[0] == '0':
        norm += 1
        norm_action_type[data[3]] +=1
    else:
        print data[0]
f.close()

print 'NORM'
fn = open('action_type3n','w')
fn.write(str(norm) + '\n')
print str(norm)
for t in norm_action_type:
    print t, norm_action_type[t]
    fn.write(' '.join([t, str(norm_action_type[t]), '\n']))
fn.close()


print 'BOT'
fb = open('action_type3b','w')
fb.write(str(bot) + '\n')
print str(bot)
for t in bot_action_type:
    print t, bot_action_type[t]
    fb.write(' '.join([t, str(bot_action_type[t]), '\n']))
fb.close()

