---
description: The Extract function extracts files from a cabinet.
ms.assetid: c6a79d81-7adf-4b8e-a1ef-fec868f7fdbf
title: Extract function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Extract
api_type: 
- DllExport
api_location: 
- Cabinet.dll
---

# Extract function

\[This function is no longer supported, so its behavior cannot be guaranteed.\]

The **Extract** function extracts files from a cabinet.

## Syntax


```C++
HRESULT Extract(
   PSESSION ps,
   LPCSTR   lpCabName
);
```



## Parameters

<dl> <dt>

*ps* 
</dt> <dd>

Pointer to a [**SESSION**](session.md) structure that contains information about the current session.

</dd> <dt>

*lpCabName* 
</dt> <dd>

Pointer to the name of the cabinet from which files are to be extracted.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**; otherwise, it returns an error code.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**DeleteExtractedFiles**](deleteextractedfiles.md)
</dt> <dt>

[**ERF**](/windows/win32/api/fdi_fci_types/ns-fdi_fci_types-erf)
</dt> <dt>

[**SESSION**](session.md)
</dt> </dl>

 

 
