from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

gvim_context = AppContext(executable="gvim")
grammar = Grammar("gvim", context=gvim_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

gvim_navigation_rule = MappingRule(
	name = "gvim_navigation",
	mapping = {
		"jump back": Key("c-b"),
		"jump forward": Key("c-f"),
		"up": Key("k"),
		"<n> up": Key("%(n)d, k"),
		"down": Key("j"),
		"<n> down": Key("%(n)d, j"),
		"line <n>": Key("colon") + Text("%(n)s\n")
		},
	extras = [
		IntegerRef("n", 1, 50)
		]
)

gvim_rule = MappingRule(
	name = "gvim",
	mapping = {
		"(okay | cancel)": Key("escape"),
		"insert": Key("i"),
		"replace": Key("r"),
		"insert above": Key("O"),
		"insert below": Key("o"),
		"slap": Key("enter"),
		"undo": Key("u"),
		"Dell": Key("d"),
		"Dell line": Key("d") + Key("d"),
		"yank line": Key("y") + Key("y"),
		"paste": Key("p"),
		"paste above": Key("P"),
		"redo": Key("c-r"),
		"(save | write) file": Text(":w\n"),
		},
	extras = [
		]
)

gvim_dragon_rule = MappingRule(
	name = "gvim_dragon",
	mapping = {
		"snore": Key("npdiv"),
		},
	extras = [
		]
)



grammar.add_rule(gvim_navigation_rule)
grammar.add_rule(gvim_rule)
grammar.add_rule(gvim_dragon_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

