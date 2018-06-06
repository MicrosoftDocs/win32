---
Description: Installs a catalog in a directory.
ms.assetid: 9741f8e3-d9db-46cd-886d-587f332b0ab8
title: InstallCatalog function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InstallCatalog function

\[This function is not supported and should not be used.\]

Installs a catalog in a directory.

## Syntax


```C++
DWORD InstallCatalog(
  _In_      LPCTSTR                  CatalogFullPath,
  _In_opt_  LPCTSTR                  NewBaseName,
  _Out_opt_ ecount_(MAX_Path) LPTSTR NewCatalogFullPath
);
```



## Parameters

<dl> <dt>

*CatalogFullPath* \[in\]
</dt> <dd>

A pointer to a string that represents the full path of the catalog before installation.

</dd> <dt>

*NewBaseName* \[in, optional\]
</dt> <dd>

A pointer to the new base name.

</dd> <dt>

*NewCatalogFullPath* \[out, optional\]
</dt> <dd>

A pointer to a string that represent the full path of the catalog after installation.

</dd> </dl>

## Return value

This function is not currently implemented, so it does not return an actual value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




