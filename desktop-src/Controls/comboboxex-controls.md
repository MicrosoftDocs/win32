---
title: About ComboBoxEx Controls
description: ComboBoxEx controls are combo box controls that provide native support for item images.
ms.assetid: a4b1aa79-40c4-4eff-801c-4f308d86fb35
ms.topic: article
ms.date: 05/31/2018
---

# About ComboBoxEx Controls

ComboBoxEx controls are combo box controls that provide native support for item images. To make item images easily accessible, the control provides image list support. By using this control, you can provide the functionality of a combo box without having to manually draw item graphics.

This topic contains the following sections.

-   [Creating ComboBoxEx Controls](#creating-comboboxex-controls)
-   [ComboBoxEx Control Styles](#comboboxex-control-styles)
-   [ComboBoxEx Control Items](#comboboxex-control-items)
-   [Callback Items](#callback-items)
-   [ComboBoxEx Control Image Lists](#comboboxex-control-image-lists)
-   [About ComboBoxEx Control Notification Messages](#about-comboboxex-control-notification-messages)
-   [ComboBoxEx Control Message Forwarding](#comboboxex-control-message-forwarding)

## Creating ComboBoxEx Controls

Effectively, a ComboBoxEx control creates a child combo box and performs owner draw tasks for you based on an assigned image list. Therefore, the [**CBS\_OWNERDRAWFIXED**](combo-box-styles.md) style is implied and it's not necessary to use it when creating the control. Because image lists are used to provide item graphics, the [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md) style cannot be used.

A ComboBoxEx control must be initialized by calling the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function, specifying ICC\_USEREX\_CLASSES in the accompanying [**INITCOMMONCONTROLSEX**](/windows/win32/api/commctrl/ns-commctrl-initcommoncontrolsex) structure.

You can create a ComboBoxEx control by using the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function and specifying [**WC\_COMBOBOXEX**](common-control-window-classes.md) as the window class. The class is registered when the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function is called as explained above.

ComboBoxEx controls are created without a default image list. To use item images, you must create an image list for the ComboBoxEx control and assign it to the control using the [**CBEM\_SETIMAGELIST**](cbem-setimagelist.md) message. If you do not assign an image list to the ComboBoxEx control, the control displays item text only.

## ComboBoxEx Control Styles

ComboBoxEx controls support only the following ComboBox styles:

-   CBS\_SIMPLE
-   CBS\_DROPDOWN
-   CBS\_DROPDOWNLIST
-   WS\_CHILD

There are also several [ComboBoxEx Control Extended Styles](comboboxex-control-extended-styles.md) that are used only by ComboBoxEx.

> [!Note]  
> The [**CBS\_SIMPLE**](combo-box-styles.md) style may not work properly in some cases.

 

Because the ComboBoxEx control performs owner draw tasks for you based on an assigned image list, the [**CBS\_OWNERDRAWFIXED**](combo-box-styles.md) style is implied; you need not use it when creating the control. Because image lists are used to provide item graphics, the [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md) style cannot be used. The ComboBoxEx control also supports [ComboBoxEx Control Extended Styles](comboboxex-control-extended-styles.md) that provide additional features.

## ComboBoxEx Control Items

ComboBoxEx controls maintain item information using a [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure. This structure includes members for item indexes, image indexes (normal, selection state, and overlay), indentation values, text strings, and item-specific values.

The ComboBoxEx control provides easy access to and manipulation of items through messaging. To add or delete an item, send the [**CBEM\_INSERTITEM**](cbem-insertitem.md) or [**CBEM\_DELETEITEM**](cbem-deleteitem.md) message. You can modify items currently in the control using the [**CBEM\_SETITEM**](cbem-setitem.md) message.

## Callback Items

ComboBoxEx controls support callback item attributes. You can specify an item as a callback item when you add it to the control using [**CBEM\_INSERTITEM**](cbem-insertitem.md). When you assign values to an item's [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure, you must specify the appropriate callback flag values. The following are **COMBOBOXEXITEM** structure members and their corresponding callback flag values.



| Member             | Callback value      |
|--------------------|---------------------|
| **pszText**        | LPSTR\_TEXTCALLBACK |
| **iImage**         | I\_IMAGECALLBACK    |
| **iSelectedImage** | I\_IMAGECALLBACK    |
| **iOverlay**       | I\_IMAGECALLBACK    |
| **iIndent**        | I\_INDENTCALLBACK   |



 

The control will request information about callback items by sending [CBEN\_GETDISPINFO](cben-getdispinfo.md) notification codes. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. When your application processes this message, it must provide the requested information for the control. If you set the **mask** member of the accompanying [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure to CBEIF\_DI\_SETITEM, the control will store the item data and will not request it again.

## ComboBoxEx Control Image Lists

If you want a ComboBoxEx control to display icons with items, you must provide an image list. ComboBoxEx controls support up to three images for an item—one for its selected state, one for its nonselected state, and one for an overlay image. Assign an existing image list to a ComboBoxEx control using the [**CBEM\_SETIMAGELIST**](cbem-setimagelist.md) message.

The [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure contains members that represent the image indexes for each image list (selected, unselected, and overlay). For each item, set these members to display the desired images. It is not necessary to specify image indexes for each type of image. You can mix and match image types as you like, but always set the **mask** member of the **COMBOBOXEXITEM** structure to indicate which members are being used. The control ignores members that have not been flagged as valid.

> [!Note]  
> If you use the [**CBS\_SIMPLE**](combo-box-styles.md) style, icons are not displayed.

 

## About ComboBoxEx Control Notification Messages

A ComboBoxEx control sends notification messages to report changes within itself or to request callback item information. The parent of the control receives all [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages from the combo box contained within the ComboBoxEx control. The ComboBoxEx control sends its own notifications using [**WM\_NOTIFY**](wm-notify.md) messages. As a result, the control's owner must be prepared to process both forms of notification messages.

Following are the ComboBoxEx-specific notification codes that are sent through [**WM\_NOTIFY**](wm-notify.md) messages.



| Notification                              | **Description**                                                                                                            |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [CBEN\_BEGINEDIT](cben-beginedit.md)     | Signals that the user has activated the drop-down list or clicked in the control's edit box.                               |
| [CBEN\_ENDEDIT](cben-endedit.md)         | Signals that the user has selected an item from the drop-down list or has concluded an edit operation within the edit box. |
| [CBEN\_DELETEITEM](cben-deleteitem.md)   | Reports that an item was deleted.                                                                                          |
| [CBEN\_GETDISPINFO](cben-getdispinfo.md) | Requests information about an item's attributes.                                                                           |
| [CBEN\_INSERTITEM](cben-insertitem.md)   | Signals that an item was inserted in the control.                                                                          |



 

## ComboBoxEx Control Message Forwarding

The following are the standard combo box messages that a ComboBoxEx control forwards to its child combo box. Some of these messages may be processed by the ComboBoxEx control either before or after the message has been forwarded.

-   [**CB\_DELETESTRING**](cb-deletestring.md)
-   [**CB\_FINDSTRINGEXACT**](cb-findstringexact.md)
-   [**CB\_GETCOUNT**](cb-getcount.md)
-   [**CB\_GETCURSEL**](cb-getcursel.md)
-   [**CB\_GETDROPPEDCONTROLRECT**](cb-getdroppedcontrolrect.md)
-   [**CB\_GETDROPPEDSTATE**](cb-getdroppedstate.md)
-   [**CB\_GETITEMDATA**](cb-getitemdata.md)
-   [**CB\_GETITEMHEIGHT**](cb-getitemheight.md)
-   [**CB\_GETLBTEXT**](cb-getlbtext.md)
-   [**CB\_GETLBTEXTLEN**](cb-getlbtextlen.md)
-   [**CB\_GETEXTENDEDUI**](cb-getextendedui.md)
-   [**CB\_LIMITTEXT**](cb-limittext.md)
-   [**CB\_RESETCONTENT**](cb-resetcontent.md)
-   [**CB\_SETCURSEL**](cb-setcursel.md)
-   [**CB\_SETDROPPEDWIDTH**](cb-setdroppedwidth.md)
-   [**CB\_SETEXTENDEDUI**](cb-setextendedui.md)
-   [**CB\_SETITEMDATA**](cb-setitemdata.md)
-   [**CB\_SETITEMHEIGHT**](cb-setitemheight.md)
-   [**CB\_SHOWDROPDOWN**](cb-showdropdown.md)

Following are the windows messages that a ComboBoxEx control forwards to its parent window:

-   [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) (This includes all of the CBN\_ notifications.)
-   [**WM\_NOTIFY**](wm-notify.md)

 

 