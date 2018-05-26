---
Description: Called when a window is registered as a Shell window.
title: DShellWindowsEvents.WindowRegistered method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

A window is granted a cookie when it is registered as a Shell window. For more information, see [**Register**](/windows/win32/Exdisp/nf-exdisp-ishellwindows-register?branch=master).

## Requirements



|                    |                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Internet Explorer 5<br/>                                                                                           |
| DLL<br/>     | <dl> <dt>Shdocvw.dll (version 5.00.2014.0216 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DShellWindowsEvents**](dshellwindowsevents.md)
</dt> <dt>

[**WindowRevoked**](dshellwindowsevents-windowrevoked.md)
</dt> <dt>

[**Register**](/windows/win32/Exdisp/nf-exdisp-ishellwindows-register?branch=master)
</dt> <dt>

[**RegisterPending**](/windows/win32/Exdisp/nf-exdisp-ishellwindows-registerpending?branch=master)
</dt> </dl>

 

 




