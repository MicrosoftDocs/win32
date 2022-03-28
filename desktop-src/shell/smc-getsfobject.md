---
description: SMC_GETSFOBJECT message - Requests a pointer to a specified object.
title: SMC_GETSFOBJECT message (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: a8478f10-77ce-4e71-a5dc-89d8a90cf513
api_name: 
 - SMC_GETSFOBJECT
api_type: 
 - HeaderDef
api_location: 
 - Shobjidl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SMC\_GETSFOBJECT message

Requests a pointer to a specified object.


```C++
SMC_GETSFOBJECT 
    wParam = (WPARAM) (REFIID) iid;
    lParam = (LPARAM) (void **) pv
            
```



## Parameters

<dl> <dt>

*iid* 
</dt> <dd>

The IID associated with the requested object.

</dd> <dt>

*pv* 
</dt> <dd>

A void pointer that receives a pointer to the requested interface.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm) method. It is similar to [**SMC\_GETOBJECT**](smc-getobject.md) but used for Shell folder items. Create the requested object and assign a pointer to the requested interface to *pv*.

The following interfaces may be requested.

- [**IStream**](/windows/win32/api/objidl/nn-objidl-istream)
- [**IShellMenu**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenu)
- [**IShellMenuCallback**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenucallback)

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 
