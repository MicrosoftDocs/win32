---
description: Notifies an appbar that the taskbar's autohide or always-on-top state has changed&\#8212;that is, the user has selected or cleared the &\#0034;Always on top&\#0034; or &\#0034;Auto hide&\#0034; check box on the taskbar's property sheet.
title: ABN_STATECHANGE message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: ac2c00a2-ac20-40a5-947e-6b75a2620a0b
api_name: 
 - ABN_STATECHANGE
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABN\_STATECHANGE message

Notifies an appbar that the taskbar's autohide or always-on-top state has changed that is, the user has selected or cleared the "Always on top" or "Auto hide" check box on the taskbar's property sheet.


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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




