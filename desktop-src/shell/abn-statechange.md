---
Description: 'Notifies an appbar that the taskbar''s autohide or always-on-top state has changed&\#8212;that is, the user has selected or cleared the &\#0034;Always on top&\#0034; or &\#0034;Auto hide&\#0034; check box on the taskbar''s property sheet.'
title: 'ABN\_STATECHANGE message'
---

# ABN\_STATECHANGE message

Notifies an appbar that the taskbar's autohide or always-on-top state has changed—that is, the user has selected or cleared the "Always on top" or "Auto hide" check box on the taskbar's property sheet.


```C++
ABN_STATECHANGE 
```



## Parameters

This message has no parameters.

## Return value

No return value.

## Remarks

An appbar can use this notification message to set its state to conform to that of the taskbar, if desired.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




