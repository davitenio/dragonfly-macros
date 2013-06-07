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
		"go first": Key("g,g"),
		"go last": Key("G"),
		"go up": Key("c-b"),
		"go down": Key("c-f"),
		"go old": Key("c-o"),

		# cursor navigation
		"up": Key("k"),
		"up up": Key("k,k"),
		"up up up": Key("k,k,k"),
		"<n> up": Key("%(n)d, k"),
		"down": Key("j"),
		"down down": Key("j,j"),
		"down down down": Key("j,j,j"),
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
		"double back": Key("b,b"),
		"back back back": Key("b,b,b"),
		"triple back": Key("b,b,b"),
		"<n> back": Key("%(n)d,b"),

		"end": Key("e"),
		"end end": Key("e,e"),
		"double end": Key("e,e"),
		"end end end": Key("e,e,e"),
		"triple end": Key("e,e,e"),
		"<n> end": Key("%(n)d,e"),

		"whiskey": Key("w"),
		"whiskey whiskey": Key("w,w"),
		"double whiskey": Key("w,w"),
		"whiskey whiskey whiskey": Key("w,w,w"),
		"triple whiskey": Key("w,w,w"),
		"<n> whiskey": Key("%(n)d,w"),
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

		# As in repeat: "re Pete"
		"Pete": Key("dot"),

		"substitute": Key("s"),
		"substitute line": Key("S"),

		# stuff related to appending
		"append": Key("a"),
		"append <text>": Key("a") + Text("%(text)s"),
		"big append": Key("A"),
		"cha whiskey": Key("c,w"),
		"cha <n> whiskey": Key("c,%(n)d,w"),
		"<n> cha whiskey": Key("c,%(n)d,w"),
		"cha a whiskey": Key("c,a,w"),
		"cha inner whiskey": Key("c,i,w"),
		"cha whiskey <text>": Key("c,w") + Text("%(text)s"),
		"replace": Key("r"),
		"replace <text>": Key("r") + Text("%(text)s"),
		"slap": Key("enter"),
		"<text> slap": Text("%(text)s\n"),
		"slap <text>": Text("\n%(text)s"),


		"undo": Key("u"),

		"delete": Key("d"),
		"delete up": Key("d,k"),
		"delete <n> up": Key("d,%(n)d,k"),
		"<n> delete up": Key("d,%(n)d,k"),
		"delete down": Key("d,j"),
		"delete <n> down": Key("d,%(n)d,j"),
		"<n> delete down": Key("d,%(n)d,j"),
		"(delete delete | DD)": Key("d") + Key("d"),
		"delete <line>": Key("colon") + Text("%(line)d") + Key("d,enter"),
		"big delete": Key("D"),
		"delete a whiskey": Key("d,a,w"),
		"delete whiskey": Key("d,w"),
		"delete end": Key("d,e"),
		"X.": Key("x"),
		"<n> X.": Key("%(n)d,x"),
		"X. X.": Key("x,x"),
		"double X.": Key("x,x"),
		"X. X. X.": Key("x,x,x"),
		"triple X.": Key("x,x,x"),

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
		"kay": Key("escape"),
		"write file": Text(":w\n"),
		"say <text>": Text("%(text)s"),
		},
	extras = [
		Dictation("text"),
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

