---
title: CBEN_DRAGBEGIN notification code (Commctrl.h)
description: Sent when the user begins dragging the image of the item displayed in the edit portion of the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: bdab2700-a605-48af-aee3-bbf573408e3f
keywords:
- CBEN_DRAGBEGIN notification code Windows Controls
topic_type:
- apiref
api_name:
- CBEN_DRAGBEGIN
- CBEN_DRAGBEGINA
- CBEN_DRAGBEGINW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEN\_DRAGBEGIN notification code

Sent when the user begins dragging the image of the item displayed in the edit portion of the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
CBEN_DRAGBEGIN

    lpnmdb = (LPNMCBEDRAGBEGIN) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**NMCBEDRAGBEGIN**](/windows/desktop/api/Commctrl/ns-commctrl-nmcbedragbegina) structure that contains information about the notification code.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

If the receiving application implements drag-and-drop functionality from the control, the application will begin the drag-and-drop operation in response to this notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **CBEN\_DRAGBEGINW** (Unicode) and **CBEN\_DRAGBEGINA** (ANSI)<br/>             |



 

 





