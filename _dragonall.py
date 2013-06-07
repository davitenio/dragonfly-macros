from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


grammar = Grammar("dragon")


dragon_rule = MappingRule(
	name = "dragon",
	mapping = {
		"snore": Key("npdiv"),
		},
	extras = [
		]
)



grammar.add_rule(dragon_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

