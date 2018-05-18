---
Description: 'The user has selected the item specified by the accompanying SMDATA structure.'
title: 'SMC\_SFSELECTITEM message'
---

# SMC\_SFSELECTITEM message

The user has selected the item specified by the accompanying [**SMDATA**](smdata.md) structure.


```C++
SMC_SFSELECTITEM
            
```



## Parameters

This message has no parameters.

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



 

 




