"""1.Clean String
2.ConvertList To set
3.Sum numbers
4.Validate Email
5.Format log message 
"""
def clean_string(text: str) -> str:
    """Trim spaces and convert to lowercase."""
    return text.strip().lower()
print(clean_string("    abc.  "))

def convertToSet(items: list) -> set:
    "Converting list to set"
    return set(items)

print(convertToSet([1,2,2,34,55,6,6,6]))

def sumNumber(a:int,b:int) -> int:
    return a+b 
print("adding values of :  ", sumNumber(20,30))

def validateEmail(text:str) ->bool:
    return "@"  and "." in text 
print("validating the email ...",validateEmail("murthuja@gmailcom"))

def formatLog(message:str,level:str="INFO") -> str:
    return f"[{level}] - {message}"
print("logging of message... ",formatLog("this is my first logger..."))
    