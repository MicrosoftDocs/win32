---
title: DsBackupGetBackupLogs function (Ntdsbcli.h)
description: Obtains the list of log files that must be backed up for the given backup context.
ms.assetid: 09b3fdac-41ea-471c-a0dd-54414181f6fe
ms.tgt_platform: multiple
keywords:
- DsBackupGetBackupLogs function Active Directory
topic_type:
- apiref
api_name:
- DsBackupGetBackupLogs
- DsBackupGetBackupLogsA
- DsBackupGetBackupLogsW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsBackupGetBackupLogs function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsBackupGetBackupLogs** function obtains the list of log files that must be backed up for the given backup context.

## Syntax


```C++
HRESULT DsBackupGetBackupLogs(
  _In_  HBC     hbc,
  _Out_ LPTSTR  *pszBackupLogFiles,
  _Out_ LPDWORD pcbSize
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the backup context handle obtained with the [**DsBackupPrepare**](dsbackupprepare.md) function.

</dd> <dt>

*pszBackupLogFiles* \[out\]
</dt> <dd>

Pointer to a string pointer that receives the list of log file names as UNC paths. Initialize this value to **NULL** before calling **DsBackupGetBackupLogs**.

This list receives a double null-terminated list of single null-terminated strings.

This buffer is allocated by the **DsBackupGetBackupLogs** function and must be freed when no longer required by calling the [**DsBackupFree**](dsbackupfree.md) function.

The first character of each of the file names contains one of the [**BFT Constants**](bft-constants.md) that identifies the type of name.

</dd> <dt>

*pcbSize* \[out\]
</dt> <dd>

Pointer to **DWORD** value that receives the size, in bytes, of the *pszBackupLogFiles* buffer.

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

*hbc*, *pszBackupLogFiles*, or *pcbSize* is invalid.

</dd> <dt>

**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd>

A memory allocation failure occurred.

</dd> </dl>

## Remarks

The **DsBackupGetBackupLogs** function provides a list of the log files necessary for a backup. A full backup consists of the database files provided by the [**DsBackupGetDatabaseNames**](dsbackupgetdatabasenames.md) function and the log files. Incremental backups of Active Directory servers are not supported.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsBackupGetBackupLogsW** (Unicode) and **DsBackupGetBackupLogsA** (ANSI)<br/>   |



## See also

<dl> <dt>

[**DsBackupFree**](dsbackupfree.md)
</dt> <dt>

[**DsBackupGetDatabaseNames**](dsbackupgetdatabasenames.md)
</dt> <dt>

[**BFT Constants**](bft-constants.md)
</dt> <dt>

[Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

