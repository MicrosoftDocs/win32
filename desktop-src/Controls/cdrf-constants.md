---
title: RF Constants (CommCtrl.h)
description: These constants are used as return values by a control in response to an NM\_CUSTOMDRAW notification code.
ms.assetid: 6b05e27e-5d18-46f2-b326-2a5148597852
topic_type:
- apiref
api_name:
- CDRF_DODEFAULT
- CDRF_NEWFONT
- CDRF_SKIPDEFAULT
- CDRF_DOERASE
- CDRF_NOTIFYPOSTPAINT
- CDRF_NOTIFYITEMDRAW
- CDRF_NOTIFYSUBITEMDRAW
- CDRF_NOTIFYPOSTERASE
- CDRF_SKIPPOSTPAINT
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RF Constants

These constants are used as return values by a control in response to an [NM\_CUSTOMDRAW](nm-customdraw.md) notification code.



| Constant/value                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CDRF_DODEFAULT"></span><span id="cdrf_dodefault"></span><dl> <dt>**CDRF\_DODEFAULT**</dt> <dt>0x00000000</dt> </dl>                         | The control will draw itself. It will not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes for this paint cycle. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_PREPAINT.<br/>                                                                                                                                                               |
| <span id="CDRF_NEWFONT"></span><span id="cdrf_newfont"></span><dl> <dt>**CDRF\_NEWFONT**</dt> <dt>0x00000002</dt> </dl>                               | The application specified a new font for the item; the control will use the new font. For more information about changing fonts, see Changing fonts and colors. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                      |
| <span id="CDRF_SKIPDEFAULT"></span><span id="cdrf_skipdefault"></span><dl> <dt>**CDRF\_SKIPDEFAULT**</dt> <dt>0x00000004</dt> </dl>                   | The application drew the item manually. The control will not draw the item. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                                                                                                          |
| <span id="CDRF_DOERASE"></span><span id="cdrf_doerase"></span><dl> <dt>**CDRF\_DOERASE**</dt> <dt>0x00000008</dt> </dl>                               | **Windows Vista and later.** The control will draw the background.<br/>                                                                                                                                                                                                                                                                                                                                                         |
| <span id="CDRF_NOTIFYPOSTPAINT"></span><span id="cdrf_notifypostpaint"></span><dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> <dt>0x00000010</dt> </dl>       | The control will notify the parent after painting an item. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                                               |
| <span id="CDRF_NOTIFYITEMDRAW"></span><span id="cdrf_notifyitemdraw"></span><dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> <dt>0x00000020</dt> </dl>          | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_PREPAINT.<br/>                                                                                                                           |
| <span id="CDRF_NOTIFYSUBITEMDRAW"></span><span id="cdrf_notifysubitemdraw"></span><dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> <dt>0x00000020</dt> </dl> | **Internet Explorer 4.0 and later.** The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_PREPAINT. This flag is identical to **CDRF\_NOTIFYITEMDRAW** and its use is context-dependent.<br/> |
| <span id="CDRF_NOTIFYPOSTERASE"></span><span id="cdrf_notifyposterase"></span><dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> <dt>0x00000040</dt> </dl>       | The control will notify the parent after erasing an item. This occurs when the **dwDrawStage** of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                                                |
| <span id="CDRF_SKIPPOSTPAINT"></span><span id="cdrf_skippostpaint"></span><dl> <dt>**CDRF\_SKIPPOSTPAINT**</dt> <dt>0x00000100</dt> </dl>             | **Windows Vista and later.** The control will not draw the focus rectangle.<br/>                                                                                                                                                                                                                                                                                                                                                |



## Remarks

These constants are defined in Commctrl.h.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

[Customizing a Control's Appearance Using Custom Draw](custom-draw.md)
</dt> </dl>

 

 





