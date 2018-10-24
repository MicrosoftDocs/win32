---
Description: Initializes a string table.
ms.assetid: 1a626243-b4ad-4e3d-a933-b81b75cae399
title: pSetupStringTableInitialize function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupStringTableInitialize
api_type: 
- DllExport
api_location: 
- Setupapi.dll
---

# pSetupStringTableInitialize function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Initializes a string table.

## Syntax


```C++
PVOID WINAPI pSetupStringTableInitialize(void);
```



## Parameters

This function has no parameters.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




