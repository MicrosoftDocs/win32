---
title: DsRestorePrepare function (Ntdsbcli.h)
description: Connects to the specified directory server and prepares it for the restore operation.
ms.assetid: e847d57a-32e1-49c0-800c-7ce0e5f442fa
ms.tgt_platform: multiple
keywords:
- DsRestorePrepare function Active Directory
topic_type:
- apiref
api_name:
- DsRestorePrepare
- DsRestorePrepareA
- DsRestorePrepareW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsRestorePrepare function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsRestorePrepare** function connects to the specified directory server and prepares it for the restore operation.

## Syntax


```C++
HRESULT DsRestorePrepare(
  _In_  LPCWSTR szServerName,
  _In_  ULONG   rtFlag,
  _In_  PVOID   pvExpiryToken,
  _In_  DWORD   cbExpiryTokenSize,
  _Out_ HBC     *phbc
);
```



## Parameters

<dl> <dt>

*szServerName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the name of the server to restore. Preceding backslashes are optional. The server must be the same computer that this function is called from. The server name cannot contain any underscore (\_) characters. An example of a server name is "\\\\server1".

</dd> <dt>

*rtFlag* \[in\]
</dt> <dd>

Specifies the type of restoration to perform. This can be zero or one of the following values.

<dt>

<span id="RESTORE_TYPE_CATCHUP"></span><span id="restore_type_catchup"></span>

<span id="RESTORE_TYPE_CATCHUP"></span><span id="restore_type_catchup"></span>**RESTORE\_TYPE\_CATCHUP**


</dt> <dd>

Default. The restored version is reconciled through the standard reconciliation logic so that the restored DIT can synchronize with other enterprise server computers.

</dd> <dt>

<span id="RESTORE_TYPE_AUTHORATATIVE"></span><span id="restore_type_authoratative"></span>

<span id="RESTORE_TYPE_AUTHORATATIVE"></span><span id="restore_type_authoratative"></span>**RESTORE\_TYPE\_AUTHORATATIVE**


</dt> <dd>

Not Supported.

</dd> <dt>

<span id="RESTORE_TYPE_ONLINE"></span><span id="restore_type_online"></span>

<span id="RESTORE_TYPE_ONLINE"></span><span id="restore_type_online"></span>**RESTORE\_TYPE\_ONLINE**


</dt> <dd>

Not Supported. Restoration is performed when NTDS is online.

</dd> </dl> </dd> <dt>

*pvExpiryToken* \[in\]
</dt> <dd>

Pointer to the expiry token associated with the backup being restored. This token was obtained from the [**DsBackupPrepare**](dsbackupprepare.md) function when the directory was backed up.

If this parameter is **NULL**, the handle returned in *phbc* can only be used to obtain the restoration directories with the [**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md) function. The handle cannot be used for any other restoration functions.

</dd> <dt>

*cbExpiryTokenSize* \[in\]
</dt> <dd>

Contains the size, in bytes, of the expiry token in *pvExpiryToken*.

</dd> <dt>

*phbc* \[out\]
</dt> <dd>

Pointer to an **HBC** value that receives the handle for the restore. This handle is used when calling other Directory Service restore functions, such as [**DsBackupOpenFile**](dsbackupopenfile.md) and [**DsRestoreEnd**](dsrestoreend.md).

</dd> </dl>

## Return value

If successful, returns a standard **HRESULT** codes; otherwise, a failure code is returned.

## Remarks

The **DsRestorePrepare** function requires that the caller is a member of the Administrators group on the server.

**DsRestorePrepare** may be used with or without a token provided. If the token is provided, it is checked for expiration, and all operations are allowed on the context returned. If the token is not provided, the context returned is restricted, and may be used only for the [**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md) function. It may not be used for the [**DsRestoreRegister**](dsrestoreregister.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsRestorePrepareW** (Unicode) and **DsRestorePrepareA** (ANSI)<br/>             |



## See also

<dl> <dt>

[Restoring an Active Directory Server](restoring-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> <dt>

[**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md)
</dt> <dt>

[**DsRestoreRegister**](dsrestoreregister.md)
</dt> <dt>

[**DsRestoreRegisterComplete**](dsrestoreregistercomplete.md)
</dt> <dt>

[**DsRestoreEnd**](dsrestoreend.md)
</dt> </dl>

 

