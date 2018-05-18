---
title: HidePaths method of the MSISCSITARGET\_ControllerConfigurationService class
description: Hides a list of SCSI logical units such as a RAID volume or tape drive from a specified list of initiator and target ports on a CIM\_SCSIProtocolController instance (SPC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dda1ef6e-3103-4773-9804-e5bd7bd07f6f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["HidePaths method iSCSI Software Target API", "HidePaths method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class", "MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , HidePaths method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.HidePaths
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# HidePaths method of the MSISCSITARGET\_ControllerConfigurationService class

Hides a list of SCSI logical units such as a RAID volume or tape drive from a specified list of initiator and target ports on a [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instance (SPC).

This method overrides the method inherited from the **CIM\_ControllerConfigurationService** class.

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

On return contains a reference to the job if one was created, otherwise contains NULL. If this method returns **Method Parameters Checked - Job Started** this parameter may be null if the job completed.

</dd> <dt>

*LUNames* \[in\]
</dt> <dd>

Specifies the IDs of existing logical unit instances to use. The logical unit instances must already exist. The members of this array must match the **Name** property of existing [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) instances. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*InitiatorPortIDs* \[in\]
</dt> <dd>

Specifies the IDs of initiator ports to use. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

Specifies the IDs of target ports to use. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*ProtocolControllers* \[in, out\]
</dt> <dd>

Contains an array of references to [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instances.

On input, this must contain exactly one SPC. On return this is an array of references to the SPCs created or modified as the result of processing the request.

The implementation will attempt to remove associations, *LUNames*, *InitiatorPortIDs*, and *TargetPortIDs*, from this SPC. The implementation may need to create new SPCs with a subset of the remaining associations.

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

## Remarks

When hiding logical units, there are three scenarios that the implementation must support. Each scenario requires a different combination of parameters. Other vendor-specific scenarios are allowed.

-   **Remove logical units from a view**

    The *LUNames* parameter must not be **NULL** and that the *InitiatorIDs* and *TargetPortIDs* parameters must be **NULL**.

-   **Remove initiator IDs from a view**

    The *LUNames* and *TargetPortIDs* parameters must be **NULL** and the *InitiatorIDs* must not be **NULL**.

-   **Remove target port IDs from a view**

    The *LUNames* and *InitiatorPortIDs* parameters must be **NULL**.

The SPC may be automatically deleted when the last logical unit, initiator ID, or target port ID is removed depending on the state of **CIM\_ProtocolControllerMaskingCapabilites** properties. If the **SPCAllowsNoLUs** property is false, then the SPC is automatically deleted when the last logical unit is removed. If the **SPCAllowsNoTargets** is false, then the SPC is automatically deleted when the last target port ID is removed. If the **SPCAllowsNoInitiators** property is false, then the SPC is automatically deleted when the last initiator port ID is removed. In all other cases, the SPC must be explicitly deleted via the **DeleteInstance** method.

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

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905)
</dt> </dl>

 

 





