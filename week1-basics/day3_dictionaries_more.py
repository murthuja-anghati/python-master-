"""Create ETL Config
Access Nested Values
Update Values
Loop Through Dictionary
Add New Transformation Rule
"""

etl_config = {

  "source" : {
      "type" :  "csv",
       "path" : "/mylocation/raw/users.csv",
       "delimiter" :  ","
  },
  "target" : {
       "type" : "postgres",
      "tableName" : "mySchema.Users",
       "host" : "localhost", 
       "port" :  5314
        

  },
  "transformation" : {
      "trimSpaces" : True,
      "doUpperCase" :  ["name","email"],
       "removeDuplicates" : True
    
  }
}

def accessNestedValues(mydict: dict) ->dict:
    return mydict["source"]["path"]
print(accessNestedValues(etl_config))

def updateNestedValus(mydict:dict)->dict:
      mydict["source"]["path"] = "c:/users/users.csv"
      return mydict
#print(etl_config)
#print(updateNestedValus(etl_config))

def readDict(myDict:dict) ->list:
     for section,values in myDict.items():
          print(f"\n{section.upper()}:")
          for key,value in values.items():
              print(f" {key} : {value}")

#readDict(etl_config)

#Add New Transformation Rule
def addNewTransformationToDict(myDict:dict)->dict:
     myDict["source"]["validate_email"] = True

#readDict (etl_config) 
print(addNewTransformationToDict(etl_config))

