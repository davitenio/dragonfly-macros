from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)


git_context = AppContext(title="git Bash")
git_context2 = AppContext(title="MINGW32:")
putty_context = AppContext(executable="putty")
grammar = Grammar("bash", context=(putty_context | git_context | git_context2))


general_rule = MappingRule(
	name = "general",
	mapping = {
		"cancel": Key("c-c"),
		"kay": Key("enter"),
		"left": Key("left"),
		"right": Key("right"),

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
		"P. W. D.": Text("pwd\n"),

		"CD dot dot": Text("cd ..\n"),
		"CD double dot": Text("cd ..\n"),
		"CD triple dot": Text("cd ../..\n"),
		"CD ": Text("cd "),
		"CD <text>": Text("cd %(text)s"),

		"copy": Text("cp "),
		"copy <text>": Text("cp %(text)s"),

		"make directory ": Text("mkdir "),
		"make directory <text>": Text("mkdir %(text)s\n"),

		"move": Text("mv "),
		"move <text>": Text("mv %(text)s"),
		"remove": Text("rm "),
		"remove <text>": Text("rm %(text)s"),

		"secure copy": Text("scp"),
		"secure copy <text>": Text("scp %(text)"),

		"change mode": Text("chmod "),

		"grep <text>": Text("grep %(text)s"),

		"cat": Text("cat "),
		"cat <text>": Text("cat %(text)s"),
		"exit": Text("exit\n"),

		"list": Text("ls\n"),
		"list <text>": Text("ls %(text)s"),
		"list minus L.": Text("ls -l\n"),
		"list minus one": Text("ls -1 "),

		"pipe": Text(" | "),

		"D. P. K. G. ": Text("dpkg "),
		"D. P. K. G. minus L.": Text("dpkg -l "),
		"D. P. K. G. minus I.": Text("dpkg -i "),

		"manual page": Text("man "),

		"word count": Text("wc "),
		"word count minus L.": Text("wc -l "),

		"repeat previous argument": Key("a-dot"),
		"up": Key("up"),

		# cursor movement
		"back": Key("a-b"),
		"[<n>] back": Key("a-b:%(n)d"),
		"[<n>] whiskey": Key("a-f:%(n)d"),
		"dollar": Key("c-e"),
		"hat": Key("c-a"),

		"delete whiskey": Key("c-w"),
		"[<n>] delete whiskey": Key("c-w:%(n)d"),
		"paste": Key("c-y"),

		"make": Text("make\n"),
		"make clean": Text("make clean\n"),

		"evince": Text("evince "),
		"evince <text>": Text("evince %(text)s"),

		"aptitude search": Text("aptitude search "),
		"pseudo-aptitude install": Text("sudo aptitude install "),
		"pseudo-aptitude update": Text("sudo aptitude update "),
		"pseudo-aptitude remove": Text("sudo aptitude remove "),

		"A. P. T. file search": Text("apt-file search "),

		"vim": Text("vim "),
		"vim <text>": Text("vim %(text)s"),


		"W. get ": Text("wget "),
		},
	extras = [
		Dictation("text"),
		IntegerRef("n", 0, 20)
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
		"git log minus P.": Text("git log -p\n"),
		"git log minus stat": Text("git log --stat\n"),

		"git diff": Text("git diff\n"),
		"git diff cache": Text("git diff --cached\n"),

		"git kay": Text("gitk\n"),
		"git kay all": Text("gitk --all\n"),

		"git commit message": Text("git commit -m ''") + Key("left"),
		"git commit": Text("git commit "),
		"git commit --amend": Text("git commit --amend\n"),

		"git check out": Text("git checkout "),
		"git check out <text>": Text("git checkout %(text)s"),
		"git check out minus F.": Text("git checkout -f\n"),

		"git stash": Text("git stash\n"),

		"git pull": Text("git pull\n"),

		"git push": Text("git push\n"),
		"git push drop box": Text("git push dropbox\n"),
		"git push origin": Text("git push origin\n"),
		"git push tomato": Text("git push tomate\n"),
		"git push all": Text("git push --all\n"),
		"git push github": Text("git push github\n"),
		"git help": Text("git help"),
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

