---
title: DsBackupGetDatabaseNames function (Ntdsbcli.h)
description: Obtains the list of database files to be backed up for the given backup context.
ms.assetid: ba0447a1-38b0-4c0a-8c63-abaefb5b908f
ms.tgt_platform: multiple
keywords:
- DsBackupGetDatabaseNames function Active Directory
topic_type:
- apiref
api_name:
- DsBackupGetDatabaseNames
- DsBackupGetDatabaseNamesA
- DsBackupGetDatabaseNamesW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsBackupGetDatabaseNames function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsBackupGetDatabaseNames** function obtains the list of database files to be backed up for the given backup context.

## Syntax


```C++
HRESULT DsBackupGetDatabaseNames(
  _In_  HBC     hbc,
  _Out_ LPTSTR  *pszAttachmentInfo,
  _Out_ LPDWORD pcbSize
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the backup context handle obtained with the [**DsBackupPrepare**](dsbackupprepare.md) function.

</dd> <dt>

*pszAttachmentInfo* \[out\]
</dt> <dd>

Pointer to a string pointer that receives the list of database file names as UNC paths. This value must be initialized to **NULL** prior to calling **DsBackupGetDatabaseNames**.

This list receives a double null-terminated list of single null-terminated strings.

This buffer is allocated by the **DsBackupGetDatabaseNames** function and must be freed when it is no longer required by calling the [**DsBackupFree**](dsbackupfree.md) function.

The first character of each file name contains one of the [**BFT Constants**](bft-constants.md) that identifies the type of name. The [**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md) function only supplies the following types of names.

<dt>

<span id="BFT_NTDS_DATABASE"></span><span id="bft_ntds_database"></span>

<span id="BFT_NTDS_DATABASE"></span><span id="bft_ntds_database"></span>**BFT\_NTDS\_DATABASE**


</dt> <dd>

The file is an NTDS database file. This file should be copied to the file identified as **BFT\_NTDS\_DATABASE** when the data is restored.

</dd> <dt>

<span id="BFT_LOG"></span><span id="bft_log"></span>

<span id="BFT_LOG"></span><span id="bft_log"></span>**BFT\_LOG**


</dt> <dd>

The file is a log file. All log files are copied to the directory identified as **BFT\_LOG\_DIR** when the data is restored.

</dd> <dt>

<span id="BFT_PATCH_FILE"></span><span id="bft_patch_file"></span>

<span id="BFT_PATCH_FILE"></span><span id="bft_patch_file"></span>**BFT\_PATCH\_FILE**


</dt> <dd>

The file is a patch file. All patch files are copied to the directory identified as **BFT\_CHECKPOINT\_DIR** when the data is restored.

</dd> </dl> </dd> <dt>

*pcbSize* \[out\]
</dt> <dd>

Pointer to **DWORD** value that receives the size, in bytes, of the *pszAttachmentInfo* buffer.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or a Win32 or RPC error code otherwise. The following list lists other possible error codes.

<dl> <dt>

**ERROR\_ACCESS\_DENIED**
</dt> <dd>

The caller does not have the proper access privileges to call this function. The [**DsSetAuthIdentity**](dssetauthidentity.md) function can be used to set the credentials to use for the backup and restore functions.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

*hbc*, *pszAttachmentInfo*, or *pcbSize* are invalid.

</dd> <dt>

**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd>

A memory allocation failure occurred.

</dd> </dl>

## Remarks

The **DsBackupGetDatabaseNames** function provides a list of the database files necessary for a backup. A full backup consists of the database files and the log files provided by the [**DsBackupGetBackupLogs**](dsbackupgetbackuplogs.md) function. Incremental backups of Active Directory servers are not supported.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                              |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl>     |
| Unicode and ANSI names<br/>   | **DsBackupGetDatabaseNamesW** (Unicode) and **DsBackupGetDatabaseNamesA** (ANSI)<br/> |



## See also

<dl> <dt>

[**DsBackupPrepare**](dsbackupprepare.md)
</dt> <dt>

[**DsBackupFree**](dsbackupfree.md)
</dt> <dt>

[**DsBackupGetBackupLogs**](dsbackupgetbackuplogs.md)
</dt> <dt>

[**BFT Constants**](bft-constants.md)
</dt> <dt>

[Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

