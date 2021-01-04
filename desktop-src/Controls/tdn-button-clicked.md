---
title: TDN_BUTTON_CLICKED notification code (Commctrl.h)
description: Sent by a task dialog when the user selects a button or command link in the task dialog. This notification code is received only through the task dialog callback function, which can be registered using the TaskDialogIndirect method.
ms.assetid: eefe48f8-8a80-4280-8a7e-244d9b699ec7
keywords:
- TDN_BUTTON_CLICKED notification code Windows Controls
topic_type:
- apiref
api_name:
- TDN_BUTTON_CLICKED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDN\_BUTTON\_CLICKED notification code

Sent by a task dialog when the user selects a button or command link in the task dialog. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.


```C++
TDN_BUTTON_CLICKED  

   WPARAM wParam;
   LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

An **int** that specifies the ID of the button or comand link that was selected.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

To prevent the task dialog from closing, the application must return **S\_FALSE**, otherwise the task dialog is closed and the button ID is returned via the original application call.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





