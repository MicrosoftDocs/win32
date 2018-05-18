---
title: IsAlreadyGenuine function
description: Specifies whether the copy of Windows running on the current system is genuine.
ms.assetid: '72139fdd-b6ac-4951-a151-9b6cc7044570'
keywords: ["IsAlreadyGenuine function Windows Genuine"]
topic_type:
- apiref
api_name:
- IsAlreadyGenuine
api_location:
- LegitLib.dll
api_type:
- DllExport
---

# IsAlreadyGenuine function

\[This function is no longer available for use as of Windows 7.\]

Specifies whether the copy of Windows running on the current system is genuine.

This function checks only the local store. It does not check remote servers.

The **IsAlreadyGenuine** function is not declared in a public header and has no associated import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to LegitLib.dll.

## Syntax


```C++
bool __stdcall IsAlreadyGenuine(void);
```



## Parameters

This function has no parameters.

## Return value

**TRUE** if the copy of Windows running on the current system is genuine; otherwise, **FALSE**.

## Remarks

The Windows Genuine Advantage (WGA) functions are available only on Windows Vista and Windows XP installations that have been validated by clicking **Validate Windows** on [http://www.microsoft.com/genuine](http://go.microsoft.com/fwlink/p/?linkid=157937).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | None supported<br/>                                                               |
| End of client support<br/>    | Windows Vista<br/>                                                                |
| End of server support<br/>    | None supported<br/>                                                               |
| DLL<br/>                      | <dl> <dt>LegitLib.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Genuine Advantage API Functions](windows-genuine-advantage-api-functions.md)
</dt> </dl>

 

 





