---
title: TDN_EXPANDO_BUTTON_CLICKED notification code (Commctrl.h)
description: Sent by the task dialog when the user clicks on the dialog's expando button. This notification is received only through the task dialog callback function, which can be registered using the TaskDialogIndirect method.
ms.assetid: 15e2a9d0-9986-4fb1-a15e-dd4839e45146
keywords:
- TDN_EXPANDO_BUTTON_CLICKED notification code Windows Controls
topic_type:
- apiref
api_name:
- TDN_EXPANDO_BUTTON_CLICKED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDN\_EXPANDO\_BUTTON\_CLICKED notification code

Sent by the task dialog when the user clicks on the dialog's expando button. This notification is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.


```C++
TDN_EXPANDO_BUTTON_CLICKED
        
   WPARAM wParam;
   LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **BOOL** that is **TRUE** if the dialog is expanded, or **FALSE** if not.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

The example in the Syntax section shows the cast to wParam before sending the notification. **LPARAM** is not used and must be zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





