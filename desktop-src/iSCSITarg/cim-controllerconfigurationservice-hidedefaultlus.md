---
title: HideDefaultLUs method of the CIM\_ControllerConfigurationService class
description: Hide a list of SCSI logical units (such as RAID volumes or tape drives) through a list of target ports on a default view SCSIProtocolController (SPC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da29e8d4-9839-45ad-a891-5bb9374c1f36
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- HideDefaultLUs method iSCSI Software Target API
- HideDefaultLUs method iSCSI Software Target API , CIM_ControllerConfigurationService class
- CIM_ControllerConfigurationService class iSCSI Software Target API , HideDefaultLUs method
topic_type:
- apiref
api_name:
- CIM_ControllerConfigurationService.HideDefaultLUs
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# HideDefaultLUs method of the CIM\_ControllerConfigurationService class

Hide a list of SCSI logical units (such as RAID volumes or tape drives) through a list of target ports on a default view SCSIProtocolController (SPC).

The parameters for this method are: Job - null if no job created, otherwise this is a reference to the job. LUNames - the list of names of the logical units to use. TargetPortIDs - the names of the target ports to use. ProtocolControllers - SPCs involved in this operation.

When hiding logical units, there are two specific use cases identified. The instrumentation MUST support the Remove LUs case and MUST support the remove target port IDs if PortsPerView is set to 'Multiple Ports per View'. Other permutations are allowed, but are vendor-specific. The use cases are: Remove LUs from a default view and Remove target port IDs from a default view. Remove LUs from a default view requires that the LUNames parameter not be null and that the TargetPortIDs parameter be null. Remove target port IDs from a default view is required if PortsPerView is Multiple Ports per view. It requires that the LUNames parameter be null.

If both LUNames and TargetIDs parameters are non-null and CIM\_ProtocolControllerMaskingCapabilities.MaximumMapCount is 0, then the instrumentation MUST create new SPCs and change associations as necessary to meet the client request and maintain the relevant rules of SCSI in the ExposeDefaultLUs description. If both LUNames and TargetIDs parameters are non-null and CIM\_ProtocolControllerMaskingCapabilities.MaximumMapCount is greater than 0, then any client request that cannot be honored by changing associations to the specified SPC will receive a 'Maximum Map Count Error' response.

The disposition of the SPC when the last logical unit or target port ID is removed depends upon the CIM\_ProtocolControllerMaskingCapabilites SPCAllowsNo\* properties. If SPCAllowsNoLUs is false, then the SPC is automatically deleted when the last logical unit is removed. If SPCAllowsNoTargets is false, then the SPC is automatically deleted when the last target port ID is removed. In all other cases, the SPC MUST be explicitly deleted via the DeleteInstance intrinsic function.

## Syntax


```mof
uint32 HideDefaultLUs(
  [out]     CIM_ConcreteJob            REF Job,
  [in]      string                         LUNames[],
  [in]      string                         TargetPortIDs[],
  [in, out] CIM_SCSIProtocolController REF ProtocolControllers[]
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

A list of IDs of logical units. Each LU instance MUST already exist. See the method description for conditions where this MAY be null.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

IDs of target ports. See the method description for conditions where this MAY be null.

</dd> <dt>

*ProtocolControllers* \[in, out\]
</dt> <dd>

An array of references to SCSIProtocolControllers (SPCs). On input, this MUST contain exactly one element; there MAY be multiple references on output. The instrumentation will attempt to remove associations (LUNames or TargetPortIDs) from this SPC. Depending upon the specific implementation, the instrumentation MAY need to create new SPCs with a subset of the remaining associations. On output, this is an array of references to SPCs created or modified as the result of processing the request.

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

**DMTF Reserved** (6 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid logical unit ID** (4097)
</dt> <dt>

**Invalid target port ID** (4098)
</dt> <dt>

**Maximum Map Count Error** (4099)
</dt> <dt>

**Method Reserved** (4100 32767)
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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ControllerConfigurationService**](cim-controllerconfigurationservice.md)
</dt> </dl>

 

 





