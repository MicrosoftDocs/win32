---
title: TTM_RELAYEVENT message (Commctrl.h)
description: Passes a mouse message to a tooltip control for processing.
ms.assetid: 76d6d0ed-f357-479e-83d8-03d2e988cbd3
keywords:
- TTM_RELAYEVENT message Windows Controls
topic_type:
- apiref
api_name:
- TTM_RELAYEVENT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_RELAYEVENT message

Passes a mouse message to a tooltip control for processing.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero. **Windows 7 and later:** If the position of the tooltip is offset from the cursor position (in order not be obstructed by a finger or pointing device), this parameter can contain extra information taken from the [**WM\_MOUSEMOVE**](/windows/desktop/inputdev/wm-mousemove) message. Retrieve this extra information with [**GetMessageExtraInfo**](/windows/desktop/api/winuser/nf-winuser-getmessageextrainfo).

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**MSG**](/windows/win32/api/winuser/ns-winuser-msg) structure that contains the message to relay.

</dd> </dl>

## Return value

No return value.

## Remarks

A tooltip control processes only the following messages passed to it by the **TTM\_RELAYEVENT** message:

-   WM\_LBUTTONDOWN
-   WM\_LBUTTONUP
-   WM\_MBUTTONDOWN
-   WM\_MBUTTONUP
-   WM\_MOUSEMOVE
-   WM\_NCMOUSEMOVE
-   WM\_RBUTTONDOWN
-   WM\_RBUTTONUP

All other messages are ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

