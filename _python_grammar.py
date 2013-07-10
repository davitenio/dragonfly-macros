# Author:Brandon Lovrien
# This script is to be used for programming in the Python programming language

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)

class PythonEnabler(CompoundRule):
    spec = "Enable Python"                  # Spoken command to enable the Python grammar.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        pythonBootstrap.disable()
        pythonGrammar.enable()
        print "Python grammar enabled"

class PythonDisabler(CompoundRule):
    spec = "switch language"                  # spoken command to disable the Python grammar.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        pythonGrammar.disable()
        pythonBootstrap.enable()
        print "Python grammar disabled"

# This is a test rule to see if the Python grammar is enabled
class PythonTestRule(CompoundRule):
    spec = "test Python"                  # Spoken form of command.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "Python grammar tested"

# Handles Python commenting syntax
class PythonCommentsSyntax(MappingRule):

    mapping  = {
                "comment":                Text("# "),
                
               
               }


# handles Python control structures
class PythonControlStructures(MappingRule):
    mapping  = {
                    "if":                   Text("if condition:") + Key("enter"),
                    "while loop":           Text("while condition:") + Key("enter"),
                    "for loop":             Text("for something in something:") + Key("enter"),
                    
                    "function":             Text("def functionName():") + Key("enter"),
                    "class":                Text("class className(inheritance):") + Key("enter"),
                    
               
               }    


# The main Python grammar rules are activated here
pythonBootstrap = Grammar("python bootstrap")                
pythonBootstrap.add_rule(PythonEnabler())
pythonBootstrap.load()

pythonGrammar = Grammar("python grammar")
pythonGrammar.add_rule(PythonTestRule())
pythonGrammar.add_rule(PythonCommentsSyntax())
pythonGrammar.add_rule(PythonControlStructures())
pythonGrammar.add_rule(PythonDisabler())
pythonGrammar.load()
pythonGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global pythonGrammar
    if pythonGrammar: pythonGrammar.unload()
    pythonGrammar = None
