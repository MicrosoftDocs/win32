---
Description: The user has clicked a chevron to expand the item specified by the accompanying SMDATA structure.
title: SMC\_CHEVRONEXPAND message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMC\_CHEVRONEXPAND message

The user has clicked a chevron to expand the item specified by the accompanying [**SMDATA**](/windows/win32/Shobjidl_core/ns-shobjidl_core-tagsmdata?branch=master) structure.


```C++
SMC_CHEVRONEXPAND
            
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



 

 




