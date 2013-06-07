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
		"jump old": Key("c-o"),
		"up": Key("k"),
		"<n> up": Key("%(n)d, k"),
		"down": Key("j"),
		"<n> down": Key("%(n)d, j"),
		"left": Key("h"),
		"<n> left": Key("%(n)d, h"),
		"right": Key("l"),
		"start of line": Key("caret"),
		"end of line": Key("dollar"),
		"<n> right": Key("%(n)d, l"),
		"line <line>": Key("colon") + Text("%(line)s\n"),

		"search <text>": Key("slash") + Text("%(text)s\n"),
		"back search <text>": Key("question") + Text("%(text)s\n"),
		"next": Key("n"),

		},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 50),
		IntegerRef("line", 1, 10000)
		]
)

gvim_edit_rule = MappingRule(
	name = "gvim_edit",
	mapping = {
		"insert": Key("i"),
		"append": Key("a"),
		"append to line": Key("A"),
		"delete to end (of) line": Key("D"),
		"change word": Key("c,w"),
		"change <n> words": Key("c,%(n)d,w"),
		"change a word": Key("c,a,w"),
		"change inner word": Key("c,i,w"),
		"replace": Key("r"),
		"insert above": Key("O"),
		"insert below": Key("o"),
		"slap": Key("enter"),
		"<text> slap": Text("%(text)s\n"),
		"undo": Key("u"),
		"(Dell | delete)": Key("d"),
		"(Dell | delete) line": Key("d") + Key("d"),
		"yank line": Key("y") + Key("y"),
		"yank to end of line": Key("y") + Key("dollar"),
		"yank": Key("y"),
		"yank down": Key("y,j"),
		"paste": Key("p"),
		"paste above": Key("P"),
		"redo": Key("c-r"),
		"cancel": Key("escape,u"),
		},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 50),
		]
)

gvim_general_rule = MappingRule(
	name = "gvim_general",
	mapping = {
		"okay": Key("escape"),
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
grammar.add_rule(gvim_edit_rule)
grammar.add_rule(gvim_general_rule)
grammar.add_rule(gvim_dragon_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

