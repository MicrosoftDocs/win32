---
title: CreateFileSystem method of the MSFT\_SMPool class
description: Creates a file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd5197e1d-9c7b-4249-8f2a-5f11bc447fae'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateFileSystem method", "CreateFileSystem method, MSFT_SMPool class", "MSFT_SMPool class, CreateFileSystem method"]
topic_type:
- apiref
api_name:
- MSFT_SMPool.CreateFileSystem
api_location:
- StorageService.dll
api_type:
- COM
---

# CreateFileSystem method of the MSFT\_SMPool class

Creates a file system.

## Syntax


```mof
UInt32 CreateFileSystem(
  [in]            String                Name,
  [in]            UInt64                Size,
  [in]            MSFT_SMFileServer REF FileServer,
  [in]            Boolean               RunAsJob,
  [out]           MSFT_SMFileSystem REF CreatedFileSystem,
  [out]           MSFT_SMJob        REF CreatedStorageJob,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A human-readable string used to identify a file share. This name must be unique within the scope of the owning file server.

</dd> <dt>

*Size* \[in\]
</dt> <dd>

File system size

</dd> <dt>

*FileServer* \[in\]
</dt> <dd>

The file server to mount the file system to.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **True**, start a job to create the file system asynchronously.

</dd> <dt>

*CreatedFileSystem* \[out\]
</dt> <dd>

The [**MSFT\_SMFileSystem**](msft-smfilesystem.md) object created by calling this method.

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

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**An unexpected I/O error has occurred** (42002)
</dt> <dt>

**The requested access path is already in use.** (42007)
</dt> <dt>

**The access path is not valid.** (42008)
</dt> </dl>

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

[**MSFT\_SMPool**](msft-smpool.md)
</dt> </dl>

 

 





