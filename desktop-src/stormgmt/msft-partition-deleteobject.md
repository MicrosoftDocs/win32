---
title: DeleteObject method of the MSFT\_Partition class
description: Deletes the partition and corresponding volume.
ms.assetid: 4B1C92EE-4835-428E-BF52-4C816A60B418
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
api_name:
- MSFT_Partition.DeleteObject
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

# DeleteObject method of the MSFT\_Partition class

Deletes the partition and corresponding volume.

## Syntax


```mof
UInt32 DeleteObject(
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

**In use** (6)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**The partition was deleted, although its access paths were not.** (42000)
</dt> <dt>

**The extended partition still contains other partitions.** (42001)
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

[**MSFT\_Partition**](msft-partition.md)
</dt> </dl>

 

 





