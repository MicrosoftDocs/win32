---
Description: Initializes a string table.
ms.assetid: 1a626243-b4ad-4e3d-a933-b81b75cae399
title: pSetupStringTableInitialize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




