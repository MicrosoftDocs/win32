---
title: HWINEVENTHOOK
description: Used to declare a window event hook function.
ms.assetid: fa193e8e-46a8-46d4-83e1-e6274276b218
keywords:
- HWINEVENTHOOK
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HWINEVENTHOOK

Used to declare a window event hook function.


```C++
typedef HANDLE HWINEVENTHOOK;
```



## Remarks

This data type is used with the [*WinEventProc*](/windows/win32/Winuser/nc-winuser-wineventproc?branch=master) callback function and the [**SetWinEventHook**](/windows/win32/Winuser/nf-winuser-setwineventhook?branch=master) and [**UnhookWinEvent**](/windows/win32/Winuser/nf-winuser-unhookwinevent?branch=master) functions.

## Requirements



|                                     |                                                                                                                               |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                          |
| Redistributable<br/>          | Active Accessibility 1.3 RDK on Windows NT 4.0 with SP6 and later and Windows 95<br/>                                   |
| Header<br/>                   | <dl> <dt>Windef.h (WINVER &gt;= 0x0500) (include Windows.h)</dt> </dl> |



 

 





