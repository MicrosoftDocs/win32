---
Description: The GetDllVersion function retrieves the version number of Cabinet.dll.
ms.assetid: b324d5cd-1ede-473e-a10f-249c95eda057
title: GetDllVersion function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetDllVersion
api_type: 
- DllExport
api_location: 
- Cabinet.dll
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

The version number of the file (see [VERSIONINFO Resource](https://msdn.microsoft.com/library/Aa381058(v=VS.85).aspx)).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**DllGetVersion**](dllgetversion.md)
</dt> </dl>

 

 




