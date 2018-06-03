---
title: ConvertSyncTypeToReplicationType method of the CIM\_ReplicationServiceCapabilities class
description: The majority of the methods in this class accept ReplicationType which represents a combination of SyncType, Mode, Local/Remote.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dddff2cb-b6d9-495f-89e8-23cbb8a975d1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertSyncTypeToReplicationType method iSCSI Software Target API
- ConvertSyncTypeToReplicationType method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , ConvertSyncTypeToReplicationType method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.ConvertSyncTypeToReplicationType
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertSyncTypeToReplicationType method of the CIM\_ReplicationServiceCapabilities class

The majority of the methods in this class accept ReplicationType which represents a combination of SyncType, Mode, Local/Remote. This method accepts the supplied information and returns the corresponding ReplicationType, which can be passed to other methods to get the additional capabilities.

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

The type of copy.

<dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>**Mirror** (6)


</dt> <dd>

Create and maintain a copy of the source.

</dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>**Snapshot** (7)


</dt> <dd>

Create a PIT, virtual copy of the source.

</dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>**Clone** (8)


</dt> <dd>

Create an unsynchronized copy of the source.

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

Mode describes whether the target elements will be updated synchronously or asynchronously.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*LocalOrRemote* \[in\]
</dt> <dd>

Copy to local or remote replica.

<dt>

<span id="Local"></span><span id="local"></span><span id="LOCAL"></span>

**Local** (2)


</dt> <dd></dd> <dt>

<span id="Remote"></span><span id="remote"></span><span id="REMOTE"></span>

**Remote** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SupportedReplicationTypes* \[out\]
</dt> <dd>

A value representing the ReplicationType.

</dd> </dl>

## Return value

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

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
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

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





