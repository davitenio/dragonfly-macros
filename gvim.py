from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


gvim_context = AppContext(executable="gvim")
grammar = Grammar("gvim", context=gvim_context)


gvim_navigation_rule = MappingRule(
	name = "gvim_navigation",
	mapping = {
		"go first (line)": Key("g,g"),
		"go last (line)": Key("G"),
		"go up": Key("c-b"),
		"go down": Key("c-f"),
		"go old": Key("c-o"),
		"go top": Key("s-h"),
		"go middle": Key("s-m"),
		"go low": Key("s-l"),

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
		"shift oh": Key("O"),
		"oh": Key("o"),

		# As in repeat: "re Pete"
		"Pete": Key("dot"),

		"substitute": Key("s"),
		"substitute line": Key("S"),

		# stuff related to appending
		"append": Key("a"),
		"append <text>": Key("a") + Text("%(text)s"),
		"shift append": Key("A"),
		"cha whiskey": Key("c,w"),
		"cha <n> whiskey": Key("c,%(n)d,w"),
		"<n> cha whiskey": Key("c,%(n)d,w"),
		"cha a whiskey": Key("c,a,w"),
		"cha inner whiskey": Key("c,i,w"),
		"cha whiskey <text>": Key("c,w") + Text("%(text)s"),
		"replace": Key("r"),
		"replace <text>": Key("r") + Text("%(text)s"),
		"slap": Key("enter"),
		"slap slap": Key("enter,enter"),
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
		"DD": Key("d,d"),
		"<n> DD": Key("d,%(n)d,d"),
		"delete <line>": Key("colon") + Text("%(line)d") + Key("d,enter"),
		"shift delete": Key("D"),
		"delete a whiskey": Key("d,a,w"),
		"delete whiskey": Key("d,w"),
		"delete end": Key("d,e"),
		"delete a paragraph": Key("d,a,p"),

		"X.": Key("x"),
		"<n> X.": Key("%(n)d,x"),
		"X. X.": Key("x,x"),
		"double X.": Key("x,x"),
		"X. X. X.": Key("x,x,x"),
		"triple X.": Key("x,x,x"),

		# yanking related stuff
		"shift yank": Key("Y"),
		"yank dollar": Key("y") + Key("dollar"),
		"yank": Key("y"),
		"yank down": Key("y,j"),
		"yank up": Key("y,k"),
		"yank a whiskey": Key("y,a,w"),
		"yank a paragraph": Key("y,a,p"),

		"paste": Key("p"),
		"shift paste": Key("P"),

		"redo": Key("c-r"),
		"cancel": Key("escape,u"),
		},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 50),
		IntegerRef("line", 1, 10000)
		]
)



gvim_symbol_names_rule = MappingRule(
	name = "gvim_symbol_names",
	mapping = {
		"D. quote": Key("dquote"),
		"D. quote <text>": Key("dquote") + Text("%(text)s"),
		"S. quote": Key("squote"),
		"S. quote <text>": Key("squote") + Text("%(text)s"),
		"lip": Key("lparen"),
		"lip <text>": Key("lparen") + Text("%(text)s"),
		"rip": Key("rparen"),
		"colon": Key("colon"),
		"langle": Key("langle"),
		"langle <text>": Key("langle") + Text("%(text)s"),
		"rangle": Key("rangle"),
		"lack": Key("lbracket"),
		"lack <text>": Key("lbracket") + Text("%(text)s"),
		"rack": Key("rbracket"),
		"lace": Key("lbrace"),
		"lace <text>": Key("lbrace") + Text("%(text)s"),
		"race": Key("rbrace"),
		},
	extras = [
		Dictation("text"),
		]
)


gvim_ex_rule = MappingRule(
	name = "gvim_execute",
	mapping = {
		"execute write": Text(":w\n"),
		"execute edit": Text(":e "),
		},
	extras = [
		Dictation("text"),
		]
)




gvim_general_rule = MappingRule(
	name = "gvim_general",
	mapping = {
		"kay": Key("escape"),
		"say <text>": Text("%(text)s"),
		},
	extras = [
		Dictation("text"),
		]
)



grammar.add_rule(gvim_navigation_rule)
grammar.add_rule(gvim_edit_rule)
grammar.add_rule(gvim_symbol_names_rule)
grammar.add_rule(gvim_ex_rule)
grammar.add_rule(gvim_general_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

