---
title: About Rich Edit Controls
description: This section introduces rich edit controls.
ms.assetid: ab9dcdf4-a311-4159-8f37-e67e144f31f6
ms.topic: article
ms.date: 05/31/2018
---

# About Rich Edit Controls

The following topics are discussed in this section.

-   [Versions of Rich Edit](#versions-of-rich-edit)
    -   [Rich Edit Version 1.0](#rich-edit-version-10)
    -   [Rich Edit Version 2.0](#rich-edit-version-20)
    -   [Rich Edit Version 3.0](#rich-edit-version-30)
    -   [Rich Edit Version 4.1](#rich-edit-version-41)
-   [Unsupported Edit Control Functionality](#unsupported-edit-control-functionality)
-   [Rich Edit Shortcut Keys](#rich-edit-shortcut-keys)
-   [Related topics](#related-topics)

## Versions of Rich Edit

The original specification for rich edit controls is Microsoft Rich Edit 1.0; the current specification is Microsoft Rich Edit 4.1. Each version of rich edit is a superset of the preceding one, except that only Asian builds of Microsoft Rich Edit 1.0 have a vertical text option. Before creating a rich edit control, you should call the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) function to verify which version of Microsoft Rich Edit is installed.

The following table shows which DLL corresponds with which version of Rich Edit. Note that the name of the file did not change from version 2.0 to version 3.0. This allows version 2.0 to be upgraded to version 3.0 without breaking existing code.



| Rich Edit version | DLL          | Window Class    |
|-------------------|--------------|-----------------|
| 1.0               | Riched32.dll | RICHEDIT\_CLASS |
| 2.0               | Riched20.dll | RICHEDIT\_CLASS |
| 3.0               | Riched20.dll | RICHEDIT\_CLASS |
| 4.1               | Msftedit.dll | MSFTEDIT\_CLASS |



 

### Rich Edit Version 1.0

Microsoft Rich Edit 1.0 includes the following features.



|    Feature   | Description   |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text entry and selection                                                           | Mostly standard (system-edit control) selection and entry of text. Selection bar support (the selection bar is an unmarked area to the left of each paragraph that when clicked, selects the line). Word-wrap and auto-word-select options. Single-, double-, and triple-click selection. |
| ANSI (single-byte character set (SBCS) and multibyte character set (MBCS)) editing | However, there is no Unicode editing.                                                                                                                                                                                                                                                     |
| Basic set of character/paragraph formatting properties                             | See [**CHARFORMAT**](/windows/win32/api/richedit/ns-richedit-charformata) and [**PARAFORMAT**](/windows/desktop/api/Richedit/ns-richedit-paraformat).                                                                                                                                                                                                                |
| Character formatting properties                                                    | Font name and size, bold, italic, solid underline, strike-out, protected, link, offset, and text color.                                                                                                                                                                                   |
| Paragraph formatting properties                                                    | Start indent, right indent, subsequent line offset, bullet, alignment (left, center, right), and tabs.                                                                                                                                                                                    |
| Find forward                                                                       | Includes case-insensitive and match-whole-word options.                                                                                                                                                                                                                                   |
| Message-based interface                                                            | Almost a superset of the system edit-control message set plus two interfaces, [**IRichEditOle**](/windows/desktop/api/Richole/nn-richole-iricheditole) and [**IRichEditOleCallback**](/windows/desktop/api/Richole/nn-richole-iricheditolecallback).                                                                                                              |
| Embedded objects                                                                   | Requires client collaboration based on [**IRichEditOle**](/windows/desktop/api/Richole/nn-richole-iricheditole) and [**IRichEditOleCallback**](/windows/desktop/api/Richole/nn-richole-iricheditolecallback) interfaces.                                                                                                                                          |
| Right-button menu support                                                          | Uses [**IRichEditOleCallback**](/windows/desktop/api/Richole/nn-richole-iricheditolecallback) interface.                                                                                                                                                                                                                      |
| Drag-and-drop editing                                                              | Drag-and-drop editing is supported.                                                                                                                                                                                                                                                       |
| Notifications                                                                      | [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages sent to client plus a number of others. This is a superset of common-control notifications.                                                                                                                                                 |
| Single-level undo/redo                                                             | Behaves similarly to the system edit control. Selecting **Undo** reverses the last action, and that action then becomes the new **Redo** action.                                                                                                                                          |
| Simple vertical text                                                               | (Asian builds only).                                                                                                                                                                                                                                                                      |
| Input Method Editor (IME) support                                                  | (Asian builds only).                                                                                                                                                                                                                                                                      |
| WYSIWYG editing using printer metrics                                              | This feature is needed for Microsoft WordPad, in particular.                                                                                                                                                                                                                              |
| Cut/Copy/Paste/StreamIn/StreamOut                                                  | With plain text (**CF\_TEXT**) or Rich Text Format (RTF) with and without objects.                                                                                                                                                                                                        |
| C code base                                                                        | The code is written in C, which provides a solid and versatile foundation.                                                                                                                                                                                                                |
| Different builds for different scripts                                             | Microsoft Rich Edit 1.0 addresses localization issues with different builds.                                                                                                                                                                                                              |



 

### Rich Edit Version 2.0

Microsoft Rich Edit 2.0 incorporated several additional features, such as support for Unicode and Asian languages, multilevel Undo, Component Object Model (COM) interfaces, and numerous UI enhancements.

Microsoft Rich Edit 2.0 includes the following features in addition to the features provided by [Microsoft Rich Edit 1.0](#rich-edit-version-10).



|    Feature                                           |    Description                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unicode                                       | Unicode eases the effort in handling international text. However effort is needed to maintain compatibility with existing non-Unicode documents that is, the ability to convert to/from non-Unicode plain and rich text.                                                                                                                                                             |
| General international support                 | General line breaking algorithm (extension of Kinsoku rules), simple font linking, keyboard font switching.                                                                                                                                                                                                                                                                          |
| Asian support                                 | Level 2 (dialog box) and 3 (inline) is supported in IMEs.                                                                                                                                                                                                                                                                                                                            |
| Find Up/Find Down support                     | Searching forward and backward is supported.                                                                                                                                                                                                                                                                                                                                         |
| Bidirectional support                         | This is included in Microsoft Rich Edit 2.1                                                                                                                                                                                                                                                                                                                                          |
| Multilevel undo                               | An extensible Undo architecture allows client to participate in application-wide Undo model.                                                                                                                                                                                                                                                                                         |
| Magellan mouse support                        | This is the mouse with a roller for scrolling.                                                                                                                                                                                                                                                                                                                                       |
| Dual-font support                             | The keyboard can automatically switch fonts when the active font is inappropriate for current keyboard, for example, Kanji characters in Times New Roman.                                                                                                                                                                                                                            |
| Smart font apply                              | Font change request does not apply Western fonts to Asian characters.                                                                                                                                                                                                                                                                                                                |
| Improved display                              | An off-screen bitmap is used when multiple fonts occur on the same line. This allows, for example, the last letter of the word cool not to be chopped off.                                                                                                                                                                                                                           |
| Transparency support                          | Also in windowless mode.                                                                                                                                                                                                                                                                                                                                                             |
| System selection colors                       | Used for selecting text.                                                                                                                                                                                                                                                                                                                                                             |
| Automatic URL recognition                     | Can check for a number of URL formats (for example, http:)                                                                                                                                                                                                                                                                                                                           |
| Microsoft Word edit UI compatibility          | Selection, cursor-keypad semantics.                                                                                                                                                                                                                                                                                                                                                  |
| Word standard EOP                             | The end-of-paragraph mark (CR) can also handle carriage return/line feed (CR/LF) (carriage return, line feed).                                                                                                                                                                                                                                                                       |
| Plain-text as well as rich-text functionality | Single-character format and single-paragraph format.                                                                                                                                                                                                                                                                                                                                 |
| Single-line and multiline controls            | Truncate at first end-of-paragraph and no wordwrap.                                                                                                                                                                                                                                                                                                                                  |
| Accelerator keys                              | Accelerator keys are supported.                                                                                                                                                                                                                                                                                                                                                      |
| Password window style                         | Password edit controls are supplied through [**EM\_GETPASSWORDCHAR**](em-getpasswordchar.md) and [**EM\_SETPASSWORDCHAR**](em-setpasswordchar.md).                                                                                                                                                                                                                                 |
| Scalable architecture                         | To reduce instance size.                                                                                                                                                                                                                                                                                                                                                             |
| Windowless operation and interfaces           | This is provided through the [**ITextHost**](/windows/desktop/api/Textserv/nl-textserv-itexthost) and [**ITextServices**](/windows/desktop/api/Textserv/nl-textserv-itextservices) interfaces.                                                                                                                                                                                                                                                                   |
| COM dual interfaces                           | Text Object Model (TOM) interfaces.                                                                                                                                                                                                                                                                                                                                                  |
| CHARFORMAT2                                   | Added font weight, background color, locale identifier, underline type, superscript and subscript (in addition to offset), disabled effect. For RTF roundtripping only, added amount to space between letters, twip size above which to kern character pair, animated-text type, various effects: font shadow/outline, all caps, small caps, hidden, embossed, imprint, and revised. |
| PARAFORMAT2                                   | Added space before and after and Word line spacing. For RTF roundtripping only, added shading weight/style, numbering start/style/tab, border space/width/sides, tab alignment/leaders, various Word paragraph effects: RTL paragraph, keep, keep-next, page-break-before, no-line-number, no-widow-control, do-not-hyphenate, side-by-side.                                         |
| More RTF roundtripping                        | All of the Word FormatFont and FormatParagraph properties.                                                                                                                                                                                                                                                                                                                           |
| Code stability and stabilization              | Examples: parameter and object validation, function invariants, reentrancy guards, object stabilization.                                                                                                                                                                                                                                                                             |
| Strong testing infrastructure                 | Including extensive regressions tests.                                                                                                                                                                                                                                                                                                                                               |
| Improved performance                          | Smaller working set, faster load and redisplay times, and so on.                                                                                                                                                                                                                                                                                                                     |
| C++ code base                                 | The code is written in C++, which provides a solid foundation on which to build Microsoft Rich Edit 3.0.                                                                                                                                                                                                                                                                             |



 

With a few exceptions, Microsoft Rich Edit 2.0 uses the same functions, structures, and messages as Microsoft Rich Edit 1.0. Note, however, the following differences:

-   The name of the Microsoft Rich Edit 1.0 window class is **RichEdit**. Microsoft Rich Edit 2.0 has both ANSI and Unicode window classes **RichEdit20A** and **RichEdit20W,** respectively. To specify the appropriate rich edit window class, use the RICHEDIT\_CLASS constant, which the Richedit.h file defines depending on the definition of the UNICODE compile flag.
-   In Microsoft Rich Edit 2.0, if you create a Unicode rich edit control (one that expects Unicode text messages), you must specify only Unicode data in any window messages sent to the control. Similarly, if you create an ANSI rich edit control, send only ANSI or double-byte character set (DBCS) data. You can use the [**IsWindowUnicode**](/windows/desktop/api/winuser/nf-winuser-iswindowunicode) function to determine whether a rich edit control uses Unicode text messages. Note that the rich edit COM interfaces use Unicode text unless they encounter a code page argument.
-   Microsoft Rich Edit 1.0 used CR/LF character combinations for paragraph markers. Microsoft Rich Edit 2.0 used only a carriage return character ('\\r'). Microsoft Rich Edit 3.0 uses only a carriage return character but can emulate Microsoft Rich Edit 1.0 in this regard.
-   Microsoft Rich Edit 2.0 introduced the following new messages. 

    | Message                                           | Description                                                             |
    |---------------------------------------------------|-------------------------------------------------------------------------|
    | [**EM\_AUTOURLDETECT**](em-autourldetect.md)     | Enables or disables automatic URL detection.                            |
    | [**EM\_CANREDO**](em-canredo.md)                 | Determines whether there are any actions in the redo queue.             |
    | [**EM\_GETIMECOMPMODE**](em-getimecompmode.md)   | Retrieves the current input method editor (IME) mode.                   |
    | [**EM\_GETLANGOPTIONS**](em-getlangoptions.md)   | Retrieves options for IME and Asian language support.                   |
    | [**EM\_GETREDONAME**](em-getredoname.md)         | Retrieves the type name of the next action in the redo queue.           |
    | [**EM\_GETTEXTMODE**](em-gettextmode.md)         | Retrieves the text mode or undo level.                                  |
    | [**EM\_GETUNDONAME**](em-getundoname.md)         | Retrieves the type name of the next action in the undo queue.           |
    | [**EM\_REDO**](em-redo.md)                       | Redoes the next action in the redo queue.                               |
    | [**EM\_SETLANGOPTIONS**](em-setlangoptions.md)   | Sets options for IME and Asian language support.                        |
    | [**EM\_SETTEXTMODE**](em-settextmode.md)         | Sets the text mode or undo level.                                       |
    | [**EM\_SETUNDOLIMIT**](em-setundolimit.md)       | Sets the maximum number of actions in the undo queue.                   |
    | [**EM\_STOPGROUPTYPING**](em-stopgrouptyping.md) | Stops grouping consecutive typing actions into the current undo action. |

    

     

-   Microsoft Rich Edit 2.0 introduced the following new structures. 

    | Structure                          | Description                                      |
    |------------------------------------|--------------------------------------------------|
    | [**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a) | Contains information about character formatting. |
    | [**PARAFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-paraformat2) | Contains information about paragraph formatting. |

    

     

-   The following messages are supported only in Asian-language versions of Microsoft Rich Edit 1.0. They are not supported in any later versions of Rich Edit.

    [**EM\_CONVPOSITION**](em-convposition.md)

    [**EM\_GETIMECOLOR**](em-getimecolor.md)

    [**EM\_GETIMEOPTIONS**](em-getimeoptions.md)

    [**EM\_GETPUNCTUATION**](em-getpunctuation.md)

    [**EM\_GETWORDWRAPMODE**](em-getwordwrapmode.md)

    [**EM\_SETIMECOLOR**](em-setimecolor.md)

    [**EM\_SETIMEOPTIONS**](em-setimeoptions.md)

    [**EM\_SETPUNCTUATION**](em-setpunctuation.md)

    [**EM\_SETWORDWRAPMODE**](em-setwordwrapmode.md)

### Rich Edit Version 3.0

Microsoft Rich Edit 3.0 is a single, scalable, world-wide DLL that offers high performance and compatibility with Word in a small package. New features for Microsoft Rich Edit 3.0 include richer text, zoom, font binding, more powerful IME support, and rich complex script support (bidirectional, Indic, and Thai).

Microsoft Rich Edit 3.0 includes the following features in addition to the features provided by [Rich Edit Version 2.0](#rich-edit-version-20).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Zoom</td>
<td>The zoom factor is given by a ratio.</td>
</tr>
<tr class="even">
<td>Paragraph numbering (single-level)</td>
<td>Numeric, upper and lower alphabetic, or Roman numeral.</td>
</tr>
<tr class="odd">
<td>Simple tables</td>
<td>Deleting and inserting rows is possible, but not resizing nor wrapping inside cells. With advanced typography turned on (see <a href="em-gettypographyoptions.md"><strong>EM_GETTYPOGRAPHYOPTIONS</strong></a>), Microsoft Rich Edit 3.0 can align columns centered or flush right, and include decimals. Cells are simulated by tabs, so text tabs and carriage returns are replaced by blanks.</td>
</tr>
<tr class="even">
<td>Normal and heading styles</td>
<td>Built-in normal style and heading styles 1 through 9 are supported by the <a href="em-setparaformat.md"><strong>EM_SETPARAFORMAT</strong></a> and <a href="text-object-model.md">Text Object Model</a> (TOM) interfaces.</td>
</tr>
<tr class="odd">
<td>More underline types</td>
<td>Dashed, dash-dot, dash-dot-dot, and dot underlining has been added.</td>
</tr>
<tr class="even">
<td>Underline coloring</td>
<td>Underlined text can be tagged with one of 15 document choices for underline colors.</td>
</tr>
<tr class="odd">
<td>Hidden text</td>
<td>Marked by CHARFORMAT2 attribute. Handy for roundtripping (writing out to a file what was read in) of information that ordinarily should not be displayed.</td>
</tr>
<tr class="even">
<td>More default hot keys</td>
<td>These hot keys function the same as those in Word. For example, European accent dead keys (U.S. keyboards only). Number hot key (CTRL+L) cycles through numbering options available, starting with bullet.</td>
</tr>
<tr class="odd">
<td>HexToUnicode IME</td>
<td>Allows a user to convert between hexadecimal and Unicode by using hot keys.</td>
</tr>
<tr class="even">
<td>Smart quotes</td>
<td>This feature is toggled on and off by CTRL+ALT+' for U.S. keyboards.</td>
</tr>
<tr class="odd">
<td>Soft hyphens</td>
<td>For plain text, use 0xAD. For RTF, use \-.</td>
</tr>
<tr class="even">
<td>Italics cursor</td>
<td>In addition, the mouse cursor changes to a hand when over URLs.</td>
</tr>
<tr class="odd">
<td>Advanced typography option</td>
<td>Microsoft Rich Edit 3.0 can use an advanced typography option for line breaking and display (see <a href="em-gettypographyoptions.md"><strong>EM_GETTYPOGRAPHYOPTIONS</strong></a>). This elegant option was added primarily to facilitate handling complex scripts (bidirectional, Indic, and Thai). In addition, a number of improvements occur for simple scripts. Examples are:
<ul>
<li>Center, right, decimal tabs</li>
<li>Fully justified text</li>
<li>Underline averaging, which provides a uniform underline even when adjacent text runs have different font sizes.</li>
</ul></td>
</tr>
<tr class="even">
<td>Complex script support</td>
<td>Microsoft Rich Edit 3.0 supports bidirectional (text with Arabic and/or Hebrew mixed with other scripts), Indic (Indian scripts like Devangari), and Thai text. For support of these complex scripts, the advanced typography and Uniscribe components are used.</td>
</tr>
<tr class="odd">
<td>Font binding</td>
<td>Microsoft Rich Edit 3.0 will automatically choose an appropriate font for characters that clearly do not belong to the current character set stamp. This is done by assigning character sets to text runs and associating fonts with those character sets. For more information, see <a href="using-rich-edit-controls.md">Font Binding</a>.</td>
</tr>
<tr class="even">
<td>Plain-text read/write options specific to character sets</td>
<td>This allows reading a file using one character set, and writing with a different character set.</td>
</tr>
<tr class="odd">
<td>UTF-8 RTF</td>
<td>This is recommended for cutting, copying, and pasting operations. This file format is more compact than ordinary RTF, faster, and compatible with Unicode.</td>
</tr>
<tr class="even">
<td>Microsoft Office 9 IME support (IME98)</td>
<td>This more powerful IME capability has been separated into an independent module. Features include:
<ul>
<li>Reconversion In the earlier versions, the user needed to delete the final string first and then type in a new string to get to the correct candidate. This new feature enables the user to convert the final string back to composition mode, thereby allowing easy selection of a different candidate string.<br/></li>
<li>Document feed This feature provides IME98 with the text for the current paragraph, which helps IME98 perform more accurate conversion during typing.<br/></li>
<li>Mouse operation This feature provides better control over the candidate and UI windows during typing.<br/></li>
<li>Caret position This feature provides the current caret and line information, which IME98 uses to position UI windows (for example, a candidate list).<br/></li>
</ul></td>
</tr>
<tr class="odd">
<td>Active Input Method Manager (IMM) support</td>
<td>Users can invoke the Active IMM object, which enables users to enter Asian characters on U.S. systems.</td>
</tr>
<tr class="even">
<td>HexToUnicode support</td>
<td>Users can convert between hexadecimal notation and Unicode by using hot keys.</td>
</tr>
<tr class="odd">
<td>More RTF roundtripping</td>
<td>RTF text that is read in from a file will be written back out intact.</td>
</tr>
<tr class="even">
<td>Improved 1.0 compatibility mode</td>
<td>Microsoft Rich Edit 3.0 can emulate Microsoft Rich Edit 1.0 behavior. For example, it is possible to change between MBCS and Unicode character-position (cp) mappings.</td>
</tr>
<tr class="odd">
<td>Increased freeze control</td>
<td>The display can be frozen over multiple API calls and then unfrozen to display the updates.</td>
</tr>
<tr class="even">
<td>Increased undo control</td>
<td>Undo can be suspended and resumed (an IME requirement).</td>
</tr>
<tr class="odd">
<td>Increase/decrease font size</td>
<td>Increases or decreases font size to one of six standard values (12, 28, 36, 48, 72, and 80 points).</td>
</tr>
</tbody>
</table>



 

### Rich Edit Version 4.1

The window class for Microsoft Rich Edit 4.1 is MSFTEDIT\_CLASS. New features for Microsoft Rich Edit 4.1 include hyphenation, page rotation, and Text Services Framework (TSF) support.

Microsoft Rich Edit 4.1 includes the following features in addition to the features provided by [Rich Edit Version 3.0](#rich-edit-version-30).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Hyphenation</td>
<td>Hyphenation is supported through the following APIs: <a href="/windows/desktop/api/Richedit/nf-richedit-hyphenateproc"><em>HyphenateProc</em></a>, <a href="em-sethyphenateinfo.md"><strong>EM_SETHYPHENATEINFO</strong></a>, and <a href="em-gethyphenateinfo.md"><strong>EM_GETHYPHENATEINFO</strong></a>.</td>
</tr>
<tr class="even">
<td>Page rotation</td>
<td>Top-to-bottom and bottom-to-top layout is supported through <a href="em-setpagerotate.md"><strong>EM_SETPAGEROTATE</strong></a> and <a href="em-getpagerotate.md"><strong>EM_GETPAGEROTATE</strong></a>.</td>
</tr>
<tr class="odd">
<td>Text Services Framework support</td>
<td><ul>
<li>To turn on TSF and certain TSF features, use the following styles in <a href="em-seteditstyle.md"><strong>EM_SETEDITSTYLE</strong></a>: SES_USECTF, SES_CTFALLOWEMBED, SES_CTFALLOWPROOFING, and SES_CTFALLOWSMARTTAG.</li>
<li>To set and get the TSF mode bias, use <a href="em-setctfmodebias.md"><strong>EM_SETCTFMODEBIAS</strong></a> and <a href="em-getctfmodebias.md"><strong>EM_GETCTFMODEBIAS</strong></a>.</li>
<li>To set and get the TSF keyboard status, use <a href="em-setctfopenstatus.md"><strong>EM_SETCTFOPENSTATUS</strong></a> and <a href="em-getctfopenstatus.md"><strong>EM_GETCTFOPENSTATUS</strong></a>.</li>
</ul></td>
</tr>
<tr class="even">
<td>Additional IME support</td>
<td><ul>
<li>To set and get the IME mode bias, use <a href="em-setimemodebias.md"><strong>EM_SETIMEMODEBIAS</strong></a> and <a href="em-getimemodebias.md"><strong>EM_GETIMEMODEBIAS</strong></a>.</li>
<li>To get the properties and capabilities of the IME, use <a href="em-getimeproperty.md"><strong>EM_GETIMEPROPERTY</strong></a>.</li>
<li>To get the IME composition text, use <a href="em-getimecomptext.md"><strong>EM_GETIMECOMPTEXT</strong></a>.</li>
<li>To determine whether the locale is an East Asian locale, use <a href="em-isime.md"><strong>EM_ISIME</strong></a>.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Additional <a href="em-seteditstyle.md"><strong>EM_SETEDITSTYLE</strong></a> settings</td>
<td>Besides the TSF settings, there are new settings that exclude IMEs, set bidirectional text flow, use draftmode fonts, and more.</td>
</tr>
<tr class="even">
<td>Additional <a href="em-setcharformat.md"><strong>EM_SETCHARFORMAT</strong></a> settings</td>
<td>New flags allow the client to set the default font and font sizes for a given LCID or character set, to set the default font for the control, to prevent keyboard switching to match the font, and more.</td>
</tr>
<tr class="odd">
<td>Restricting input to ANSI text</td>
<td>Using <a href="/windows/win32/api/richedit/ne-richedit-textmode"><strong>TM_SINGLECODEPAGE</strong></a> in <a href="em-settextmode.md"><strong>EM_SETTEXTMODE</strong></a> prevents Unicode input from entering a Rich Edit control.</td>
</tr>
<tr class="even">
<td>Unsupported RTF keyword notification</td>
<td><a href="en-lowfirtf.md">EN_LOWFIRTF</a> warns an application when there is an unsupported RTF keyword.</td>
</tr>
<tr class="odd">
<td>Additional language support</td>
<td>Additional languages include Armenian, Divehi, Telugu, and others.</td>
</tr>
<tr class="even">
<td>Improved table support</td>
<td>Features include: wrapping within cells, improved handling via RTF, and improved navigation.</td>
</tr>
<tr class="odd">
<td>ES_VERTICAL</td>
<td>The <a href="rich-edit-control-styles.md"><strong>ES_VERTICAL</strong></a> window style is supported.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-unichar"><strong>WM_UNICHAR</strong></a> support</td>
<td>To send or post Unicode characters to ANSI windows, use <a href="/windows/desktop/inputdev/wm-unichar"><strong>WM_UNICHAR</strong></a>. It is equivalent to <a href="/windows/desktop/inputdev/wm-char"><strong>WM_CHAR</strong></a>, but it uses (UTF)-32.</td>
</tr>
</tbody>
</table>



 

## Unsupported Edit Control Functionality

Rich edit controls support most but not all functionality for multiline edit controls. This section lists the edit control messages and window styles that are *not* supported by rich edit controls.

The following messages are processed by edit controls but *not* by rich edit controls.



| Unsupported message                         | Comments                                                                                                                    |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**EM\_FMTLINES**](em-fmtlines.md)         | Not supported.                                                                                                              |
| [**EM\_GETHANDLE**](em-gethandle.md)       | Rich edit controls do not store text as a simple array of characters.                                                       |
| [**EM\_GETIMESTATUS**](em-getimestatus.md) | Not supported.                                                                                                              |
| [**EM\_GETMARGINS**](em-getmargins.md)     | Not supported.                                                                                                              |
| [**EM\_SETHANDLE**](em-sethandle.md)       | Rich edit controls do not store text as a simple array of characters.                                                       |
| [**EM\_SETIMESTATUS**](em-setimestatus.md) | Not supported.                                                                                                              |
| [**EM\_SETMARGINS**](em-setmargins.md)     | Supported in Microsoft Rich Edit 3.0.                                                                                       |
| [**EM\_SETRECTNP**](em-setrectnp.md)       | Not supported.                                                                                                              |
| [**EM\_SETTABSTOPS**](em-settabstops.md)   | The [**EM\_SETPARAFORMAT**](em-setparaformat.md) message is used instead. Supported in Microsoft Rich Edit 3.0.<br/> |
| [**WM\_CTLCOLOR**](/windows/desktop/DevNotes/wm-ctlcolor-)    | The [**EM\_SETBKGNDCOLOR**](em-setbkgndcolor.md) message is used instead.                                                  |
| [**WM\_GETFONT**](/windows/desktop/winmsg/wm-getfont)        | The [**EM\_GETCHARFORMAT**](em-getcharformat.md) message is used instead.                                                  |



 

The following window styles are used with multiline edit controls but not with rich edit controls: [**ES\_LOWERCASE**](edit-control-styles.md), [**ES\_UPPERCASE**](edit-control-styles.md), and [**ES\_OEMCONVERT**](edit-control-styles.md).

## Rich Edit Shortcut Keys

Rich edit controls support the following shortcut keys.



| Keys                      | Operations                                                                                                                               | Comments                                                                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shift+Backspace           | Generate a LRM/LRM on a bidi keyboard                                                                                                    | BiDi specific                                                                                                                                                                                                                  |
| Ctrl+Tab                  | Tab                                                                                                                                      |                                                                                                                                                                                                                                |
| Ctrl+Clear                | Select all                                                                                                                               |                                                                                                                                                                                                                                |
| Ctrl+Number Pad 5         | Select all                                                                                                                               |                                                                                                                                                                                                                                |
| Ctrl+A                    | Select all                                                                                                                               |                                                                                                                                                                                                                                |
| Ctrl+E                    | Center alignment                                                                                                                         |                                                                                                                                                                                                                                |
| Ctrl+J                    | Justify alignment                                                                                                                        |                                                                                                                                                                                                                                |
| Ctrl+R                    | Right alignment                                                                                                                          |                                                                                                                                                                                                                                |
| Ctrl+L                    | Left alignment                                                                                                                           |                                                                                                                                                                                                                                |
| Ctrl+C                    | Copy                                                                                                                                     |                                                                                                                                                                                                                                |
| Ctrl+V                    | Paste                                                                                                                                    |                                                                                                                                                                                                                                |
| Ctrl+X                    | Cut                                                                                                                                      |                                                                                                                                                                                                                                |
| Ctrl+Z                    | Undo                                                                                                                                     |                                                                                                                                                                                                                                |
| Ctrl+Y                    | Redo                                                                                                                                     |                                                                                                                                                                                                                                |
| Ctrl+'+' (Ctrl+Shift+'=') | Superscript                                                                                                                              |                                                                                                                                                                                                                                |
| Ctrl+'='                  | Subscript                                                                                                                                |                                                                                                                                                                                                                                |
| Ctrl+1                    | Line spacing = 1 line.                                                                                                                   |                                                                                                                                                                                                                                |
| Ctrl+2                    | Line spacing = 2 lines.                                                                                                                  |                                                                                                                                                                                                                                |
| Ctrl+5                    | Line spacing = 1.5 lines.                                                                                                                |                                                                                                                                                                                                                                |
| Ctrl+' (apostrophe)       | Accent acute                                                                                                                             | After pressing the short cut key, press the appropriate letter (for example a, e, or u). This applies to English, French, German, Italian, and Spanish keyboards only.                                                         |
| Ctrl+\` (grave)           | Accent grave                                                                                                                             | See Ctrl+' comments.                                                                                                                                                                                                           |
| Ctrl+~ (tilde)            | Accent tilde                                                                                                                             | See Ctrl+' comments.                                                                                                                                                                                                           |
| Ctrl+; (semicolon)        | Accent umlaut                                                                                                                            | See Ctrl+' comments.                                                                                                                                                                                                           |
| Ctrl+Shift+6              | Accent caret (circumflex)                                                                                                                | See Ctrl+' comments.                                                                                                                                                                                                           |
| Ctrl+, (comma)            | Accent cedilla                                                                                                                           | See Ctrl+' comments.                                                                                                                                                                                                           |
| Ctrl+Shift+' (apostrophe) | Activate smart quotes                                                                                                                    |                                                                                                                                                                                                                                |
| Backspace                 | If text is protected, beep and do not delete it. Otherwise, delete previous character.                                                   |                                                                                                                                                                                                                                |
| Ctrl+Backspace            | Delete previous word. This generates a VK\_F16 code.                                                                                     |                                                                                                                                                                                                                                |
| F16                       | Same as Backspace.                                                                                                                       |                                                                                                                                                                                                                                |
| Ctrl+Insert               | Copy                                                                                                                                     |                                                                                                                                                                                                                                |
| Shift+Insert              | Paste                                                                                                                                    |                                                                                                                                                                                                                                |
| Insert                    | Overwrite                                                                                                                                | DBCS does not overwrite.                                                                                                                                                                                                       |
| Ctrl+Left Arrow           | Move cursor one word to the left.                                                                                                        | On bidi keyboard, this depends on the direction of the text.                                                                                                                                                                   |
| Ctrl+Right Arrow          | Move cursor one word to the right.                                                                                                       | See Ctrl+Left Arrow comments.                                                                                                                                                                                                  |
| Ctrl+Left Shift           | Left alignment                                                                                                                           | In BiDi documents, this is for left-to-right reading order.                                                                                                                                                                    |
| Ctrl+Right Shift          | Right alignment                                                                                                                          | In BiDi documents, this is for right-to-left reading order.                                                                                                                                                                    |
| Ctrl+Up Arrow             | Move to the line above.                                                                                                                  |                                                                                                                                                                                                                                |
| Ctrl+Down Arrow           | Move to the line below.                                                                                                                  |                                                                                                                                                                                                                                |
| Ctrl+Home                 | Move to the beginning of the document.                                                                                                   |                                                                                                                                                                                                                                |
| Ctrl+End                  | Move to the end of the document.                                                                                                         |                                                                                                                                                                                                                                |
| Ctrl+Page Up              | Move one page up.                                                                                                                        | If in SystemEditMode and Single Line control, do nothing.                                                                                                                                                                      |
| Ctrl+Page Down            | Move one page down.                                                                                                                      | See Ctrl+Page Up comments.                                                                                                                                                                                                     |
| Ctrl+Delete               | Delete the next word or selected characters.                                                                                             |                                                                                                                                                                                                                                |
| Shift+Delete              | Cut the selected characters.                                                                                                             |                                                                                                                                                                                                                                |
| Esc                       | Stop drag-drop.                                                                                                                          | While doing a drag-drop of text.                                                                                                                                                                                               |
| Alt+Esc                   | Change the active application.                                                                                                           |                                                                                                                                                                                                                                |
| Alt+X                     | Converts the Unicode hexadecimal value preceding the insertion point to the corresponding Unicode character.                             |                                                                                                                                                                                                                                |
| Alt+Shift+X               | Converts the Unicode character preceding the insertion point to the corresponding Unicode hexadecimal value.                             |                                                                                                                                                                                                                                |
| Alt+0xxx (Number Pad)     | Inserts Unicode values if xxx is greater than 255. When xxx is less than 256, ASCI range text is inserted based on the current keyboard. | Must enter decimal values.                                                                                                                                                                                                     |
| Alt+Shift+Ctrl+F12        | Hex to Unicode.                                                                                                                          | In case Alt+X is already taken for another use.                                                                                                                                                                                |
| Alt+Shift+Ctrl+F11        | Selected text will be output to the debugger window and saved to %temp%\\DumpFontInfo.txt.                                               | For Debug only (need to set Flag=8 in Win.ini)                                                                                                                                                                                 |
| Ctrl+Shift+A              | Set all caps.                                                                                                                            |                                                                                                                                                                                                                                |
| Ctrl+Shift+L              | Fiddle bullet style.                                                                                                                     |                                                                                                                                                                                                                                |
| Ctrl+Shift+Right Arrow    | Increase font size.                                                                                                                      | Font size changes by 1 point in the range 4pt-11pt; by 2points for 12pt-28pt; it changes from 28pt -> 36pt -> 48pt -> 72pt -> 80pt; it changes by 10 points in the range 80pt - 1630pt; the maximum value is 1638. |
| Ctrl+Shift+Left Arrow     | Decrease font size.                                                                                                                      | See Ctrl+Shift+Right Arrow comments.                                                                                                                                                                                           |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windowless Rich Edit Controls](windowless-rich-edit-controls.md)
</dt> </dl>

