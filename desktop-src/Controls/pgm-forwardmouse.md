---
title: PGM\_FORWARDMOUSE message
description: Enables or disables mouse forwarding for the pager control. When mouse forwarding is enabled, the pager control forwards WM\_MOUSEMOVE messages to the contained window. You can send this message explicitly or use the Pager\_ForwardMouse macro.
ms.assetid: '269972fe-50b3-4c9f-b5ac-65e768b30684'
keywords: ["PGM_FORWARDMOUSE message Windows Controls"]
topic_type:
- apiref
api_name:
- PGM_FORWARDMOUSE
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# PGM\_FORWARDMOUSE message

Enables or disables mouse forwarding for the pager control. When mouse forwarding is enabled, the pager control forwards [**WM\_MOUSEMOVE**](https://msdn.microsoft.com/library/windows/desktop/ms645616) messages to the contained window. You can send this message explicitly or use the [**Pager\_ForwardMouse**](pager-forwardmouse.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**BOOL** value that determines if mouse forwarding is enabled or disabled. If this value is nonzero, mouse forwarding is enabled. If this value is zero, mouse forwarding is disabled.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





