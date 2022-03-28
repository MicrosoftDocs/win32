---
description: SMC_GETOBJECT message - Requests a pointer to a specified object.
title: SMC_GETOBJECT message (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 36e8f304-a92a-485f-8413-b9c416087ec9
api_name: 
 - SMC_GETOBJECT
api_type: 
 - HeaderDef
api_location: 
 - Shobjidl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SMC\_GETOBJECT message

Requests a pointer to a specified object.


```C++
SMC_GETOBJECT 
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

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm) method. Create the requested object and assign a pointer to the requested interface to *pv*.

The following interfaces may be requested.

- [**IShellMenu**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenu)
- [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu)
- [**IShellMenuCallback**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenucallback)
- [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget)

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 
