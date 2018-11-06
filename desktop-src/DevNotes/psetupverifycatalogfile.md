---
Description: Verifies a single catalog file using standard operating system code signing policy, such as driver signing.
ms.assetid: 1e2a18a5-506e-46a8-9309-666bec92182d
title: pSetupVerifyCatalogFile function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupVerifyCatalogFile
api_type: 
- DllExport
api_location: 
- Setupapi.dll
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

If the function succeeds, it returns **ERROR\_SUCCESS**; otherwise, it returns the error from [**WinVerifyTrust**](https://msdn.microsoft.com/en-us/library/Aa388208(v=VS.85).aspx).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SetupVerifyInfFile**](https://msdn.microsoft.com/en-us/library/Aa377447(v=VS.85).aspx)
</dt> <dt>

[**WinVerifyTrust**](https://msdn.microsoft.com/en-us/library/Aa388208(v=VS.85).aspx)
</dt> </dl>

 

 




