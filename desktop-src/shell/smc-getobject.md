---
Description: Requests a pointer to a specified object.
title: SMC_GETOBJECT message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

-   [**IShellMenu**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenu)
-   [**IContextMenu**](https://msdn.microsoft.com/en-us/library/Bb776095(v=VS.85).aspx)
-   [**IShellMenuCallback**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenucallback)
-   [**IDropTarget**](https://msdn.microsoft.com/en-us/library/ms679679(v=VS.85).aspx)

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




