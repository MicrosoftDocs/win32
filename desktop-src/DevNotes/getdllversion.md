---
Description: The GetDllVersion function retrieves the version number of Cabinet.dll.
ms.assetid: b324d5cd-1ede-473e-a10f-249c95eda057
title: GetDllVersion function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetDllVersion function

\[This function is no longer supported, so its behavior cannot be guaranteed. \]

The **GetDllVersion** function retrieves the version number of Cabinet.dll.

## Syntax


```C++
LPCSTR WINAPI GetDllVersion(void);
```



## Parameters

This function has no parameters.

## Return value

The version number of the file (see [VERSIONINFO Resource](tools.versioninfo_resource)).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**DllGetVersion**](dllgetversion.md)
</dt> </dl>

 

 




