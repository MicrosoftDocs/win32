---
title: About the Clipboard
description: This section discusses the clipboard.
ms.assetid: 14c91730-a668-495b-9ec6-b835234821a5
keywords:
- clipboard,about
- clipboard,formats
- clipboard,commands
- clipboard,windows
- clipboard,sequence numbers
- clipboard,viewers
- clipboard,viewer windows
- clipboard,display formats
- clipboard,owner display formats
- display clipboard formats
- owner display clipboard formats
ms.topic: article
ms.date: 05/31/2018
---

# About the Clipboard

The *clipboard* is a set of functions and messages that enable applications to transfer data. Because all applications have access to the clipboard, data can be easily transferred between applications or within an application.

The clipboard is user-driven. A window should transfer data to or from the clipboard only in response to a command from the user. A window must not use the clipboard to transfer data without the user's knowledge.

A memory object on the clipboard can be in any data format, called a clipboard format. Each format is identified by an unsigned integer value. For standard (predefined) clipboard formats, this value is a constant defined in Winuser.h; for registered clipboard formats, it is the return value of the [**RegisterClipboardFormat**](/windows/desktop/api/Winuser/nf-winuser-registerclipboardformata) function.

Except for registering clipboard formats, individual windows perform most clipboard operations. Typically, a window procedure transfers information to or from the clipboard in response to the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.

This section discusses the following:

-   [Clipboard Commands](#clipboard-commands)
-   [Clipboard Sequence Number](#clipboard-sequence-number)
-   [Clipboard Viewers](#clipboard-viewers)
    -   [Clipboard Viewer Windows](#clipboard-viewer-windows)
    -   [Display Formats](#display-formats)
    -   [Owner Display Format](#owner-display-format)
-   [Related topics](#related-topics)

## Clipboard Commands

A user typically carries out clipboard operations by choosing commands from an application's **Edit** menu. Following is a brief description of the standard clipboard commands.



|  Command        |  Description                                                                                                                                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cut**    | Places a copy of the current selection on the clipboard and deletes the selection from the document. The previous content of the clipboard is destroyed.                                                          |
| **Copy**   | Places a copy of the current selection on the clipboard. The document remains unchanged. The previous content of the clipboard is destroyed.                                                                      |
| **Paste**  | Replaces the current selection with the content of the clipboard. The content of the clipboard is not changed.                                                                                                    |
| **Delete** | Deletes the current selection from the document. The content of the clipboard is not changed. This command does not involve the clipboard, but it should appear with the clipboard commands on the **Edit** menu. |



 

## Clipboard Sequence Number

The clipboard for each window station has an associated clipboard sequence number. This number is incremented whenever the contents of the clipboard change. To obtain the clipboard sequence number, call the [**GetClipboardSequenceNumber**](/windows/desktop/api/Winuser/nf-winuser-getclipboardsequencenumber) function.

## Clipboard Viewers

A clipboard viewer is a window that displays the current content of the clipboard. The clipboard viewer window is a convenience for the user and does not affect the data-transaction functions of the clipboard.

Typically, a clipboard viewer window can display at least the three most common formats: **CF\_TEXT**, **CF\_BITMAP**, and **CF\_METAFILEPICT**. If a window does not make data available in any of these three formats, it should provide data in a display format or use the owner-display format.

A *clipboard viewer chain* is the linking together of two or more entities so that they are dependent upon one another for operation. This interdependency (chain) allows all running clipboard viewer applications to receive the messages sent to the current clipboard.

The following topics are discussed in this section.

-   [Clipboard Viewer Windows](#clipboard-viewer-windows)
-   [Display Formats](#display-formats)
-   [Owner Display Format](#owner-display-format)

### Clipboard Viewer Windows

A window adds itself to the clipboard viewer chain by calling the [**SetClipboardViewer**](/windows/desktop/api/Winuser/nf-winuser-setclipboardviewer) function. The return value is the handle to the next window in the chain. To retrieve the handle to the first window in the chain, call the [**GetClipboardViewer**](/windows/desktop/api/Winuser/nf-winuser-getclipboardviewer) function.

Each clipboard viewer window must keep track of the next window in the clipboard viewer chain. When the content of the clipboard changes, the system sends a [**WM\_DRAWCLIPBOARD**](wm-drawclipboard.md) message to the first window in the chain. After updating its display, each clipboard viewer window must pass this message on to the next window in the chain.

Before closing, a clipboard viewer window must remove itself from the clipboard viewer chain by calling the [**ChangeClipboardChain**](/windows/desktop/api/Winuser/nf-winuser-changeclipboardchain) function. The system then sends a [**WM\_CHANGECBCHAIN**](wm-changecbchain.md) message to the first window in the chain.

For more information about processing the [**WM\_DRAWCLIPBOARD**](wm-drawclipboard.md) and [**WM\_CHANGECBCHAIN**](wm-changecbchain.md) messages, see [Creating a Clipboard Viewer Window](using-the-clipboard.md).

### Display Formats

A display format is a clipboard format used to display information in a clipboard viewer window. A clipboard owner that uses a private or registered clipboard format, and none of the most common standard formats, must provide data in a display format for viewing in a clipboard viewer window. The display formats are intended for viewing only and must not be pasted into a document.

The four display formats are: **CF\_DSPBITMAP**, **CF\_DSPMETAFILEPICT**, **CF\_DSPTEXT**, and **CF\_DSPENHMETAFILE**. These display formats are rendered in the same way as the standard formats, which are: **CF\_BITMAP**, **CF\_TEXT**, **CF\_METAFILEPICT**, and **CF\_ENHMETAFILE**.

### Owner Display Format

For a clipboard owner that does not use any of the common standard clipboard formats, an alternative to providing a display format is to use the owner-display (**CF\_OWNERDISPLAY**) clipboard format.

By using the owner-display format, a clipboard owner can avoid the overhead of rendering data in an additional format by taking direct control over painting the clipboard viewer window. The clipboard viewer window sends messages to the clipboard owner whenever a portion of the window must be repainted or when the window is scrolled or resized.

## Related topics

<dl> <dt>

[Standard Clipboard Formats](standard-clipboard-formats.md)
</dt> </dl>

 

 