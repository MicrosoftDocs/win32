---
Description: 'Verifies a single catalog file using standard operating system code signing policy, such as driver signing.'
ms.assetid: '1e2a18a5-506e-46a8-9309-666bec92182d'
title: pSetupVerifyCatalogFile function
---

# pSetupVerifyCatalogFile function

\[This function is no longer supported by Microsoft. For an INF file (device install), developers should use **SetupVerifyInfFile**. To validate a non-INF based catalog, use **WinVerifyTrust**.\]

Verifies a single catalog file using standard operating system code signing policy, such as driver signing.

## Syntax


```C++
DWORD pSetupVerifyCatalogFile(
  _In_ LPCTSTR CatalogFullPath
);
```



## Parameters

<dl> <dt>

*CatalogFullPath* \[in\]
</dt> <dd>

The fully qualified path of the catalog file to be verified.

</dd> </dl>

## Return value

If the function succeeds, it returns **ERROR\_SUCCESS**; otherwise, it returns the error from [**WinVerifyTrust**](security.winverifytrust).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SetupVerifyInfFile**](setup.setupverifyinffile)
</dt> <dt>

[**WinVerifyTrust**](security.winverifytrust)
</dt> </dl>

 

 




