---
title: TF_LBMENUF_ Constants (Ctfutb.h)
description: The TF\_LBMENUF\_\ constants are used in the ITfMenu AddMenuItem method to specify the characteristics of a menu item in the language bar.
ms.assetid: f8f3f397-b84e-4635-b454-31369c679ce2
topic_type:
- apiref
api_name:
- TF_LBMENUF_CHECKED
- TF_LBMENUF_SUBMENU
- TF_LBMENUF_SEPARATOR
- TF_LBMENUF_RADIOCHECKED
- TF_LBMENUF_GRAYED
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_LBMENUF\_\* Constants

The **TF\_LBMENUF\_\*** constants are used in the [ITfMenu::AddMenuItem](/windows/desktop/api/Ctfutb/nf-ctfutb-itfmenu-addmenuitem) method to specify the characteristics of a menu item in the language bar.



| Constant/value                                                                                                                                                                                                                                         | Description                                     |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------|
| <span id="TF_LBMENUF_CHECKED"></span><span id="tf_lbmenuf_checked"></span><dl> <dt>**TF\_LBMENUF\_CHECKED**</dt> <dt>0x01</dt> </dl>                | The menu item is checked.<br/>            |
| <span id="TF_LBMENUF_SUBMENU"></span><span id="tf_lbmenuf_submenu"></span><dl> <dt>**TF\_LBMENUF\_SUBMENU**</dt> <dt>0x02</dt> </dl>                | The menu item is a submenu.<br/>          |
| <span id="TF_LBMENUF_SEPARATOR"></span><span id="tf_lbmenuf_separator"></span><dl> <dt>**TF\_LBMENUF\_SEPARATOR**</dt> <dt>0x04</dt> </dl>          | The menu item is a separator.<br/>        |
| <span id="TF_LBMENUF_RADIOCHECKED"></span><span id="tf_lbmenuf_radiochecked"></span><dl> <dt>**TF\_LBMENUF\_RADIOCHECKED**</dt> <dt>0x08</dt> </dl> | The menu item is a radio check mark.<br/> |
| <span id="TF_LBMENUF_GRAYED"></span><span id="tf_lbmenuf_grayed"></span><dl> <dt>**TF\_LBMENUF\_GRAYED**</dt> <dt>0x10</dt> </dl>                   | The menu item is disabled.<br/>           |



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

[ITfMenu::AddMenuItem](/windows/desktop/api/Ctfutb/nf-ctfutb-itfmenu-addmenuitem)
</dt> </dl>

 

 





