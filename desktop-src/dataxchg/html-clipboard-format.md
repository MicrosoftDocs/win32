---
title: HTML Clipboard Format
description: This section discusses the HTML Clipboard format.
ms.assetid: e891393f-234f-4c94-b581-c4e5f885d2ab
keywords:
- Windows User Interface,clipboard
- clipboard,cutting data
- clipboard,copying data
- clipboard,pasting data
- clipboard,formats
- clipboard,HTML format
- clipboard,cutting HTML text
- clipboard,pasting HTML text
- CF_HTML clipboard format
- clipboard,CF_HTML format
ms.topic: article
ms.date: 05/31/2018
---

# HTML Clipboard Format

The requirements for transferring HTML text by means of the clipboard differ depending on scenario. This article is concerned with cutting and pasting fragments of an HTML document. There may be requirements for transferring entire HTML documents through the clipboard; however, this article is driven by a requirement to transfer fragments of selected HTML text. As such, a method that required the entire HTML document to be copied to the clipboard is seen as too heavyweight.

The `CF_HTML` clipboard format allows a fragment of raw HTML text and its context (i.e. outer HTML) to be stored on the clipboard as ASCII. This allows the context of the HTML fragment, which consists of all preceding surrounding tags, to be examined by an application so that the surrounding tags of the HTML fragment can be noted with their attributes. Although it is up to applications to decide how to interpret such fragments, some basic guidelines are included here based on IE4/MSHTML implementations.

The official name of the clipboard (the string used by `RegisterClipboardFormat`) is "`HTML Format`".

