---
title: TB\_INDETERMINATE message
description: Sets or clears the indeterminate state of the specified button in a toolbar.
ms.assetid: '6a0f2b82-8241-4c2e-b349-606975ba1a24'
keywords: ["TB_INDETERMINATE message Windows Controls"]
topic_type:
- apiref
api_name:
- TB_INDETERMINATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TB\_INDETERMINATE message

Sets or clears the indeterminate state of the specified button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button whose indeterminate state is to be set or cleared.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) is a **BOOL** that indicates whether to set or clear the indeterminate state. If **TRUE**, the indeterminate state is set. If **FALSE**, the state is cleared.

The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) must be zero.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





