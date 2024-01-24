---
title: TB_SETPARENT message (Commctrl.h)
description: Sets the window to which the toolbar control sends notification messages.
ms.assetid: 4863bd9f-021b-4295-9483-459fc19325d9
keywords:
- TB_SETPARENT message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETPARENT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETPARENT message

Sets the window to which the toolbar control sends notification messages.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the window to receive notification messages.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value is a handle to the previous notification window, or **NULL** if there is no previous notification window.

## Remarks

The **TB\_SETPARENT** message does not change the parent window that was specified when the control was created. Calling the [**GetParent**](/windows/desktop/api/winuser/nf-winuser-getparent) function for a toolbar control will return the actual parent window, not the window specified in **TB\_SETPARENT**. To change the control's parent window, call the [**SetParent**](/windows/desktop/api/winuser/nf-winuser-setparent) function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

