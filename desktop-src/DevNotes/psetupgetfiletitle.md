---
description: Retrieves the file title for the specified file path.
ms.assetid: 9a559d71-4883-4905-b3ad-64b256a2f51e
title: pSetupGetFileTitle function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupGetFileTitle
api_type: 
- DllExport
api_location: 
- Setupapi.dll
---

# pSetupGetFileTitle function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Retrieves the file title for the specified file path.

## Syntax


```C++
PCTSTR pSetupGetFileTitle(
  _In_ PCTSTR FilePath
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

The file path.

</dd> </dl>

## Return value

A pointer to string that receives the file title.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 
