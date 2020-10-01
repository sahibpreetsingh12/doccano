from doccano_api_client import DoccanoClient
doccano_client = DoccanoClient('http://15.207.89.34','admin','spinnaker')
ls=[]
for i in range(123719,124718):#
	try:
		# ls.append(doccano_client.get_document_detail(1,i)['id'])
		id_= doccano_client.get_document_detail(4,i)['id']
		text=doccano_client.get_document_detail(4,i)['text']

		if text=='Like':
			print(doccano_client.get_document_detail(4,i))
			ls.append(id_)
			doccano_client.delete_document(1,i)
			
	except:
		continue
	# print(doccano_client.get_document_detail(3,i)['id'])
	# if text=='Like':
	# 	ls.append(id_)
	# 	doccano_client.delete_document(3,id_)


	# else:
	# 	continue

	
print(len(ls))