---
Description: Loads a specified version of a .NET Framework library DLL.
ms.assetid: f001774d-ea9a-4820-aec0-99ce958b1e1d
title: LoadLibraryShim function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LoadLibraryShim function

Loads a specified version of a .NET Framework library DLL.

## Syntax


```C++
HRESULT LoadLibraryShim(
  _In_  LPCWSTR szDllName,
  _In_  LPCWSTR szVersion,
        LPVOID  pvReserved,
  _Out_ HMODULE *phModDll
);
```



## Parameters

<dl> <dt>

*szDllName* \[in\]
</dt> <dd>

The name of the DLL to be loaded from the .NET Framework.

</dd> <dt>

*szVersion* \[in\]
</dt> <dd>

The version of the DLL to be loaded. If *szVersion* is **NULL**, the latest version of the specified DLL is loaded.

</dd> <dt>

*pvReserved* 
</dt> <dd>

Reserved.

</dd> <dt>

*phModDll* \[out\]
</dt> <dd>

A handle to the module.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This function is used to load library DLLs that are included in the .NET Framework redistributable package, not user-generated DLLs.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Mscoree.dll</dt> </dl> |



 

 




