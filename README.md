# HTML BeautifySoup v1.1
## SublimeText (version 2 & 3)
- by Le Dang Duong
- 12 Aug 2014
- url:			[https://github.com/leduong/HTML-BeautifySoup](https://github.com/leduong/HTML-BeautifySoup)
- e-mail:		i[at]leduong[dot]com

---

A plugin for [Sublime Text ](http://sublimetext.com/), that formats (indents) HTML source code.
It makes code easier for humans to read.

---

## Key Commands Reverted Back to Original
Due to a conflict with other keymaps in Sublime Text, I am reverting the keymap back to the original setting:

- Mac OS X: `Command-Option-Shift-Z`
- Windows: `Control-Alt-Shift-Z`
- Linux: `Control-Alt-Shift-Z`

(To change this, see instructions later in this README…)

## Notes
- This script assumes an effort has been made by the user to expand tags to different lines. This script will **not**  automatically expand minimized/compressed code—it will only try to “clean-up” code that needs to be re-indented
- Currently, this script chokes a bit with inline comments.
	- For example:

		`<div class="something"> <!-- HTMLBeautifySoup will ignore this line since it is inline -->`
	- So, a workaround is to keep comments on their own lines:

		`<!-- this comment is ok -->`

        `<div class="something">`

        `<!-- this comment is ok too -->`
	- (TODO: Fix this!)

- This script uses `\t` characters to create indentation levels and spacing—ST appears to honor whether the user prefers spaces or tabs in ST settings and adjusts accordingly.
- Use `tag_pos_inline` setting to define tags that _might_ appear on one line.
- Windows Users: You **must** restart Sublime Text to complete the installation.

## Installation (Manual)
- Download the zip, re-name resulting folder to: `HTMLBeautifySoup`, then put the folder into your Sublime Text Packages folder.

or clone (git clone https://github.com/leduong/HTML-BeautifySoup.git) this repository in

* Windows: `%APPDATA%/Roaming/Sublime Text 2/Packages/`
* OSX: `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux: `~/.Sublime Text 2/Packages/`
* Portable Installation: `Sublime Text 2/Data/`

## Usage
- Open a file containing HTML.
- Select HTML code you want to beautify. (If no selection is made the plugin will run on the whole file.)
- Use the appropriate key command to run HTMLBeautifySoup—or use HTMLBeautifySoup from the Edit menu.
- You can test the script with `HTMLBeautifySoupTest.html`: an HTML file with wacky indenting so you to see how this script works.

## Changing the Key Binding
You can create your own custom keymap (key command/macro) in your keymap file: `Packages/User/Default[OS].sublime-keymap`

<pre>
{
	"keys": ["super+alt+shift+z"], //  create your own key command combination here!
	"command": "html_beautifulsoup", // command that executes html_beautifulsoup
	"context": [{
		// these options ensure that the command is executed in the right files/context
		"key": "selector",
		"operator": "equal",
		"operand": "text.html,text.html.twig,text.twig,source.html,source.html.twig,source.twig"
	}]
}
</pre>

For more details:  [Sublime Text Unofficial Documentation: Key Bindings](http://sublime-text-unofficial-documentation.readthedocs.org/en/sublime-text-2/reference/key_bindings.html)


## Disclaimer
This script has been tested for basic HTML coding situations, but your mileage may vary—use with caution if using this in a production environment. (Please report bugs or contribute corrections to the script!) Although the script does not remove or modify code directly (it only attempts to adjust indentation levels), be sure to test this script throughly to make sure it works as expected! The author is not responsible for any bugs that might be introduced to your HTML. :)

