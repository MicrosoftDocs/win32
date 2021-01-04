---
title: TTM_HITTEST message (Commctrl.h)
description: Tests a point to determine whether it is within the bounding rectangle of the specified tool and, if it is, retrieves information about the tool.
ms.assetid: d4dcc29b-c64c-41b8-a153-300df68ecdf5
keywords:
- TTM_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- TTM_HITTEST
- TTM_HITTESTA
- TTM_HITTESTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_HITTEST message

Tests a point to determine whether it is within the bounding rectangle of the specified tool and, if it is, retrieves information about the tool.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TTHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-tthittestinfoa) structure. When sending the message, the **hwnd** member must specify the handle to a tool and the **pt** member must specify the coordinates of a point. If the return value is **TRUE**, the **ti** member (a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure) receives information about the tool that occupies the point. The **cbSize** member of the **ti** structure must be filled in before sending this message.

</dd> </dl>

## Return value

Returns **TRUE** if the tool occupies the specified point, or **FALSE** otherwise.

## Remarks

This message must be sent when the tool has the TTF\_TRACK flag set. For more information on this flag, see [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa). TTM\_HITTEST will fail if TTF\_TRACK is not set, regardless if the hit point is in the tools rectangle or not.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_HITTESTW** (Unicode) and **TTM\_HITTESTA** (ANSI)<br/>                   |



 

 





