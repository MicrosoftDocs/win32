---
title: NM_CUSTOMDRAW (list view) notification code (Commctrl.h)
description: Sent by a list-view control to notify its parent windows about drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 4e9b91e3-d042-4fd0-b063-a9e6ea9ad564
keywords:
- NM_CUSTOMDRAW (list view) notification code Windows Controls
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

# NM\_CUSTOMDRAW (list view) notification code

Sent by a list-view control to notify its parent windows about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW

    lpNMCustomDraw = (LPNMLVCUSTOMDRAW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**NMLVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmlvcustomdraw) structure that contains information about the drawing operation. The first member of this structure, **nmcd**, is a pointer to an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure. The **dwItemSpec** member of the structure pointed to by **nmcd** contains the identifier of the item being drawn and the **lItemlParam** member contains its application-defined data.

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control will draw itself. It will not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes for this paint cycle. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                                                            |
| <dl> <dt>**CDRF\_DOERASE**</dt> </dl>           | Windows Vista. The control will only paint the background. <br/>                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                        |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control will notify the parent after painting an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | The application specified a new font for the item; the control will use the new font. For more information about changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                                                              |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | [Version 4.71.](common-control-versions.md) Your application will receive an [NM\_CUSTOMDRAW](nm-customdraw.md) control code with **dwDrawStage** set to CDDS\_ITEMPREPAINT \| CDDS\_SUBITEM before each list-view subitem is drawn. You can then specify font and color for each subitem separately or return [**CDRF\_DODEFAULT**](cdrf-constants.md) for default processing. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | The application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**CDRF\_SKIPPOSTPAINT**</dt> </dl>     | Windows Vista. The control will not draw the focus rectangle. <br/>                                                                                                                                                                                                                                                                                                                                                                                                   |



 

## Remarks

[Version 5.80.](common-control-versions.md) If you change the font by returning [**CDRF\_NEWFONT**](cdrf-constants.md), the list-view control might display clipped text. This behavior is necessary for backward compatibility with earlier versions of the common controls. If you want to change the font of a list-view control, you will get better results if you send a [**CCM\_SETVERSION**](ccm-setversion.md) message with the *wParam* value set to 5 before adding any items to the control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





