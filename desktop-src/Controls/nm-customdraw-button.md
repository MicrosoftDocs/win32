---
title: NM_CUSTOMDRAW (button) notification code (Commctrl.h)
description: Notifies the parent window of a button control about custom draw operations on the button. The button control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: cabe5515-ba64-4c53-8746-7a0559df8989
keywords:
- NM_CUSTOMDRAW (button) notification code Windows Controls
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

# NM\_CUSTOMDRAW (button) notification code

Notifies the parent window of a button control about custom draw operations on the button.

The button control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


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



| Return code                                                                                          | Description                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CDRF\_NOTIFYPOSTERASE**</dt> </dl> | The control will notify the parent after erasing an item. This can be used only if **dwDrawStage** equals CDDS\_PREERASE.<br/>                                  |
| <dl> <dt>**CDRF\_NOTIFYPOSTPAINT**</dt> </dl> | The control will notify the parent after painting an item. This can be used only if **dwDrawStage** equals CDDS\_PREPAINT.<br/>                                 |
| <dl> <dt>**CDRF\_SKIPDEFAULT**</dt> </dl>     | The application drew the item manually. The control will not draw the item. This can be used when **dwDrawStage** equals CDDS\_PREERASE or CDDS\_PREPAINT.<br/> |



 

## Remarks

If the button control is marked ownerdraw (BS\_OWNERDRAW), the NM\_CUSTOMDRAW notification code is not sent.

See [Using Custom Draw](custom-draw.md) for further discussion.

> [!Note]  
> To use this notification code, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Commctrl.h (include Windows.h)</dt> </dl> |



 

 





