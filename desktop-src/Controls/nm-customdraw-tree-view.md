---
title: NM_CUSTOMDRAW (tree view) notification code (Commctrl.h)
description: Sent by a tree-view control to notify its parent window about drawing operations. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: eafe2427-20eb-4f3b-9407-bece897ffe16
keywords:
- NM_CUSTOMDRAW (tree view) notification code Windows Controls
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

# NM\_CUSTOMDRAW (tree view) notification code

Sent by a tree-view control to notify its parent window about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CUSTOMDRAW

    lpNMCustomDraw = (LPNMTVCUSTOMDRAW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmtvcustomdraw) structure that contains and receives information about the drawing operation. The **dwItemSpec** member of the **nmcd** member of this structure contains the handle of the item being drawn. The **lItemlParam** member of the **nmcd** member of this structure contains the *lParam* of the item being drawn.

</dd> </dl>

## Return value

The value your application can return depends on the current drawing stage. The **dwDrawStage** member of the associated [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure holds a value that specifies the drawing stage. You must return one of the following values.



| Return code                                                                                            | Description                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_DODEFAULT**</dt> </dl>         | The control draws itself. It does not send any additional [NM\_CUSTOMDRAW](nm-customdraw.md) codes for this paint cycle. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                              |
| <dl> <dt>**CDRF\_NOTIFYITEMDRAW**</dt> </dl>    | The control notifies the parent of any item-related drawing operations. It sends [NM\_CUSTOMDRAW](nm-customdraw.md) notification codes before and after drawing items. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                |
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl>   | The control notifies the parent after erasing an item.This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                  |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl>   | The control notifies the parent after painting an item. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                                                                                |
| <dl> <dt>**CDRF\_NOTIFYSUBITEMDRAW**</dt> </dl> | [Version 4.71.](common-control-versions.md) The control notifies the parent when a list-view subitem is being drawn. This occurs when **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                                                                                  |
| <dl> <dt>**CDRF\_NEWFONT**</dt> </dl>           | Your application specified a new font for the item; the control will use the new font. For more information on changing fonts, see [Changing fonts and colors](custom-draw.md). This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/> |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>       | Your application drew the item manually. The control will not draw the item. This occurs when **dwDrawStage** equals CDDS\_ITEMPREPAINT.<br/>                                                                                                                                       |



 

## Remarks

[Version 5.80.](common-control-versions.md) If you change the font by returning [**CDRF\_NEWFONT**](cdrf-constants.md), the tree-view control might display clipped text. This behavior is necessary for backward compatibility with earlier versions of the common controls. If you want to change the font of a tree-view control, you will get better results if you send a [**CCM\_SETVERSION**](ccm-setversion.md) message with the *wParam* value set to 5 before adding any items to the control.

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

 

 





