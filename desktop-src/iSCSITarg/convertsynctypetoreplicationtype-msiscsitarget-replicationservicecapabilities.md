---
title: ConvertSyncTypeToReplicationType method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Converts the specified SyncType, Mode, and LocalOrRemote parameter values to a SupportedReplicationTypes value. This method is the inverse of the ConvertReplicationTypeToSyncType method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3e25189f-2336-4c99-8a2e-40a6b214aa89
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertSyncTypeToReplicationType method iSCSI Software Target API
- ConvertSyncTypeToReplicationType method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class
- MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , ConvertSyncTypeToReplicationType method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.ConvertSyncTypeToReplicationType
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConvertSyncTypeToReplicationType method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Converts the specified *SyncType*, *Mode*, and *LocalOrRemote* parameter values to a **SupportedReplicationTypes** value. This method is the inverse of the [**ConvertReplicationTypeToSyncType**](convertreplicationtypetosynctype-msiscsitarget-replicationservicecapabilities.md) method.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 ConvertSyncTypeToReplicationType(
  [in]  uint16 SyncType,
  [in]  uint16 Mode,
  [in]  uint16 LocalOrRemote,
  [out] uint16 SupportedReplicationTypes
);
```



## Parameters

<dl> <dt>

*SyncType* \[in\]
</dt> <dd>

Specifies the type of copy.

<dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>**Mirror** (6)


</dt> <dd>

Creates and maintains a copy of the source.

</dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>**Snapshot** (7)


</dt> <dd>

Creates a point-in-time (PIT), virtual copy of the source.

</dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>**Clone** (8)


</dt> <dd>

Creates an unsynchronized copy of the source.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

*Mode* \[in\]
</dt> <dd>

Specifies whether the target elements are updated synchronously or asynchronously.

The possible values are.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*LocalOrRemote* \[in\]
</dt> <dd>

Specifies local or remote replication.

The possible values are.

<dt>

<span id="Local"></span><span id="local"></span><span id="LOCAL"></span>

**Local** (2)


</dt> <dd></dd> <dt>

<span id="Remote"></span><span id="remote"></span><span id="REMOTE"></span>

**Remote** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SupportedReplicationTypes* \[out\]
</dt> <dd>

On return, contains a **SupportedReplicationTypes** value that represents the specified parameters.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Success** (0)
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

**DMTF Reserved** (7 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
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

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> <dt>

[**ConvertReplicationTypeToSyncType**](convertreplicationtypetosynctype-msiscsitarget-replicationservicecapabilities.md)
</dt> </dl>

 

 





