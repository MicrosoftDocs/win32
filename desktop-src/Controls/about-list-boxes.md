---
title: About List Boxes
description: This section describes list box features.
ms.assetid: 359bb363-5b97-4e0c-bdc4-bfa6a6504a76
ms.topic: article
ms.date: 05/31/2018
---

# About List Boxes

A list box control contains a simple list from which the user can generally select one or more items. List boxes provide limited flexibility compared with [List View](list-view-control-reference.md) controls.

List box items can be represented by text strings, bitmaps, or both. If the list box is not large enough to display all the list box items at once, the list box provides a scroll bar. The user scrolls through the list box items and applies or removes selection status as necessary. Selecting a list box item changes its visual appearance, usually by changing the text and background colors to those specified by the relevant operating system metrics. When the user selects or deselects an item, the system sends a notification message to the parent window of the list box.

For an ANSI application, the system converts the text in a list box to Unicode by using the **CP\_ACP** code page. This can cause problems. For example, accented Roman characters in a non-Unicode list box in Windows, Japanese version will come out garbled. To fix this, either compile the application as Unicode or use an owner-drawn list box.

This section discusses the following topics:

-   [Creating a List Box](#creating-a-list-box)
-   [List Box Types and Styles](#list-box-types-and-styles)
-   [List Box Functions](#list-box-functions)
-   [Notification Messages from List Boxes](#notification-messages-from-list-boxes)
-   [Messages to List Boxes](#notification-messages-from-list-boxes)
-   [Default Window Message Processing](#default-window-message-processing)
-   [Owner-Drawn List Boxes](#owner-drawn-list-boxes)
-   [Drag List Boxes](#drag-list-boxes)
    -   [Creating Drag List Boxes](#creating-drag-list-boxes)
    -   [Drag List Box Messages](#drag-list-box-messages)
    -   [Drag List Box Notification Codes](#drag-list-box-notification-codes)

## Creating a List Box

The easiest way to create a list box in a dialog box is to drag it from the Toolbox in Microsoft Visual Studio onto your dialog resource. To create a list box dynamically, or to create a list box in a window other than a dialog box, use the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, specifying the [**WC\_LISTBOX**](common-control-window-classes.md) window class and the appropriate [list box styles](list-box-styles.md).

## List Box Types and Styles

There are two types of list boxes: single-selection (the default) and multiple-selection. In a single-selection list box, the user can select only one item at a time. In a multiple-selection list box, the user can select more than one item at a time. To create a multiple-selection list box, specify the [**LBS\_MULTIPLESEL**](list-box-styles.md) or the [**LBS\_EXTENDEDSEL**](list-box-styles.md) style.

The appearance and operation of a list box is controlled by [list box styles](list-box-styles.md) and window styles. These styles indicate whether the list is sorted, arranged in multiple columns, drawn by the application, and so on. The dimensions and styles of a list box are typically defined in a dialog box template that is included in an application's resources.

> [!Note]  
> To use visual styles with these controls, an application must include a manifest and must call [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols) at the beginning of the program. For information on visual styles, see [Visual Styles](themes-overview.md). For information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## List Box Functions

The [**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista) function replaces the contents of a list box with the names of drives, directories, and files that match a specified set of criteria. The [**DlgDirSelectEx**](/windows/desktop/api/Winuser/nf-winuser-dlgdirselectexa) function retrieves the current selection in a list box that is initialized by **DlgDirList**. These functions make it possible for the user to select a drive, directory, or file from a list box without typing the location and name of the file.

Also, the [**GetListBoxInfo**](/windows/desktop/api/Winuser/nf-winuser-getlistboxinfo) function returns the number of items per column in a specified list box.

## Notification Messages from List Boxes

When an event occurs in a list box, the list box sends a notification code, in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message, to the dialog box procedure of the owner window. List box notification codes are sent when a user selects, double-clicks, or cancels a list box item; when the list box receives or loses the keyboard focus; and when the system cannot allocate enough memory for a list box request. A **WM\_COMMAND** message contains the list box identifier in the low-order word of the *wParam* parameter, and the notification code in the high-order word. The *lParam* parameter contains the control window handle.

A dialog box procedure is not required to process these messages; the default window procedure processes them.

An application should monitor and process the following list box notification codes.



| Notification code                   | Description                                                      |
|-------------------------------------|------------------------------------------------------------------|
| [LBN\_DBLCLK](lbn-dblclk.md)       | The user double-clicks an item in the list box.                  |
| [LBN\_ERRSPACE](lbn-errspace.md)   | The list box cannot allocate enough memory to fulfill a request. |
| [LBN\_KILLFOCUS](lbn-killfocus.md) | The list box loses the keyboard focus.                           |
| [LBN\_SELCANCEL](lbn-selcancel.md) | The user cancels the selection of an item in the list box.       |
| [LBN\_SELCHANGE](lbn-selchange.md) | The selection in a list box is about to change.                  |
| [LBN\_SETFOCUS](lbn-setfocus.md)   | The list box receives the keyboard focus.                        |



 

## Messages to List Boxes

A dialog box procedure can send messages to a list box to add, delete, examine, and change list box items. For example, a dialog box procedure could send an [**LB\_ADDSTRING**](lb-addstring.md) message to a list box to add an item, and an [**LB\_GETSEL**](lb-getsel.md) message to determine whether the item is selected. Other messages set and retrieve information about the size, appearance, and behavior of the list box. For example, the [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) message sets the scrollable width of a list box. A dialog box procedure can send any message to a list box by using the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) or [**SendDlgItemMessage**](/windows/desktop/api/winuser/nf-winuser-senddlgitemmessagea) function.

A list box item is often referenced by its *index*, an integer that represents the item's position in the list box. The index of the first item in a list box is 0, the index of the second item is 1, and so on.

The following table describes how the predefined list box procedure responds to list box messages.



| Message                                                   | Response                                                                                                                                                                                                                         |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LB\_ADDFILE**](lb-addfile.md)                         | Inserts a file into a directory list box that is filled by the [**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista) function and retrieves the list box index of the inserted item.                                                                  |
| [**LB\_ADDSTRING**](lb-addstring.md)                     | Adds a string to a list box and returns its index.                                                                                                                                                                               |
| [**LB\_DELETESTRING**](lb-deletestring.md)               | Removes a string from a list box and returns the number of strings that remain in the list.                                                                                                                                      |
| [**LB\_DIR**](lb-dir.md)                                 | Adds a list of file names to a list box and returns the index of the last file name added.                                                                                                                                       |
| [**LB\_FINDSTRING**](lb-findstring.md)                   | Returns the index of the first string in the list box that begins with a specified string.                                                                                                                                       |
| [**LB\_FINDSTRINGEXACT**](lb-findstringexact.md)         | Returns the index of the string in the list box that is equal to a specified string.                                                                                                                                             |
| [**LB\_GETANCHORINDEX**](lb-getanchorindex.md)           | Returns the index of the item that the mouse last selected.                                                                                                                                                                      |
| [**LB\_GETCARETINDEX**](lb-getcaretindex.md)             | Returns the index of the item that has the focus rectangle.                                                                                                                                                                      |
| [**LB\_GETCOUNT**](lb-getcount.md)                       | Returns the number of items in the list box.                                                                                                                                                                                     |
| [**LB\_GETCURSEL**](lb-getcursel.md)                     | Returns the index of the currently selected item.                                                                                                                                                                                |
| [**LB\_GETHORIZONTALEXTENT**](lb-gethorizontalextent.md) | Returns the scrollable width, in pixels, of a list box.                                                                                                                                                                          |
| [**LB\_GETITEMDATA**](lb-getitemdata.md)                 | Returns the value that is associated with the specified item.                                                                                                                                                                    |
| [**LB\_GETITEMHEIGHT**](lb-getitemheight.md)             | Returns the height, in pixels, of an item in a list box.                                                                                                                                                                         |
| [**LB\_GETITEMRECT**](lb-getitemrect.md)                 | Retrieves the client coordinates of the specified list box item.                                                                                                                                                                 |
| [**LB\_GETLOCALE**](lb-getlocale.md)                     | Retrieves the locale of the list box. The high-order word contains the country/region code and the low-order word contains the language identifier.                                                                              |
| [**LB\_GETSEL**](lb-getsel.md)                           | Returns the selection state of a list box item.                                                                                                                                                                                  |
| [**LB\_GETSELCOUNT**](lb-getselcount.md)                 | Returns the number of selected items in a multiple-selection list box.                                                                                                                                                           |
| [**LB\_GETSELITEMS**](lb-getselitems.md)                 | Creates an array of the indexes of all selected items in a multiple-selection list box and returns the total number of selected items.                                                                                           |
| [**LB\_GETTEXT**](lb-gettext.md)                         | Retrieves the string associated with a specified item and the length of the string.                                                                                                                                              |
| [**LB\_GETTEXTLEN**](lb-gettextlen.md)                   | Returns the length, in characters, of the string associated with a specified item.                                                                                                                                               |
| [**LB\_GETTOPINDEX**](lb-gettopindex.md)                 | Returns the index of the first visible item in a list box.                                                                                                                                                                       |
| [**LB\_INITSTORAGE**](lb-initstorage.md)                 | Allocates memory for the specified number of items and their associated strings.                                                                                                                                                 |
| [**LB\_INSERTSTRING**](lb-insertstring.md)               | Inserts a string at a specified index in a list box.                                                                                                                                                                             |
| [**LB\_ITEMFROMPOINT**](lb-itemfrompoint.md)             | Retrieves the zero-based index of the item nearest the specified point in a list box.                                                                                                                                            |
| [**LB\_RESETCONTENT**](lb-resetcontent.md)               | Removes all items from a list box.                                                                                                                                                                                               |
| [**LB\_SELECTSTRING**](lb-selectstring.md)               | Selects the first string it finds that matches a specified prefix.                                                                                                                                                               |
| [**LB\_SELITEMRANGE**](lb-selitemrange.md)               | Selects a specified range of items in a list box.                                                                                                                                                                                |
| [**LB\_SELITEMRANGEEX**](lb-selitemrangeex.md)           | Selects a specified range of items if the index of the first item in the range is less than the index of the last item in the range. Cancels the selection in the range if the index of the first item is greater than the last. |
| [**LB\_SETANCHORINDEX**](lb-setanchorindex.md)           | Sets the item that the mouse last selected to a specified item.                                                                                                                                                                  |
| [**LB\_SETCARETINDEX**](lb-setcaretindex.md)             | Sets the focus rectangle to a specified list box item.                                                                                                                                                                           |
| [**LB\_SETCOLUMNWIDTH**](lb-setcolumnwidth.md)           | Sets the width, in pixels, of all columns in a list box.                                                                                                                                                                         |
| [**LB\_SETCOUNT**](lb-setcount.md)                       | Sets the number of items in a list box.                                                                                                                                                                                          |
| [**LB\_SETCURSEL**](lb-setcursel.md)                     | Selects a specified list box item.                                                                                                                                                                                               |
| [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) | Sets the scrollable width, in pixels, of a list box.                                                                                                                                                                             |
| [**LB\_SETITEMDATA**](lb-setitemdata.md)                 | Associates a value with a list box item.                                                                                                                                                                                         |
| [**LB\_SETITEMHEIGHT**](lb-setitemheight.md)             | Sets the height, in pixels, of an item or items in a list box.                                                                                                                                                                   |
| [**LB\_SETLOCALE**](lb-setlocale.md)                     | Sets the locale of a list box and returns the previous locale identifier.                                                                                                                                                        |
| [**LB\_SETSEL**](lb-setsel.md)                           | Selects an item in a multiple-selection list box.                                                                                                                                                                                |
| [**LB\_SETTABSTOPS**](lb-settabstops.md)                 | Sets the tab stops to those specified in a specified array.                                                                                                                                                                      |
| [**LB\_SETTOPINDEX**](lb-settopindex.md)                 | Scrolls the list box so the specified item is at the top of the visible range.                                                                                                                                                   |



 

## Default Window Message Processing

The window procedure for the predefined list box window class carries out default processing for all messages that the list box does not process. When the list box procedure returns **FALSE** for a message, the predefined window procedure checks the message and performs default actions, as shown in the following table.



| Message                                            | Default action                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CHAR**](/windows/desktop/inputdev/wm-char)                   | Moves the selection to the first item that begins with the character that the user typed. If the list box has the L[**BS\_OWNERDRAW**](button-styles.md) style, no action occurs. Multiple characters that are typed within a short interval are treated as a group, and the first item that begins with that series of characters is selected.<br/> |
| [**WM\_CREATE**](/windows/desktop/winmsg/wm-create)                 | Creates an empty list box.                                                                                                                                                                                                                                                                                                                                               |
| [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy)               | Destroys the list box and frees any resources that it uses.                                                                                                                                                                                                                                                                                                              |
|                                                    | Passes the message to the dialog box procedure or parent window process.                                                                                                                                                                                                                                                                                                 |
| [**WM\_ENABLE**](/windows/desktop/winmsg/wm-enable)                 | If the control is visible, invalidates the rectangle so the strings can be painted gray.                                                                                                                                                                                                                                                                                 |
| [**WM\_ERASEBKGND**](/windows/desktop/winmsg/wm-erasebkgnd)         | Erases the background of a list box. If the list box has the L[**BS\_OWNERDRAW**](button-styles.md) style, the background is not erased.                                                                                                                                                                                                                   |
| [**WM\_GETDLGCODE**](/windows/desktop/dlgbox/wm-getdlgcode)         | Returns DLGC\_WANTARROWS \| DLGC\_WANTCHARS, indicating that the default list box procedure processes the arrow keys and [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) messages.                                                                                                                                                                                                      |
| [**WM\_GETFONT**](/windows/desktop/winmsg/wm-getfont)               | Returns a handle to the current font for the list box.                                                                                                                                                                                                                                                                                                                   |
| [**WM\_HSCROLL**](wm-hscroll.md)                  | Scrolls the list box horizontally.                                                                                                                                                                                                                                                                                                                                       |
| [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown)             | Processes virtual keys for scrolling. The virtual key is the index of the item to move the caret to. The selection is not changed.                                                                                                                                                                                                                                       |
| [**WM\_KILLFOCUS**](/windows/desktop/inputdev/wm-killfocus)         | Turns the caret off and destroys it. Sends an [LBN\_KILLFOCUS](lbn-killfocus.md) notification code to the owner of the list box.                                                                                                                                                                                                                                        |
| [**WM\_LBUTTONDBLCLK**](/windows/desktop/inputdev/wm-lbuttondblclk) | Tracks the mouse in the list box client area. This enables the user to cancel a selection if the mouse button is released outside the list box client area.                                                                                                                                                                                                              |
| [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown)     | Tracks the mouse in the list box client area. This enables the user to cancel a selection if the mouse button is released outside the list box client area.                                                                                                                                                                                                              |
| [**WM\_LBUTTONUP**](/windows/desktop/inputdev/wm-lbuttonup)         | Tracks the mouse in the list box client area. This enables the user to cancel a selection if the mouse button is released outside the list box client area.                                                                                                                                                                                                              |
| [**WM\_MOUSEMOVE**](/windows/desktop/inputdev/wm-mousemove)         | Tracks the mouse in the list box client area. This enables the user to cancel a selection if the mouse button is released outside the list box client area.                                                                                                                                                                                                              |
| [**WM\_PAINT**](/windows/desktop/gdi/wm-paint)                      | Performs a subclassed paint operation by using the list box handle to the device context (DC).                                                                                                                                                                                                                                                                           |
| [**WM\_SETFOCUS**](/windows/desktop/inputdev/wm-setfocus)           | Turns the caret on and sends an [LBN\_SETFOCUS](lbn-setfocus.md) notification code to the owner of the list box.                                                                                                                                                                                                                                                        |
| [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont)               | Sets a new font for the list box.                                                                                                                                                                                                                                                                                                                                        |
| [**WM\_SETREDRAW**](/windows/desktop/gdi/wm-setredraw)              | Sets or clears the redraw flag based on the value of *wParam*.                                                                                                                                                                                                                                                                                                           |
| [**WM\_SIZE**](/windows/desktop/winmsg/wm-size)                     | Resizes the list box to an integral number of items.                                                                                                                                                                                                                                                                                                                     |
| [**WM\_VSCROLL**](wm-vscroll.md)                  | Scrolls the list box vertically.                                                                                                                                                                                                                                                                                                                                         |



 

The predefined list box procedure passes all other messages to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) for default processing.

## Owner-Drawn List Boxes

An application can create an *owner-drawn* list box to take responsibility for painting list items. The parent window or dialog box of an owner-drawn list box (its *owner*) receives [**WM\_DRAWITEM**](wm-drawitem.md) messages when a portion of the list box needs to be painted. An owner-drawn list box can list information other than, or in addition to, text strings.

The owner of an owner-drawn list box must process the [**WM\_DRAWITEM**](wm-drawitem.md) message. This message is sent whenever a portion of the list box must be redrawn. The owner may need to process other messages, depending on the styles specified for the list box.

An application can create an owner-drawn list box by specifying the [**LBS\_OWNERDRAWFIXED**](list-box-styles.md) or [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style. If all list items in the list box are the same height, such as strings or icons, an application can use the **LBS\_OWNERDRAWFIXED** style. If list items are of varying height (for example, bitmaps of different size) an application can use the **LBS\_OWNERDRAWVARIABLE** style.

The owner of an owner-drawn list box can process a [**WM\_MEASUREITEM**](wm-measureitem.md) message to specify the dimensions of list items. If the application creates the list box by using the [**LBS\_OWNERDRAWFIXED**](list-box-styles.md) style, the system sends the **WM\_MEASUREITEM** message only once. The dimensions that are specified by the owner are used for all list items. If the [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style is used, the system sends a **WM\_MEASUREITEM** message for each list item that is added to the list box. The owner can determine or set the height of a list item at any time by using the [**LB\_GETITEMHEIGHT**](lb-getitemheight.md) and [**LB\_SETITEMHEIGHT**](lb-setitemheight.md) messages, respectively.

If the information displayed in an owner-drawn list box includes text, an application can keep track of the text for each list item by specifying the [**LBS\_HASSTRINGS**](list-box-styles.md) style. List boxes with the [**LBS\_SORT**](list-box-styles.md) style are sorted based on this text. If a list box is sorted, but is not of the **LBS\_HASSTRINGS** style, the owner must process the [**WM\_COMPAREITEM**](wm-compareitem.md) message.

In an owner-drawn list box, the owner must keep track of list items that contain information other than or in addition to text. One convenient way to do this is to save the handle to the information as item data by using the [**LB\_SETITEMDATA**](lb-setitemdata.md) message. To free data objects associated with items in a list box, the owner can process the [**WM\_DELETEITEM**](wm-deleteitem.md) message.

For an example of an owner-drawn list box, see [How to Create an Owner-Drawn List Box](create-an-owner-drawn-list-box.md).

## Drag List Boxes

A drag list box is a special type of list box that enables the user to drag items from one position to another. An application can use a drag list box to display strings in a particular sequence and enable the user to change the sequence by dragging the items into position.

### Creating Drag List Boxes

Drag list boxes have the same window styles and process the same messages as standard list boxes. To create a drag list box, first create a standard list box and then call the [**MakeDragList**](/windows/desktop/api/Commctrl/nf-commctrl-makedraglist) function. To convert a list box in a dialog box to a drag list box, you can call **MakeDragList** when the WM\_INITDIALOG message is processed.

### Drag List Box Messages

A drag list box notifies the parent window of drag events by sending it a drag list message. The parent window must process the drag list message.

The drag list box registers this message when the [**MakeDragList**](/windows/desktop/api/Commctrl/nf-commctrl-makedraglist) function is called. To retrieve the message identifier (numeric value) of the drag list message, call the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function and specify the DRAGLISTMSGSTRING value.

The *wParam* parameter of the drag list message is the control identifier for the drag list box. The *lParam* parameter is the address of a [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo) structure, which contains the notification code for the drag event and other information. The return value of the message depends on the notification.

### Drag List Box Notification Codes

The drag list notification code, which is identified by the **uNotification** member of the [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo) structure included with the drag list message, can be [DL\_BEGINDRAG](dl-begindrag.md), [DL\_DRAGGING](dl-dragging.md), [DL\_CANCELDRAG](dl-canceldrag.md), or [DL\_DROPPED](dl-dropped.md).

The [DL\_BEGINDRAG](dl-begindrag.md) notification code is sent when the cursor is on a list item and the user clicks the left mouse button. The parent window can return **TRUE** to begin the drag operation or **FALSE** to disallow dragging. In this way, the parent window can enable dragging for some list items and disable it for others. You can determine which list item is at the specified location by using the [**LBItemFromPt**](/windows/desktop/api/Commctrl/nf-commctrl-lbitemfrompt) function.

If dragging is in effect, the [DL\_DRAGGING](dl-dragging.md) notification code is sent whenever the mouse is moved, or at regular intervals if the mouse is not being moved. The parent window should first determine the list item under the cursor by using [**LBItemFromPt**](/windows/desktop/api/Commctrl/nf-commctrl-lbitemfrompt) and then draw the insert icon by using the [**DrawInsert**](/windows/desktop/api/Commctrl/nf-commctrl-drawinsert) function. By specifying **TRUE** for the *bAutoScroll* parameter of **LBItemFromPt**, you can cause the list box to scroll by one line if the cursor is above or below its client area. The value you return for this notification specifies the type of mouse cursor that the drag list box should set.

The [DL\_CANCELDRAG](dl-canceldrag.md) notification code is sent if the user cancels a drag operation by clicking the right mouse button or pressing the ESC key. The [DL\_DROPPED](dl-dropped.md) notification code is sent if the user completes a drag operation by releasing the left mouse button, even if the cursor is not over a list item. The drag list box releases the mouse capture before sending either notification. The return value of these two notifications is ignored. Drag List

 

