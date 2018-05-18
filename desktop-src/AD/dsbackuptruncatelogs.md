---
title: DsBackupTruncateLogs function
description: Truncates the previously read backup logs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'fae2e19f-08b8-410f-a735-dd4d41fc71a6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["DsBackupTruncateLogs function Active Directory"]
topic_type:
- apiref
api_name:
- DsBackupTruncateLogs
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
---

# DsBackupTruncateLogs function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](http://go.microsoft.com/fwlink/p/?linkid=99156) instead.\]

The **DsBackupTruncateLogs** function truncates the previously read backup logs.

## Syntax


```C++
HRESULT DsBackupTruncateLogs(
  _In_ HBC hbc
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the backup context handle obtained with the [**DsBackupPrepare**](dsbackupprepare.md) function.

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

*hbc* is invalid.

</dd> </dl>

## Remarks

Use the **DsBackupTruncateLogs** function when a full or incremental backup has completed successfully.

> \[!Caution\]  
> If this function is called after a differential backup, all of the incremental backup information will be lost.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |



## See also

<dl> <dt>

[**DsBackupPrepare**](dsbackupprepare.md)
</dt> <dt>

[**DsBackupGetBackupLogs**](dsbackupgetbackuplogs.md)
</dt> <dt>

[**DsSetCurrentBackupLog**](dssetcurrentbackuplog.md)
</dt> <dt>

[Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

 





