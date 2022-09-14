---
title: ComboBoxEx Control
description: This section contains information about the programming elements used with ComboBoxEx controls.
ms.assetid: 'vs|controls|~\controls\comboex\reflist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# ComboBoxEx Control

This section contains information about the programming elements used with ComboBoxEx controls.

### Overviews



| Topic                                                | Contents                                                                                           |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [About ComboBoxEx Controls](comboboxex-controls.md) | ComboBoxEx controls are combo box controls that provide native support for item images.<br/> |
| [Using ComboBoxEx Controls](using-comboboxex.md)    | This section contains sample code and information about how to use ComboBoxEx controls.<br/> |



 

### Messages



| Topic                                                   | Contents                                                                                                                                                                                                   |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CBEM\_DELETEITEM**](cbem-deleteitem.md)             | Removes an item from a ComboBoxEx control. <br/>                                                                                                                                                     |
| [**CBEM\_GETCOMBOCONTROL**](cbem-getcombocontrol.md)   | Gets the handle to the child combo box control. <br/>                                                                                                                                                |
| [**CBEM\_GETEDITCONTROL**](cbem-geteditcontrol.md)     | Gets the handle to the edit control portion of a ComboBoxEx control. A ComboBoxEx control uses an edit box when it is set to the [**CBS\_DROPDOWN**](combo-box-styles.md) style. <br/> |
| [**CBEM\_GETEXTENDEDSTYLE**](cbem-getextendedstyle.md) | Gets the extended styles that are in use for a ComboBoxEx control. <br/>                                                                                                                             |
| [**CBEM\_GETIMAGELIST**](cbem-getimagelist.md)         | Gets the handle to an image list assigned to a ComboBoxEx control. <br/>                                                                                                                             |
| [**CBEM\_GETITEM**](cbem-getitem.md)                   | Gets item information for a given ComboBoxEx item.<br/>                                                                                                                                              |
| [**CBEM\_GETUNICODEFORMAT**](cbem-getunicodeformat.md) | Gets the UNICODE character format flag for the control. <br/>                                                                                                                                        |
| [**CBEM\_HASEDITCHANGED**](cbem-haseditchanged.md)     | Determines whether the user has changed the text of a ComboBoxEx edit control.<br/>                                                                                                                  |
| [**CBEM\_INSERTITEM**](cbem-insertitem.md)             | Inserts a new item in a ComboBoxEx control. <br/>                                                                                                                                                    |
| [**CBEM\_KILLCOMBOFOCUS**](cbem-killcombofocus.md)     | This message is not implemented. <br/>                                                                                                                                                               |
| [**CBEM\_SETCOMBOFOCUS**](cbem-setcombofocus.md)       | This message is not implemented. <br/>                                                                                                                                                               |
| [**CBEM\_SETEXTENDEDSTYLE**](cbem-setextendedstyle.md) | Sets extended styles within a ComboBoxEx control. <br/>                                                                                                                                              |
| [**CBEM\_SETIMAGELIST**](cbem-setimagelist.md)         | Sets an image list for a ComboBoxEx control. <br/>                                                                                                                                                   |
| [**CBEM\_SETITEM**](cbem-setitem.md)                   | Sets the attributes for an item in a ComboBoxEx control. <br/>                                                                                                                                       |
| [**CBEM\_SETUNICODEFORMAT**](cbem-setunicodeformat.md) | Sets the UNICODE character format flag for the control. This message enables you to change the character set used by the control at run time rather than having to re-create the control. <br/>      |
| [**CBEM\_SETWINDOWTHEME**](cbem-setwindowtheme.md)     | Sets the visual style of a ComboBoxEx control.<br/>                                                                                                                                                  |



 

### Notifications



| Topic                                                      | Contents                                                                                                                                                                                                                                                     |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CBEN\_BEGINEDIT](cben-beginedit.md)                      | Sent when the user activates the drop-down list or clicks in the control's edit box. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                    |
| [CBEN\_DELETEITEM](cben-deleteitem.md)                    | Sent when an item has been deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                     |
| [CBEN\_DRAGBEGIN](cben-dragbegin.md)                      | Sent when the user begins dragging the image of the item displayed in the edit portion of the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                  |
| [CBEN\_ENDEDIT](cben-endedit.md)                          | Sent when the user has concluded an operation within the edit box or has selected an item from the control's drop-down list. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                             |
| [CBEN\_GETDISPINFO](cben-getdispinfo.md)                  | Sent to retrieve display information about a callback item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                             |
| [CBEN\_INSERTITEM](cben-insertitem.md)                    | Sent when a new item has been inserted in the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                  |
| [NM\_SETCURSOR (ComboBoxEx)](nm-setcursor-comboboxex-.md) | Notifies a ComboBoxEx control's parent window that the control is setting the cursor in response to a [**WM\_SETCURSOR**](/windows/desktop/menurc/wm-setcursor) message. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |



 

### Structures



| Topic                                    | Contents                                                                                                                                                                                     |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) | Contains information about an item in a ComboBoxEx control.<br/>                                                                                                                       |
| [**NMCBEDRAGBEGIN**](/windows/desktop/api/Commctrl/ns-commctrl-nmcbedragbegina) | Contains information used with the [CBEN\_DRAGBEGIN](cben-dragbegin.md) notification code. <br/>                                                                                      |
| [**NMCBEENDEDIT**](/windows/desktop/api/Commctrl/ns-commctrl-nmcbeendedita)     | Contains information about the conclusion of an edit operation within a ComboBoxEx control. This structure is used with the [CBEN\_ENDEDIT](cben-endedit.md) notification code. <br/> |
| [**NMCOMBOBOXEX**](/windows/desktop/api/Commctrl/ns-commctrl-nmcomboboxexa)     | Contains information specific to ComboBoxEx items for use with notification codes. <br/>                                                                                               |



 

### Constants



| Topic                                                                        | Contents                                                                                                                  |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [ComboBoxEx Control Extended Styles](comboboxex-control-extended-styles.md) | Support the extended styles that are listed in this section as well as most standard combo box control styles.<br/> |



 

 

