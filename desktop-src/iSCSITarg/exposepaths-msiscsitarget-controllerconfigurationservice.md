---
title: ExposePaths method of the MSISCSITARGET\_ControllerConfigurationService class
description: Exposes a list of SCSI logical units, such as RAID volumes or tape drives through one or more CIM\_SCSIProtocolController instances (SPCs).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'eb8865cd-7e79-4b86-acb1-0b9e56c2c9f9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExposePaths method iSCSI Software Target API", "ExposePaths method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class", "MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , ExposePaths method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.ExposePaths
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# ExposePaths method of the MSISCSITARGET\_ControllerConfigurationService class

Exposes a list of SCSI logical units, such as RAID volumes or tape drives through one or more [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instances (SPCs).

This method overrides the method inherited from the **CIM\_ControllerConfigurationService** class.

## Syntax


```mof
uint32 ExposePaths(
  [out]     CIM_ConcreteJob REF            Job,
  [in]      string                         LUNames[],
  [in]      string                         InitiatorPortIDs[],
  [in]      string                         TargetPortIDs[],
  [in]      string                         DeviceNumbers[],
  [in]      uint16                         DeviceAccesses[],
  [in, out] CIM_SCSIProtocolController REF ProtocolControllers[]
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

Specifies the IDs of existing logical unit instances to use. The members of this array must match the **Name** property of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) instances that represent SCSI logical units. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*InitiatorPortIDs* \[in\]
</dt> <dd>

Specifies the IDs of initiator ports to use. If existing [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instances exist, they must be used. If no **MSISCSITARGET\_StorageHardwareID** instance matches, then one is implicitly created. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

Specifies the IDs of target ports to use. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*DeviceNumbers* \[in\]
</dt> <dd>

Specifies logical unit numbers to assign to the corresponding logical unit in the *LUNames* parameter. If the *LUNames* parameter is **NULL**, then this parameter must be **NULL**. Otherwise, if this parameter is **NULL**, all logical unit numbers are assigned by the hardware or instrumentation. For more information on when this parameter may be **NULL**, see Remarks.

</dd> <dt>

*DeviceAccesses* \[in\]
</dt> <dd>

Specifies permissions to assign to the corresponding logical unit in the *LUNames* parameter. This specifies the permission to assign within the context of the elements specified in the other parameters. Setting this to **No Access** assigns the device number for the associated initiators, but does not grant read or write access. For more information on when this parameter may be **NULL**, see Remarks.

> [!Note]  
> A value is required in this array for each element in the *LUNames* parameter. If *LUNames* is **NULL** then this parameter should be **NULL**.

 

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>

**Read Write** (2)


</dt> <dd></dd> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>

**Read-Only** (3)


</dt> <dd></dd> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>

**No Access** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–15999</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000 = *value* </dd> </dl> </dd> <dt>

*ProtocolControllers* \[in, out\]
</dt> <dd>

Contains an array of references to [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instances (SPCs).

On input, this can be **NULL**, or contain exactly one element. If **NULL** on input, the instrumentation will create one or more new SPC instances. If an SPC is specified, the instrumentation will attempt to add associations to one or more existing SPCs. If the first array element is a valid SPC reference and SCSI semantics can be preserved, the instrumentation must attach associations to the specified SPC.

On output, this is an array of references to SPCs created or modified as the result of processing the request. There may be multiple references on output.

> [!Note]  
> If this parameter contains multiple elements on input, the instrumentation must return an **Invalid Parameter** error.

 

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

**Invalid permission** (4100)
</dt> <dt>

**Target/initiator combination already exposed** (4101)
</dt> <dt>

**Requested logical unit number in use** (4102)
</dt> <dt>

**Maximum Map Count Exceeded** (4103)
</dt> <dt>

**Method Reserved** (4104–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Remarks

This method has two modes of operation, create and modify. If the *ProtocolControllers* parameter is **NULL** then the implementation will create at least one SPC that satisfies the request. Depending upon the implementation, more than one SPC may be created. For example, if the *CIM\_ProtocolControllerMaskingCapabilities.OneHardwareIDPerView* property is **True** and the *InitiatorPortIDs* parameter contains more than one initiator port ID then the implementation will create one SPC per ID.

If the *ProtocolControllers* parameter contains an SPC, then the implementation attempts to add the new paths to the existing SPC. Depending upon the implementation capabilities, this may result in the creation of additional SPCs. The implementation may return an error if honoring this request would violate SCSI semantics.

For example:

-   An SPC may not be exposed through a particular host/target port pair that is in use by another SPC. That is, an SPC together with its associated logical units and ports correspond to the logical unit inventory provided by SCSI REPORT LUNS and INQUIRY commands.
-   Each logical device associated to an SPC must have a unique **ProtocolControllerForUnit.DeviceNumber** logical unit number.

When creating an SPC, some parameters are required depending on the value of specific **CIM\_ProtocolControllerMaskingCapabilities** properties.

-   If the **SPCAllowsNoLUs** property is **false**, the *LUNames* parameter must contain at least one element. If it is **True**, the *LUNames* parameter is optional.
-   If the **SPCAllowsNoTargets** property is **false** and **PortsPerView** is not **All Ports share the same View** the *TargetPortIDs* parameter must specify a list of IDs. If it is **True**, the *TargetPortIDs* parameter is optional.
-   If the **SPCAllowsNoInitiators** is **false**, the *InitiatorPortIDs* parameter must specify a list of IDs. If it is **True**, the *InitiatorPortIDs* parameter is optional.
-   If the **ClientSelectableDeviceNumbers** property is **false**, the *LUNames* parameter must be **NULL**. If it is**True** then the client may provide a list of device numbers (LUNs) in this parameter.

The *LUNames*, *DeviceNumbers*, and *DeviceAccesses* parameter arrays are indexed in parallel. Each element in *DeviceNumbers* or *DeviceAccesses* specifies a property relative to the logical device instance named in the corresponding element of *LUNames*.

*DeviceAccesses* must have the same number of elements as *LUNames*. *DeviceNumbers* must have the same number of elements as *LUNames* or must be **NULL**. You can specify all of them or none. The implementation will assign IDs if they are not specified. If these conditions are not met, this method must return an **Invalid Parameter** return code or a [**CIM\_Error**](https://msdn.microsoft.com/library/cc150671).

The implementation must support three scenarios for modifying an SPC. Other vendor-specific scenarios are allowed.

-   **Add logical units to a view.**
    -   The *LUNames* and *DeviceAccesses* parameters are required and cannot be **NULL**.
    -   The *InitiatorIDs* and *TargetPortIDs* parameters must be **NULL**.
    -   The *DeviceNumbers* parameter may be **NULL** if the **CIM\_ProtocolControllerMaskingCapabilities.ClientSelectableDeviceNumbers**property is **false**.
-   **Add initiator IDs to a view.**
    -   The *InitiatorIDs* parameter is required and cannot be **NULL**.
    -   The *LUNames*, *TargetPortIDs*, *DeviceNumbers*, and *DeviceAccesses* parameters must be **NULL**.
-   **Add target port IDs to a view.**
    -   This scenario is only possible if the **CIM\_ProtocolControllerMaskingCapabilities.PortsPerView** property has the value **Multiple Ports Per View**.
    -   The *LUNames*, *InitiatorPortIDs*, *DeviceNumbers*, and *DeviceAccesses* parameters must be **NULL**.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerMaskingCapabilities**](msiscsitarget-protocolcontrollermaskingcapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md)
</dt> <dt>

[**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md)
</dt> </dl>

 

 





