---
title: DsRestoreRegister function (Ntdsbcli.h)
description: Registers a restore operation.
ms.assetid: 83a56985-89be-4a95-9a8d-7c6f78d61c9a
ms.tgt_platform: multiple
keywords:
- DsRestoreRegister function Active Directory
topic_type:
- apiref
api_name:
- DsRestoreRegister
- DsRestoreRegisterA
- DsRestoreRegisterW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsRestoreRegister function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsRestoreRegister** function registers a restore operation.This function interlocks all subsequent restore operations and prevents the restore target from starting until the [**DsRestoreRegisterComplete**](dsrestoreregistercomplete.md) function is called.

## Syntax


```C++
HRESULT DsRestoreRegister(
  _In_ HBC        hbc,
  _In_ LPCTSTR    szCheckPointFilePath,
  _In_ LPCTSTR    szLogPath,
  _In_ EDB_RSTMAP rgrstmap[],
  _In_ LONG       crstmap,
  _In_ LPCTSTR    szBackupLogPath,
  _In_ ULONG      genLow,
  _In_ ULONG      genHigh
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the restoration context handle obtained with the [**DsRestorePrepare**](dsrestoreprepare.md) function.

</dd> <dt>

*szCheckPointFilePath* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the path to the checkpoint file. This path is provided by the [**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md) function and has a **BFT** value of **BFT\_CHECKPOINT\_DIR**. Typically this is the same as the system database path. This path is required for proper backup restore function. This parameter cannot be **NULL**. Passing **NULL** in this parameter will cause an error during the restore process.

</dd> <dt>

*szLogPath* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the path where the log files will be restored. This path is provided by the [**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md) function and has a **BFT** value of **BFT\_LOG\_DIR**. If the path points to an empty directory, new log files are created there. This parameter cannot be **NULL**.

</dd> <dt>

*rgrstmap* \[in\]
</dt> <dd>

An array of [**EDB\_RSTMAP**](edb-rstmap.md) structures that contains the old and new paths for each database. There is one structure for each database. For the directory, there is a structure for the system database and another structure for the directory database. The order of the elements in the array does not matter. The *crstmap* parameter contains the number of elements in the array.

</dd> <dt>

*crstmap* \[in\]
</dt> <dd>

Contains the number of elements in the *rgrstmap* array.

</dd> <dt>

*szBackupLogPath* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the path where the backed up log files currently reside. This parameter cannot be **NULL**.

</dd> <dt>

*genLow* \[in\]
</dt> <dd>

Contains the lowest log number to restore in this restore session. This is a hexadecimal number in the range from 0x00000 to 0xFFFFF.

</dd> <dt>

*genHigh* \[in\]
</dt> <dd>

Contains the highest log number to restore in this restore session. This is a hexadecimal number in the range from 0x00000 to 0xFFFFF.

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

One or more parameters are invalid.

</dd> <dt>

**hrMissingExpiryToken**
</dt> <dd>

The expiry token supplied to [**DsRestorePrepare**](dsrestoreprepare.md) was invalid. This value is defined in Ntdsbmsg.h.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsRestoreRegisterW** (Unicode) and **DsRestoreRegisterA** (ANSI)<br/>           |



## See also

<dl> <dt>

[**DsRestoreRegisterComplete**](dsrestoreregistercomplete.md)
</dt> <dt>

[**DsRestorePrepare**](dsrestoreprepare.md)
</dt> <dt>

[**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md)
</dt> <dt>

[**DsRestoreEnd**](dsrestoreend.md)
</dt> <dt>

[**EDB\_RSTMAP**](edb-rstmap.md)
</dt> <dt>

[Restoring Active Directory](restoring-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

