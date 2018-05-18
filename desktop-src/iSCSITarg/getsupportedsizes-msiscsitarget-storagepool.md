---
title: GetSupportedSizes method of the MSISCSITARGET\_StoragePool class
description: Retrieves a list of supported sizes for pools that support discrete sizes for volume or pool creation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '55dceffc-95bc-41ff-ab45-98dd94fefdbd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedSizes method iSCSI Software Target API", "GetSupportedSizes method iSCSI Software Target API , MSISCSITARGET_StoragePool class", "MSISCSITARGET_StoragePool class iSCSI Software Target API , GetSupportedSizes method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StoragePool.GetSupportedSizes
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedSizes method of the MSISCSITARGET\_StoragePool class

Retrieves a list of supported sizes for pools that support discrete sizes for volume or pool creation. The retrieved sizes may change after this method returns due to requests from other clients.

Different implementations may support either or both the **GetSupportedSizes** and [**GetSupportedSizeRange**](getsupportedsizerange-msiscsitarget-storagepool.md) methods, depending on pool configuration.

## Syntax


```mof
uint32 GetSupportedSizes(
  [in]  uint16                 ElementType,
  [in]  CIM_StorageSetting REF Goal,
  [out] uint64                 Sizes[]
);
```



## Parameters

<dl> <dt>

*ElementType* \[in\]
</dt> <dd>

Specifies the requested element type.

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

Specifies the [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance describing the requested element type.

</dd> <dt>

*Sizes* \[out\]
</dt> <dd>

On return contains a list of supported sizes in bytes.

</dd> </dl>

## Return value

This method returns one of the following values.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> </dl>

 

 





