import pickle
serialized_data=input("enter serialized data:")
deserialized_data=pickle.loads(serialized_data.encode('latin1'))