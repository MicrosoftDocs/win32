---
title: Edit Control Text Operations
description: The system automatically processes all user-initiated text operations and notifies the application when the operations are completed.
ms.assetid: 9af3a1bc-4c87-4cc9-966d-50742be7c811
ms.topic: article
ms.date: 05/31/2018
---

# Edit Control Text Operations

The system automatically processes all user-initiated text operations and notifies the application when the operations are completed.

The following topics discuss user-initiated text operations and the application's response:

-   [Selecting an Edit Control](#selecting-an-edit-control)
-   [Setting and Retrieving Text](#setting-and-retrieving-text)
-   [Selecting Text](#selecting-text)
-   [Replacing Text](#replacing-text)
-   [Changing the Font Used by an Edit Control](#changing-the-font-used-by-an-edit-control)
-   [Cut Copy Paste and Clear Operations](#cut-copy-paste-and-clear-operations)
-   [Modifying Text](#modifying-text)
-   [Limiting User Entered Text](#limiting-user-entered-text)
-   [Character and Line Operations](#character-and-line-operations)
-   [Scrolling Text in an Edit Control](#scrolling-text-in-an-edit-control)
-   [Setting Tab Stops and Margins](#setting-tab-stops-and-margins)
-   [Concealing User Input](#concealing-user-input)
-   [Using Integers](#using-integers)
-   [Undoing Text Operations](#undoing-text-operations)
-   [Handling Wordwrap and Line Breaks](#handling-wordwrap-and-line-breaks)
-   [Retrieving Points and Characters](#retrieving-points-and-characters)
-   [Autocompletion of Strings](#autocompletion-of-strings)
-   [Complex Script in Edit Controls](#complex-script-in-edit-controls)

## Selecting an Edit Control

The user can select an edit control by clicking it with the mouse or by pressing the TAB key to move to it. The tabbing method is part of a predefined keyboard interface that the system provides. For a complete description of this interface, see [Dialog Boxes](/windows/desktop/dlgbox/dialog-boxes). When the user selects an edit control, the system gives the control the keyboard focus (see "Keyboard Focus and Activation" in [About Keyboard Input](/windows/desktop/inputdev/about-keyboard-input)) and highlights its text by using reverse video.

## Setting and Retrieving Text

An application can set the text of an edit control by using the [**SetWindowText**](/windows/desktop/api/winuser/nf-winuser-setwindowtexta) function, the [**SetDlgItemText**](/windows/desktop/DevNotes/-setdlgitemtext) function, or by sending the control a [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message.

To retrieve all text from an edit control, first use the [**GetWindowTextLength**](/windows/desktop/api/winuser/nf-winuser-getwindowtextlengtha) function or the [**WM\_GETTEXTLENGTH**](/windows/desktop/winmsg/wm-gettextlength) message to determine the size of buffer needed to contain the text. Next, retrieve the text by using the [**GetWindowText**](/windows/desktop/DevNotes/-getwindowtext) function, the [**GetDlgItemText**](/windows/desktop/api/winuser/nf-winuser-getdlgitemtexta) function, or the [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext) message.

## Selecting Text

After selecting an edit control, the user can select text in the control by using the mouse or the keyboard. An application can retrieve the starting and ending character positions of the current selection in an edit control by sending the control an [**EM\_GETSEL**](em-getsel.md) message. The return value for the ending position is one greater than the last character in the selection (that is, the position of the first character following the last selected character).

An application can also select text in an edit control by sending the control an [**EM\_SETSEL**](em-setsel.md) message with the starting and ending character indexes for the selection. For example, the application can use **EM\_SETSEL** with [**EM\_REPLACESEL**](em-replacesel.md) to delete text from an edit control.

These three messages apply to both single-line and multiline edit controls.

## Replacing Text

An application can replace selected text in an edit control by sending the control an [**EM\_REPLACESEL**](em-replacesel.md) message with a pointer to the replacement text. If there is no current selection, **EM\_REPLACESEL** inserts the replacement text at the insertion point. The application may receive an [EN\_ERRSPACE](en-errspace.md) notification code if the replacement text exceeds the available memory. This message applies to both single-line and multiline edit controls.

An application can use [**EM\_REPLACESEL**](em-replacesel.md) to replace part of an edit control's text or the [**SetDlgItemText**](/windows/desktop/api/winuser/nf-winuser-setdlgitemtexta) function to replace all of it.

## Changing the Font Used by an Edit Control

An application can change the font that an edit control uses by sending the [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont) message. Most applications do this while processing the [**WM\_INITDIALOG**](/windows/desktop/dlgbox/wm-initdialog) message. Changing the font does not change the size of the edit control; applications that send the **WM\_SETFONT** message may have to retrieve the font metrics for the text and recalculate the size of the edit control. For more information about fonts and font metrics, see [Fonts and Text](/windows/desktop/gdi/fonts-and-text).

## Cut Copy Paste and Clear Operations

There are four messages for moving text between an edit control and the clipboard. The [**WM\_COPY**](/windows/desktop/dataxchg/wm-copy) message copies the current selection (if any) from an edit control to the clipboard without deleting it from the edit control. The [**WM\_CUT**](/windows/desktop/dataxchg/wm-cut) message deletes the current selection (if any) in the edit control and copies the deleted text to the clipboard. The [**WM\_CLEAR**](/windows/desktop/dataxchg/wm-clear) message deletes the current selection (if any) from an edit control, but does not copy it to the clipboard (unless the user pressed the SHIFT key). The [**WM\_PASTE**](/windows/desktop/dataxchg/wm-paste) message copies text from the clipboard into an edit control at the insertion point. These four messages apply to both single-line and multiline edit controls.

Microsoft Windows NT 4.0 and later: An edit control includes a built-in context menu that makes it easy for the user to move text between the edit control and the clipboard. The context menu appears when the user right-clicks the control. The commands in the context menu include **Undo**, **Cut**, **Copy**, **Paste**, **Delete**, and **Select All**.

## Modifying Text

The user can select, delete, or move text in an edit control. The system maintains an internal flag for each edit control indicating whether the content of the control has been modified. The system clears this flag when it creates the control and sets the flag whenever the text in the control is modified. An application can retrieve the modification flag by sending the control an [**EM\_GETMODIFY**](em-getmodify.md) message. The application can then set or clear the modification flag by sending the control an [**EM\_SETMODIFY**](em-setmodify.md) message. These messages apply to both single-line and multiline edit controls.

## Limiting User Entered Text

The default limit to the amount of text a user can enter in an edit control is 32 KB. An application can change the default limit by sending the control an [**EM\_SETLIMITTEXT**](em-setlimittext.md) message. This message sets a hard limit to the number of bytes the user can enter into an edit control, but affects neither text that is already in the control when the message was sent nor text copied to the control by the [**SetDlgItemText**](/windows/desktop/api/winuser/nf-winuser-setdlgitemtexta) function or the [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message. For example, suppose that the application uses the **SetDlgItemText** function to place 500 bytes in an edit control, and the user also enters 500 bytes (1,000 bytes total). If the application then sends an **EM\_SETLIMITTEXT** message limiting user-entered text to 300 bytes, the 1,000 bytes already in the edit control remain there, and the user cannot add any more text. On the other hand, if the application sends an **EM\_SETLIMITTEXT** message limiting user-entered text to 1,300 bytes, the 1,000 bytes remain, but the user can add 300 more bytes.

When the user reaches the character limit of an edit control, the system sends the application a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message containing an [EN\_MAXTEXT](en-maxtext.md) notification code. This notification code does not mean that memory has been exhausted, but that the limit for user-entered text has been reached; the user cannot enter any more text. To change this limit, an application must send the control a new [**EM\_SETLIMITTEXT**](em-setlimittext.md) message with a higher limit.

As an example of the use of [**EM\_SETLIMITTEXT**](em-setlimittext.md) and [EN\_MAXTEXT](en-maxtext.md), suppose that the application must limit the user to no more than four characters in an edit control. The application would use **EM\_SETLIMITTEXT** to specify a four-character limit. If the user tried to enter a fifth character, the system would send an EN\_MAXTEXT notification code to the application.

## Character and Line Operations

There are several messages that return information about the characters and lines in an edit control. Most of the messages return an index, usually a zero-based number, to refer to a character or line. For example, in a single-line edit control that contains n characters, the line index is zero and the characters are indexed from zero to n-1. In a multiline edit control that contains m lines and n characters, the lines are indexed from zero to m-1, and the characters are indexed from zero to n-1. Note that character indexing ignores line breaks.

An application can determine the number of characters in an edit control by sending the [**WM\_GETTEXTLENGTH**](/windows/desktop/winmsg/wm-gettextlength) message to the edit control. This message returns the length, in characters (not including the terminating null character), of the text in a single-line or multiline edit control. The [**EM\_LINELENGTH**](em-linelength.md) message returns the length, in characters, of a line specified by the character index of a character in the line. The returned length does not include any selected characters. An application can use these messages in a single-line or multiline edit control.

The [**EM\_GETFIRSTVISIBLELINE**](em-getfirstvisibleline.md) message returns the zero-based index of the uppermost visible line in a multiline edit control, or the zero-based index of the first visible character in a single-line edit control. An application can copy a line from an edit control to a buffer by sending the [**EM\_GETLINE**](em-getline.md) message to the edit control. The line is specified by its line index and the first word of the receiving buffer contains the maximum number of bytes to be copied to the buffer. The return value is the number of bytes copied. This message can also be used in a single-line or multiline edit control.

There are unique messages available to return the information about a line in a multiline edit control. The [**EM\_GETLINECOUNT**](em-getlinecount.md) message returns the number of lines in an edit control. The [**EM\_LINEFROMCHAR**](em-linefromchar.md) message returns the index of the line containing a specified character index. The [**EM\_LINEINDEX**](em-lineindex.md) message returns the index of the first character in a specified line.

## Scrolling Text in an Edit Control

To implement scrolling in an edit control, you can use the automatic scrolling styles discussed in [Edit Control Types and Styles](about-edit-controls.md), or you can explicitly add scroll bars to the edit control. To add a horizontal scroll bar, use the style WS\_HSCROLL; to add a vertical scroll bar, use the style [**WS\_VSCROLL**](/windows/desktop/winmsg/window-styles). An edit control with scroll bars processes its own scroll bar messages. For detailed information about adding scroll bars to edit controls, see [Scroll Bars](scroll-bars.md).

The system provides three messages that an application can send to an edit control with scroll bars. The [**EM\_LINESCROLL**](em-linescroll.md) message can scroll a multiline edit control both vertically and horizontally. The *lParam* parameter specifies the number of lines to scroll vertically starting from the current line and the *wParam* parameter specifies the number of characters to scroll horizontally, starting from the current character. The edit control does not acknowledge horizontal scrolling messages if it has the [**ES\_CENTER**](edit-control-styles.md) or [**ES\_RIGHT**](edit-control-styles.md) style. The **EM\_LINESCROLL** message applies to multiline edit controls only.

The [**EM\_SCROLL**](em-scroll.md) message scrolls a multiline edit control vertically. The *wParam* parameter specifies the scrolling action. The **EM\_SCROLL** message applies to multiline edit controls only. **EM\_SCROLL** has the same effect as the [**WM\_VSCROLL**](wm-vscroll.md) message.

The [**EM\_SCROLLCARET**](em-scrollcaret.md) message scrolls the caret into view in an edit control.

## Setting Tab Stops and Margins

An application can set tab stops in a multiline edit control by using the [**EM\_SETTABSTOPS**](em-settabstops.md) message. (The default for a tab stop is eight characters.) When an application adds text to the edit control, tab characters in the text automatically generate space up to the next tab stop. The **EM\_SETTABSTOPS** message does not automatically cause the system to redraw the text. To do that, an application can call the [**InvalidateRect**](/windows/desktop/api/winuser/nf-winuser-invalidaterect) function. The **EM\_SETTABSTOPS** message applies to multiline edit controls only.

An application can set the width of the left and right margins for an edit control by using the [**EM\_SETMARGINS**](em-setmargins.md) message. After sending this message, the system redraws the edit control to reflect the new margin settings. An application can retrieve the width of the left or right margin by sending the [**EM\_GETMARGINS**](em-getmargins.md) message. By default, the edit control margins are set just wide enough to accommodate the largest character horizontal overhang (negative ABC widths) for the current font being used in the edit control.

## Concealing User Input

An application can use a password character in an edit control to conceal user input. When a password character is set, it is displayed in place of each character the user types. When a password character is removed, the control displays the characters the user types. If the application creates a single-line edit control using the style [**ES\_PASSWORD**](edit-control-styles.md), the default password character is an asterisk (\*). An application can use the [**EM\_SETPASSWORDCHAR**](em-setpasswordchar.md) message to remove or define a different password character and the [**EM\_GETPASSWORDCHAR**](em-getpasswordchar.md) message to retrieve the current password character. These messages apply to single-line edit controls only.

## Using Integers

There are two integer-conversion functions for edit controls designed to contain numbers only. The [**SetDlgItemInt**](/windows/desktop/api/winuser/nf-winuser-setdlgitemint) function creates the string representation of a specified integer (signed or unsigned) and sends the string to an edit control. **SetDlgItemInt** returns no value. The [**GetDlgItemInt**](/windows/desktop/api/winuser/nf-winuser-getdlgitemint) function creates an integer (signed or unsigned) from its string representation in an edit control. **GetDlgItemInt** returns the integer (or an error value).

## Undoing Text Operations

Every edit control maintains an undo flag that indicates whether an application can reverse or undo the most recent operation on the edit control (undoing a text deletion, for example). The edit control sets the undo flag to indicate that the operation can be undone and resets it to indicate that the operation cannot be undone. An application can determine the setting of the undo flag by sending the control an [**EM\_CANUNDO**](em-canundo.md) message.

An application can undo the most recent operation by sending the control an [**EM\_UNDO**](em-undo.md) message. An operation can be undone provided no other edit control operation occurs first. For example, the user can delete text, replace the text (undo the deletion), and then delete the text again (undo the replacement). The **EM\_UNDO** message applies to both single-line and multiline edit controls and always works for single-line edit controls.

An application can reset an edit control's undo flag by sending the control an [**EM\_EMPTYUNDOBUFFER**](em-emptyundobuffer.md) message. The system automatically resets the undo flag whenever an edit control receives an [**EM\_SETHANDLE**](em-sethandle.md) or [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message. The [**SetDlgItemText**](/windows/desktop/api/winuser/nf-winuser-setdlgitemtexta) function sends a **WM\_SETTEXT** message.

## Handling Wordwrap and Line Breaks

An application can use Wordwrap functions with multiline edit controls to locate the word or word fragment that should be wrapped to the next line. Using the default Wordwrap function provided by the system, lines always end at the spaces between words. An application can specify its own Wordwrap function by supplying an [*EditWordBreakProc*](/windows/win32/api/winuser/nc-winuser-editwordbreakproca) Wordwrap function and sending the edit control an [**EM\_SETWORDBREAKPROC**](em-setwordbreakproc.md) message. An application can retrieve the address of the current Wordwrap function by sending the control an [**EM\_GETWORDBREAKPROC**](em-getwordbreakproc.md) message.

An application may direct a multiline edit control to add or remove a soft line break character (two carriage returns and a line feed) automatically at the end of wrapped-text lines. An application can turn this feature on or off by sending the edit control an [**EM\_FMTLINES**](em-fmtlines.md) message. This message applies only to multiline edit controls and does not affect a line that ends with a hard line break (one carriage return and a line feed entered by the user). Also in multiline edit controls, an application can specify the [**ES\_WANTRETURN**](edit-control-styles.md) style to request that the system insert a carriage return when the user presses the ENTER key in the edit control.

## Retrieving Points and Characters

To determine the character closest to a specified point in the client area of an edit control, send the [**EM\_CHARFROMPOS**](em-charfrompos.md) message to the control. The message returns the character index and line index of the character nearest the point. Similarly, you can retrieve the client area coordinates of a specified character by sending the [**EM\_POSFROMCHAR**](em-posfromchar.md) message. The message returns the x and y coordinates of the upper-left corner of the specified character.

## Autocompletion of Strings

Autocompletion expands strings that have been partially entered in an edit control into complete strings. For example, when a user starts to enter a URL in the Address edit control that is embedded in the Windows Internet Explorer toolbar, autocompletion expands the string into one or more complete URLs that are consistent with the existing partial string. A partial URL string such as "mic" might be expanded to "https://www.microsoft.com" or "https://www.microsoft.com/windows". Autocompletion is typically used with edit controls or with controls that have an embedded edit control.

For more information, see the [**IAutoComplete**](/windows/desktop/api/shldisp/nn-shldisp-iautocomplete) and [**IAutoComplete2**](/windows/desktop/api/shldisp/nn-shldisp-iautocomplete2) interface documentation.

## Complex Script in Edit Controls

A *complex script* is a language whose printed form is not laid out in a simple way. For example, a complex script may allow bidirectional rendering, contextual shaping of glyphs, or combining characters. The standard edit controls have been extended to support multilingual text and complex scripts. This includes not only input and display, but also correct cursor movement over character clusters (in Thai and Devanagari script, for example).

A well-written application receives this support automatically, without modification. Again, you should consider adding support for right-to-left reading order and right alignment. In this case, toggle the extended style flags of the edit control window to control these attributes, as shown in the following example.


```
// ID_EDITCONTROL is the control ID in the resource file.
HANDLE hWndEdit = GetDlgItem(hDlg, ID_EDITCONTROL);
LONG lAlign = GetWindowLong(hWndEdit, GWL_EXSTYLE) ;

// To toggle alignment
lAlign ^= WS_EX_RIGHT ;

// To toggle reading order
lAlign ^= WS_EX_RTLREADING ;
```



After setting the **lAlign** value, enable the new display by setting the extended style of the edit control window as follows.


```
// This assumes your edit control is in a dialog box. If not, 
// get the edit control handle from another source.

SetWindowLong(hWndEdit, GWL_EXSTYLE, lAlign);
InvalidateRect(hWndEdit, NULL, FALSE);
```



Uniscribe is another set of functions that provide fine control for processing complex scripts. For more information, see [Uniscribe](/windows/desktop/Intl/uniscribe).

 

 