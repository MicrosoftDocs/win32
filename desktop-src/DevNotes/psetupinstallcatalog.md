---
description: Installs a catalog file.
ms.assetid: bea74e91-1a87-4785-b983-5fec87e03499
title: pSetupInstallCatalog function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupInstallCatalog
api_type: 
- DllExport
api_location: 
- Setupapi.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CryptCATAdminAddCatalog**](/windows/win32/api/mscat/nf-mscat-cryptcatadminaddcatalog)
</dt> </dl>

 

 
