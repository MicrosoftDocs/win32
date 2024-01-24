---
title: TTM_SETTOOLINFO message (Commctrl.h)
description: Sets the information that a tooltip control maintains for a tool.
ms.assetid: ba18f651-2e52-46e2-871b-c1760e94ab59
keywords:
- TTM_SETTOOLINFO message Windows Controls
topic_type:
- apiref
api_name:
- TTM_SETTOOLINFO
- TTM_SETTOOLINFOA
- TTM_SETTOOLINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_SETTOOLINFO message

Sets the information that a tooltip control maintains for a tool.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure that specifies the information to set. The **cbSize** member of this structure must be set before sending this message.

</dd> </dl>

## Return value

No return value.

## Remarks

Some internal properties of a tool are established when the tool is created, and are not recomputed when a **TTM\_SETTOOLINFO** message is sent. If you simply assign values to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure and pass it to the tooltip control with a **TTM\_SETTOOLINFO** message, these properties may be lost. Instead, your application should first request the tool's current **TOOLINFO** structure by sending the tooltip control a [**TTM\_GETTOOLINFO**](ttm-gettoolinfo.md) message. Then, modify the members of this structure as needed and pass it back to the tooltip control with **TTM\_SETTOOLINFO**.

When calling **TTM\_SETTOOLINFO**, the string pointed to by the **lpszText** member of the [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure must not exceed 80 **TCHARs** in length, including the terminating **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_SETTOOLINFOW** (Unicode) and **TTM\_SETTOOLINFOA** (ANSI)<br/>           |



 

 





