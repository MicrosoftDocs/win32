---
title: List Box
description: This section contains information about the programming elements used with list boxes. A list box is a control window that contains a simple list of items from which the user can choose.
ms.assetid: 'vs|controls|~\controls\listboxes\listboxes.htm'
ms.topic: article
ms.date: 05/31/2018
---

# List Box

This section contains information about the programming elements used with list boxes. A list box is a control window that contains a simple list of items from which the user can choose. For more complex lists, use the [List View](list-view-control-reference.md) instead.

### Overviews



| Topic                                    | Contents                                                              |
|------------------------------------------|-----------------------------------------------------------------------|
| [About List Boxes](about-list-boxes.md) | Describes list box features.<br/>                               |
| [Using List Boxes](using-list-boxes.md) | Explains how to perform tasks associated with list boxes. <br/> |



 

### Functions



| Topic                                    | Contents                                                                                                                |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista)         | Replaces the contents of a list box with the names of the subdirectories and files in a specified directory.<br/> |
| [**DlgDirSelectEx**](/windows/desktop/api/Winuser/nf-winuser-dlgdirselectexa) | Retrieves the current selection from a single-selection list box.<br/>                                            |
| [**DrawInsert**](/windows/desktop/api/Commctrl/nf-commctrl-drawinsert)         | Draws the insert icon in the parent window of the specified drag list box. <br/>                                  |
| [**GetListBoxInfo**](/windows/desktop/api/Winuser/nf-winuser-getlistboxinfo) | Retrieves information about the specified list box.<br/>                                                          |
| [**LBItemFromPt**](/windows/desktop/api/Commctrl/nf-commctrl-lbitemfrompt)     | Retrieves the index of the item at the specified point in a list box. <br/>                                       |
| [**MakeDragList**](/windows/desktop/api/Commctrl/nf-commctrl-makedraglist)     | Changes the specified single-selection list box to a drag list box. <br/>                                         |



 

### Messages



