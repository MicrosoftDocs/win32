---
title: NM_CUSTOMDRAW (header) notification code (Commctrl.h)
description: Sent by a header control to notify its parent window about drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 44dab54b-45ef-4fba-93b8-2a3e35cda23f
keywords:
- NM_CUSTOMDRAW (header) notification code Windows Controls
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

# NM\_CUSTOMDRAW (header) notification code

Sent by a header control to notify its parent window about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW

    lpNMCustomDraw = (LPNMCUSTOMDRAW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure that contains information about the drawing operation. The **dwItemSpec** member of this structure contains the index of the item being drawn and the **lItemlParam** member of this structure contains the item's *lParam*.

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control will draw itself. It will not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) messages for this paint cycle. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                       |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control will notify the parent of any item-related drawing operations. It will send NM\_CUSTOMDRAW notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                              |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control will notify the parent after erasing an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                              |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control will notify the parent after painting an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                             |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | [Common Control Versions](common-control-versions.md). The control will notify the parent when a list-view subitem is being drawn. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                    |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | Your application specified a new font for the item; the control will use the new font. For more information on changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | Your application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                       |



 

## Remarks

See [Using Custom Draw](custom-draw.md) for further discussion.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





