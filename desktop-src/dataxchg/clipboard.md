---
title: Clipboard
description: The clipboard is a set of functions and messages that enable applications to transfer data.
ms.assetid: '14c91730-a668-495b-9ec6-b835234821a5'
keywords: ["clipboard,about"]
---

# Clipboard

The *clipboard* is a set of functions and messages that enable applications to transfer data. Because all applications have access to the clipboard, data can be easily transferred between applications or within an application.

This overview does not describe how to copy and paste linked or embedded objects. For information on these subjects, see the Component Object Model (COM) documentation.

### In This Section



| Name                                                          | Description                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About the Clipboard](about-the-clipboard.md)<br/>     | Discusses the clipboard.<br/>                                                                                                                                                                                                                                 |
| [Clipboard Formats](clipboard-formats.md)<br/>         | Discusses the clipboard formats. A window can place more than one object on the clipboard, each representing the same information in a different clipboard format. Users need not be aware of the clipboard formats used for an object on the clipboard.<br/> |
| [Clipboard Operations](clipboard-operations.md)<br/>   | Discusses clipboard operations. A window should use the clipboard when cutting, copying, or pasting data. A window places data on the clipboard for cut and copy operations and retrieves data from the clipboard for paste operations.<br/>                  |
| [HTML Clipboard Format](html-clipboard-format.md)<br/> | Discusses the HTML Clipboard format.<br/>                                                                                                                                                                                                                     |
| [Using the Clipboard](using-the-clipboard.md)<br/>     | A clipboard viewer window displays the current content of the clipboard, and receives messages when the clipboard content changes.<br/>                                                                                                                       |
| [Clipboard Reference](clipboard-reference.md)<br/>     | Contains the API reference.<br/>                                                                                                                                                                                                                              |



 

### Clipboard Functions



| Name                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddClipboardFormatListener**](addclipboardformatlistener.md)<br/>       | Places the given window in the system-maintained clipboard format listener list.<br/>                                                                                                                                                                                                                                                                                                                                                                                |
| [**ChangeClipboardChain**](changeclipboardchain.md)<br/>                   | Removes a specified window from the chain of clipboard viewers. <br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| [**CloseClipboard**](closeclipboard.md)<br/>                               | Closes the clipboard. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**CountClipboardFormats**](countclipboardformats.md)<br/>                 | Retrieves the number of different data formats currently on the clipboard. <br/>                                                                                                                                                                                                                                                                                                                                                                                     |
| [**EmptyClipboard**](emptyclipboard.md)<br/>                               | Empties the clipboard and frees handles to data in the clipboard. The function then assigns ownership of the clipboard to the window that currently has the clipboard open. <br/>                                                                                                                                                                                                                                                                                    |
| [**EnumClipboardFormats**](enumclipboardformats.md)<br/>                   | Enumerates the data formats currently available on the clipboard. <br/> Clipboard data formats are stored in an ordered list. To perform an enumeration of clipboard data formats, you make a series of calls to the [**EnumClipboardFormats**](enumclipboardformats.md) function. For each call, the *format* parameter specifies an available clipboard format, and the function returns the next available clipboard format. <br/>                         |
| [**GetClipboardData**](getclipboarddata.md)<br/>                           | Retrieves data from the clipboard in a specified format. The clipboard must have been opened previously. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**GetClipboardFormatName**](getclipboardformatname.md)<br/>               | Retrieves from the clipboard the name of the specified registered format. The function copies the name to the specified buffer. <br/>                                                                                                                                                                                                                                                                                                                                |
| [**GetClipboardOwner**](getclipboardowner.md)<br/>                         | Retrieves the window handle of the current owner of the clipboard. <br/>                                                                                                                                                                                                                                                                                                                                                                                             |
| [**GetClipboardSequenceNumber**](getclipboardsequencenumber.md)<br/>       | Retrieves the clipboard sequence number for the current window station. <br/>                                                                                                                                                                                                                                                                                                                                                                                        |
| [**GetClipboardViewer**](getclipboardviewer.md)<br/>                       | Retrieves the handle to the first window in the clipboard viewer chain. <br/>                                                                                                                                                                                                                                                                                                                                                                                        |
| [**GetOpenClipboardWindow**](getopenclipboardwindow.md)<br/>               | Retrieves the handle to the window that currently has the clipboard open. <br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| [**GetPriorityClipboardFormat**](getpriorityclipboardformat.md)<br/>       | Retrieves the first available clipboard format in the specified list. <br/>                                                                                                                                                                                                                                                                                                                                                                                          |
| [**GetUpdatedClipboardFormats**](getupdatedclipboardformats.md)<br/>       | Retrieves the currently supported Clipboard formats.<br/>                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**IsClipboardFormatAvailable**](isclipboardformatavailable.md)<br/>       | Determines whether the clipboard contains data in the specified format. <br/>                                                                                                                                                                                                                                                                                                                                                                                        |
| [**OpenClipboard**](openclipboard.md)<br/>                                 | Opens the clipboard for examination and prevents other applications from modifying the clipboard content. <br/>                                                                                                                                                                                                                                                                                                                                                      |
| [**RegisterClipboardFormat**](registerclipboardformat.md)<br/>             | Registers a new clipboard format. This format can then be used as a valid clipboard format. <br/>                                                                                                                                                                                                                                                                                                                                                                    |
| [**RemoveClipboardFormatListener**](removeclipboardformatlistener.md)<br/> | Removes the given window from the system-maintained clipboard format listener list.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| [**SetClipboardData**](setclipboarddata.md)<br/>                           | Places data on the clipboard in a specified clipboard format. The window must be the current clipboard owner, and the application must have called the [**OpenClipboard**](openclipboard.md) function. (When responding to the [**WM\_RENDERFORMAT**](wm-renderformat.md) and [**WM\_RENDERALLFORMATS**](wm-renderallformats.md) messages, the clipboard owner must not call **OpenClipboard** before calling [**SetClipboardData**](setclipboarddata.md).)<br/> |
| [**SetClipboardViewer**](setclipboardviewer.md)<br/>                       | Adds the specified window to the chain of clipboard viewers. Clipboard viewer windows receive a [**WM\_DRAWCLIPBOARD**](wm-drawclipboard.md) message whenever the content of the clipboard changes. <br/>                                                                                                                                                                                                                                                           |



 

