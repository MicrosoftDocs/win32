---
description: Called when a window is registered as a Shell window.
title: DShellWindowsEvents.WindowRegistered method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DShellWindowsEvents.WindowRegistered
api_type: 
- COM
api_location: 
- Shdocvw.dll
ms.assetid: 7faf758a-daa0-47f5-9f95-61fe3d8286ea

---

# DShellWindowsEvents.WindowRegistered method

Called when a window is registered as a Shell window.

## Syntax


```JScript
DShellWindowsEvents.WindowRegistered(
  lCookie
)
```



## Parameters

<dl> <dt>

*lCookie* \[in\]
</dt> <dd>

Type: **Integer**

The cookie that identifies the window that was registered.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A window is granted a cookie when it is registered as a Shell window. For more information, see [**Register**](/windows/desktop/api/Exdisp/nf-exdisp-ishellwindows-register).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Internet Explorer 5<br/>                                                                                           |
| DLL<br/>     | <dl> <dt>Shdocvw.dll (version 5.00.2014.0216 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DShellWindowsEvents**](dshellwindowsevents.md)
</dt> <dt>

[**WindowRevoked**](dshellwindowsevents-windowrevoked.md)
</dt> <dt>

[**Register**](/windows/desktop/api/Exdisp/nf-exdisp-ishellwindows-register)
</dt> <dt>

[**RegisterPending**](/windows/desktop/api/Exdisp/nf-exdisp-ishellwindows-registerpending)
</dt> </dl>

 

 




