---
title: Combo Box Styles (CommCtrl.h)
description: To create a combo box using the CreateWindow or CreateWindowEx function, specify the COMBOBOX class, appropriate window style constants, and a combination of the following combo box styles.
ms.assetid: 4dc347b2-7da7-4aa0-b61f-781acf652d84
topic_type:
- apiref
api_name:
- CBS_AUTOHSCROLL
- CBS_DISABLENOSCROLL
- CBS_DROPDOWN
- CBS_DROPDOWNLIST
- CBS_HASSTRINGS
- CBS_LOWERCASE
- CBS_NOINTEGRALHEIGHT
- CBS_OEMCONVERT
- CBS_OWNERDRAWFIXED
- CBS_OWNERDRAWVARIABLE
- CBS_SIMPLE
- CBS_SORT
- CBS_UPPERCASE
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Combo Box Styles

To create a combo box using the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, specify the COMBOBOX class, appropriate window style constants, and a combination of the following combo box styles.



| Constant                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CBS_AUTOHSCROLL"></span><span id="cbs_autohscroll"></span><dl> <dt>**CBS\_AUTOHSCROLL**</dt> </dl>                   | Automatically scrolls the text in an edit control to the right when the user types a character at the end of the line. If this style is not set, only text that fits within the rectangular boundary is allowed.<br/>                                                                                                                                                                                                                                                                                  |
| <span id="CBS_DISABLENOSCROLL"></span><span id="cbs_disablenoscroll"></span><dl> <dt>**CBS\_DISABLENOSCROLL**</dt> </dl>       | Shows a disabled vertical scroll bar in the list box when the box does not contain enough items to scroll. Without this style, the scroll bar is hidden when the list box does not contain enough items.<br/>                                                                                                                                                                                                                                                                                          |
| <span id="CBS_DROPDOWN"></span><span id="cbs_dropdown"></span><dl> <dt>**CBS\_DROPDOWN**</dt> </dl>                            | Similar to CBS\_SIMPLE, except that the list box is not displayed unless the user selects an icon next to the edit control.<br/>                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CBS_DROPDOWNLIST"></span><span id="cbs_dropdownlist"></span><dl> <dt>**CBS\_DROPDOWNLIST**</dt> </dl>                | Similar to CBS\_DROPDOWN, except that the edit control is replaced by a static text item that displays the current selection in the list box.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| <span id="CBS_HASSTRINGS"></span><span id="cbs_hasstrings"></span><dl> <dt>**CBS\_HASSTRINGS**</dt> </dl>                      | Specifies that an owner-drawn combo box contains items consisting of strings. The combo box maintains the memory and address for the strings so the application can use the [**CB\_GETLBTEXT**](cb-getlbtext.md) message to retrieve the text for a particular item.<br/> For accessibility issues, see [Exposing Owner-Drawn Combo Box Items](/windows/desktop/WinAuto/exposing-owner-drawn-combo-box-items)<br/>                                                                                               |
| <span id="CBS_LOWERCASE"></span><span id="cbs_lowercase"></span><dl> <dt>**CBS\_LOWERCASE**</dt> </dl>                         | Converts to lowercase all text in both the selection field and the list. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="CBS_NOINTEGRALHEIGHT"></span><span id="cbs_nointegralheight"></span><dl> <dt>**CBS\_NOINTEGRALHEIGHT**</dt> </dl>    | Specifies that the size of the combo box is exactly the size specified by the application when it created the combo box. Normally, the system sizes a combo box so that it does not display partial items.<br/>                                                                                                                                                                                                                                                                                        |
| <span id="CBS_OEMCONVERT"></span><span id="cbs_oemconvert"></span><dl> <dt>**CBS\_OEMCONVERT**</dt> </dl>                      | Converts text entered in the combo box edit control from the Windows character set to the OEM character set and then back to the Windows character set. This ensures proper character conversion when the application calls the [**CharToOem**](/windows/desktop/api/winuser/nf-winuser-chartooema) function to convert a Windows string in the combo box to OEM characters. This style is most useful for combo boxes that contain file names and applies only to combo boxes created with the CBS\_SIMPLE or CBS\_DROPDOWN style.<br/> |
| <span id="CBS_OWNERDRAWFIXED"></span><span id="cbs_ownerdrawfixed"></span><dl> <dt>**CBS\_OWNERDRAWFIXED**</dt> </dl>          | Specifies that the owner of the list box is responsible for drawing its contents and that the items in the list box are all the same height. The owner window receives a [**WM\_MEASUREITEM**](wm-measureitem.md) message when the combo box is created and a [**WM\_DRAWITEM**](wm-drawitem.md) message when a visual aspect of the combo box has changed.<br/>                                                                                                                                     |
| <span id="CBS_OWNERDRAWVARIABLE"></span><span id="cbs_ownerdrawvariable"></span><dl> <dt>**CBS\_OWNERDRAWVARIABLE**</dt> </dl> | Specifies that the owner of the list box is responsible for drawing its contents and that the items in the list box are variable in height. The owner window receives a [**WM\_MEASUREITEM**](wm-measureitem.md) message for each item in the combo box when you create the combo box and a [**WM\_DRAWITEM**](wm-drawitem.md) message when a visual aspect of the combo box has changed.<br/>                                                                                                       |
| <span id="CBS_SIMPLE"></span><span id="cbs_simple"></span><dl> <dt>**CBS\_SIMPLE**</dt> </dl>                                  | Displays the list box at all times. The current selection in the list box is displayed in the edit control.<br/>                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CBS_SORT"></span><span id="cbs_sort"></span><dl> <dt>**CBS\_SORT**</dt> </dl>                                        | Automatically sorts strings added to the list box.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="CBS_UPPERCASE"></span><span id="cbs_uppercase"></span><dl> <dt>**CBS\_UPPERCASE**</dt> </dl>                         | Converts to uppercase all text in both the selection field and the list.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                          |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

