---
title: TDN_DIALOG_CONSTRUCTED notification code (Commctrl.h)
description: Sent by a task dialog after the dialog has been created and before it is displayed. This notification code is received only through the task dialog callback function, which can be registered using the TaskDialogIndirect method.
ms.assetid: e8556039-a74d-4e33-931d-a63ad5b2d4b0
keywords:
- TDN_DIALOG_CONSTRUCTED notification code Windows Controls
topic_type:
- apiref
api_name:
- TDN_DIALOG_CONSTRUCTED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDN\_DIALOG\_CONSTRUCTED notification code

Sent by a task dialog after the dialog has been created and before it is displayed. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.


```C++
TDN_DIALOG_CONSTRUCTED
     
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



 

 





