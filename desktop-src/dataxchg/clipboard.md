---
title: Clipboard
description: The clipboard is a set of functions and messages that enable applications to transfer data.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\dataexchange\clipboard.htm'
keywords:
- clipboard,about
ms.topic: concept-article
ms.date: 07/09/2025
# customer intent: As a Windows developer, I want to understand how to use the clipboard in my applications so that I can implement data transfer features effectively.
---

# Clipboard

The *clipboard* is a set of functions and messages that enable applications to transfer data. Because all applications have access to the clipboard, data can be easily transferred between applications or within an application.

This overview does not describe how to copy and paste linked or embedded objects. For information on these subjects, see the Component Object Model (COM) documentation.

### In this section

The following topics provide information about the clipboard, clipboard formats, clipboard operations, and clipboard messages. The API reference contains the functions and messages that you can use to work with the clipboard.

| Name | Description |
|------|-------------|
| [About the Clipboard](about-the-clipboard.md) | Discusses the clipboard. |
| [Clipboard Formats](clipboard-formats.md) | Discusses the clipboard formats. A window can place more than one object on the clipboard, each representing the same information in a different clipboard format. Users need not be aware of the clipboard formats used for an object on the clipboard. |
| [Clipboard Operations](clipboard-operations.md) | Discusses clipboard operations. A window should use the clipboard when cutting, copying, or pasting data. A window places data on the clipboard for cut and copy operations and retrieves data from the clipboard for paste operations. |
| [HTML Clipboard Format](html-clipboard-format.md) | Discusses the HTML Clipboard format. |
| [Using the Clipboard](using-the-clipboard.md) | A clipboard viewer window displays the current content of the clipboard, and receives messages when the clipboard content changes. |
| [Clipboard Reference](clipboard-reference.md) | Contains the API reference. |

### Clipboard Functions

The following table lists the functions that you can use to work with the clipboard:

| Name | Description |
|------|-------------|
| [AddClipboardFormatListener](/windows/win32/api/Winuser/nf-winuser-addclipboardformatlistener) | Places the given window in the system-maintained clipboard format listener list. |
| [ChangeClipboardChain](/windows/win32/api/Winuser/nf-winuser-changeclipboardchain) | Removes a specified window from the chain of clipboard viewers. |
| [CloseClipboard](/windows/win32/api/Winuser/nf-winuser-closeclipboard) | Closes the clipboard. |
| [CountClipboardFormats](/windows/win32/api/Winuser/nf-winuser-countclipboardformats) | Retrieves the number of different data formats currently on the clipboard. |
| [EmptyClipboard](/windows/win32/api/Winuser/nf-winuser-emptyclipboard) | Empties the clipboard and frees handles to data in the clipboard. The function then assigns ownership of the clipboard to the window that currently has the clipboard open. |
| [EnumClipboardFormats](/windows/win32/api/Winuser/nf-winuser-enumclipboardformats) | Enumerates the data formats currently available on the clipboard. Clipboard data formats are stored in an ordered list. To perform an enumeration of clipboard data formats, you make a series of calls to the [EnumClipboardFormats](/windows/win32/api/Winuser/nf-winuser-enumclipboardformats) function. For each call, the *format* parameter specifies an available clipboard format, and the function returns the next available clipboard format. |
| [GetClipboardData](/windows/win32/api/Winuser/nf-winuser-getclipboarddata) | Retrieves data from the clipboard in a specified format. The clipboard must have been opened previously. |
| [GetClipboardFormatName](/windows/win32/api/Winuser/nf-winuser-getclipboardformatnamea) | Retrieves from the clipboard the name of the specified registered format. The function copies the name to the specified buffer. |
| [GetClipboardOwner](/windows/win32/api/Winuser/nf-winuser-getclipboardowner) | Retrieves the window handle of the current owner of the clipboard. |
| [GetClipboardSequenceNumber](/windows/win32/api/Winuser/nf-winuser-getclipboardsequencenumber) | Retrieves the clipboard sequence number for the current window station. |
| [GetClipboardViewer](/windows/win32/api/Winuser/nf-winuser-getclipboardviewer) | Retrieves the handle to the first window in the clipboard viewer chain. |
| [GetOpenClipboardWindow](/windows/win32/api/Winuser/nf-winuser-getopenclipboardwindow) | Retrieves the handle to the window that currently has the clipboard open. |
| [GetPriorityClipboardFormat](/windows/win32/api/Winuser/nf-winuser-getpriorityclipboardformat) | Retrieves the first available clipboard format in the specified list. |
| [GetUpdatedClipboardFormats](/windows/win32/api/Winuser/nf-winuser-getupdatedclipboardformats) | Retrieves the currently supported Clipboard formats. |
| [IsClipboardFormatAvailable](/windows/win32/api/Winuser/nf-winuser-isclipboardformatavailable) | Determines whether the clipboard contains data in the specified format. |
| [OpenClipboard](/windows/win32/api/Winuser/nf-winuser-openclipboard) | Opens the clipboard for examination and prevents other applications from modifying the clipboard content. |
| [RegisterClipboardFormat](/windows/win32/api/Winuser/nf-winuser-registerclipboardformata) | Registers a new clipboard format. This format can then be used as a valid clipboard format. |
| [RemoveClipboardFormatListener](/windows/win32/api/Winuser/nf-winuser-removeclipboardformatlistener) | Removes the given window from the system-maintained clipboard format listener list. |
| [SetClipboardData](/windows/win32/api/winuser/nf-winuser-setclipboarddata) | Places data on the clipboard in a specified clipboard format. The window must be the current clipboard owner, and the application must have called the [OpenClipboard](/windows/win32/api/winuser/nf-winuser-openclipboard) function. (When responding to the [WM\_RENDERFORMAT](wm-renderformat.md) message, the clipboard owner must not call OpenClipboard before calling [SetClipboardData](/windows/win32/api/winuser/nf-winuser-setclipboarddata).) |
| [SetClipboardViewer](/windows/win32/api/Winuser/nf-winuser-setclipboardviewer) | Adds the specified window to the chain of clipboard viewers. Clipboard viewer windows receive a [WM\_DRAWCLIPBOARD](wm-drawclipboard.md) message whenever the content of the clipboard changes. |

