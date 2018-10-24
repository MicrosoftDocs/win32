---
Description: Requests information about a regular menu item.
title: SMC_GETINFO message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SMC\_GETINFO message

Requests information about a regular menu item.


```C++
SMC_GETINFO 
    lParam = (LPARAM) (LPSMINFO) psminfo
            
```



## Parameters

<dl> <dt>

*psminfo* 
</dt> <dd>

A pointer to a [**SMINFO**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-tagsminfo) structure. Fill the structure with the appropriate information and return S\_OK.

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



 

 




