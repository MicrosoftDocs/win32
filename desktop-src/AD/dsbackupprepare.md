---
title: DsBackupPrepare function (Ntdsbcli.h)
description: Prepares the directory on the specified server for the online backup and returns a backup context handle used in subsequent calls to other backup functions.
ms.assetid: 18c6dbcf-b707-4674-9af5-40f2178e6d2b
ms.tgt_platform: multiple
keywords:
- DsBackupPrepare function Active Directory
topic_type:
- apiref
api_name:
- DsBackupPrepare
- DsBackupPrepareA
- DsBackupPrepareW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsBackupPrepare function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsBackupPrepare** function prepares the directory on the specified server for the online backup and returns a backup context handle used in subsequent calls to other backup functions.

## Syntax


```C++
HRESULT DsBackupPrepare(
  _In_  LPCTSTR szBackupServer,
  _In_  ULONG   grbit,
  _In_  ULONG   btBackupType,
  _Out_ PVOID   *ppvExpiryToken,
  _Out_ LPDWORD pcbExpiryTokenSize,
  _Out_ HBC     *phbc
);
```



## Parameters

<dl> <dt>

*szBackupServer* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the name of the server to backup. Preceding backslashes are optional. The server must be the same computer that this function is called from. The server name cannot contain an underscore (\_) character. An example of a server name is "\\\\server1".

</dd> <dt>

*grbit* \[in\]
</dt> <dd>

Determines if the log files will be backed up. This value should always be 0 because incremental backups are not supported.

</dd> <dt>

*btBackupType* \[in\]
</dt> <dd>

Specifies the type of backup. This can be one of the following values.

<dt>

<span id="BACKUP_TYPE_FULL"></span><span id="backup_type_full"></span>

<span id="BACKUP_TYPE_FULL"></span><span id="backup_type_full"></span>**BACKUP\_TYPE\_FULL**


</dt> <dd>

Specifies a full backup. The complete directory (DIT, log files, and update files) are backed up. All data is backed up and transaction log files are truncated. Only full backups are supported.

</dd> <dt>

<span id="BACKUP_TYPE_LOGS_ONLY"></span><span id="backup_type_logs_only"></span>

<span id="BACKUP_TYPE_LOGS_ONLY"></span><span id="backup_type_logs_only"></span>**BACKUP\_TYPE\_LOGS\_ONLY**


</dt> <dd>

This value is not supported. Specifies that only the database logs, and not the database itself, will be backed up. This is normally used when performing a differential or incremental backup.

</dd> <dt>

<span id="BACKUP_TYPE_INCREMENTAL"></span><span id="backup_type_incremental"></span>

<span id="BACKUP_TYPE_INCREMENTAL"></span><span id="backup_type_incremental"></span>**BACKUP\_TYPE\_INCREMENTAL**


</dt> <dd>

This value is not supported. **DsBackupPrepare** returns **ERROR\_INVALID\_PARAMETER**.

</dd> </dl> </dd> <dt>

*ppvExpiryToken* \[out\]
</dt> <dd>

Pointer to a **PVOID** value that receives a pointer to an expiry token associated with this backup. *pcbExpiryTokenSize* receives the size, in bytes, of this data. The caller must save the contents of this token with the backup because the token must be passed to [**DsRestorePrepare**](dsrestoreprepare.md) when attempting to restore data. After the token has been stored and is no longer required, the caller should free the allocated memory using [**DsBackupFree**](dsbackupfree.md).

</dd> <dt>

*pcbExpiryTokenSize* \[out\]
</dt> <dd>

Pointer to a **DWORD** value that receives the size, in bytes, of the token in *ppvExpiryToken*.

</dd> <dt>

*phbc* \[out\]
</dt> <dd>

Pointer to an **HBC** value that receives the handle for the backup. This handle is used when calling other Directory Service backup functions, such as [**DsBackupOpenFile**](dsbackupopenfile.md) and [**DsBackupEnd**](dsbackupend.md).

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or an error code otherwise. The following list lists other possible error codes.

<dl> <dt>

**ERROR\_ACCESS\_DENIED**
</dt> <dd>

The caller does not have the proper access privileges to call this function. The [**DsSetAuthIdentity**](dssetauthidentity.md) function can be used to set the credentials to use for the backup and restore functions.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

*szBackupServer* or *phbcBackupContext* are not valid.

</dd> <dt>

**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd>

A memory allocation failure occurred.

</dd> <dt>

**hrCouldNotConnect**
</dt> <dd>

The server in *szBackupServer* could not be found, is not a domain controller or *szBackupServer* is not formatted correctly. This value is defined in ntdsbmsg.h.

</dd> <dt>

**hrInvalidParam**
</dt> <dd>

*ppvExpiryToken* and/or *pcbExpiryTokenSize* are invalid. This value is defined in Ntdsbmsg.h.

</dd> <dt>

**RPC\_S\_INVALID\_BINDING**
</dt> <dd>

The function is called remotely or the server in *szServerName* is not a domain controller.

</dd> </dl>

## Remarks

This function requires that the caller has the **SE\_BACKUP\_NAME** privilege. The [**DsSetAuthIdentity**](dssetauthidentity.md) function can be used to change the security context under which this function is called.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsBackupPrepareW** (Unicode) and **DsBackupPrepareA** (ANSI)<br/>               |



## See also

<dl> <dt>

[**DsRestorePrepare**](dsrestoreprepare.md)
</dt> <dt>

[**DsBackupFree**](dsbackupfree.md)
</dt> <dt>

[**DsBackupOpenFile**](dsbackupopenfile.md)
</dt> <dt>

[**DsBackupEnd**](dsbackupend.md)
</dt> <dt>

[**DsSetAuthIdentity**](dssetauthidentity.md)
</dt> <dt>

[Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

