---
Description: Closes a search handle.
ms.assetid: 2e6a547f-26a7-401a-b1e4-3f085ce82729
title: CSCFindClose function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSCFindClose
api_type: 
- DllExport
api_location: 
- Cscmig.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cscmig.dll</dt> </dl> |



## See also

<dl> <dt>

[**CSCFindFirstFileW**](cscfindfirstfilew.md)
</dt> </dl>

 

 




