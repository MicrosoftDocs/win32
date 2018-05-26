---
title: ConvertReplicationTypeToSyncType method of the CIM\_ReplicationServiceCapabilities class
description: This method does the opposite of the method ConvertSyncTypeToReplicationType. This method translates ReplicationType to the corresponding SyncType, Mode, Local/Remote.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99aa0470-1f54-4249-b9fc-d221a12280a8
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ConvertReplicationTypeToSyncType method iSCSI Software Target API
- ConvertReplicationTypeToSyncType method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , ConvertReplicationTypeToSyncType method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.ConvertReplicationTypeToSyncType
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConvertReplicationTypeToSyncType method of the CIM\_ReplicationServiceCapabilities class

This method does the opposite of the method ConvertSyncTypeToReplicationType. This method translates ReplicationType to the corresponding SyncType, Mode, Local/Remote.

## Syntax


```mof
uint32 ConvertReplicationTypeToSyncType(
  [in]  uint16 ReplicationType,
  [out] uint16 SyncType,
  [out] uint16 Mode,
  [out] uint16 LocalOrRemote
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*SyncType* \[out\]
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

*Mode* \[out\]
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

*LocalOrRemote* \[out\]
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


</dt> <dd>32768 65535</dd> </dl> </dd> </dl>

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

 

 





