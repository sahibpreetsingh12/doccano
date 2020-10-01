from doccano_api_client import DoccanoClient
doccano_client = DoccanoClient('http://15.207.89.34','admin','spinnaker')
import pickle

labels_list=[]
for i in range(len(doccano_client.get_label_list(3))):
	labels_list.append(doccano_client.get_label_list(3)[i]['text'])

print(len(labels_list))


with open("/home/sahib/Downloads/labels_list", "wb") as fp:
    pickle.dump(labels_list, fp)
