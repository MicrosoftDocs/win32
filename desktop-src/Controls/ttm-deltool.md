---
title: TTM_DELTOOL message (Commctrl.h)
description: Removes a tool from a tooltip control.
ms.assetid: 433b6f1c-3e9f-4e3a-9834-d447a3f9e6a5
keywords:
- TTM_DELTOOL message Windows Controls
topic_type:
- apiref
api_name:
- TTM_DELTOOL
- TTM_DELTOOLA
- TTM_DELTOOLW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_DELTOOL message

Removes a tool from a tooltip control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure. The **hwnd** and **uId** members identify the tool to remove, and the **cbSize** member must specify the size of the structure. All other members are ignored.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_DELTOOLW** (Unicode) and **TTM\_DELTOOLA** (ANSI)<br/>                   |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TTM\_ADDTOOL**](ttm-addtool.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Tooltip Controls](tooltip-controls.md)
</dt> </dl>

 

 