### Clipboard messages

The following table lists the messages that are sent to clipboard viewer windows:

| Name | Description |
|------|-------------|
| [WM\_CLEAR](wm-clear.md) | Sent to an edit control or combo box to delete (clear) the current selection, if any, from the edit control. |
| [WM\_COPY](wm-copy.md) | Sent to an edit control or combo box to copy the current selection to the clipboard in [CF\_TEXT](standard-clipboard-formats.md) format. |
| [WM\_CUT](wm-cut.md) | Sent to an edit control or combo box to delete (cut) the current selection, if any, in the edit control and copy the deleted text to the clipboard in [CF\_TEXT](standard-clipboard-formats.md) format. |
| [WM\_PASTE](wm-paste.md) | Sent to an edit control or combo box to copy the current content of the clipboard to the edit control at the current caret position. Data is inserted only if the clipboard contains data in [CF\_TEXT](standard-clipboard-formats.md) format. |

### Clipboard Notifications

The following table lists the clipboard notification messages that are sent to clipboard viewer windows:

| Name | Description |
|------|-------------|
| [WM\_ASKCBFORMATNAME](wm-askcbformatname.md) | Sent to the clipboard owner by a clipboard viewer window to request the name of a [CF\_OWNERDISPLAY](standard-clipboard-formats.md) clipboard format. |
| [WM\_CHANGECBCHAIN](wm-changecbchain.md) | Sent to the first window in the clipboard viewer chain when a window is being removed from the chain. |
| [WM\_CLIPBOARDUPDATE](wm-clipboardupdate.md) | Sent when the contents of the clipboard have changed. |
| [WM\_DESTROYCLIPBOARD](wm-destroyclipboard.md) | Sent to the clipboard owner when a call to the [EmptyClipboard](/windows/win32/api/Winuser/nf-winuser-emptyclipboard) function empties the clipboard. |
| [WM\_DRAWCLIPBOARD](wm-drawclipboard.md) | Sent to the first window in the clipboard viewer chain when the content of the clipboard changes. This enables a clipboard viewer window to display the new content of the clipboard. |
| [WM\_HSCROLLCLIPBOARD](wm-hscrollclipboard.md) | Sent to the clipboard owner by a clipboard viewer window. This occurs when the clipboard contains data in the [CF\_OWNERDISPLAY](standard-clipboard-formats.md) format and an event occurs in the clipboard viewer's horizontal scroll bar. The owner should scroll the clipboard image and update the scroll bar values. |
| [WM\_PAINTCLIPBOARD](wm-paintclipboard.md) | Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [CF\_OWNERDISPLAY](standard-clipboard-formats.md) format and the clipboard viewer's client area needs repainting. |
| [WM\_RENDERALLFORMATS](wm-renderallformats.md) | Sent to the clipboard owner before it is destroyed, if the clipboard owner has delayed rendering one or more clipboard formats. For the content of the clipboard to remain available to other applications, the clipboard owner must render data in all the formats it is capable of generating, and place the data on the clipboard by calling the [SetClipboardData](/windows/win32/api/Winuser/nf-winuser-setclipboarddata) function. |
| [WM\_RENDERFORMAT](wm-renderformat.md) | Sent to the clipboard owner if it has delayed rendering a specific clipboard format and if an application has requested data in that format. The clipboard owner must render data in the specified format and place it on the clipboard by calling the [SetClipboardData](/windows/win32/api/Winuser/nf-winuser-setclipboarddata) function. |
| [WM\_SIZECLIPBOARD](wm-sizeclipboard.md) | Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [CF\_OWNERDISPLAY](standard-clipboard-formats.md) format and the clipboard viewer's client area has changed size. |
| [WM\_VSCROLLCLIPBOARD](wm-vscrollclipboard.md) | Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [CF\_OWNERDISPLAY](standard-clipboard-formats.md) format and an event occurs in the clipboard viewer's vertical scroll bar. The owner should scroll the clipboard image and update the scroll bar values. |

### Structures

The following table lists the structures that are used with the clipboard:

| Name | Description |
|------|-------------|
| [METAFILEPICT](/windows/win32/api/wingdi/ns-wingdi-metafilepict) | Defines the metafile picture format used for exchanging metafile data through the clipboard. |
