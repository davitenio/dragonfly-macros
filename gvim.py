#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
# Modified by David Gessner
# Contains some code obtained from
# https://github.com/danielgm/JarvisGrammars/blob/master/vim.py

"""
Command-module for cursor movement and **editing**
============================================================================

This module allows the user to control the cursor and 
efficiently perform multiple text editing actions within a 
single phrase.


Example commands
----------------------------------------------------------------------------

*Note the "/" characters in the examples below are simply 
to help the reader see the different parts of each voice 
command.  They are not present in the actual command and 
should not be spoken.*

Example: **"up 4 / down 1 page / home / space 2"**
   This command will move the cursor up 4 lines, down 1 page,
   move to the beginning of the line, and then insert 2 spaces.

Example: **"left 7 words / backspace 3 / insert hello Cap world"**
   This command will move the cursor left 7 words, then delete
   the 3 characters before the cursor, and finally insert
   the text "hello World".

Example: **"home / space 4 / down / 43 times"**
   This command will insert 4 spaces at the beginning of 
   of this and the next 42 lines.  The final "43 times" 
   repeats everything in front of it that many times.


Discussion of this module
----------------------------------------------------------------------------

This command-module creates a powerful voice command for 
editing and cursor movement.  This command's structure can 
be represented by the following simplified language model:

 - *CommandRule* -- top-level rule which the user can say
    - *repetition* -- sequence of actions (name = "sequence")
       - *KeystrokeRule* -- rule that maps a single 
         spoken-form to an action
    - *optional* -- optional specification of repeat count
       - *integer* -- repeat count (name = "n")
       - *literal* -- "times"

The top-level command rule has a callback method which is 
called when this voice command is recognized.  The logic 
within this callback is very simple:

1. Retrieve the sequence of actions from the element with 
   the name "sequence".
2. Retrieve the repeat count from the element with the name
   "n".
3. Execute the actions the specified number of times.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

from dragonfly import *


#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up")

class LetterRule(MappingRule):
	exported = True
	mapping = {
		'alpha': Key('a', static=True),
		'bravo': Key('b', static=True),
		'charlie': Key('c', static=True),
		'dixie': Key('d', static=True),
		'echo': Key('e', static=True),
		'foxtrot': Key('f', static=True),
		'golf': Key('g', static=True),
		'hotel': Key('h', static=True),
		'india': Key('i', static=True),
		'juliet': Key('j', static=True),
		'kilo': Key('k', static=True),
		'lima': Key('l', static=True),
		'mike': Key('m', static=True),
		'november': Key('n', static=True),
		'oscar': Key('o', static=True),
		'papa': Key('p', static=True),
		'quebec': Key('q', static=True),
		'romeo': Key('r', static=True),
		'sierra': Key('s', static=True),
		'tango': Key('t', static=True),
		'uniform': Key('u', static=True),
		'victor': Key('v', static=True),
		'whiskey': Key('w', static=True),
		'x-ray': Key('x', static=True),
		'yankee': Key('y', static=True),
		'zulu': Key('z', static=True),

		'upper alpha': Key('A', static=True),
		'upper bravo': Key('B', static=True),
		'upper charlie': Key('C', static=True),
		'upper dixie': Key('D', static=True),
		'upper echo': Key('E', static=True),
		'upper foxtrot': Key('F', static=True),
		'upper golf': Key('G', static=True),
		'upper hotel': Key('H', static=True),
		'upper india': Key('I', static=True),
		'upper juliet': Key('J', static=True),
		'upper kilo': Key('K', static=True),
		'upper lima': Key('L', static=True),
		'upper mike': Key('M', static=True),
		'upper november': Key('N', static=True),
		'upper oscar': Key('O', static=True),
		'upper papa': Key('P', static=True),
		'upper quebec': Key('Q', static=True),
		'upper romeo': Key('R', static=True),
		'upper sierra': Key('S', static=True),
		'upper tango': Key('T', static=True),
		'upper uniform': Key('U', static=True),
		'upper victor': Key('V', static=True),
		'upper whiskey': Key('W', static=True),
		'upper x-ray': Key('X', static=True),
		'upper yankee': Key('Y', static=True),
		'upper zulu': Key('Z', static=True),

		'0': Key('0'),
		'1': Key('1'),
		'2': Key('2'),
		'3': Key('3'),
		'4': Key('4'),
		'5': Key('5'),
		'6': Key('6'),
		'7': Key('7'),
		'8': Key('8'),
		'9': Key('9'),

		'space': Key('space'),
		'tab': Key('tab'),

		'ampersand': Key('ampersand'),
		'apostrophe': Key('apostrophe'),
		'asterisk': Key('asterisk'),
		'at': Key('at'),
		'backslash': Key('backslash'),
		'backtick': Key('backtick'),
		'bar': Key('bar'),
		'caret': Key('caret'),
		'colon': Key('colon'),
		'comma': Key('comma'),
		'dollar': Key('dollar'),
		'dot': Key('dot'),
		'double quote': Key('dquote'),
		'equal': Key('equal'),
		'exclamation': Key('exclamation'),
		'hash': Key('hash'),
		'hyphen': Key('hyphen'),
		'minus': Key('minus'),
		'percent': Key('percent'),
		'plus': Key('plus'),
		'question': Key('question'),
#'semicolon': Key('semicolon'), # Getting Invalid key name: 'semicolon'
		'slash': Key('slash'),
		'[single] quote': Key('squote'),
		'tilde': Key('tilde'),
		'underscore | score': Key('underscore'),

		'angle left': Key('langle'),
		'brace left': Key('lbrace'),
		'bracket left': Key('lbracket'),
		'paren left': Key('lparen'),
		'angle right': Key('rangle'),
		'brace right': Key('rbrace'),
		'bracket right': Key('rbracket'),
		'paren right': Key('rparen'),
	}

letter = RuleRef(rule=LetterRule(), name='letter')
letter_sequence = Repetition(letter, min=1, max=32, name='letter_sequence')

def executeLetter(letter):
	letter.execute()

def executeLetterSequence(letter_sequence):
	for letter in letter_sequence:
		letter.execute()

def findOnce(letter, n):
	Key('f').execute()
	letter.execute()

def find(letter, n):
	f = Key('f')
	for i in range(n):
		f.execute()
		letter.execute()


#---------------------------------------------------------------------------
# Set up this module's configuration.

# This defines a configuration object with the name "gvim".
config            = Config("gvim")
config.cmd        = Section("Language section")
config.cmd.map    = Item(
    {
	# Spoken-form    ->    ->    ->     Action object

	"[<n>] up":                         Key("k:%(n)d"),
	"[<n>] down":                       Key("j:%(n)d"),
	"[<n>] left":                       Key("h:%(n)d"),
	"[<n>] right":                      Key("l:%(n)d"),
	"go up [<n>]":                    Key("c-b:%(n)d"),
	"go down [<n>]":                  Key("c-f:%(n)d"),
	"up <n> (page | pages)":            Key("pgup:%(n)d"),
	"down <n> (page | pages)":          Key("pgdown:%(n)d"),
	"left <n> (word | words)":          Key("c-left:%(n)d"),
	"right <n> (word | words)":         Key("c-right:%(n)d"),
	"hat":                              Key("caret"),
	"dollar":                           Key("dollar"),
	"match":                          Key("percent"),
	"doc home":                         Key("c-home"),
	"doc end":                          Key("c-end"),

	"visual":                          Key("v"),
	"visual line":                          Key("s-v"),
	"visual block":                          Key("c-v"),

	"next": Key("n"),
	"previous": Key("N"),
	"[<n>] back": Key("b:%(n)d"),
	"[<n>] whiskey": Key("w:%(n)d"),
	"[<n>] end": Key("e:%(n)d"),

	"Center": Key("z,dot"),
	"format": Key("g,q"),

	"a parentheses": Key("a,rparen"),
	"inner parentheses": Key("i,rparen"),

	"inner": Key("i"),
	"a": Key("a"),

	"a paragraph": Key("a,p"),
	"inner paragraph": Key("i,p"),
	"next paragraph": Key("rbrace"),
	"previous paragraph": Key("lbrace"),

	"space [<n>]":                      Key("space:%(n)d"),
	"[<n>] slap":                       Key("enter:%(n)d"),
	"[<n>] tab":                        Key("tab:%(n)d"),
	"[<n>] X.":            	       Key("x:%(n)d"),
	"[<n>] backspace":                  Key("backspace:%(n)d"),

	"kay":                              Key("escape"),

	"oh":                               Key("o"),
	"shift oh":                         Key("O"),

	"cheese":			Key("tilde"),

	"(delete | D.)":                       Key("d"),
	"shift (delete | D.)":                       Key("s-d"),
	"change":                       Key("c"),
	"shift change":                       Key("C"),
	"[<n>] undo":                       Key("u:%(n)d"),
	"[<n>] redo": Key("c-r:%(n)d"),
	"shift insert":                       Key("I"),
	"insert":                       Key("i"),
	"append":                       Key("a"),
	"shift append":                       Key("A"),

	'[<n>] find <letter>': Text('%(n)df') + Function(executeLetter),
	'[<n>] shift find <letter>': Text('%(n)dF') + Function(executeLetter),
	'find [<n>] <letter>': Text('%(n)df') + Function(executeLetter),
	'shift find [<n>] <letter>': Text('%(n)dF') + Function(executeLetter),

	'[<n>] again': Text('%(n)d;'),
	'[<n>] shift again': Text('%(n)d,'),

	'[<n>] until <letter>': Text('%(n)dt') + Function(executeLetter),
	'[<n>] shift until <letter>': Text('%(n)dT') + Function(executeLetter),
	'until [<n>] <letter>': Text('%(n)dt') + Function(executeLetter),
	'shift until [<n>] <letter>': Text('%(n)dT') + Function(executeLetter),

	"yank":                             Key("y"),
	"shift yank":                       Key("Y"),

	"paste":                            Key("p"),
	"shift paste":                      Key("P"),

	"replace":                            Key("r"),
	"shift replace":                      Key("R"),

	# Pete is shorthand for repeat
	"Pete":                      Key("dot"),

	"say <text>":                       release + Text("%(text)s"),
	"mimic <text>":                     release + Mimic(extra="text"),
    },
    namespace={
     "Key":   Key,
     "Text":  Text,
    }
)

# This searches for a file with the same name as this file (gvim.py), but with
# the extension ".py" replaced by ".txt". In other words, it loads the
# configuration specified in the file gvim.txt
namespace = config.load()

#---------------------------------------------------------------------------
# Here we prepare the list of formatting functions from the config file.

# Retrieve text-formatting functions from this module's config file.
#  Each of these functions must have a name that starts with "format_".
format_functions = {}
if namespace:
    for name, function in namespace.items():
     if name.startswith("format_") and callable(function):
        spoken_form = function.__doc__.strip()

        # We wrap generation of the Function action in a function so
        #  that its *function* variable will be local.  Otherwise it
        #  would change during the next iteration of the namespace loop.
        def wrap_function(function):
            def _function(dictation):
                formatted_text = function(dictation)
                Text(formatted_text).execute()
            return Function(_function)

        action = wrap_function(function)
        format_functions[spoken_form] = action


# Here we define the text formatting rule.
# The contents of this rule were built up from the "format_*"
#  functions in this module's config file.
if format_functions:
    class FormatRule(MappingRule):

        mapping  = format_functions
        extras   = [Dictation("dictation")]

else:
    FormatRule = None


#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these 
#  include special elements like the number with name "n" 
#  or the dictation with name "text".  This rule is not 
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when 
#  processing a recognition will be the right side of the 
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html
class KeystrokeRule(MappingRule):

    exported = False

    mapping  = config.cmd.map
    extras   = [
		letter,
		letter_sequence,
                IntegerRef("n", 1, 100),
                Dictation("text"),
                Dictation("text2"),
               ]
    defaults = {
                "n": 1,
               }
    # Note: when processing a recognition, the *value* of 
    #  this rule will be an action object from the right side 
    #  of the mapping given above.  This is default behavior 
    #  of the MappingRule class' value() method.  It also 
    #  substitutes any "%(...)." within the action spec
    #  with the appropriate spoken values.


#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

# First we create an element that references the keystroke rule.
#  Note: when processing a recognition, the *value* of this element
#  will be the value of the referenced rule: an action.
alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
if FormatRule:
    alternatives.append(RuleRef(rule=FormatRule()))
single_action = Alternative(alternatives)

# Second we create a repetition of keystroke elements.
#  This element will match anywhere between 1 and 16 repetitions
#  of the keystroke elements.  Note that we give this element
#  the name "sequence" so that it can be used as an extra in
#  the rule definition below.
# Note: when processing a recognition, the *value* of this element
#  will be a sequence of the contained elements: a sequence of
#  actions.
sequence = Repetition(single_action, min=1, max=16, name="sequence")


#---------------------------------------------------------------------------
# Here we define the top-level rule which the user can say.

# This is the rule that actually handles recognitions. 
#  When a recognition occurs, it's _process_recognition() 
#  method will be called.  It receives information about the 
#  recognition in the "extras" argument: the sequence of 
#  actions and the number of times to repeat them.
class RepeatRule(CompoundRule):

    # Here we define this rule's spoken-form and special elements.
    spec     = "<sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
                sequence,                 # Sequence of actions defined above.
                IntegerRef("n", 1, 100),  # Times to repeat the sequence.
               ]
    defaults = {
                "n": 1,                   # Default repeat count.
               }

    # This method gets called when this rule is recognized.
    # Arguments:
    #  - node -- root node of the recognition parse tree.
    #  - extras -- dict of the "extras" special elements:
    #     . extras["sequence"] gives the sequence of actions.
    #     . extras["n"] gives the repeat count.
    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]   # A sequence of actions.
        count = extras["n"]             # An integer repeat count.
        for i in range(count):
            for action in sequence:
                action.execute()
        release.execute()


#---------------------------------------------------------------------------

gvim_ex_rule = MappingRule(
	name = "gvim_execute",
	mapping = {
		"execute": Text(":"),
		"execute write file": Text(":w\n"),
		"execute edit file": Text(":e "),
		"execute tab edit (file)": Text(":tabe "),
		"execute set ignore case": Text(":set ignorecase\n"),
		},
	extras = [
		Dictation("text"),
		]
)


#---------------------------------------------------------------------------

gvim_window_rule = MappingRule(
	name = "gvim_window",
	mapping = {
		# window navigation commands 
		"window left": Key("c-w,h"),
		"window right": Key("c-w,l"),
		"window up": Key("c-w,k"),
		"window down": Key("c-w,j"),

		# window creation commands
		"window split": Key("c-w,s"),
		"window vertical split": Key("c-w,v"),
		},
	extras = [
		]
)

#---------------------------------------------------------------------------

gvim_tabulator_rule = MappingRule(
	name = "gvim_tabulators",
	mapping = {
		# tabulator navigation commands 
		"tabby next": Key("g,t"),
		"tabby previous": Key("g,T"),
		},
	extras = [
		]
)

#---------------------------------------------------------------------------

gvim_general_rule = MappingRule(
	name = "gvim_general",
	mapping = {
		"cancel": Key("escape,u"),
		},
	extras = [
		]
)

#---------------------------------------------------------------------------

gvim_navigation_rule = MappingRule(
	name = "gvim_navigation",
	mapping = {
		"go first (line)": Key("g,g"),
		"go last (line)": Key("G"),
		"go old": Key("c-o"),
		"go top": Key("s-h"),
		"go middle": Key("s-m"),
		"go low": Key("s-l"),

		# line navigation
		"go <line>": Key("colon") + Text("%(line)s\n"),

		# searching
		"search <text>": Key("slash") + Text("%(text)s\n"),
		"search this": Key("asterisk"),
		"back search <text>": Key("question") + Text("%(text)s\n"),

		},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 50),
		IntegerRef("line", 1, 10000)
		]
)

#---------------------------------------------------------------------------
# Create and load this module's grammar.

gvim_context = AppContext(executable="gvim")
grammar = Grammar("gvim", context=gvim_context)
grammar.add_rule(RepeatRule())
grammar.add_rule(gvim_window_rule)
grammar.add_rule(gvim_tabulator_rule)
grammar.add_rule(gvim_general_rule)
grammar.add_rule(gvim_navigation_rule)
grammar.add_rule(gvim_ex_rule)

grammar.load()                    # Load the grammar.

# Unload function which will be called at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
