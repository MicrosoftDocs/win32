---
description: Deletes a string table.
ms.assetid: a3ac1672-f898-44a0-bb7b-64ac24bdb9bf
title: pSetupStringTableDestroy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupStringTableDestroy
api_type: 
- DllExport
api_location: 
- Setupapi.dll
---

# pSetupStringTableDestroy function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Deletes a string table.

## Syntax


```C++
void WINAPI pSetupStringTableDestroy(
  _In_ PVOID StringTable
);
```



## Parameters

<dl> <dt>

*StringTable* \[in\]
</dt> <dd>

A pointer to the string table.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 
