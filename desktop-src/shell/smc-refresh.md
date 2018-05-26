---
Description: Sends notification that the menus have completely refreshed and you can reset your state.
title: SMC\_REFRESH message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMC\_REFRESH message

Sends notification that the menus have completely refreshed and you can reset your state.


```C++
SMC_REFRESH
            
```



## Parameters

This message has no parameters.

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



 

 




