---
Description: 'Notifies you that a change has taken place.'
title: 'SMC\_SHCHANGENOTIFY message'
---

# SMC\_SHCHANGENOTIFY message

Notifies you that a change has taken place.


```C++
SMC_SHCHANGENOTIFY
    lParam = (LPARAM) (PSMCSCHANGENOTIFYSTRUCT) psmc
            
```



## Parameters

<dl> <dt>

*psmc* 
</dt> <dd>

A pointer to an [**SMCSHCHANGENOTIFYSTRUCT**](smcshchangenotifystruct.md) structure with information on the change.

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



 

 




