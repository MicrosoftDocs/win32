---
title: TF_LBI_ Constants (Ctfutb.h)
description: The TF\_LBI\_\ constants are used with the ITfLangBarItemSink OnUpdate method to indicate which language bar items changed.
ms.assetid: ed84012f-19ba-43b3-bbb5-7373ed174c33
topic_type:
- apiref
api_name:
- TF_LBI_ICON
- TF_LBI_TEXT
- TF_LBI_TOOLTIP
- TF_LBI_BITMAP
- TF_LBI_BALLOON
- TF_LBI_STATUS
- TF_LBI_BMPALL
- TF_LBI_BMPBTNALL
- TF_LBI_BTNALL
api_location:
- Ctfutb.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_LBI\_\* Constants

The **TF\_LBI\_\*** constants are used with the [ITfLangBarItemSink::OnUpdate](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritemsink-onupdate) method to indicate which language bar items changed.



| Constant/value                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                         |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_LBI_ICON"></span><span id="tf_lbi_icon"></span><dl> <dt>**TF\_LBI\_ICON**</dt> <dt>0x00000001</dt> </dl>                                                        | The icon of the item has changed. The language bar calls [ITfLangBarItemButton::GetIcon](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembutton-geticon) in response to this notification.<br/>                                                                                                                                             |
| <span id="TF_LBI_TEXT"></span><span id="tf_lbi_text"></span><dl> <dt>**TF\_LBI\_TEXT**</dt> <dt>0x00000002</dt> </dl>                                                        | The text of a button or bitmap button item has changed. The language bar calls [ITfLangBarItemButton::GetText](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembutton-gettext) or [ITfLangBarItemBitmapButton::GetText](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembitmapbutton-gettext), whichever is appropriate, in response to this notification.<br/>           |
| <span id="TF_LBI_TOOLTIP"></span><span id="tf_lbi_tooltip"></span><dl> <dt>**TF\_LBI\_TOOLTIP**</dt> <dt>0x00000004</dt> </dl>                                               | The tooltip text of the item changed. The language bar calls [ITfLangBarItem::GetTooltipString](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-gettooltipstring) in response to this notification.<br/>                                                                                                                                   |
| <span id="TF_LBI_BITMAP"></span><span id="tf_lbi_bitmap"></span><dl> <dt>**TF\_LBI\_BITMAP**</dt> <dt>0x00000008</dt> </dl>                                                  | The bitmap of a bitmap or bitmap button item changed. The language bar calls [ITfLangBarItemBitmap::DrawBitmap](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembitmap-drawbitmap) or [ITfLangBarItemBitmapButton::DrawBitmap](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritembitmapbutton-drawbitmap), whichever is appropriate, in response to this notification.<br/> |
| <span id="TF_LBI_BALLOON"></span><span id="tf_lbi_balloon"></span><dl> <dt>**TF\_LBI\_BALLOON**</dt> <dt>0x00000010</dt> </dl>                                               | The information for a balloon item changed. The language bar calls [ITfLangBarItemBalloon::GetBalloonInfo](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritemballoon-getballooninfo) in response to this notification.<br/>                                                                                                                   |
| <span id="TF_LBI_STATUS"></span><span id="tf_lbi_status"></span><dl> <dt>**TF\_LBI\_STATUS**</dt> <dt>0x00010000</dt> </dl>                                                  | The item status changed. The language bar calls [ITfLangBarItem::GetStatus](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritem-getstatus) in response to this notification.<br/>                                                                                                                                                              |
| <span id="TF_LBI_BMPALL"></span><span id="tf_lbi_bmpall"></span><dl> <dt>**TF\_LBI\_BMPALL**</dt> <dt>TF\_LBI\_BITMAP\| TF\_LBI\_TOOLTIP</dt> </dl>                          | Combines TF\_LBI\_BITMAP and TF\_LBI\_TOOLTIP.<br/>                                                                                                                                                                                                                                                           |
| <span id="TF_LBI_BMPBTNALL"></span><span id="tf_lbi_bmpbtnall"></span><dl> <dt>**TF\_LBI\_BMPBTNALL**</dt> <dt>TF\_LBI\_BITMAP\| TF\_LBI\_TEXT\| TF\_LBI\_TOOLTIP</dt> </dl> | Combines TF\_LBI\_BITMAP, TF\_LBI\_TEXT and TF\_LBI\_TOOLTIP.<br/>                                                                                                                                                                                                                                            |
| <span id="TF_LBI_BTNALL"></span><span id="tf_lbi_btnall"></span><dl> <dt>**TF\_LBI\_BTNALL**</dt> <dt>TF\_LBI\_ICON\| TF\_LBI\_TEXT\| TF\_LBI\_TOOLTIP</dt> </dl>            | Combines TF\_LBI\_ICON, TF\_LBI\_TEXT and TF\_LBI\_TOOLTIP.<br/>                                                                                                                                                                                                                                              |



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

[ITfLangBarItemSink::OnUpdate](/windows/desktop/api/Ctfutb/nf-ctfutb-itflangbaritemsink-onupdate)
</dt> </dl>

 

 





