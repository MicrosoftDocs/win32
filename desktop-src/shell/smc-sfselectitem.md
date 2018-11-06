---
Description: The user has selected the item specified by the accompanying SMDATA structure.
title: SMC_SFSELECTITEM message
ms.topic: article
ms.date: 05/31/2018
---

# SMC\_SFSELECTITEM message

The user has selected the item specified by the accompanying [**SMDATA**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-tagsmdata) structure.


```C++
SMC_SFSELECTITEM
            
```



## Parameters

This message has no parameters.

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



 

 




