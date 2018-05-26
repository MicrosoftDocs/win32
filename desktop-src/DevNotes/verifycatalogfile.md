---
Description: Verifies a single catalog file.
ms.assetid: 1e2a18a5-506e-46a8-9309-666bec92182d
title: VerifyCatalogFile function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VerifyCatalogFile function

\[This function is not supported and should not be used.\]

Verifies a single catalog file.

## Syntax


```C++
DWORD VerifyCatalogFile(
   LPCTSTR CatalogFullPath
);
```



## Parameters

<dl> <dt>

*CatalogFullPath* 
</dt> <dd>

The fully qualified path of the catalog file to be verified.

</dd> </dl>

## Return value

If the function succeeds, it returns **ERROR\_SUCCESS**; otherwise, it returns the error from [**WinVerifyTrust**](security.winverifytrust).

If the catalog is an Authenticode-signed catalog, this function returns **ERROR\_AUTHENTICODE\_TRUSTED\_PUBLISHER** if it succeeds; otherwise, it returns **ERROR\_AUTHENTICODE\_TRUST\_NOT\_ESTABLISHED**.

If the function is unable to determine whether the publisher is trusted, it may also return **ERROR\_UNIDENTIFIED\_ERROR**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




