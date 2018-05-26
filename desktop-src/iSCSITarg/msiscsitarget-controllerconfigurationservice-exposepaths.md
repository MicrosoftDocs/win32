---
title: ExposePaths method of the MSISCSITARGET\_ControllerConfigurationService class
description: Expose a list of SCSI logical units (such as RAID volumes or tape drives) to a list of initiators through a list of target ports, through one or more SCSIProtocolControllers (SPCs).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6fc0c930-4084-4c8f-816f-4a7de9765ef3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExposePaths method iSCSI Software Target API
- ExposePaths method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class
- MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , ExposePaths method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.ExposePaths
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExposePaths method of the MSISCSITARGET\_ControllerConfigurationService class

Expose a list of SCSI logical units (such as RAID volumes or tape drives) to a list of initiators through a list of target ports, through one or more SCSIProtocolControllers (SPCs).

The relevant rules of SCSI semantics are:

\- an SPC MAY NOT be exposed through a particular host/target port pair that is in use by another SPC. (In other words, an SPC and its associated logical units and ports together correspond to the logical unit inventory provided by SCSI REPORT LUNS and INQUIRY commands)

\- each LogicalDevice associated to an SPC MUST have a unique ProtocolControllerForUnit DeviceNumber (logical unit number)

The instrumentation MUST report an error if the client request would violate one of these rules.

If the instrumentation provides PrivilegeManagementService, the results of setting DeviceAccesses MUST be synchronized with PrivilegeManagementService as described in the ProtocolControllerForUnit DeviceAccess description.

## Syntax


```mof
uint32 ExposePaths(
  [out]     CIM_ConcreteJob            REF Job,
  [in]      string                         LUNames[],
  [in]      string                         InitiatorPortIDs[],
  [in]      string                         TargetPortIDs[],
  [in]      string                         DeviceNumbers[],
  [in]      uint16                         DeviceAccesses[],
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

An array of IDs of logical unit instances. The LU instances MUST already exist. The members of this array MUST match the Name property of LogicalDevice instances that represent SCSI logical units. See the method description for conditions where this MAY be null.

</dd> <dt>

*InitiatorPortIDs* \[in\]
</dt> <dd>

IDs of initiator ports. If existing StorageHardwareID instances exist, they MUST be used. If no StorageHardwareID instance matches, then one is implicitly created. See the method description for conditions where this MAY be null.

</dd> <dt>

*TargetPortIDs* \[in\]
</dt> <dd>

IDs of target ports. See the method description for conditions where this MAY be null.

</dd> <dt>

*DeviceNumbers* \[in\]
</dt> <dd>

A list of logical unit numbers to assign to the corresponding logical unit in the LUNames parameter. (within the context of the elements specified in the other parameters). If the LUNames parameter is null, then this parameter MUST be null. Otherwise, if this parameter is null, all LU numbers are assigned by the hardware or instrumentation.

</dd> <dt>

*DeviceAccesses* \[in\]
</dt> <dd>

A list of permissions to assign to the corresponding logical unit in the LUNames parameter. This specifies the permission to assign within the context of the elements specified in the other parameters. Setting this to 'No Access' assigns the DeviceNumber for the associated initiators, but does not grant read or write access. If the LUNames parameter is not null then this parameter MUST be specified.

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


</dt> <dd>5 15999</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000 65535</dd> </dl> </dd> <dt>

*ProtocolControllers* \[in, out\]
</dt> <dd>

An array of references to SCSIProtocolControllers (SPCs). On input, this can be null, or contain exactly one element; there MAY be multiple references on output. If null on input, the instrumentation will create one or more new SPC instances. If an SPC is specified, the instrumentation will attempt to add associations to one or more existing SPCs. If the first array element is a valid SPC reference and SCSI semantics can be preserved, the instrumentation MUST attach associations to the specified SPC. If multiple elements are non-null on input, the instrumentation MUST report an invalid parameter. On output, this is an array of references to SPCs created or modified as the result of processing the request.

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

**Method Reserved** (4104 32767)
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

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> </dl>

 

 





