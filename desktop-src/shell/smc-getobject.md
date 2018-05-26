---
Description: Requests a pointer to a specified object.
title: SMC\_GETOBJECT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm?branch=master) method. Create the requested object and assign a pointer to the requested interface to *pv*.

The following interfaces may be requested.

-   [**IShellMenu**](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellmenu?branch=master)
-   [**IContextMenu**](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master)
-   [**IShellMenuCallback**](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellmenucallback?branch=master)
-   [**IDropTarget**](com.idroptarget)

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




