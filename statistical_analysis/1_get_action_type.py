action_type = ['CREATE_DOCUMENT', 'GUEST', 'LINK_CLICK', 'LIKE', 'VOTE', 'DOCUMENT_DELETED', 'MARK_PHOTO',  'PHOTO_TEXT',
               'RE_SHARE', 'VIDEO_CALL_INCOMING', 'VIDEO_CALL', 'VOTE_PHOTO', 'SEND_PRESENT', 'PHOTOPIN']
for filename in ['data/part-r-00004', 'data/part-r-00005', 'data/part-r-00006', 'data/part-r-00007', 'data/part-r-00008', 'data/part-r-00009']:
    print(filename)
    f = open(filename)
    for line in f:
        data = line.split(",")
        if data[3] not in action_type:
            action_type.append(data[3])
            print data[3]
    f.close()

f2 = open('action_type','w')
for i in action_type:
    f2.write(i)
    f2.write('\n')
f2.close()

