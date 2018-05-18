---
title: GetSupportedReplicationSettingData method of the CIM\_ReplicationServiceCapabilities class
description: This method, for a given ReplicationType and a supplied property, returns an array of supported settings that can be utilized in an instance of the ReplicationSettingData class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c94358fd-4049-4c8c-92a3-d60ae099d752'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedReplicationSettingData method iSCSI Software Target API", "GetSupportedReplicationSettingData method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedReplicationSettingData method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedReplicationSettingData
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedReplicationSettingData method of the CIM\_ReplicationServiceCapabilities class

This method, for a given ReplicationType and a supplied property, returns an array of supported settings that can be utilized in an instance of the ReplicationSettingData class.

## Syntax


```mof
uint32 GetSupportedReplicationSettingData(
  [in]  uint16 ReplicationType,
  [in]  uint16 PropertyName,
  [out] uint64 SupportedValues[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*PropertyName* \[in\]
</dt> <dd>

A value representing the property name.

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


</dt> <dd>16–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*SupportedValues* \[out\]
</dt> <dd>

An array containing the supported values that can be supplied in an instance of a ReplicationSettingData. Refer to the class ReplicationSettingData for the possible values for each property. For boolean data, use the following data mapping: 2="false", 3="true".

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

**DMTF Reserved** (7–32767)
</dt> <dt>

**Vendor Specific** (32768–4294967295)
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

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





