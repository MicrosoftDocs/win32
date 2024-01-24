---
title: DsRestoreEnd function (Ntdsbcli.h)
description: Called to terminate a restore operation.
ms.assetid: 2c3b9aba-3e92-4e5b-afff-3ed9bf64832b
ms.tgt_platform: multiple
keywords:
- DsRestoreEnd function Active Directory
topic_type:
- apiref
api_name:
- DsRestoreEnd
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsRestoreEnd function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsRestoreEnd** function is called to terminate a restore operation.

## Syntax


```C++
HRESULT DsRestoreEnd(
  _In_ HBC hbc
);
```



## Parameters

<dl> <dt>

*hbc* \[in\]
</dt> <dd>

Contains the restoration context handle obtained with the [**DsRestorePrepare**](dsrestoreprepare.md) function.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or a Win32 or RPC error code otherwise. The following list lists possible error codes.

<dl> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

*hbc* is not valid.

</dd> </dl>

## Remarks

The **DsRestoreEnd** function closes outstanding binding handles and performs a cleanup operation after a restore attempt.

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

[**DsRestorePrepare**](dsrestoreprepare.md)
</dt> <dt>

[Restoring an Active Directory Server](restoring-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

