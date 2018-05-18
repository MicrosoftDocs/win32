---
title: HWINEVENTHOOK
description: Used to declare a window event hook function.
ms.assetid: 'fa193e8e-46a8-46d4-83e1-e6274276b218'
keywords: ["HWINEVENTHOOK"]
---

# HWINEVENTHOOK

Used to declare a window event hook function.


```C++
typedef HANDLE HWINEVENTHOOK;
```



## Remarks

This data type is used with the [*WinEventProc*](wineventproc-callback-function.md) callback function and the [**SetWinEventHook**](setwineventhook.md) and [**UnhookWinEvent**](unhookwinevent.md) functions.

## Requirements



|                                     |                                                                                                                               |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                          |
| Redistributable<br/>          | Active Accessibility 1.3 RDK on Windows NT 4.0 with SP6 and later and Windows 95<br/>                                   |
| Header<br/>                   | <dl> <dt>Windef.h (WINVER &gt;= 0x0500) (include Windows.h)</dt> </dl> |



 

 





