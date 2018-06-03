---
title: GetSupportedSizes method of the CIM\_StoragePool class
description: For pools that support discrete sizes for volume or pool creation, this method can be used to retrieve a list of supported sizes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d1e42e0d-de28-4508-9e89-c3bfb9076964
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedSizes method iSCSI Software Target API
- GetSupportedSizes method iSCSI Software Target API , CIM_StoragePool class
- CIM_StoragePool class iSCSI Software Target API , GetSupportedSizes method
topic_type:
- apiref
api_name:
- CIM_StoragePool.GetSupportedSizes
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedSizes method of the CIM\_StoragePool class

For pools that support discrete sizes for volume or pool creation, this method can be used to retrieve a list of supported sizes. Note that different pool implementations may support either or both the GetSupportedSizes and GetSupportedSizeRanges methods at different times, depending on Pool configuration. Also note that the advertised sizes may change after the call due to requests from other clients. If the pool currently only supports a range of sizes, then the return value will be set to 1.

## Syntax


```mof
uint32 GetSupportedSizes(
  [in]  uint16                 ElementType,
  [in]  CIM_StorageSetting REF Goal,
  [out] uint64                 Sizes[]
);
```



## Parameters

<dl> <dt>

*ElementType* \[in\]
</dt> <dd>

The type of element for which supported sizes are reported for.

<dt>

<span id="Storage_Pool"></span><span id="storage_pool"></span><span id="STORAGE_POOL"></span>

**Storage Pool** (2)


</dt> <dd></dd> <dt>

<span id="Storage_Volume"></span><span id="storage_volume"></span><span id="STORAGE_VOLUME"></span>

**Storage Volume** (3)


</dt> <dd></dd> <dt>

<span id="Logical_Disk"></span><span id="logical_disk"></span><span id="LOGICAL_DISK"></span>

**Logical Disk** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*Goal* \[in\]
</dt> <dd>

The StorageSetting for which supported sizes should be reported for.

</dd> <dt>

*Sizes* \[out\]
</dt> <dd>

List of supported sizes for a Volume/Pool creation or modification.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Use GetSupportedSizeRange instead** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StoragePool**](cim-storagepool.md)
</dt> </dl>

 

 





