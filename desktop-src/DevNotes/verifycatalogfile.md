---
description: Verifies a single catalog file.
ms.assetid: '4b2de733-ef95-4b0a-8f53-7bc73ffaa2c2'
title: VerifyCatalogFile function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- VerifyCatalogFile
api_type: 
- DllExport
api_location: 
- Setupapi.dll
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

If the function succeeds, it returns **ERROR\_SUCCESS**; otherwise, it returns the error from [**WinVerifyTrust**](/windows/win32/api/wintrust/nf-wintrust-winverifytrust).

If the catalog is an Authenticode-signed catalog, this function returns **ERROR\_AUTHENTICODE\_TRUSTED\_PUBLISHER** if it succeeds; otherwise, it returns **ERROR\_AUTHENTICODE\_TRUST\_NOT\_ESTABLISHED**.

If the function is unable to determine whether the publisher is trusted, it may also return **ERROR\_UNIDENTIFIED\_ERROR**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 