### Clipboard Messages



| Name                                     | Description                                                                                                                                                                                                                                                             |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CLEAR**](wm-clear.md)<br/> | Sent to an edit control or combo box to delete (clear) the current selection, if any, from the edit control. <br/>                                                                                                                                                |
| [**WM\_COPY**](wm-copy.md)<br/>   | Sent to an edit control or combo box to copy the current selection to the clipboard in [**CF\_TEXT**](standard-clipboard-formats.md#cf-text) format. <br/>                                                                                                       |
| [**WM\_CUT**](wm-cut.md)<br/>     | Sent to an edit control or combo box to delete (cut) the current selection, if any, in the edit control and copy the deleted text to the clipboard in [**CF\_TEXT**](standard-clipboard-formats.md#cf-text) format. <br/>                                        |
| [**WM\_PASTE**](wm-paste.md)<br/> | Sent to an edit control or combo box to copy the current content of the clipboard to the edit control at the current caret position. Data is inserted only if the clipboard contains data in [**CF\_TEXT**](standard-clipboard-formats.md#cf-text) format. <br/> |



 

### Clipboard Notifications



| Name                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_ASKCBFORMATNAME**](wm-askcbformatname.md)<br/>   | Sent to the clipboard owner by a clipboard viewer window to request the name of a [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md#cf-ownerdisplay) clipboard format. <br/>                                                                                                                                                                                                                                 |
| [**WM\_CHANGECBCHAIN**](wm-changecbchain.md)<br/>       | Sent to the first window in the clipboard viewer chain when a window is being removed from the chain. <br/>                                                                                                                                                                                                                                                                                                      |
| [**WM\_CLIPBOARDUPDATE**](wm-clipboardupdate.md)<br/>   | Sent when the contents of the clipboard have changed.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md)<br/> | Sent to the clipboard owner when a call to the [**EmptyClipboard**](emptyclipboard.md) function empties the clipboard. <br/>                                                                                                                                                                                                                                                                                    |
| [**WM\_DRAWCLIPBOARD**](wm-drawclipboard.md)<br/>       | Sent to the first window in the clipboard viewer chain when the content of the clipboard changes. This enables a clipboard viewer window to display the new content of the clipboard. <br/>                                                                                                                                                                                                                      |
| [**WM\_HSCROLLCLIPBOARD**](wm-hscrollclipboard.md)<br/> | Sent to the clipboard owner by a clipboard viewer window. This occurs when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md#cf-ownerdisplay) format and an event occurs in the clipboard viewer's horizontal scroll bar. The owner should scroll the clipboard image and update the scroll bar values. <br/>                                                             |
| [**WM\_PAINTCLIPBOARD**](wm-paintclipboard.md)<br/>     | Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md#cf-ownerdisplay) format and the clipboard viewer's client area needs repainting. <br/>                                                                                                                                                                    |
| [**WM\_RENDERALLFORMATS**](wm-renderallformats.md)<br/> | Sent to the clipboard owner before it is destroyed, if the clipboard owner has delayed rendering one or more clipboard formats. For the content of the clipboard to remain available to other applications, the clipboard owner must render data in all the formats it is capable of generating, and place the data on the clipboard by calling the [**SetClipboardData**](setclipboarddata.md) function. <br/> |
| [**WM\_RENDERFORMAT**](wm-renderformat.md)<br/>         | Sent to the clipboard owner if it has delayed rendering a specific clipboard format and if an application has requested data in that format. The clipboard owner must render data in the specified format and place it on the clipboard by calling the [**SetClipboardData**](setclipboarddata.md) function. <br/>                                                                                              |
| [**WM\_SIZECLIPBOARD**](wm-sizeclipboard.md)<br/>       | Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md#cf-ownerdisplay) format and the clipboard viewer's client area has changed size. <br/>                                                                                                                                                                    |
| [**WM\_VSCROLLCLIPBOARD**](wm-vscrollclipboard.md)<br/> | Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md#cf-ownerdisplay) format and an event occurs in the clipboard viewer's vertical scroll bar. The owner should scroll the clipboard image and update the scroll bar values. <br/>                                                                            |



 

### Structures



| Name                                            | Description                                                                                              |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**METAFILEPICT**](metafilepict.md)<br/> | Defines the metafile picture format used for exchanging metafile data through the clipboard. <br/> |



 

 

 





