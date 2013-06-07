from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


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
		"jump (forward | foo)": Key("c-f"),
		"jump old": Key("c-o"),

		# cursor navigation
		"up": Key("k"),
		"<n> up": Key("%(n)d, k"),
		"down": Key("j"),
		"<n> down": Key("%(n)d, j"),
		"left": Key("h"),
		"<n> left": Key("%(n)d, h"),
		"right": Key("l"),
		"<n> right": Key("%(n)d, l"),


		# line navigation
		"(line | go) <line>": Key("colon") + Text("%(line)s\n"),
		"start of line": Key("caret"),
		"end of line": Key("dollar"),


		"Center": Key("z,dot"),


		"search <text>": Key("slash") + Text("%(text)s\n"),
		"search this": Key("asterisk"),
		"back search <text>": Key("question") + Text("%(text)s\n"),
		"next": Key("n"),
		"previous": Key("N"),

		"back": Key("b"),
		"back back": Key("b,b"),
		"back back back": Key("b,b,b"),
		"<n> back": Key("%(n)d,b"),

		"end": Key("e"),
		"end end": Key("e,e"),
		"end end end": Key("e,e,e"),
		"<n> end": Key("%(n)d,e"),

		"word": Key("w"),
		"word word": Key("w,w"),
		"word word word": Key("w,w,w"),
		"<n> words": Key("%(n)d,w"),
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
		"insert <text>": Key("i") + Text("%(text)s"),
		"insert above": Key("O"),
		"insert below": Key("o"),

		"substitute": Key("s"),
		"substitute line": Key("S"),
		"append": Key("a"),
		"append to line": Key("A"),
		"change word": Key("c,w"),
		"change <n> words": Key("c,%(n)d,w"),
		"change a word": Key("c,a,w"),
		"change inner word": Key("c,i,w"),
		"replace": Key("r"),

		"slap": Key("enter"),
		"<text> slap": Text("%(text)s\n"),
		"slap <text>": Text("\n%(text)s"),


		"undo": Key("u"),

		"Dell": Key("d"),
		"Dell up": Key("d,k"),
		"Dell <n> up": Key("d,%(n)d,k"),
		"Dell down": Key("d,j"),
		"Dell <n> down": Key("d,%(n)d,j"),
		"Dell line": Key("d") + Key("d"),
		"Dell line <line>": Key("colon") + Text("%(line)d") + Key("d,enter"),
		"Dell to end (of) line": Key("D"),
		"Dell word": Key("d,w"),
		"X.": Key("x"),

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
		IntegerRef("line", 1, 10000)
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

