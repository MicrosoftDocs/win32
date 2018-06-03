---
title: GetAvailableExtents method of the MSISCSITARGET\_StoragePool class
description: Retrieves a list of available CIM\_StorageExtent instances that can be used in the creation or modification of a MSISCSITARGET\_StoragePool, MSISCSITARGET\_StorageVolume, or CIM\_LogicalDisk instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4025861-518f-4647-8f3f-16fe2bc26483
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetAvailableExtents method iSCSI Software Target API
- GetAvailableExtents method iSCSI Software Target API , MSISCSITARGET_StoragePool class
- MSISCSITARGET_StoragePool class iSCSI Software Target API , GetAvailableExtents method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StoragePool.GetAvailableExtents
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetAvailableExtents method of the MSISCSITARGET\_StoragePool class

Retrieves a list of available **CIM\_StorageExtent** instances that can be used in the creation or modification of a [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md), [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md), or **CIM\_LogicalDisk** instance. The **GetAvailableExtents** method must return the extents from the set of component extents of the pool on which the method is being invoked. The returned extents are available at the time the method returns; there is no guarantee that they are available later.

## Syntax


```mof
uint32 GetAvailableExtents(
  [in]  CIM_StorageSetting Ref Goal,
  [out] CIM_StorageExtent Ref  AvailableExtents[]
);
```



## Parameters

<dl> <dt>

*Goal* \[in\]
</dt> <dd>

Specifies the [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance that defines the qualities of service and goals, which requested extents must support.

If set to **NULL** this method will return all available extents, which might cause an error if an extent is used inappropriately.

</dd> <dt>

*AvailableExtents* \[out\]
</dt> <dd>

On return, contains a list of references to available storage extents or subclass instances.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 4097)
</dt> <dt>

**Method Reserved** (4098 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> </dl>

 

 





