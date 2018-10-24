---
Description: The Extract function extracts files from a cabinet.
ms.assetid: c6a79d81-7adf-4b8e-a1ef-fec868f7fdbf
title: Extract function
ms.author: windowssdkdev
ms.topic: article
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**DeleteExtractedFiles**](deleteextractedfiles.md)
</dt> <dt>

[**ERF**](https://msdn.microsoft.com/en-us/library/Bb432257(v=VS.85).aspx)
</dt> <dt>

[**SESSION**](session.md)
</dt> </dl>

 

 




