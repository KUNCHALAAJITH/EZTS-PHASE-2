#disctionary (Forest of 3 trees)
Families={
    'Charley':{'Sam':{'Boxy','Rosy'},
               'nila':{'pepsi'}},
    'devi':{'Tommmy':{'tonny'},
            'Timmy':{'Hamster'},
            'tammy':{'Hamster'}},
    'Charlos':{'Diego':'Cat','Ferret':'Fox'}}
for Parent,Children in Families.items():
    print(f"{Parent} has {len(Children)}kid(s):")
    print(f"{' , and '.join([str(Child) for Child in[*Children]])}")
