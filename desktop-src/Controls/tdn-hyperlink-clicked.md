---
title: TDN_HYPERLINK_CLICKED notification code (Commctrl.h)
description: Sent by a task dialog when the user clicks a hyperlink in the task dialog content. This notification code is received only through the task dialog callback function, which can be registered using the TaskDialogIndirect method.
ms.assetid: b769af31-32d0-463e-be15-6abf5dcb425c
keywords:
- TDN_HYPERLINK_CLICKED notification code Windows Controls
topic_type:
- apiref
api_name:
- TDN_HYPERLINK_CLICKED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDN\_HYPERLINK\_CLICKED notification code

Sent by a task dialog when the user clicks a hyperlink in the task dialog content. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.


```C++
TDN_HYPERLINK_CLICKED

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

Pointer to a wide-character string containing the URL of the hyperlink.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





