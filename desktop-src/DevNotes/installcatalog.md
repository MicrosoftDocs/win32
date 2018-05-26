---
Description: Installs a catalog in a directory.
ms.assetid: 9741f8e3-d9db-46cd-886d-587f332b0ab8
title: InstallCatalog function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




