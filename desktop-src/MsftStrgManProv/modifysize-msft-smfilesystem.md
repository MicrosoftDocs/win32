---
title: ModifySize method of the MSFT\_SMFileSystem class
description: Resizes the file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '370d4e2e-e079-4696-a8ba-037cd5f20ae0'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifySize method", "ModifySize method, MSFT_SMFileSystem class", "MSFT_SMFileSystem class, ModifySize method"]
topic_type:
- apiref
api_name:
- MSFT_SMFileSystem.ModifySize
api_location:
- StorageService.dll
api_type:
- COM
---

# ModifySize method of the MSFT\_SMFileSystem class

Resizes the file system.

## Syntax


```mof
UInt32 ModifySize(
  [in, out]       UInt64                Size,
  [in]            Boolean               RunAsJob,
  [out]           MSFT_SMJob        REF CreatedStorageJob,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Size* \[in, out\]
</dt> <dd>

The new size of the file system, in bytes.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

**true** to start a job to modifies the file system asynchronously; otherwise, **False**.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMFileSystem**](msft-smfilesystem.md)
</dt> </dl>

 

 





