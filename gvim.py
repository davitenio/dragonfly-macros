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
		"go go": Key("g,g"),
		"big go": Key("G"),
		"go back": Key("c-b"),
		"go (forward | foo)": Key("c-f"),
		"go old": Key("c-o"),

		# cursor navigation
		"up": Key("k"),
		"<n> up": Key("%(n)d, k"),
		"down": Key("j"),
		"<n> down": Key("%(n)d, j"),
		"left": Key("h"),
		"left left": Key("h,h"),
		"<n> left": Key("%(n)d, h"),
		"right": Key("l"),
		"<n> right": Key("%(n)d, l"),


		# line navigation
		"(line | go) <line>": Key("colon") + Text("%(line)s\n"),
		"hat": Key("caret"),
		"dollar": Key("dollar"),


		"Center": Key("z,dot"),


		# searching
		"search <text>": Key("slash") + Text("%(text)s\n"),
		"search this": Key("asterisk"),
		"back search <text>": Key("question") + Text("%(text)s\n"),
		"next": Key("n"),
		"previous": Key("N"),

		# word navigation
		"back": Key("b"),
		"back back": Key("b,b"),
		"back back back": Key("b,b,b"),
		"<n> back": Key("%(n)d,b"),

		"end": Key("e"),
		"end end": Key("e,e"),
		"end end end": Key("e,e,e"),
		"<n> end": Key("%(n)d,e"),

		"woo": Key("w"),
		"woo woo": Key("w,w"),
		"woo woo woo": Key("w,w,w"),
		"<n> woos": Key("%(n)d,w"),
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
		"big oh": Key("O"),
		"oh": Key("o"),

		"substitute": Key("s"),
		"substitute line": Key("S"),

		"append": Key("a"),
		"append <text>": Key("a") + Text("%(text)s"),
		"append to line": Key("A"),
		"change woo": Key("c,w"),
		"change <n> woos": Key("c,%(n)d,w"),
		"<n> change woos": Key("c,%(n)d,w"),
		"change a woo": Key("c,a,w"),
		"change inner woo": Key("c,i,w"),
		"replace": Key("r"),

		"slap": Key("enter"),
		"<text> slap": Text("%(text)s\n"),
		"slap <text>": Text("\n%(text)s"),


		"undo": Key("u"),

		"Dell": Key("d"),
		"Dell up": Key("d,k"),
		"Dell <n> up": Key("d,%(n)d,k"),
		"<n> Dell up": Key("d,%(n)d,k"),
		"Dell down": Key("d,j"),
		"Dell <n> down": Key("d,%(n)d,j"),
		"<n> Dell down": Key("d,%(n)d,j"),
		"Dell Dell": Key("d") + Key("d"),
		"Dell <line>": Key("colon") + Text("%(line)d") + Key("d,enter"),
		"big Dell": Key("D"),
		"Dell woo": Key("d,w"),
		"X.": Key("x"),
		"X. X.": Key("x,x"),
		"X. X. X.": Key("x,x,x"),

		# yanking related stuff
		"big yank": Key("Y"),
		"yank dollar": Key("y") + Key("dollar"),
		"yank": Key("y"),
		"yank down": Key("y,j"),

		"paste": Key("p"),
		"big paste": Key("P"),

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

