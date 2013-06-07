from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

bash_context = AppContext(executable="putty")
grammar = Grammar("bash", context=bash_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

bash_rule = MappingRule(
	name = "bash",
	mapping = {
		"cancel": Key("c-c"),
		"okay": Key("enter"),

		"CD double dot": Text("cd ..\n"),
		"CD triple dot": Text("cd ../..\n"),
		"CD <text>": Text("cd %(text)s\n"),

		"move <text>": Text("mv %(text)s"),

		"secure copy": Text("scp"),
		"secure copy <text>": Text("scp %(text)"),

		"exit": Text("exit\n"),

		"git status": Text("git status\n"),

		"list": Text("ls\n"),
		"list <text>": Text("ls %(text)s\n"),
		},
	extras = [           # Special elements in the specs of the mapping.
		Dictation("text"),
		],
)

prefix_key = "c-a"

screen_rule = MappingRule(
	name = "screen",
	mapping = {
		"switch to (screen | window) <n>": Key(prefix_key) + Key("%(n)d"),
		"switch to (window next | next window | screen next | next screen)":
			Key(prefix_key) + Key("n"),
		"switch to (window previous | previous window | screen previous | previous screen)":
			Key(prefix_key) + Key("p"),
		"create (screen | window)": Key(prefix_key) + Key("c"),
		},
	extras = [
		IntegerRef("n", 0, 20)
		]
)


grammar.add_rule(bash_rule)
grammar.add_rule(screen_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

