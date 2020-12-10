---
title: TDN_DESTROYED notification code (Commctrl.h)
description: Sent by a task dialog when it is destroyed and its window handle is no longer valid. This notification code is received only through the task dialog callback function, which can be registered using the TaskDialogIndirect method.
ms.assetid: bbebb77f-e078-46bf-a42d-65dab4f8a972
keywords:
- TDN_DESTROYED notification code Windows Controls
topic_type:
- apiref
api_name:
- TDN_DESTROYED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDN\_DESTROYED notification code

Sent by a task dialog when it is destroyed and its window handle is no longer valid. This notification code is received only through the task dialog callback function, which can be registered using the [**TaskDialogIndirect**](/windows/desktop/api/Commctrl/nf-commctrl-taskdialogindirect) method.


```C++
TDN_DESTROYED

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



 

 





