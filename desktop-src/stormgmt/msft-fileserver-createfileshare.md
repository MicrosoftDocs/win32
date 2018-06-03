---
title: CreateFileShare method of the MSFT\_FileServer class
description: Creates a file share on the file server.
ms.assetid: 0567E773-D3C4-4BE8-83AA-2929A8064F45
keywords:
- CreateFileShare method Windows Storage Management API
- CreateFileShare method Windows Storage Management API , MSFT_FileServer class
- MSFT_FileServer class Windows Storage Management API , CreateFileShare method
topic_type:
- apiref
api_name:
- MSFT_FileServer.CreateFileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateFileShare method of the MSFT\_FileServer class

Creates a file share on the file server.

## Syntax


```mof
UInt32 CreateFileShare(
  [in]  String              Name,
  [in]  String              Description,
  [in]  String              SourceVolume,
  [in]  String              VolumeRelativePath,
  [in]  Boolean             ContinuouslyAvailable,
  [in]  Boolean             EncryptData,
  [in]  UInt16              FileSharingProtocol,
  [out] String              CreatedFileShare,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A semi-unique (scoped to the owning file server), human-readable string used to identify the file share.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A user settable description of the file share. This field can be used to store extra free-form information, such as notes or details about the intended usage.

</dd> <dt>

*SourceVolume* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_Volume**](msft-volume.md) object specifying the volume on which the share is to be created.

</dd> <dt>

*VolumeRelativePath* \[in\]
</dt> <dd>

The volume relative path of an existing directory to share. If this parameter is not provided, an empty share will be created.

</dd> <dt>

*ContinuouslyAvailable* \[in\]
</dt> <dd>

If **TRUE**, the share will be continuously available.

</dd> <dt>

*EncryptData* \[in\]
</dt> <dd>

If **TRUE**, the share data will be encrypted during transport.

</dd> <dt>

*FileSharingProtocol* \[in\]
</dt> <dd>

The file sharing protocol to be used by the share if the server supports more than one protocol.

<dl> <dt>

<span id="NFS"></span><span id="nfs"></span>**NFS** (2)
</dt> <dt>

<span id="CIFS_SMB_"></span><span id="cifs_smb_"></span>**CIFS(SMB)** (3)
</dt> </dl> </dd> <dt>

*CreatedFileShare* \[out\]
</dt> <dd>

This parameter receives a string that contains an embedded [**MSFT\_FileShare**](msft-fileshare.md) object representing the new file share.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**The requested access path is already in use.** (42002)
</dt> <dt>

**The access path is not valid.** (42007)
</dt> <dt>

**You must specify a name for this file share.** (58000)
</dt> <dt>

**You must specify a sharing protocol for this file share.** (58001)
</dt> <dt>

**You must specify a volume for this file share.** (58002)
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

[**MSFT\_FileServer**](msft-fileserver.md)
</dt> </dl>

 

 





