---
title: DsRestoreRegisterComplete function (Ntdsbcli.h)
description: Called to unlock an Active Directory server after a restore operation is complete.
ms.assetid: 781cd2ec-d2e2-4f3a-903d-feda4b871de5
ms.tgt_platform: multiple
keywords:
- DsRestoreRegisterComplete function Active Directory
topic_type:
- apiref
api_name:
- DsRestoreRegisterComplete
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsRestoreRegisterComplete function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsRestoreRegisterComplete** function is called to unlock an Active Directory server after a restore operation is complete. This function is counterpart to the [**DsRestoreRegister**](dsrestoreregister.md) function.

## Syntax


```C++
HRESULT DsRestoreRegisterComplete(
  _In_ HBC     hbc,
  _In_ HRESULT hrRestoreState
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the restoration context handle obtained with the [**DsRestorePrepare**](dsrestoreprepare.md) function.

</dd> <dt>

*hrRestoreState* \[in\]
</dt> <dd>

Contains the final status of the restore operation. This parameter should contain **S\_OK** if the restore operation was successful or an error code otherwise.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or a Win32 or RPC error code otherwise. The following list lists possible error codes.

<dl> <dt>

**ERROR\_ACCESS\_DENIED**
</dt> <dd>

The caller does not have the proper access privileges to call this function. The [**DsSetAuthIdentity**](dssetauthidentity.md) function can be used to set the credentials to use for the backup and restore functions.

</dd> </dl>

## Remarks

Before you restart the domain controller, call this function to provide the status of the restore operation. If the status is not successful, the directory service will not start until a valid database has been restored. This function completes the restore operation and allows Active Directory Domain Services to start.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | None supported<br/>                                                               |
| End of client support<br/>    | None supported<br/>                                                               |
| End of server support<br/>    | None supported<br/>                                                               |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |



## See also

<dl> <dt>

[**DsRestoreRegister**](dsrestoreregister.md)
</dt> <dt>

[**DsRestorePrepare**](dsrestoreprepare.md)
</dt> <dt>

[**DsSetAuthIdentity**](dssetauthidentity.md)
</dt> <dt>

[Restoring an Active Directory Server](restoring-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

