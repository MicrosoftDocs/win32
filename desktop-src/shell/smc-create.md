---
Description: Notifies you that a menu band has been created.
title: SMC_CREATE message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SMC\_CREATE message

Notifies you that a menu band has been created.


```C++
SMC_CREATE 
    lParam = (LPARAM) (LPSMDATA) psmd
            
```



## Parameters

<dl> <dt>

*psmd* 
</dt> <dd>

A pointer to the **pvUserData** member of an [**SMDATA**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-tagsmdata) structure.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




