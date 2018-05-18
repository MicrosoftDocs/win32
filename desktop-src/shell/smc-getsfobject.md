---
Description: 'Requests a pointer to a specified object.'
title: 'SMC\_GETSFOBJECT message'
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

This notification is received by the [**IShellMenuCallback::CallbackSM**](ishellmenucallback-callbacksm.md) method. It is similar to [**SMC\_GETOBJECT**](smc-getobject.md) but used for Shell folder items. Create the requested object and assign a pointer to the requested interface to *pv*.

The following interfaces may be requested.

-   [**IStream**](stg.istream)
-   [**IShellMenu**](ishellmenu.md)
-   [**IShellMenuCallback**](ishellmenucallback.md)

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




