---
title: DsSetCurrentBackupLog function (Ntdsbcli.h)
description: Sets the current backup log number after a successful restore.
ms.assetid: 903bddea-c5a7-4b3f-819c-0467a9c5ae1b
ms.tgt_platform: multiple
keywords:
- DsSetCurrentBackupLog function Active Directory
topic_type:
- apiref
api_name:
- DsSetCurrentBackupLog
- DsSetCurrentBackupLogA
- DsSetCurrentBackupLogW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsSetCurrentBackupLog function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsSetCurrentBackupLog** function sets the current backup log number after a successful restore. Because Active Directory Domain Services only support circular logging, this function is not normally used.

## Syntax


```C++
HRESULT DsSetCurrentBackupLog(
  _In_ LPCWSTR szServerName,
  _In_ DWORD   dwCurrentLog
);
```



## Parameters

<dl> <dt>

*szServerName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the name of the server to set the backup log number for. Preceding backslashes are optional. The server must be the same computer that this function is called from. The server name cannot contain any underscore (\_) characters. An example of a server name is "\\\\server1".

</dd> <dt>

*dwCurrentLog* \[in\]
</dt> <dd>

Contains the backup log number to set.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or a Win32 or RPC error code otherwise. The following list lists possible error codes.

<dl> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

One or more parameters are invalid.

</dd> <dt>

**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd>

A memory allocation failure occurred.

</dd> </dl>

## Remarks

It is not normally required to call the **DsSetCurrentBackupLog** function. The backup functions automatically determine and set the last log number backed up. Use **DsSetCurrentBackupLog** to prevent another incremental backup from succeeding until a full backup is performed.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsSetCurrentBackupLogW** (Unicode) and **DsSetCurrentBackupLogA** (ANSI)<br/>   |



## See also

<dl> <dt>

[Backing Up and Restoring an Active Directory Server](backing-up-and-restoring-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