| Topic                                                     | Contents                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LB\_ADDFILE**](lb-addfile.md)                         | Adds the specified file name to a list box that contains a directory listing. <br/>                                                                                                                                                                                     |
| [**LB\_ADDSTRING**](lb-addstring.md)                     | Adds a string to a list box. <br/>                                                                                                                                                                                                                                      |
| [**LB\_DELETESTRING**](lb-deletestring.md)               | Deletes a string in a list box. <br/>                                                                                                                                                                                                                                   |
| [**LB\_DIR**](lb-dir.md)                                 | Adds names to the list displayed by a list box. <br/>                                                                                                                                                                                                                   |
| [**LB\_FINDSTRING**](lb-findstring.md)                   | Finds the first string in a list box that begins with the specified string. <br/>                                                                                                                                                                                       |
| [**LB\_FINDSTRINGEXACT**](lb-findstringexact.md)         | Finds the first list box string that exactly matches the specified string, except that the search is not case sensitive. <br/>                                                                                                                                          |
| [**LB\_GETANCHORINDEX**](lb-getanchorindex.md)           | Gets the index of the anchor item that is, the item from which a multiple selection starts. <br/>                                                                                                                                                                       |
| [**LB\_GETCARETINDEX**](lb-getcaretindex.md)             | Retrieves the index of the item that has the focus rectangle in a multiple-selection list box. The item may or may not be selected. <br/>                                                                                                                               |
| [**LB\_GETCOUNT**](lb-getcount.md)                       | Gets the number of items in a list box. <br/>                                                                                                                                                                                                                           |
| [**LB\_GETCURSEL**](lb-getcursel.md)                     | Gets the index of the currently selected item, if any, in a single-selection list box. <br/>                                                                                                                                                                            |
| [**LB\_GETHORIZONTALEXTENT**](lb-gethorizontalextent.md) | Gets the width, in pixels, that a list box can be scrolled horizontally (the scrollable width) if the list box has a horizontal scroll bar. <br/>                                                                                                                       |
| [**LB\_GETITEMDATA**](lb-getitemdata.md)                 | Gets the application-defined value associated with the specified list box item. <br/>                                                                                                                                                                                   |
| [**LB\_GETITEMHEIGHT**](lb-getitemheight.md)             | Gets the height of items in a list box. <br/>                                                                                                                                                                                                                           |
| [**LB\_GETITEMRECT**](lb-getitemrect.md)                 | Gets the dimensions of the rectangle that bounds a list box item as it is currently displayed in the list box. <br/>                                                                                                                                                    |
| [**LB\_GETLISTBOXINFO**](lb-getlistboxinfo.md)           | Gets the number of items per column in a specified list box. <br/>                                                                                                                                                                                                      |
| [**LB\_GETLOCALE**](lb-getlocale.md)                     | Gets the current locale of the list box. <br/>                                                                                                                                                                                                                          |
| [**LB\_GETSEL**](lb-getsel.md)                           | Gets the selection state of an item. <br/>                                                                                                                                                                                                                              |
| [**LB\_GETSELCOUNT**](lb-getselcount.md)                 | Gets the total number of selected items in a multiple-selection list box. <br/>                                                                                                                                                                                         |
| [**LB\_GETSELITEMS**](lb-getselitems.md)                 | Fills a buffer with an array of integers that specify the item numbers of selected items in a multiple-selection list box. <br/>                                                                                                                                        |
| [**LB\_GETTEXT**](lb-gettext.md)                         | Gets a string from a list box. <br/>                                                                                                                                                                                                                                    |
| [**LB\_GETTEXTLEN**](lb-gettextlen.md)                   | Gets the length of a string in a list box. <br/>                                                                                                                                                                                                                        |
| [**LB\_GETTOPINDEX**](lb-gettopindex.md)                 | Gets the index of the first visible item in a list box. <br/>                                                                                                                                                                                                           |
| [**LB\_INITSTORAGE**](lb-initstorage.md)                 | Allocates memory for storing list box items. This message is used before an application adds a large number of items to a list box.<br/>                                                                                                                                |
| [**LB\_INSERTSTRING**](lb-insertstring.md)               | Inserts a string or item data into a list box. Unlike the [**LB\_ADDSTRING**](lb-addstring.md) message, the [**LB\_INSERTSTRING**](lb-insertstring.md) message does not cause a list with the [**LBS\_SORT**](list-box-styles.md) style to be sorted. <br/> |
| [**LB\_ITEMFROMPOINT**](lb-itemfrompoint.md)             | Gets the zero-based index of the item nearest the specified point in a list box.<br/>                                                                                                                                                                                   |
| [**LB\_RESETCONTENT**](lb-resetcontent.md)               | Removes all items from a list box. <br/>                                                                                                                                                                                                                                |
| [**LB\_SELECTSTRING**](lb-selectstring.md)               | Searches a list box for an item that begins with the characters in a specified string. <br/>                                                                                                                                                                            |
| [**LB\_SELITEMRANGE**](lb-selitemrange.md)               | Selects or deselects one or more consecutive items in a multiple-selection list box. <br/>                                                                                                                                                                              |
| [**LB\_SELITEMRANGEEX**](lb-selitemrangeex.md)           | Selects one or more consecutive items in a multiple-selection list box. <br/>                                                                                                                                                                                           |
| [**LB\_SETANCHORINDEX**](lb-setanchorindex.md)           | Sets the anchor item that is, the item from which a multiple selection starts. A multiple selection spans all items from the anchor item to the caret item.<br/>                                                                                                        |
| [**LB\_SETCARETINDEX**](lb-setcaretindex.md)             | Sets the focus rectangle to the item at the specified index in a multiple-selection list box. If the item is not visible, it is scrolled into view. <br/>                                                                                                               |
| [**LB\_SETCOLUMNWIDTH**](lb-setcolumnwidth.md)           | Sets the width, in pixels, of all columns in a multiple-column list box. <br/>                                                                                                                                                                                          |
| [**LB\_SETCOUNT**](lb-setcount.md)                       | Sets the count of items in a list box created with the [**LBS\_NODATA**](list-box-styles.md) style and not created with the [**LBS\_HASSTRINGS**](list-box-styles.md) style. <br/>                                                          |
| [**LB\_SETCURSEL**](lb-setcursel.md)                     | Selects a string and scrolls it into view, if necessary. <br/>                                                                                                                                                                                                          |
| [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) | Sets the width, in pixels, by which a list box can be scrolled horizontally (the scrollable width). <br/>                                                                                                                                                               |
| [**LB\_SETITEMDATA**](lb-setitemdata.md)                 | Sets a value that is associated with the specified item in a list box. <br/>                                                                                                                                                                                            |
| [**LB\_SETITEMHEIGHT**](lb-setitemheight.md)             | Sets the height, in pixels, of items in a list box. <br/>                                                                                                                                                                                                               |
| [**LB\_SETLOCALE**](lb-setlocale.md)                     | Sets the current locale of the list box. <br/>                                                                                                                                                                                                                          |
| [**LB\_SETSEL**](lb-setsel.md)                           | Selects a string in a multiple-selection list box. <br/>                                                                                                                                                                                                                |
| [**LB\_SETTABSTOPS**](lb-settabstops.md)                 | Sets the tab-stop positions in a list box. <br/>                                                                                                                                                                                                                        |
| [**LB\_SETTOPINDEX**](lb-settopindex.md)                 | Ensures that the specified item in a list box is visible. <br/>                                                                                                                                                                                                         |



 

