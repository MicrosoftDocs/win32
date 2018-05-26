---
title: Offline method of the MSFT\_Disk class
description: Takes the disk offline.
ms.assetid: B7AA8543-0623-40C6-A906-09DE0B0D19FB
keywords:
- Offline method Windows Storage Management API
- Offline method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , Offline method
topic_type:
- apiref
api_name:
- MSFT_Disk.Offline
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

# Offline method of the MSFT\_Disk class

Takes the disk offline.

## Syntax


```mof
UInt32 Offline(
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

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

**Disk is in use** (6)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**Operation not supported on a critical disk.** (41009)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](msft-disk.md)
</dt> </dl>

 

 





