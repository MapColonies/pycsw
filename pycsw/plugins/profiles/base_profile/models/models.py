from typing import Dict

class ClassDict(object):
    def __getitem__(self, key): 
        return self.__dict__[key]

class Queryable(ClassDict):
    def __init__(self, dbcol: str, xpath: str):
        self.dbcol: str = dbcol
        self.xpath: str = xpath



QueryablesObject = Dict[str, Dict[str, Queryable]]
MappingsObject = Dict[str,Dict[str,str]]

class TypenameModel(ClassDict):
    def __init__(self, outputschema: str, queryables: QueryablesObject, mappings: MappingsObject) -> None:
        self.outputschema = outputschema
        self.queryables = queryables
        self.mappings = mappings



ProfileRepository = Dict[str, TypenameModel]