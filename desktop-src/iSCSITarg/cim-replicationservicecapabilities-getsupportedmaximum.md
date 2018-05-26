---
title: GetSupportedMaximum method of the CIM\_ReplicationServiceCapabilities class
description: This method accepts a ReplicationType and a component, it then returns a static numeric value representing the maximum number of the specified component that the service supports.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: deff4294-4358-4f57-bd3b-9beacc622dde
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedMaximum method iSCSI Software Target API
- GetSupportedMaximum method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedMaximum method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedMaximum
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedMaximum method of the CIM\_ReplicationServiceCapabilities class

This method accepts a ReplicationType and a component, it then returns a static numeric value representing the maximum number of the specified component that the service supports. A value of 0 indicates unlimited components of the given type. In all cases the maximum value is bound by the availability of resources on the computer system. Effectively, the method informs clients of the edge conditions.

## Syntax


```mof
uint32 GetSupportedMaximum(
  [in]  uint16 ReplicationType,
  [in]  uint16 Component,
  [out] uint64 MaxValue
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*Component* \[in\]
</dt> <dd>

For the given Mirror, Snapshot, Clone and their mode and locality variations as specified by ReplicationType, this parameter represents one of the following components: Number of groups: Maximum number of groups supported by the replication service.Number of elements per source group: Maximum number of elements in a group that can be used as a source group. Number of elements per target group: Maximum number of elements in a group that can be used as a target group. Number of target elements per source element: Maximum number of target elements per source element. Number of total source elements: Maximum number of total source elements supported by the service. Number of total target elements: Maximum number of total target elements supported by the source. Number of peer systems: Maximum number of peer systems that replication service can communicate with. Number of hops in multi-hop replication: Maximum number of hops in multi-hop replication the service can manage.

<dt>

<span id="Number_of_groups"></span><span id="number_of_groups"></span><span id="NUMBER_OF_GROUPS"></span>

**Number of groups** (2)


</dt> <dd></dd> <dt>

<span id="Number_of_elements_per_source_group"></span><span id="number_of_elements_per_source_group"></span><span id="NUMBER_OF_ELEMENTS_PER_SOURCE_GROUP"></span>

**Number of elements per source group** (3)


</dt> <dd></dd> <dt>

<span id="Number_of_elements_per_target_group"></span><span id="number_of_elements_per_target_group"></span><span id="NUMBER_OF_ELEMENTS_PER_TARGET_GROUP"></span>

**Number of elements per target group** (4)


</dt> <dd></dd> <dt>

<span id="Number_of_target_elements_per_source_element"></span><span id="number_of_target_elements_per_source_element"></span><span id="NUMBER_OF_TARGET_ELEMENTS_PER_SOURCE_ELEMENT"></span>

**Number of target elements per source element** (5)


</dt> <dd></dd> <dt>

<span id="Number_of_total_source_elements"></span><span id="number_of_total_source_elements"></span><span id="NUMBER_OF_TOTAL_SOURCE_ELEMENTS"></span>

**Number of total source elements** (6)


</dt> <dd></dd> <dt>

<span id="Number_of_total_target_elements"></span><span id="number_of_total_target_elements"></span><span id="NUMBER_OF_TOTAL_TARGET_ELEMENTS"></span>

**Number of total target elements** (7)


</dt> <dd></dd> <dt>

<span id="Number_of_peer_systems"></span><span id="number_of_peer_systems"></span><span id="NUMBER_OF_PEER_SYSTEMS"></span>

**Number of peer systems** (8)


</dt> <dd></dd> <dt>

<span id="Number_of_hops_in_multi-hop_copy"></span><span id="number_of_hops_in_multi-hop_copy"></span><span id="NUMBER_OF_HOPS_IN_MULTI-HOP_COPY"></span>

**Number of hops in multi-hop copy** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*MaxValue* \[out\]
</dt> <dd>

The maximum value, or 0 if the maximum is unlimited.

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

**Information is not available** (7)
</dt> <dt>

**DMTF Reserved** (8 32767)
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

 

 





