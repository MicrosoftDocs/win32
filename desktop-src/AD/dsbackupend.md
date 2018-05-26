---
title: DsBackupEnd function
description: Called to terminate a backup operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 872645bc-3dbe-4b12-af4f-778d54feb18f
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- DsBackupEnd function Active Directory
topic_type:
- apiref
api_name:
- DsBackupEnd
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DsBackupEnd function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](http://go.microsoft.com/fwlink/p/?linkid=99156) instead.\]

The **DsBackupEnd** function is called to terminate a backup operation.

## Syntax


```C++
HRESULT DsBackupEnd(
  _In_ HBC hbc
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

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

*hbc* is not valid.

</dd> </dl>

## Remarks

The **DsBackupEnd** function closes outstanding binding handles and performs a cleanup after a successful or unsuccessful backup attempt.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |



## See also

<dl> <dt>

[**DsSetAuthIdentity**](dssetauthidentity.md)
</dt> <dt>

[Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

 





