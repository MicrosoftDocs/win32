---
title: GetSupportedSizeRange method of the CIM\_StoragePool class
description: For pools that support a range of sizes for volume or pool creation, this method can be used to retrieve the supported range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '72d1ec89-a3f2-4e72-b423-a31f7d36bd11'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedSizeRange method iSCSI Software Target API", "GetSupportedSizeRange method iSCSI Software Target API , CIM_StoragePool class", "CIM_StoragePool class iSCSI Software Target API , GetSupportedSizeRange method"]
topic_type:
- apiref
api_name:
- CIM_StoragePool.GetSupportedSizeRange
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedSizeRange method of the CIM\_StoragePool class

For pools that support a range of sizes for volume or pool creation, this method can be used to retrieve the supported range. Note that different pool implementations may support either or both the GetSupportedSizes and GetSupportedSizeRanges methods at different times, depending on Pool configuration. Also note that the advertised sizes may change after the call due to requests from other clients. If the pool currently only supports discrete sizes, then the return value will be set to 1.

## Syntax


```mof
uint32 GetSupportedSizeRange(
  [in]  uint16                 ElementType,
  [in]  CIM_StorageSetting REF Goal,
  [out] uint64                 MinimumVolumeSize,
  [out] uint64                 MaximumVolumeSize,
  [out] uint64                 VolumeSizeDivisor
);
```



## Parameters

<dl> <dt>

*ElementType* \[in\]
</dt> <dd>

The type of element for which supported size ranges are reported for.

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

The StorageSetting for which supported size ranges should be reported for.

</dd> <dt>

*MinimumVolumeSize* \[out\]
</dt> <dd>

The minimum size for a volume/pool in bytes.

</dd> <dt>

*MaximumVolumeSize* \[out\]
</dt> <dd>

The maximum size for a volume/pool in bytes.

</dd> <dt>

*VolumeSizeDivisor* \[out\]
</dt> <dd>

A volume/pool size must be a multiple of this value which is specified in bytes.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Use GetSupportedSizes instead** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StoragePool**](cim-storagepool.md)
</dt> </dl>

 

 





