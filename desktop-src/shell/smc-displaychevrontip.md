---
Description: 'Notifies you that an infotip is about to be displayed for the chevron associated with the item specified by the accompanying SMDATA structure.'
title: 'SMC\_DISPLAYCHEVRONTIP message'
---

# SMC\_DISPLAYCHEVRONTIP message

Notifies you that an infotip is about to be displayed for the chevron associated with the item specified by the accompanying [**SMDATA**](smdata.md) structure.


```C++
SMC_DISPLAYCHEVRONTIP
            
```



## Parameters

This message has no parameters.

## Return value

Return S\_OK to display the infotip. Return S\_FALSE to prevent the infotip from being displayed.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](ishellmenucallback-callbacksm.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




