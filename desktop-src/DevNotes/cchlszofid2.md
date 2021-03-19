---
description: Decodes and stores a string.
ms.assetid: 6ababd6e-57b7-49eb-98c9-a4bcb558a377
title: CchLszOfId2 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CchLszOfId2
api_type: 
- DllExport
api_location: 
- Msjint40.dll
---

# CchLszOfId2 function

Decodes and stores a string.

## Syntax


```C++
UINT CchLszOfId2(
   UINT  id,
   WCHAR *lsz,
   UINT  cbmax
);
```



## Parameters

<dl> <dt>

*id* 
</dt> <dd>

The identifier of the string in the resource file to be decoded and stored. The validity of the string is not verified.

</dd> <dt>

*lsz* 
</dt> <dd>

A pointer to a buffer with a length of *cbmax*. Strings that are longer than *cbmax* are truncated.

</dd> <dt>

*cbmax* 
</dt> <dd>

The maximum length of the string to be stored in the *lsz* parameter.

</dd> </dl>

## Return value

This function returns the decoded string.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjint40.dll</dt> </dl> |



 

 
