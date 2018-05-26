---
Description: Notifies you that a change has taken place.
title: SMC\_SHCHANGENOTIFY message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMC\_SHCHANGENOTIFY message

Notifies you that a change has taken place.


```C++
SMC_SHCHANGENOTIFY
    lParam = (LPARAM) (PSMCSCHANGENOTIFYSTRUCT) psmc
            
```



## Parameters

<dl> <dt>

*psmc* 
</dt> <dd>

A pointer to an [**SMCSHCHANGENOTIFYSTRUCT**](/windows/win32/shobjidl_core/ns-shobjidl_core-shcschangenotifystruct?branch=master) structure with information on the change.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm?branch=master) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




