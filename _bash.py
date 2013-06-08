from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


git_context = AppContext(title="Git Bash")
putty_context = AppContext(executable="putty")
grammar = Grammar("bash", context=(putty_context | git_context) )


general_rule = MappingRule(
	name = "general",
	mapping = {
		"cancel": Key("c-c"),
		"kay": Key("enter"),

		"say <text>": Text("%(text)s"),
		},
	extras = [
		Dictation("text"),
		],
)



file_extensions_rule = MappingRule(
	name = "file extensions",
	mapping = {
		"dot text": Text(".txt"),
		"dot pie": Text(".py"),
		},
	extras = [
		],
)


bash_rule = MappingRule(
	name = "bash",
	mapping = {
		"cancel": Key("c-c"),
		"kay": Key("enter"),

		"CD double dot": Text("cd ..\n"),
		"CD triple dot": Text("cd ../..\n"),
		"CD <text>": Text("cd %(text)s\n"),

		"move": Text("mv "),
		"move <text>": Text("mv %(text)s"),
		"remove": Text("rm "),
		"remove <text>": Text("rm %(text)s"),

		"secure copy": Text("scp"),
		"secure copy <text>": Text("scp %(text)"),

		"change mode": Text("chmod "),

		"exit": Text("exit\n"),

		"list": Text("ls\n"),
		"list minus L.": Text("ls -l\n"),

		"repeat previous argument": Key("a-dot"),
		"up": Key("up"),

		# cursor movement
		"back": Key("a-b"),
		"whiskey": Key("a-f"),

		"delete previous whiskey": Key("c-w"),
		},
	extras = [
		Dictation("text"),
		],
)


git_rule = MappingRule(
	name = "git",
	mapping = {
		# commands for git version control
		"git add": Text("git add "),
		"git add <text>": Text("git add %(text)s"),
		"git remove": Text("git rm "),
		"git remove <text>": Text("git rm %(text)s"),
		"git move": Text("git move "),
		"git move <text>": Text("git mv %(text)s"),
		"git status": Text("git status\n"),
		"git patch": Text("git add -p\n"),

		"git log": Text("git log\n"),

		"git diff": Text("git diff\n"),
		"git diff cache": Text("git diff --cached\n"),

		"git kay": Text("gitk\n"),
		"git kay all": Text("gitk --all\n"),

		"git commit message": Text("git commit -m ''") + Key("left"),
		"git commit": Text("git commit\n"),
		"git commit --amend": Text("git commit --amend\n"),

		"git check out minus F.": Text("git checkout -f\n"),

		"git pull": Text("git pull\n"),

		"git push": Text("git push\n"),
		"git push origin": Text("git push origin\n"),
		"git push tomato": Text("git push tomate\n"),
		"git push all": Text("git push --all\n"),
		"git push github": Text("git push github\n"),
		"git help push": Text("git help push\n"),

		"git remote add": Text("git remote add"),
		"yes": Key("y,enter"),
		"no": Key("n,enter"),
		"quit": Key("q,enter"),
		},
	extras = [
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


grammar.add_rule(general_rule)
grammar.add_rule(file_extensions_rule)
grammar.add_rule(bash_rule)
grammar.add_rule(screen_rule)
grammar.add_rule(git_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

