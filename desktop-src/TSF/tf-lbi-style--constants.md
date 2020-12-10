---
title: TF_LBI_STYLE_ Constants (Ctfutb.h)
description: The TF\_LBI\_STYLE\_\ constants are used in the dwStyle member of the TF\_LANGBARITEMINFO structure to specify the style of a language bar item.
ms.assetid: 9180a666-774f-401b-bea3-68d5396fab30
topic_type:
- apiref
api_name:
- TF_LBI_STYLE_HIDDENSTATUSCONTROL
- TF_LBI_STYLE_SHOWNINTRAY
- TF_LBI_STYLE_HIDEONNOOTHERITEMS
- TF_LBI_STYLE_SHOWNINTRAYONLY
- TF_LBI_STYLE_HIDDENBYDEFAULT
- TF_LBI_STYLE_TEXTCOLORICON
- TF_LBI_STYLE_BTN_BUTTON
- TF_LBI_STYLE_BTN_MENU
- TF_LBI_STYLE_BTN_TOGGLE
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_LBI\_STYLE\_\* Constants

The **TF\_LBI\_STYLE\_\*** constants are used in the **dwStyle** member of the [TF\_LANGBARITEMINFO](/windows/desktop/api/Ctfutb/ns-ctfutb-tf_langbariteminfo) structure to specify the style of a language bar item.

If this style is combined with TF\_LBI\_STYLE\_BTN\_BUTTON, a drop-down arrow will be displayed for the item in addition to the text. The drop-down arrow functions as the menu button and clicking it will cause **ITfLangBarItemButton::InitMenu** to be called. Clicking the text portion of the button will cause **ITfLangBarItemButton::OnClick** to be called.



| Constant/value                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_LBI_STYLE_HIDDENSTATUSCONTROL"></span><span id="tf_lbi_style_hiddenstatuscontrol"></span><dl> <dt>**TF\_LBI\_STYLE\_HIDDENSTATUSCONTROL**</dt> <dt>0x00000001</dt> </dl> | The item can be hidden or shown dynamically using the TF\_LBI\_STATUS\_HIDDEN value in the [ITfLangBarItem::GetStatus](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-getstatus) method. If this value is not present, the item cannot be hidden in this manner.<br/>                                                                                                                                                                                                                                                                         |
| <span id="TF_LBI_STYLE_SHOWNINTRAY"></span><span id="tf_lbi_style_shownintray"></span><dl> <dt>**TF\_LBI\_STYLE\_SHOWNINTRAY**</dt> <dt>0x00000002</dt> </dl>                         | The item will be displayed in the notification icon tray in addition to the language bar. This flag is not currently supported.<br/>                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="TF_LBI_STYLE_HIDEONNOOTHERITEMS"></span><span id="tf_lbi_style_hideonnootheritems"></span><dl> <dt>**TF\_LBI\_STYLE\_HIDEONNOOTHERITEMS**</dt> <dt>0x00000004</dt> </dl>    | The language bar is hidden if all items in the language bar contain this style. If any item in the language bar does not contain this style, the language bar is displayed.<br/>                                                                                                                                                                                                                                                                                                                                  |
| <span id="TF_LBI_STYLE_SHOWNINTRAYONLY"></span><span id="tf_lbi_style_shownintrayonly"></span><dl> <dt>**TF\_LBI\_STYLE\_SHOWNINTRAYONLY**</dt> <dt>0x00000008</dt> </dl>             | The item will only be displayed in the notification icon tray and not in the language bar. This flag is not currently supported.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="TF_LBI_STYLE_HIDDENBYDEFAULT"></span><span id="tf_lbi_style_hiddenbydefault"></span><dl> <dt>**TF\_LBI\_STYLE\_HIDDENBYDEFAULT**</dt> <dt>0x00000010</dt> </dl>             | The item is not displayed in the toolbar until it is selected from the language bar options menu. This flag is ignored if the TF\_LBI\_STYLE\_HIDDENSTATUSCONTROL is set or the user has already changed the hidden/shown state using the language bar options menu.<br/>                                                                                                                                                                                                                                         |
| <span id="TF_LBI_STYLE_TEXTCOLORICON"></span><span id="tf_lbi_style_textcoloricon"></span><dl> <dt>**TF\_LBI\_STYLE\_TEXTCOLORICON**</dt> <dt>0x00000020</dt> </dl>                   | Any black pixel within the icon will be converted to the text color of the selected theme. The icon must be monochrome.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="TF_LBI_STYLE_BTN_BUTTON"></span><span id="tf_lbi_style_btn_button"></span><dl> <dt>**TF\_LBI\_STYLE\_BTN\_BUTTON**</dt> <dt>0x00010000</dt> </dl>                           | The item is a push button. [ITfLangBarItemButton::OnClick](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembutton-onclick) is called when the item is pressed.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="TF_LBI_STYLE_BTN_MENU"></span><span id="tf_lbi_style_btn_menu"></span><dl> <dt>**TF\_LBI\_STYLE\_BTN\_MENU**</dt> <dt>0x00020000</dt> </dl>                                 | The item is a menu. [ITfLangBarItemButton::InitMenu](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembutton-initmenu) is called when the item is pressed.<br/> If this style is combined with TF\_LBI\_STYLE\_BTN\_BUTTON, a drop-down arrow will be displayed for the item in addition to the text. The drop-down arrow functions as the menu button and clicking it will cause **ITfLangBarItemButton::InitMenu** to be called. Clicking the text portion of the button will cause **ITfLangBarItemButton::OnClick** to be called.<br/> |
| <span id="TF_LBI_STYLE_BTN_TOGGLE"></span><span id="tf_lbi_style_btn_toggle"></span><dl> <dt>**TF\_LBI\_STYLE\_BTN\_TOGGLE**</dt> <dt>0x00040000</dt> </dl>                           | The item is a toggle button and operates similar to a check box. **ITfLangBarItemButton::OnClick** is called when the item is pressed.<br/>                                                                                                                                                                                                                                                                                                                                                                       |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>Ctfutb.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Ctfutb.idl</dt> </dl> |



## See also

<dl> <dt>

[TF\_LANGBARITEMINFO](/windows/desktop/api/Ctfutb/ns-ctfutb-tf_langbariteminfo)
</dt> <dt>

[ITfLangBarItem::GetInfo](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-getinfo)
</dt> <dt>

[ITfLangBarItem::GetStatus](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-getstatus)
</dt> </dl>

 

 





