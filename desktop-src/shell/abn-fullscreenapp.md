---
description: Notifies an appbar when a full-screen application is opening or closing. This notification is sent in the form of an application-defined message that is set by the ABM\_NEW message.
title: ABN_FULLSCREENAPP message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: c67ec934-088c-43e0-bff4-900d76a456e5
api_name: 
 - ABN_FULLSCREENAPP
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABN\_FULLSCREENAPP message

Notifies an appbar when a full-screen application is opening or closing. This notification is sent in the form of an application-defined message that is set by the [**ABM\_NEW**](abm-new.md) message.


```C++

ABN_FULLSCREENAPP 

    fOpen = (BOOL) lParam; 

            
```



## Parameters

<dl> <dt>

*fOpen* 
</dt> <dd>

A flag specifying whether a full-screen application is opening or closing. This parameter is **TRUE** if the application is opening or **FALSE** if it is closing.

</dd> </dl>

## Return value

No return value.

## Remarks

When a full-screen application is opening, an appbar must drop to the bottom of the z-order. When it is closing, the appbar should restore its z-order position.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




