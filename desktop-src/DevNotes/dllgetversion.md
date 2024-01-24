---
description: The DllGetVersion function retrieves the version number of Cabinet.dll using the CABINETDLLVERSIONINFO structure.
ms.assetid: 93f6c29e-6a62-46c2-a42b-8270fe522494
title: DllGetVersion function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DllGetVersion
api_type: 
- DllExport
api_location: 
- Cabinet.dll
---

# DllGetVersion function

\[This function is no longer supported, so its behavior cannot be guaranteed.\]

The **DllGetVersion** function retrieves the version number of Cabinet.dll using the [**CABINETDLLVERSIONINFO**](cabinetdllversioninfo.md) structure.

## Syntax


```C++
VOID WINAPI DllGetVersion(
   PCABINETDLLVERSIONINFO pcdvi
);
```



## Parameters

<dl> <dt>

*pcdvi* 
</dt> <dd>

Pointer to the [**CABINETDLLVERSIONINFO**](cabinetdllversioninfo.md) structure that contains the version information.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**CABINETDLLVERSIONINFO**](cabinetdllversioninfo.md)
</dt> <dt>

[**GetDllVersion**](getdllversion.md)
</dt> </dl>

 

 
