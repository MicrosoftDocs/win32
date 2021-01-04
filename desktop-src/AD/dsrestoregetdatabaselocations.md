---
title: DsRestoreGetDatabaseLocations function (Ntdsbcli.h)
description: Obtains the locations where backup files should be copied during a restore operation.
ms.assetid: f91d701c-72cf-418a-8d1c-6bf6ef41c2c1
ms.tgt_platform: multiple
keywords:
- DsRestoreGetDatabaseLocations function Active Directory
topic_type:
- apiref
api_name:
- DsRestoreGetDatabaseLocations
- DsRestoreGetDatabaseLocationsA
- DsRestoreGetDatabaseLocationsW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsRestoreGetDatabaseLocations function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsRestoreGetDatabaseLocations** function obtains the locations where backup files should be copied during a restore operation.

## Syntax


```C++
HRESULT DsRestoreGetDatabaseLocations(
  _In_  HBC     hbc,
  _Out_ LPWSTR  *pszDatabaseLocationList,
  _Out_ LPDWORD pcbSize
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the restoration context handle obtained with the [**DsRestorePrepare**](dsrestoreprepare.md) function.

</dd> <dt>

*pszDatabaseLocationList* \[out\]
</dt> <dd>

Pointer to a string pointer that receives the list of database locations as UNC paths. This list receives a double null-terminated list of single null-terminated strings.

This buffer is allocated by the **DsRestoreGetDatabaseLocations** function and must be freed when it is no longer required by calling the [**DsBackupFree**](dsbackupfree.md) function.

The first character of each of the file names contains one of the [**BFT Constants**](bft-constants.md) that identifies the name type. The **DsRestoreGetDatabaseLocations** function only supplies the following name types.

<dt>

<span id="BFT_NTDS_DATABASE"></span><span id="bft_ntds_database"></span>

<span id="BFT_NTDS_DATABASE"></span><span id="bft_ntds_database"></span>**BFT\_NTDS\_DATABASE**


</dt> <dd>

The NTDS database file should be copied to this file. This is the file that was identified as **BFT\_NTDS\_DATABASE** when the backup was performed.

</dd> <dt>

<span id="BFT_LOG_DIR"></span><span id="bft_log_dir"></span>

<span id="BFT_LOG_DIR"></span><span id="bft_log_dir"></span>**BFT\_LOG\_DIR**


</dt> <dd>

All log files are copied to this directory. The log files were identified as **BFT\_LOG** when the backup was performed.

</dd> <dt>

<span id="BFT_CHECKPOINT_DIR"></span><span id="bft_checkpoint_dir"></span>

<span id="BFT_CHECKPOINT_DIR"></span><span id="bft_checkpoint_dir"></span>**BFT\_CHECKPOINT\_DIR**


</dt> <dd>

All patch files are copied to this directory. The patch files were identified as **BFT\_PATCH\_FILE** when the backup was performed.

</dd> </dl> </dd> <dt>

*pcbSize* \[out\]
</dt> <dd>

Pointer to **DWORD** value that receives the size, in bytes, of the *pszDatabaseLocationList* buffer.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or a Win32 or RPC error code otherwise. The following list lists possible error codes.

<dl> <dt>

**ERROR\_ACCESS\_DENIED**
</dt> <dd>

The caller does not have the proper access privileges to call this function. The [**DsSetAuthIdentity**](dssetauthidentity.md) function can be used to set the credentials to use for the backup and restore functions.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

*hbc*, *pszDatabaseLocationList*, or *pcbSize* are invalid.

</dd> <dt>

**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd>

A memory allocation failure occurred.

</dd> </dl>

## Remarks

The **DsRestoreGetDatabaseLocations** function can be used to obtain the restoration directories without access to the backed up data. To do this, call [**DsRestorePrepare**](dsrestoreprepare.md) with **NULL** for the *pvExpiryToken* parameter. This causes **DsRestorePrepare** to return a restricted context handle which can only be used with the **DsRestoreGetDatabaseLocations** function.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                        |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>                 |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl>               |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl>               |
| Unicode and ANSI names<br/>   | **DsRestoreGetDatabaseLocationsW** (Unicode) and **DsRestoreGetDatabaseLocationsA** (ANSI)<br/> |



## See also

<dl> <dt>

[**DsRestorePrepare**](dsrestoreprepare.md)
</dt> <dt>

[**DsBackupFree**](dsbackupfree.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> <dt>

[Restoring Active Directory](restoring-an-active-directory-server.md)
</dt> </dl>

 

