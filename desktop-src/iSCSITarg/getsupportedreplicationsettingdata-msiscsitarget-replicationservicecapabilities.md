---
title: GetSupportedReplicationSettingData method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the supported property values for the specified CIM\_ReplicationSettingData property and replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9026370d-6400-47df-9235-64dd5fbb4cf5
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedReplicationSettingData method iSCSI Software Target API
- GetSupportedReplicationSettingData method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class
- MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedReplicationSettingData method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedReplicationSettingData
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedReplicationSettingData method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the supported property values for the specified **CIM\_ReplicationSettingData** property and replication type.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedReplicationSettingData(
  [in]  uint16 ReplicationType,
  [in]  uint16 PropertyName,
  [out] uint64 SupportedValues[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Specifies the replication type.

The [**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md).**SupportedReplicationTypes** property values are.

<dt>

<span id="Synchronous_Mirror_Local"></span><span id="synchronous_mirror_local"></span><span id="SYNCHRONOUS_MIRROR_LOCAL"></span>

**Synchronous Mirror Local** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Local"></span><span id="asynchronous_mirror_local"></span><span id="ASYNCHRONOUS_MIRROR_LOCAL"></span>

**Asynchronous Mirror Local** (3)


</dt> <dd></dd> <dt>

<span id="Synchronous_Mirror_Remote"></span><span id="synchronous_mirror_remote"></span><span id="SYNCHRONOUS_MIRROR_REMOTE"></span>

**Synchronous Mirror Remote** (4)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Remote"></span><span id="asynchronous_mirror_remote"></span><span id="ASYNCHRONOUS_MIRROR_REMOTE"></span>

**Asynchronous Mirror Remote** (5)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Local"></span><span id="synchronous_snapshot_local"></span><span id="SYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Synchronous Snapshot Local** (6)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Local"></span><span id="asynchronous_snapshot_local"></span><span id="ASYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Asynchronous Snapshot Local** (7)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Remote"></span><span id="synchronous_snapshot_remote"></span><span id="SYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Synchronous Snapshot Remote** (8)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Remote"></span><span id="asynchronous_snapshot_remote"></span><span id="ASYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Asynchronous Snapshot Remote** (9)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Local"></span><span id="synchronous_clone_local"></span><span id="SYNCHRONOUS_CLONE_LOCAL"></span>

**Synchronous Clone Local** (10)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Local"></span><span id="asynchronous_clone_local"></span><span id="ASYNCHRONOUS_CLONE_LOCAL"></span>

**Asynchronous Clone Local** (11)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Remote"></span><span id="synchronous_clone_remote"></span><span id="SYNCHRONOUS_CLONE_REMOTE"></span>

**Synchronous Clone Remote** (12)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Remote"></span><span id="asynchronous_clone_remote"></span><span id="ASYNCHRONOUS_CLONE_REMOTE"></span>

**Asynchronous Clone Remote** (13)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*PropertyName* \[in\]
</dt> <dd>

Specifies the property name to query.

The possible values are.

<dt>

<span id="ConsistentPointInTime"></span><span id="consistentpointintime"></span><span id="CONSISTENTPOINTINTIME"></span>

**ConsistentPointInTime** (2)


</dt> <dd></dd> <dt>

<span id="DesiredCopyMethodology"></span><span id="desiredcopymethodology"></span><span id="DESIREDCOPYMETHODOLOGY"></span>

**DesiredCopyMethodology** (3)


</dt> <dd></dd> <dt>

<span id="Multihop"></span><span id="multihop"></span><span id="MULTIHOP"></span>

**Multihop** (4)


</dt> <dd></dd> <dt>

<span id="OnGroupOrListError"></span><span id="ongrouporlisterror"></span><span id="ONGROUPORLISTERROR"></span>

**OnGroupOrListError** (5)


</dt> <dd></dd> <dt>

<span id="UnequalGroupsAction"></span><span id="unequalgroupsaction"></span><span id="UNEQUALGROUPSACTION"></span>

**UnequalGroupsAction** (6)


</dt> <dd></dd> <dt>

<span id="TargetElementSupplier"></span><span id="targetelementsupplier"></span><span id="TARGETELEMENTSUPPLIER"></span>

**TargetElementSupplier** (7)


</dt> <dd></dd> <dt>

<span id="ThinProvisioningPolicy"></span><span id="thinprovisioningpolicy"></span><span id="THINPROVISIONINGPOLICY"></span>

**ThinProvisioningPolicy** (8)


</dt> <dd></dd> <dt>

<span id="Pairing"></span><span id="pairing"></span><span id="PAIRING"></span>

**Pairing** (9)


</dt> <dd></dd> <dt>

<span id="FailedCopyStopsHostIO"></span><span id="failedcopystopshostio"></span><span id="FAILEDCOPYSTOPSHOSTIO"></span>

**FailedCopyStopsHostIO** (10)


</dt> <dd></dd> <dt>

<span id="CopyRecoveryMode"></span><span id="copyrecoverymode"></span><span id="COPYRECOVERYMODE"></span>

**CopyRecoveryMode** (11)


</dt> <dd></dd> <dt>

<span id="UnequalListsAction"></span><span id="unequallistsaction"></span><span id="UNEQUALLISTSACTION"></span>

**UnequalListsAction** (12)


</dt> <dd></dd> <dt>

<span id="DeltaUpdateInterval"></span><span id="deltaupdateinterval"></span><span id="DELTAUPDATEINTERVAL"></span>

**DeltaUpdateInterval** (13)


</dt> <dd></dd> <dt>

<span id="DeltaUpdateBlocks"></span><span id="deltaupdateblocks"></span><span id="DELTAUPDATEBLOCKS"></span>

**DeltaUpdateBlocks** (14)


</dt> <dd></dd> <dt>

<span id="ReadOnly"></span><span id="readonly"></span><span id="READONLY"></span>

**ReadOnly** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SupportedValues* \[out\]
</dt> <dd>

On return, indicates the supported values for the specified property.

For a list of possible values for each property, see the **CIM\_ReplicationSettingData** class on the [DMTF](http://schemas.dmtf.org/wbem/cim-html/2.31.0+/CIM_ReplicationSettingData.mdl) website at http://schemas.dmtf.org/wbem/cim-html/2.31.0+/CIM\_ReplicationSettingData.html.

For Boolean properties, 3 indicates **True** and 2 indicates **false.**

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

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





