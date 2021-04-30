---
title: NM_CUSTOMDRAW (rebar) notification code (Commctrl.h)
description: Sent by the rebar control to notify its parent window about drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 3ba9bb59-f297-4af1-a9a9-d8789def5bde
keywords:
- NM_CUSTOMDRAW (rebar) notification code Windows Controls
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

# NM\_CUSTOMDRAW (rebar) notification code

Sent by the rebar control to notify its parent window about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW

    lpNMCustomDraw = (LPNMCUSTOMDRAW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure that contains information about the drawing operation. The **dwItemSpec** member of this structure contains the identifier of the band being drawn. The **lItemlParam** member of this structure contains the *lParam* of the band being drawn.

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control will draw itself. It will not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) notifications for this paint cycle. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                    |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                           |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control will notify the parent after painting an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                               |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | The control will notify the parent of any item-related drawing operations. It will send [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                           |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | The application specified a new font for the item; the control will use the new font. For more information about changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | The application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                          |



 

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

 

 