-   [Description](#description)
-   [Scenarios](#scenarios)

## Description

* `CF_HTML` is a text clipboard format, though always using UTF-8 encoding. Note that the use of UTF-8 here is an exception to the general rule that the Windows API uses UTF-16 for representing text strings, especially human-readable (i.e. localizable) strings.

* The general layout, or grammar (or syntax?), of the `CF_HTML` clipboard can be described in pseudo-Backus–Naur form like so:

   **NOTE: This grammar is non-normative**

   ```
   <cf-html>                ::= <description-header> <context>
   <context>                ::= [<preceding-context>] <fragment> [<trailing-context>]

   <description-header>     ::= "Version:" <version> <br> ( <header-offset-keyword> ":" <header-offset-value> <br> )*
   <header-offset-keyword>  ::= "StartHTML" | "EndHTML" | "StartFragment" | "EndFragment" | "StartSelection" | "EndSelection"
   <header-offset-value>    ::= { Base 10 (decimal) integer string with optional _multiple_ leading zero digits (see "Offset syntax" below) }
   <version>                ::= "0.9" | "1.0"

   <fragment>               ::= <fragment-start-comment> <fragment-text> <fragment-end-comment>
   <fragment-start-comment> ::= "<!--StartFragment -->"
   <fragment-end-comment>   ::= "<!--EndFragment -->"

   <preceding-context>      ::= { Arbitrary HTML }
   <trailing-context>       ::= { Arbitrary HTML }
   <fragment-text>          ::= { Arbitrary HTML }

   <br>                     ::= "\r" | "\n" | "\r\n"
   ```

### Description Headers and Offsets

The description header includes the clipboard version number and offsets, indicating where the context and the fragment start and end. The description is a list of ASCII text keywords followed by a string and separated by a colon (:).

* `Version`: vv version number of the clipboard. Starting version is `Version:0.9`. As of Windows 10 20H2 this is now `Version:1.0`.
* `StartHTML`: Offset (in bytes) from the beginning of the clipboard to the start of the context, or `-1` if no context.
* `EndHTML`: Offset (in bytes) from the beginning of the clipboard to the end of the context, or `-1` if no context.
* `StartFragment`: Offset (in bytes) from the beginning of the clipboard to the start of the fragment.
* `EndFragment`: Offset (in bytes) from the beginning of the clipboard to the end of the fragment.
* `StartSelection`: Optional. Offset (in bytes) from the beginning of the clipboard to the start of the selection.
* `EndSelection`: Optional. Offset (in bytes) from the beginning of the clipboard to the end of the selection.

The `StartSelection` and `EndSelection` keywords are optional and must both be omitted if you do not want the application to generate this information.

Future revisions of the `CF_HTML` clipboard format may extend the header, for example, since the HTML starts at the `StartHTML` offset then multiple `StartFragment` and `EndFragment` pairs could be added later to support noncontiguous selection of fragments.

### Offset syntax

For the convenience of the programs generating the byte offsets, the offset values may be optionally left-padded with an arbitrary amount of zero digits `'0'`. The reason for this is that programs sniffing the HTML for the offsets could write ten (10) zeros to its output buffer for each keyword (e.g. `StartHTML: 0000000000`). Later, when the exact `StartHTML` offset is known (say, 71), the program can overwrite the rightmost zeroes with "71" in the buffer (e.g. resulting in `StartHTML: 0000000071`).

The only character set supported by the clipboard is Unicode (UTF-8). Because the first characters of UTF-8 and ASCII match, the description is always ASCII, but the bytes of the context (starting at `StartHTML`) could be using any other characters encoded in UTF-8.

End of lines in the clipboard format header (`<br>` above) may be represented by CRLF (Windows), LF (Unix), or lone CR (archaic).

### The fragment, the selection, and their context

| Element   | Description headers                 | Must be well-formed HTML? | Start and End character positions must
|-----------|-------------------------------------|---------------------------|
| Context   | `StartHTML` and `EndHTML`           | Yes						  |
| Fragment  | `StartFragment` and `EndFragment`   | Yes						  |
| Selection | `StartSelection` and `EndSelection` | No						  |

#### Context

The _context_ is a valid, complete HTML document - though this does not mean the entire original source HTML document containing the user's selection will be carried-over verbatim; on the contrary, it can be a minimal, but well-formed, HTML document.

This _context_ contains the _fragment_ and all preceding surrounding tags (start and end tags; these preceding surrounding tags represent all the parent nodes of the fragment, until the HTML node). Observe that the above example article has a complete HTML `<head>` element which permits the use of `<base href="">` and `<title>` elements, for example, to be included so this additional information can be obtained. An application copying a fragment of HTML to the clipboard can choose to create a `<base href="">` element to include in the context if such an element is not already present so that non-absolute URIs in the HTML fragment can be resolved.

The _context_ is optional, as sufficient information is included in the fragment for basic pasting of an HTML fragment to take place. If the context is not stored, the fragment only is stored and the `StartHTML=EndHTML=-1`.


#### Fragment

The _fragment_ (`<fragment-text>` above) contains a valid HTML fragment.

A _valid_ HTML fragment consists of a single outer HTML element. This element may contain descendant HTML elements provided they are correctly nested. For example, a fragment could be a single `<div>` element that contains 3 `<p>` elements. A fragment consisting of a `<span>` element that contains three `<p>` elements would be invalid because a `<span>` element (an element) cannot contain block-level elements as children.

Thus, the fragment effectively represents the _greater area_ on-screen within, which the user made their text selection (to copy, for example). The selection contains the selected text plus the opening tags and attributes of any element that has an end tag within the selected text, and end tags at the end of the fragment for any start tag included. This is all information required for basic pasting of an HTML fragment.

* The _fragment_ should be preceded and followed by the HTML comments `<!--StartFragment-->` and `<!--EndFragment-->` which indicate where the fragment starts and ends; these HTML comments must be used _verbatim_, with no whitespace chars within each comment itself. Thus, the start and end of the fragment are indicated by the presence of these comments _and_ by the `StartFragment` and `EndFragment` headers. Tools are expected to produce this information. This redundancy is intentional and was introduced to be able to rapidly find the start of the fragment (from the byte count) and mark the position of the fragment directly in the HTML tree.

#### Selection

* The _selection_ is optional, as sufficient information is included in the fragment for basic pasting. If the selection is not stored, both `StartSelection` and `EndSelection` are not stored in the header.

* If the _selection_ is present then it represents the **exact** text range that the user has selected (within the _fragment_); this adds more information to the fragment by indicating the exact selected text, **without** the well-formed and balanced start and end tags and end tags.

* Remember the _selection_ can represents a run of text which can start in any given element and end in **any** subsequent - or ancestor - element. Consequently it is impossible to represent a text selection using HTML.


## Scenarios

The following scenarios describe how the IE4/MSHTML HTML editor handles HTML cut and paste; other applications may or may not follow these scenarios. The clipboard format described here is intended to allow flexibility for how an application chooses to function. (These scenarios show only good HTML, that is, no overlapping tags.)

### Scenario 1. Simple Fragment of HTML.

#### HTML Text

> ```
> <body>This is normal. <b>This is bold.</b> <i><b>This is bold italic.</b> This is italic.</i></body>
> ```

#### Appears as

> This is normal. **This is bold.**  **_This is bold italic._**  _This is italic._

(TODO: Screenshot of Word showing the selected text *before* copying? omg)
(TODO: Screenshot of Word after pasting it)

#### How MSHTML handles copying a substring of HTML:

1. Supposing your user has the above HTML text loaded into a MSHTML-based application (MSHTML, _aka_ Trident, was Internet Explorer's engine).
2. The user then makes a text selection from the start of the word "bold" (in "This is bold.") through to the end of the word "This" (in "This is italic.") without any leading nor trailing whitespace in the selection.
   * i.e. The selection is represented by the square-brackets in `"This is normal **This is \[bold**  **_This is bold italic_**  _This\] is italic_"`.
3. The user then clicks the Copy command button to copy the selection to the clipboard.
4. MSHTML will consequently place this HTML text (below) into the Windows Clipboard:

      ```
      Version:1.0
      StartHTML:0121
      EndHTML:0272
      StartFragment:0006
      EndFragment:0106
      StartSelection:0180
      EndSelection:0225
      <html><!--StartFragment--><body>This is normal. <b>This is bold.</b> <i><b>This is bold italic.</b> This is italic.</i></body><!--EndFragment--></html>
      ```


### Scenario 2. Fragment of a table in HTML.

(Please do not use these uppercase mid-1990s HTML tables, aiieee)

#### HTML Text

> ```
> <BODY><TABLE BORDER><TR><TH ROWSPAN=2>Head1</TH><TD>Item 1</TD><TD>Item 2</TD><TD>Item 3</TD><TD>Item 4</TD></TR><TR><TD>Item 5</TD><TD>Item 6</TD><TD>Item 7</TD><TD>Item 8</TD></TR><TR><TH>Head2</TH><TD>Item 9</TD><TD>Item 10</TD><TD>Item 11</TD><TD>Item 12</TD></TR></TABLE></BODY>
> ```

#### Appears as

> <TABLE BORDER>
> 	<TR>
> 		<TH ROWSPAN=2>Head 1</TH>
> 		<TD>Item 1</TD>
> 		<TD>Item 2</TD>
> 		<TD>Item 3</TD>
> 		<TD>Item 4</TD>
> 	</TR>
> 	<TR>
> 		<TD>Item 5</TD>
> 		<TD>Item 6</TD>
> 		<TD>Item 7</TD>
> 		<TD>Item 8</TD>
> 	</TR>
> 	<TR>
> 		<TH>Head 2</TH>
> 		<TD>Item 9</TD>
> 		<TD>Item 10</TD>
> 		<TD>Item 11</TD>
> 		<TD>Item 12</TD>
> 	</TR>
> </TABLE>


#### How MSHTML handles copying a substring of HTML:

When the user uses their mouse to make a text selection covering the table cells <b>Item 6</b>, <b>Item 7</b>, <b>Item 10</b>, and <b>Item 11</b>. This selection is then copied into the clipboard.

What follows is what will be on the clipboard (note this is IE4/MSHTML's interpretation). Line-breaks have been added for clarity.

```
<!DOCTYPE
<HTML>
<BODY>
<TABLE BORDER>
<!--StartFragment-->
	**<TR>
		<TD>Item 6</TD>
		<TD>Item 7</TD>
	</TR>
	<TR>
		<TD>Item 10</TD>
		<TD>Item 11</TD>
	</TR>**
<!--EndFragment-->
</TABLE>
</BODY>
</HTML>
```

The selection, as delimited by `StartSelection` and `EndSelection`, is shown in bold.

### Scenario 3. Pasting a fragment of an ordered list `<ol>` into plain text.

<!-- TODO: If a user copies a middle subsection of an ordered list, and then pastes it elsewhere, should the values of those bullet-points be preserved? If so, then how should the DOM represent it? -->

#### HTML Text

> ```
> <BODY><OL TYPE="a"><LI>Item 1<LI>Item 2<LI>Item 3<LI>Item 4<LI>Item 5<LI>Item 6</OL></BODY>
> ```

#### Appears as

<!-- or just let Markdown do its own thang?
> <ol>
> 	<li>Item 1</li>
> 	<li>Item 2</li>
> 	<li>Item 3</li>
> 	<li>Item 4</li>
> 	<li>Item 5</li>
> 	<li>Item 6</li>
> </ol>
 -->

1.  Item 1
2.  Item 2
3.  Item 3
4.  Item 4
5.  Item 5
6.  Item 6


(TODO: screenshot? but is that really necessary for markup this simple?)


#### How MSHTML handles copying a substring of HTML:

1. The user makes a text selection from the start of **item 3**, through **item 4**, and to the end of **item 5**. The user invokes the Copy command.
2. The following HTML is in the clipboard (line-breaks added for clarity - the precise location of the `<!--Star/EndFragment -->` comments depends on how careless or careful the user was in fighting their browser's horrible broken text selection logic):


```
<html>
<body>
<ol>
<!-- StartFragment-->
<li>Item 3</li>
<li>Item 4</li>
<li>Item 5</li>
<!-- EndFragment-->
</ol>
</body>
</html>
```

If this fragment were to now be pasted into an empty document, the following HTML will be created:

```
<body>
<ol>
<li>Item 3</li>
<li>Item 4</li>
<li>Item 5</li>
</ol>
</body>
```

Appearing as:

> 1.  Item 3
> 2.  Item 4
> 3.  Item 5

### Scenario 5. Pasting a partially selected region.

#### HTML Text

> ```
> <p>IE4/MSHTML is a WYSIWYG Editor that supports:</p>
> <ul><li>Cut<li>Copy<li>Paste</ul>
> <p>This is a Great Tool!</p>
> ```

#### Appears as


> IE4/MSHTML is a WYSIWYG Editor that supports:
>  -   Cut
>  -   Copy
>  -   Paste
> This is a Great Tool!

(TODO: screenshot? but is that really necessary for markup this simple?)


#### How MSHTML handles copying a substring of HTML:

The user uses their mouse to drag a text selection starting from (and including) "WYSIWYG" throgh to "Cop" (in "Copy").

(TODO: Screenshot of selection attempt)

As though it were plain-text, that selection would look like this broken HTML fragment:)

```
WYSIWYG Editor, which supports:</p>
<ul>
	<li>Cut</li>
	<li>Cop
```

When the user presses the Copy comamd button, their clipboard will look like this (line-breaks have been added for clarity; the bold text denotes what the user actually selected);

<!-- Hiding this because we can't make parts of it bold (or can we?) to highlight the subset that was actually selected by the user.
```
<html>
<body>
<!-- StartFragment-->
<p>WYSIWYG Editor, which supports</p>
<ul>
	<li>Cut</li>
	<li>Cop</li>
</ul>
<!-- EndFragment-->
</body>
</html>
```
-->

<pre>
&lt;html&gt;
&lt;body&gt;
&lt;!-- StartFragment--&gt;
&lt;p&gt;<b>WYSIWYG Editor, which supports&lt;/p&gt;
&lt;ul&gt;
	&lt;li&gt;Cut&lt;/li&gt;
	&lt;li&gt;Cop</b>&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- EndFragment--&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

Observe that:
* The text prior to "WYSIWYG" was removed.
* The list item (`<li>Paste</li>`) was removed as none of it was in the user's selection.
* The "y" from "Copy" was removed.