### Notifications



| Topic                                             | Contents                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LBN\_DBLCLK](lbn-dblclk.md)                     | Notifies the application that the user has double-clicked an item in a list box. <br/>                                                                                                                                                                                                                                         |
| [LBN\_ERRSPACE](lbn-errspace.md)                 | Notifies the application that the list box cannot allocate enough memory to meet a specific request. <br/>                                                                                                                                                                                                                     |
| [LBN\_KILLFOCUS](lbn-killfocus.md)               | Notifies the application that the list box has lost the keyboard focus. <br/>                                                                                                                                                                                                                                                  |
| [LBN\_SELCANCEL](lbn-selcancel.md)               | Notifies the application that the user has canceled the selection in a list box. <br/>                                                                                                                                                                                                                                         |
| [LBN\_SELCHANGE](lbn-selchange.md)               | Notifies the application that the selection in a list box has changed. <br/>                                                                                                                                                                                                                                                   |
| [LBN\_SETFOCUS](lbn-setfocus.md)                 | Notifies the application that the list box has received the keyboard focus. <br/>                                                                                                                                                                                                                                              |
| [**WM\_CHARTOITEM**](wm-chartoitem.md)           | Sent by a list box with the [**LBS\_WANTKEYBOARDINPUT**](list-box-styles.md) style to its owner in response to a [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) message. <br/>                                                                                                                                        |
| [**WM\_CTLCOLORLISTBOX**](wm-ctlcolorlistbox.md) | Sent to the parent window of a list box before the system draws the list box. By responding to this message, the parent window can set the text and background colors of the list box by using the specified display device context handle. <br/>                                                                              |
| [**WM\_DELETEITEM**](wm-deleteitem.md)           | Sent to the owner of a list box or combo box when the list box or combo box is destroyed or when items are removed by the [**LB\_DELETESTRING**](lb-deletestring.md), [**LB\_RESETCONTENT**](lb-resetcontent.md), [**CB\_DELETESTRING**](cb-deletestring.md), or [**CB\_RESETCONTENT**](cb-resetcontent.md) message. <br/> |
| [**WM\_VKEYTOITEM**](wm-vkeytoitem.md)           | Sent by a list box with the [**LBS\_WANTKEYBOARDINPUT**](list-box-styles.md) style to its owner in response to a [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) message. <br/>                                                                                                                                  |
| [DL\_BEGINDRAG](dl-begindrag.md)                 | Notifies the drag list box's parent window that the user has clicked the left mouse button on an item. <br/>                                                                                                                                                                                                                   |
| [DL\_CANCELDRAG](dl-canceldrag.md)               | Signals that the user has canceled a drag operation by clicking the right mouse button or pressing the ESC key. <br/>                                                                                                                                                                                                          |
| [DL\_DRAGGING](dl-dragging.md)                   | Signals that the user has moved the mouse while dragging an item. <br/>                                                                                                                                                                                                                                                        |
| [DL\_DROPPED](dl-dropped.md)                     | Signals that the user has completed a drag operation by releasing the left mouse button. <br/>                                                                                                                                                                                                                                 |



 

### Structures



| Topic                                        | Contents                                                                                                                                                               |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DELETEITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-deleteitemstruct) | Contains information about a deleted list box or combo box item.<br/>                                                                                            |
| [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo)         | Contains information about a drag event. The pointer to [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo) is passed as the *lParam* parameter of the drag list message. <br/> |



 

### Constants



| Topic                                  | Contents                                                                |
|----------------------------------------|-------------------------------------------------------------------------|
| [List Box Styles](list-box-styles.md) | Describes the window styles that define a list box control. <br/> |



 

 

