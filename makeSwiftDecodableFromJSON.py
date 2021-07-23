import ast

def findTypeInBrackets(bracket, iterations=1):
    if isinstance(bracket[0], str):
        valType = ""
        for i in range(0,iterations):
            valType+=valType + "["
            
        valType+="String"
        for i in range(0,iterations):
            valType+=valType + "]"
        return valType
    if isinstance(bracket[0], int):
        valType = ""
        for i in range(0,iterations):
            valType+=valType + "["
            
        valType+="Int"
        for i in range(0,iterations):
            valType+=valType + "]"
        return valType
    if isinstance(bracket[0], bool):
        valType = ""
        for i in range(0,iterations):
            valType+=valType + "["
            
        valType+="Bool"
        for i in range(0,iterations):
            valType+=valType + "]"
        return valType
    if isinstance(bracket[0], float):
        valType = ""
        for i in range(0,iterations):
            valType+=valType + "["
            
        valType+="Double"
        for i in range(0,iterations):
            valType+=valType + "]"
        return valType
    if isinstance(bracket[0], list):
        iterations+=1
        findTypeInBrackets(bracket[0],iterations)
    '''
    if isinstance(val, dict):
        dict_dict[key] = val
        valType = f"{key}"
    '''
    
    

def makeSwiftDecodableFromJSON(json,struct_name):
    '''This function takes a string of a JSON dictionary and 
    converts it to a decodable struct that can be used in mobile
    apps that are built from Swift'''
    
    
    
    print(f"struct {struct_name}: Decodable", end ="" )
    print("{")
    print()
    
    
    json = json.replace("null","None")
    json = json.replace("false","False")
    json = json.replace("true","True")
    json = ast.literal_eval(json)
    dict_dict = {}
    #null = None
    #false = False
    #true = True
    for key in json.keys():
        val = json[key]
        valType=""
        if isinstance(val, str):
            valType = "String"
        if isinstance(val, bool):
            valType = "Bool"
        if isinstance(val, type(None)):
            continue
        if isinstance(val, int):
            valType = "Int"
        if isinstance(val, float):
            valType = "Double"
        if isinstance(val, list):
            valType = findTypeInBrackets(val)
        if isinstance(val, dict):
            dict_dict[key] = val
            valType = f"{key}"

        print(f"    public let {key}: {valType}?")
    

    print()
    print()
    print("    private enum CodingKeys: String, CodingKey {")
    print()
    
    for key in json.keys():
        print(f"        case {key} =  \"{key}\"")
        
        
    print("    }") 
    print("}")    
    print()
    
    for key in dict_dict.keys():
        makeSwiftDecodableFromJSON(f'{dict_dict[key]}', key)
        

json = '{"string information":"string","int information":0,"float information":0.0,"bool information":true,"list information":["string 1", "string 2"]}'
makeSwiftDecodableFromJSON(json, "InformationPreview")

'''
OUTPUT:

struct InformationPreview: Decodable{

    public let string information: String?
    public let int information: Int?
    public let float information: Double?
    public let bool information: Int?
    public let list information: [String]?


    private enum CodingKeys: String, CodingKey {

        case string information =  "string information"
        case int information =  "int information"
        case float information =  "float information"
        case bool information =  "bool information"
        case list information =  "list information"
    }
}
'''
