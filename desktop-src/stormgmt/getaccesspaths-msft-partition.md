---
title: GetAccessPaths method of the MSFT\_Partition class
description: Retrieves all mount points and drive letters that can be used to access the partition.
ms.assetid: a7c0e34e-b9f3-40ce-b81d-b4a46dc9c0ec
keywords:
- GetAccessPaths method Windows Storage Management API
- GetAccessPaths method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , GetAccessPaths method
topic_type:
- apiref
api_name:
- MSFT_Partition.GetAccessPaths
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

# GetAccessPaths method of the MSFT\_Partition class

Retrieves all mount points and drive letters that can be used to access the partition.

## Syntax


```mof
UInt32 GetAccessPaths(
  [out] String AccessPaths[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccessPaths* \[out\]
</dt> <dd>

An array of all the various mount points for the partition. This list includes drive letters, in addition to mounted folders.

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

 

 





