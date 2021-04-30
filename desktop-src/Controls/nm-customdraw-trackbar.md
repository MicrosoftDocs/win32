---
title: NM_CUSTOMDRAW (trackbar) notification code (Commctrl.h)
description: Sent by a trackbar control to notify its parent windows about drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b31d774d-e418-4162-aa2a-40fa49452d58
keywords:
- NM_CUSTOMDRAW (trackbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CUSTOMDRAW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_CUSTOMDRAW (trackbar) notification code

Sent by a trackbar control to notify its parent windows about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW

    lpNMCustomDraw = (LPNMCUSTOMDRAW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure that contains information about the drawing operation. The **dwItemSpec** member of this structure will contain one of the [Custom Draw Values](custom-draw-values.md) that indicates which part of the control is being drawn. Trackbar controls insert the following values into the **dwItemSpec** member of this structure to identify the portion of the control being drawn:



| Value                                                                                                                                                      | Meaning                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <span id="TBCD_CHANNEL"></span><span id="tbcd_channel"></span><dl> <dt>**TBCD\_CHANNEL**</dt> </dl> | Identifies the channel that the trackbar control's thumb marker slides along. <br/>                           |
| <span id="TBCD_THUMB"></span><span id="tbcd_thumb"></span><dl> <dt>**TBCD\_THUMB**</dt> </dl>       | Identifies the trackbar control's thumb marker. This is the portion of the control that the user moves. <br/> |
| <span id="TBCD_TICS"></span><span id="tbcd_tics"></span><dl> <dt>**TBCD\_TICS**</dt> </dl>          | Identifies the increment tick marks that appear along the edge of the trackbar control. <br/>                 |



 

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control will draw itself. It will not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes for this paint cycle. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                             |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                         |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                              |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control will notify the parent after painting an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                             |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | [Version 4.71](common-control-versions.md). The control will notify the parent when a list-view subitem is being drawn. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                               |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | Your application specified a new font for the item; the control will use the new font. For more information on changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | Your application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Using Custom Draw](custom-draw.md)
</dt> </dl>

 

 





