---
title: Miscellaneous Language Bar Constants
description: The miscellaneous language bar constants set certain properties of language bars.
ms.assetid: c1740636-7ba3-4748-9005-ee94d04dbb15
topic_type:
- apiref
api_name:
- TF_DTLBI_USEPROFILEICON
- TF_INVALIDMENUITEM
- TF_LBI_BMPF_VERTICAL
- TF_LBI_DESC_MAXLEN
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Miscellaneous Language Bar Constants

The miscellaneous language bar constants set certain properties of language bars.



| Constant/value                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                              |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_DTLBI_USEPROFILEICON"></span><span id="tf_dtlbi_useprofileicon"></span><dl> <dt>**TF\_DTLBI\_USEPROFILEICON**</dt> <dt>0x00000001</dt> </dl> | The system language bar item should display the icon specified for the language profile. Used in the [ITfSystemDeviceTypeLangBarItem::GetIconMode](/windows/win32/Ctfutb/nf-ctfutb-itfsystemdevicetypelangbaritem-geticonmode?branch=master) and [ITfSystemDeviceTypeLangBarItem::SetIconMode](/windows/win32/Ctfutb/nf-ctfutb-itfsystemdevicetypelangbaritem-seticonmode?branch=master) methods.<br/> |
| <span id="TF_INVALIDMENUITEM"></span><span id="tf_invalidmenuitem"></span><dl> <dt>**TF\_INVALIDMENUITEM**</dt> <dt>(UINT)(-1)</dt> </dl>                 | Not used.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="TF_LBI_BMPF_VERTICAL"></span><span id="tf_lbi_bmpf_vertical"></span><dl> <dt>**TF\_LBI\_BMPF\_VERTICAL**</dt> <dt>0x00000001</dt> </dl>         | Not used.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="TF_LBI_DESC_MAXLEN"></span><span id="tf_lbi_desc_maxlen"></span><dl> <dt>**TF\_LBI\_DESC\_MAXLEN**</dt> <dt>32</dt> </dl>                       | Length, in WCHAR characters, of structure member [TF\_LANGBARITEMINFO.szDescription](/windows/win32/Ctfutb/ns-ctfutb-tf_langbariteminfo?branch=master).<br/>                                                                                                                                                                                                 |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>Ctfutb.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Ctfutb.idl</dt> </dl> |



## See also

<dl> <dt>

[ITfSystemDeviceTypeLangBarItem::GetIconMode](/windows/win32/Ctfutb/nf-ctfutb-itfsystemdevicetypelangbaritem-geticonmode?branch=master)
</dt> <dt>

[ITfSystemDeviceTypeLangBarItem::SetIconMode](/windows/win32/Ctfutb/nf-ctfutb-itfsystemdevicetypelangbaritem-seticonmode?branch=master)
</dt> <dt>

[TF\_LANGBARITEMINFO](/windows/win32/Ctfutb/ns-ctfutb-tf_langbariteminfo?branch=master)
</dt> </dl>

 

 





