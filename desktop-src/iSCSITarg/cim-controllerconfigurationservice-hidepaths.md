---
title: HidePaths method of the CIM\_ControllerConfigurationService class
description: Hide a list of SCSI logical units (such as a RAID volume or tape drive) from a list of initiators and/or target ports on a SCSIProtocolController (SPC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0475cd41-57fb-414c-976f-061d77b83e6c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["HidePaths method iSCSI Software Target API", "HidePaths method iSCSI Software Target API , CIM_ControllerConfigurationService class", "CIM_ControllerConfigurationService class iSCSI Software Target API , HidePaths method"]
topic_type:
- apiref
api_name:
- CIM_ControllerConfigurationService.HidePaths
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# HidePaths method of the CIM\_ControllerConfigurationService class

Hide a list of SCSI logical units (such as a RAID volume or tape drive) from a list of initiators and/or target ports on a SCSIProtocolController (SPC).

When hiding logical units, there are three specific use cases identified. The instrumentation MUST support these use cases. Other permutations are allowed, but are vendor-specific. The use cases are: Remove LUs from a view, Remove initiator IDs from a view, and Remove target port IDs from a view. Remove LUs from a view requires that the LUNames parameter not be null and that the InitiatorIDs and TargetPortIDs parameters be null. Remove initiator IDs from a view requires that the LUNames parameter be null, that the InitiatorIDs not be null, and that the TargetPortIDs parameters be null. Remove target port IDs from a view requires that the LUNames and InitiatorPortIDs parameters be null.

The disposition of the SPC when the last logical unit, initiator ID, or target port ID is removed depends upon the CIM\_ProtocolControllerMaskingCapabilites SPCAllowsNo\* properties. If SPCAllowsNoLUs is false, then the SPC is automatically deleted when the last logical unit is removed. If SPCAllowsNoTargets is false, then the SPC is automatically deleted when the last target port ID is removed. If SPCAllowsNoInitiators is false, then the SPC is automatically deleted when the last initiator port ID is removed. In all other cases, the SPC MUST be explicitly deleted via the DeleteInstance intrinsic function.

## Syntax


```mof
uint32 HidePaths(
  [out]     CIM_ConcreteJob            REF Job,
  [in]      string                         LUNames[],
  [in]      string                         InitiatorPortIDs[],
  [in]      string                         TargetPortIDs[],
  [in, out] CIM_SCSIProtocolController REF ProtocolControllers[]
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job if 'Method Parameters Checked - Job Started' is returned (MAY be null if job completed).

</dd> <dt>

*LUNames* \[in\]
</dt> <dd>

An array of IDs of logical units. The LU instances MUST already exist. The members of this array MUST match the Name property of LogicalDevice instances. See the method description for conditions where this MAY be null.

</dd> <dt>

*InitiatorPortIDs* \[in\]
</dt> <dd>

IDs of initiator ports. See the method description for conditions where this MAY be null.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

IDs of target ports. See the method description for conditions where this MAY be null.

</dd> <dt>

*ProtocolControllers* \[in, out\]
</dt> <dd>

An array of references to SCSIProtocolControllers (SPCs). On input, this MUST contain exactly one element; there MAY be multiple references on output. The instrumentation will attempt to remove associations (LUNames, InitiatorPortIDs, or TargetPortIDs) from this SPC. Depending upon the specific implementation, the instrumentation MAY need to create new SPCs with a subset of the remaining associations. On output, this is an array of references to SPCs created or modified as the result of processing the request.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid logical unit ID** (4097)
</dt> <dt>

**Invalid initiator port ID** (4098)
</dt> <dt>

**Invalid target port ID** (4099)
</dt> <dt>

**Target/initiator combination not exposed** (4100)
</dt> <dt>

**Method Reserved** (4101–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
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

[**CIM\_ControllerConfigurationService**](cim-controllerconfigurationservice.md)
</dt> </dl>

 

 





