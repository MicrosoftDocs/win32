---
title: DsBackupRead function (Ntdsbcli.h)
description: Reads a block of data from the current open file, into a buffer.
ms.assetid: 01576d41-3cd6-4540-966b-7d98561f7b8c
ms.tgt_platform: multiple
keywords:
- DsBackupRead function Active Directory
topic_type:
- apiref
api_name:
- DsBackupRead
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsBackupRead function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsBackupRead** function reads a block of data from the current open file, into a buffer. The client application is expected to call this function repeatedly until the entire backup file has been received. The [**DsBackupOpenFile**](dsbackupopenfile.md) function provides the entire size of the backup file.

## Syntax


```C++
HRESULT DsBackupRead(
  _In_  HBC    hbc,
  _In_  PVOID  pvBuffer,
  _In_  DWORD  cbBuffer,
  _Out_ PDWORD pcbRead
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the backup context handle obtained with the [**DsBackupPrepare**](dsbackupprepare.md) function.

</dd> <dt>

*pvBuffer* \[in\]
</dt> <dd>

Pointer to a buffer that receives the data. This buffer must be at least *cbBuffer* bytes in size.

</dd> <dt>

*cbBuffer* \[in\]
</dt> <dd>

Contains the size, in bytes, of the buffer at *pvBuffer*. This value must be a multiple of 8192 and must be greater than or equal to 24576.

</dd> <dt>

*pcbRead* \[out\]
</dt> <dd>

Pointer to a **DWORD** value that receives the actual number of bytes read. This may be less than the number of bytes requested because some transports fragment the buffer being transmitted instead of filling the entire buffer with data.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or a Win32 or RPC error code otherwise. Possible error codes include the following.

<dl> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

One or more parameters are not valid.

</dd> <dt>

**ERROR\_HANDLE\_EOF**
</dt> <dd>

The end of the backup file was reached.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |



## See also

<dl> <dt>

[**DsBackupOpenFile**](dsbackupopenfile.md)
</dt> <dt>

[**DsBackupPrepare**](dsbackupprepare.md)
</dt> <dt>

[**DsBackupFree**](dsbackupfree.md)
</dt> <dt>

[Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

