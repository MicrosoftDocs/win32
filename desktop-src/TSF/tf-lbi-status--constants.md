---
title: TF_LBI_STATUS_ Constants (Ctfutb.h)
description: The TF\_LBI\_STATUS\_\ constants indicate the status of a language bar item. These values are used with the ITfLangBarItem GetStatus method.
ms.assetid: 5f2c0e61-f7e5-4dcc-86a3-7bd1c994b8bc
topic_type:
- apiref
api_name:
- TF_LBI_STATUS_HIDDEN
- TF_LBI_STATUS_DISABLED
- TF_LBI_STATUS_BTN_TOGGLED
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_LBI\_STATUS\_\* Constants

The **TF\_LBI\_STATUS\_\*** constants indicate the status of a language bar item. These values are used with the [ITfLangBarItem::GetStatus](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-getstatus) method.



| Constant/value                                                                                                                                                                                                                                                       | Description                                                                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_LBI_STATUS_HIDDEN"></span><span id="tf_lbi_status_hidden"></span><dl> <dt>**TF\_LBI\_STATUS\_HIDDEN**</dt> <dt>0x00000001</dt> </dl>                 | The item is hidden. This style is ignored if the item does not include the TF\_LBI\_STYLE\_HIDDENSTATUSCONTROL style.<br/>                  |
| <span id="TF_LBI_STATUS_DISABLED"></span><span id="tf_lbi_status_disabled"></span><dl> <dt>**TF\_LBI\_STATUS\_DISABLED**</dt> <dt>0x00000002</dt> </dl>           | The item is disabled.<br/>                                                                                                                  |
| <span id="TF_LBI_STATUS_BTN_TOGGLED"></span><span id="tf_lbi_status_btn_toggled"></span><dl> <dt>**TF\_LBI\_STATUS\_BTN\_TOGGLED**</dt> <dt>0x00010000</dt> </dl> | The item is in the toggled or pressed state. This style is ignored if the item does not include the TF\_LBI\_STYLE\_BTN\_TOGGLE style.<br/> |



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

[ITfLangBarItem::GetStatus](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-getstatus)
</dt> </dl>

 

 





