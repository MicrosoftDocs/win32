---
title: CreateFileServer method of the MSFT\_StorageSubSystem class
description: Creates a file server on a storage subsystem.
ms.assetid: 60B1D607-A675-484C-8893-2B0F332A5094
keywords:
- CreateFileServer method Windows Storage Management API
- CreateFileServer method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , CreateFileServer method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateFileServer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateFileServer method of the MSFT\_StorageSubSystem class

Creates a file server on a storage subsystem.

## Syntax


```mof
UInt32 CreateFileServer(
  [in]  String              FriendlyName,
  [in]  UInt16              FileSharingProtocols[],
  [in]  String              HostNames[],
  [out] String              CreatedFileServer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Allows the user to specify the *FriendlyName* when the file server is created. A *FriendlyName* is expected to be descriptive, but it is not required to be unique.

Note that some storage subsystems do not allow setting a friendly name during file server creation. If a subsystem doesn't support this, file server creation will still succeed, but the file server may have a different name assigned to it.

</dd> <dt>

*FileSharingProtocols* \[in\]
</dt> <dd>

The file sharing protocols supported by the file server.

<dl> <dt>

<span id="NFS"></span><span id="nfs"></span>**NFS** (2)
</dt> <dt>

<span id="SMB"></span><span id="smb"></span>**SMB** (3)
</dt> </dl> </dd> <dt>

*HostNames* \[in\]
</dt> <dd>

The host name associated with each protocol specified in *FileSharingProtocols*.

</dd> <dt>

*CreatedFileServer* \[out\]
</dt> <dd>

If the file server is created successfully, this parameter receives a string that contains an embedded [**MSFT\_FileServer**](msft-fileserver.md) object.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Returns a reference to the storage job object used to track the long-running operation.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

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

**Object Not Found** (8)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





