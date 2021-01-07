---
description: Requests information about a Shell folder menu item.
title: SMC_GETSFINFO message (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 4459670c-f0fd-4ae8-8a1f-810e1dcac713
api_name: 
 - SMC_GETSFINFO
api_type: 
 - HeaderDef
api_location: 
 - Shobjidl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SMC\_GETSFINFO message

Requests information about a Shell folder menu item.


```C++
SMC_GETINFO 
    lParam = (LPARAM) (LPSMINFO) psminfo
            
```



## Parameters

<dl> <dt>

*psminfo* 
</dt> <dd>

Pointer to a [**SMINFO**](/windows/win32/api/shobjidl_core/ns-shobjidl_core-sminfo) structure. Fill the structure with the appropriate information and return S\_OK.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm) method.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




