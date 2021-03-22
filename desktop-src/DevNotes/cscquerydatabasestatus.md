---
description: Retrieves the status of the Offline Files cache.
ms.assetid: a8cc0dbb-0005-4e74-892e-898e2ebe0465
title: CSCQueryDatabaseStatus function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSCQueryDatabaseStatus
api_type: 
- DllExport
api_location: 
- Cscmig.dll
---

# CSCQueryDatabaseStatus function

\[This function is not supported and should not be used.\]

Retrieves the status of the Offline Files cache.

## Syntax


```C++
BOOL WINAPI CSCQueryDatabaseStatus(
   ULONG *pulStatus,
   ULONG *pulErrors
);
```



## Parameters

<dl> <dt>

*pulStatus* 
</dt> <dd>

The status. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                               | Meaning                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <span id="FLAG_DATABASESTATUS_ENCRYPTED"></span><span id="flag_databasestatus_encrypted"></span><dl> <dt>**FLAG\_DATABASESTATUS\_ENCRYPTED**</dt> <dt>0x00000002</dt> </dl>                                      | The cache is marked for encryption and all files in the cache are encrypted.<br/>                |
| <span id="FLAG_DATABASESTATUS_PARTIALLY_ENCRYPTED"></span><span id="flag_databasestatus_partially_encrypted"></span><dl> <dt>**FLAG\_DATABASESTATUS\_PARTIALLY\_ENCRYPTED**</dt> <dt>0x00000004</dt> </dl>       | The cache is marked for encryption, but some files in the cache are not encrypted.<br/>          |
| <span id="FLAG_DATABASESTATUS_PARTIALLY_UNENCRYPTED"></span><span id="flag_databasestatus_partially_unencrypted"></span><dl> <dt>**FLAG\_DATABASESTATUS\_PARTIALLY\_UNENCRYPTED**</dt> <dt>0x00000004</dt> </dl> | The cache is not marked for encryption, but not all files in the cache have been decrypted.<br/> |
| <span id="FLAG_DATABASESTATUS_UNENCRYPTED"></span><span id="flag_databasestatus_unencrypted"></span><dl> <dt>**FLAG\_DATABASESTATUS\_UNENCRYPTED**</dt> <dt>0x00000000</dt> </dl>                                | The cache is not marked for encryption and all files in the cache have been decrypted.<br/>      |



 

</dd> <dt>

*pulErrors* 
</dt> <dd>

This parameter is a nonzero value if there is an internal database error or 0 otherwise.

</dd> </dl>

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cscmig.dll</dt> </dl> |



## See also

<dl> <dt>

[**CSCIsCSCEnabled**](csciscscenabled.md)
</dt> </dl>

 

 
