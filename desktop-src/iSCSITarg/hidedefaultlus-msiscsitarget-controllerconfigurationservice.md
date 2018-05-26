---
title: HideDefaultLUs method of the MSISCSITARGET\_ControllerConfigurationService class
description: Hides a list of SCSI logical units, such as RAID volumes or tape drives, through a list of target ports on a default view CIM\_SCSIProtocolController (SPC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5ed7bfeb-cbbe-47cd-91b7-98e4bded331e
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- HideDefaultLUs method iSCSI Software Target API
- HideDefaultLUs method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class
- MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , HideDefaultLUs method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.HideDefaultLUs
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# HideDefaultLUs method of the MSISCSITARGET\_ControllerConfigurationService class

Hides a list of SCSI logical units, such as RAID volumes or tape drives, through a list of target ports on a default view [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) (SPC).

This method is inherited from the **CIM\_ControllerConfigurationService** class.

## Syntax


```mof
uint32 HideDefaultLUs(
  [out]     CIM_ConcreteJob Ref            Job,
  [in]      string                         LUNames[],
  [in]      string                         TargetPortIDs[],
  [in, out] CIM_SCSIProtocolController Ref ProtocolControllers[]
);
```



## Parameters

<dl> <dt>

*Job* \[out\]
</dt> <dd>

On return contains a reference to the job if one is created. **NULL** if no job is created or it has completed.

</dd> <dt>

*LUNames* \[in\]
</dt> <dd>

Specifies the IDs of existing logical unit instances to use. The logical unit instances must already exist. The members of this array must match the **Name** property of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) instances that represent SCSI logical units. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

Specifies the IDs of target ports to use. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*ProtocolControllers* \[in, out\]
</dt> <dd>

Contains an array of references to [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instances.

On input, this must contain exactly one SPC. On return this is an array of references to the SPCs created or modified as the result of processing the request.

The implementation will attempt to remove associations, *LUNames* and *TargetPortIDs*, from this SPC. The implementation may need to create new SPCs with a subset of the remaining associations.

</dd> </dl>

## Return value

This method returns one of the following values.

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

## Remarks

When hiding logical units, there are two scenarios that the implementation must support. Each scenario requires a different combination of parameters. Other vendor-specific scenarios are allowed.

-   **Remove logical units from a default view**

    The *LUNames* parameter must not be **NULL** and that the *TargetPortIDs* parameter must be **NULL**.

-   **Remove target port IDs from a default view**

    This scenario is only possible if the **CIM\_ProtocolControllerMaskingCapabilities.PortsPerView** property has the value **Multiple Ports Per View**.

    The *LUNames* parameter must be **NULL**.

If both the *LUNames* and *TargetIDs* parameters are non-null and the **CIM\_ProtocolControllerMaskingCapabilities.MaximumMapCount** is zero, then the instrumentation must create new SPCs and change associations as necessary to meet the client request and maintain the relevant SCSI rules.

For example:

-   An SPC may not be exposed through a particular host/target port pair that is in use by another SPC. That is, an SPC together with its associated logical units and ports correspond to the logical unit inventory provided by SCSI REPORT LUNS and INQUIRY commands.
-   Each logical device associated to an SPC must have a unique **ProtocolControllerForUnit.DeviceNumber** logical unit number.

If both the *LUNames* and *TargetIDs* parameters are non-null and the **CIM\_ProtocolControllerMaskingCapabilities.MaximumMapCount** is greater than zero, then any client request that cannot be honored by changing associations to the specified SPC will return a **Maximum Map Count Error** error.

The SPC may be automatically deleted when the last logical unit, initiator ID, or target port ID is removed depending on the state of **CIM\_ProtocolControllerMaskingCapabilites** properties. If the **SPCAllowsNoLUs** property is false, then the SPC is automatically deleted when the last logical unit is removed. If the **SPCAllowsNoTargets** is false, then the SPC is automatically deleted when the last target port ID is removed. In all other cases, the SPC must be explicitly deleted via the **DeleteInstance** method.

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

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerMaskingCapabilities**](msiscsitarget-protocolcontrollermaskingcapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerForUnit**](msiscsitarget-protocolcontrollerforunit.md)
</dt> <dt>

[**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md)
</dt> </dl>

 

 





