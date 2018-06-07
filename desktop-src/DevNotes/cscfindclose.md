---
Description: Closes a search handle.
ms.assetid: 2e6a547f-26a7-401a-b1e4-3f085ce82729
title: CSCFindClose function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CSCFindClose function

\[This function is not supported and should not be used.\]

Closes a search handle.

## Syntax


```C++
BOOL WINAPI CSCFindClose(
  _In_ HANDLE hFind
);
```



## Parameters

<dl> <dt>

*hFind* \[in\]
</dt> <dd>

A search handle returned by the [**CSCFindFirstFileW**](cscfindfirstfilew.md) function.

</dd> </dl>

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cscmig.dll</dt> </dl> |



## See also

<dl> <dt>

[**CSCFindFirstFileW**](cscfindfirstfilew.md)
</dt> </dl>

 

 




