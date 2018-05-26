---
Description: The Extract function extracts files from a cabinet.
ms.assetid: c6a79d81-7adf-4b8e-a1ef-fec868f7fdbf
title: Extract function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**DeleteExtractedFiles**](deleteextractedfiles.md)
</dt> <dt>

[**ERF**](/windows/win32/Fdi/ns-acpitabl-_firmware_boot_performance_table?branch=master)
</dt> <dt>

[**SESSION**](session.md)
</dt> </dl>

 

 




