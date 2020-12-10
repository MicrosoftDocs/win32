---
title: TDN_HELP notification code (Commctrl.h)
description: Sent by a task dialog when the user presses F1 on the keyboard while the dialog has focus. This notification code is received only through the task dialog callback function, which can be registered using the TaskDialogIndirect method.
ms.assetid: 207ba231-639d-4906-b5dc-1592f2717f1c
keywords:
- TDN_HELP notification code Windows Controls
topic_type:
- apiref
api_name:
- TDN_HELP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDN\_HELP notification code

Sent by a task dialog when the user presses F1 on the keyboard while the dialog has focus. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.


```C++
TDN_HELP
        
   WPARAM wParam;
   LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





