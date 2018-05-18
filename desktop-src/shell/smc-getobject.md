---
Description: 'Requests a pointer to a specified object.'
title: 'SMC\_GETOBJECT message'
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

This notification is received by the [**IShellMenuCallback::CallbackSM**](ishellmenucallback-callbacksm.md) method. Create the requested object and assign a pointer to the requested interface to *pv*.

The following interfaces may be requested.

-   [**IShellMenu**](ishellmenu.md)
-   [**IContextMenu**](icontextmenu.md)
-   [**IShellMenuCallback**](ishellmenucallback.md)
-   [**IDropTarget**](com.idroptarget)

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




