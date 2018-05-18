---
Description: 'Requests information about a regular menu item.'
title: 'SMC\_GETINFO message'
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

A pointer to a [**SMINFO**](sminfo.md) structure. Fill the structure with the appropriate information and return S\_OK.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](ishellmenucallback-callbacksm.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




