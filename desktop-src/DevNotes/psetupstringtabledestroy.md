---
Description: Deletes a string table.
ms.assetid: a3ac1672-f898-44a0-bb7b-64ac24bdb9bf
title: pSetupStringTableDestroy function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




