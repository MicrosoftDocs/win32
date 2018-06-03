---
Description: Installs a catalog file.
ms.assetid: bea74e91-1a87-4785-b983-5fec87e03499
title: pSetupInstallCatalog function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# pSetupInstallCatalog function

\[This function is no longer supported by Microsoft. Developers should use **CryptCATAdminAddCatalog**.\]

Installs a catalog file.

## Syntax


```C++
DWORD pSetupInstallCatalog(
  _In_      LPCTSTR CatalogFullPath,
  _In_      LPCTSTR NewBaseName,
  _Out_opt_ LPTSTR  NewCatalogFullPath
);
```



## Parameters

<dl> <dt>

*CatalogFullPath* \[in\]
</dt> <dd>

The fully qualified path of the catalog to be installed on the system.

</dd> <dt>

*NewBaseName* \[in\]
</dt> <dd>

The new base name to use when the catalog file is copied into the catalog store.

</dd> <dt>

*NewCatalogFullPath* \[out, optional\]
</dt> <dd>

Optionally receives the fully qualified path of the catalog file within the catalog store. This buffer should be at least **MAX\_PATH** bytes (ANSI version) or chars (Unicode version).

</dd> </dl>

## Return value

If the function succeeds, it returns **NO\_ERROR**; otherwise, it returns a Win32 error code that indicates the cause of the failure.

## Remarks

The file is copied by the system into a special directory and is optionally renamed.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CryptCATAdminAddCatalog**](https://msdn.microsoft.com/windows/desktop/a227597c-a0af-4b86-bd29-03f478aef244)
</dt> </dl>

 

 




