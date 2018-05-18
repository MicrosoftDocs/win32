---
title: CreateFileShare method of the MSFT\_SMFileServer class
description: Creates a file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e1fe80a6-e8c8-403a-a102-23f624cce97d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateFileShare method", "CreateFileShare method, MSFT_SMFileServer class", "MSFT_SMFileServer class, CreateFileShare method"]
topic_type:
- apiref
api_name:
- MSFT_SMFileServer.CreateFileShare
api_location:
- StorageService.dll
api_type:
- COM
---

# CreateFileShare method of the MSFT\_SMFileServer class

Creates a file share.

## Syntax


```mof
UInt32 CreateFileShare(
  [in]            MSFT_SMFileSystem REF fileSystem,
  [in]            String                Name,
  [in]            UInt16                FileSharingProtocol,
  [in]            Boolean               IsContinuouslyAvailable,
  [in]            Boolean               EncryptData,
  [in]            Boolean               RunAsJob,
  [out]           MSFT_SMFileShare  REF CreatedFileShare,
  [out]           MSFT_SMJob        REF CreatedStorageJob,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*fileSystem* \[in\]
</dt> <dd>

The pool or volume on which the share is created.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

A human-readable string used to identify a file share. This name must be unique within the scope of the owning file server.

</dd> <dt>

*FileSharingProtocol* \[in\]
</dt> <dd>

The file sharing protocol used by the share.

The possible values are.

<dt>

<span id="NFS"></span><span id="nfs"></span>

**NFS** (2)


</dt> <dd></dd> <dt>

<span id="SMB"></span><span id="smb"></span>

**SMB** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*IsContinuouslyAvailable* \[in\]
</dt> <dd>

If **True** the share is continuously available.

</dd> <dt>

*EncryptData* \[in\]
</dt> <dd>

If **True** the share is encrypted.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **True**, start a job to create the file share asynchronously.

</dd> <dt>

*CreatedFileShare* \[out\]
</dt> <dd>

The [**MSFT\_SMFileShare**](msft-smfileshare.md) object created by calling this method.

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

[**MSFT\_SMFileServer**](msft-smfileserver.md)
</dt> </dl>

 

 





