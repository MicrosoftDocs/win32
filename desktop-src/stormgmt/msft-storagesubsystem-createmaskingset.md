---
title: CreateMaskingSet method of the MSFT\_StorageSubSystem class
description: Creates a new masking set.
ms.assetid: '479E1710-0101-4791-9936-07B1F1644454'
keywords: ["CreateMaskingSet method Windows Storage Management API", "CreateMaskingSet method Windows Storage Management API , MSFT_StorageSubSystem class", "MSFT_StorageSubSystem class Windows Storage Management API , CreateMaskingSet method"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateMaskingSet
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# CreateMaskingSet method of the MSFT\_StorageSubSystem class

Creates a new masking set.

A masking set is a logical grouping of virtual disks, target ports, and initiators for the purpose of showing virtual disks to host computers

## Syntax


```mof
UInt32 CreateMaskingSet(
  [in]  String              FriendlyName,
  [in]  String              VirtualDiskNames[],
  [in]  UInt16              DeviceAccesses[],
  [in]  String              DeviceNumbers[],
  [in]  String              TargetPortAddresses[],
  [in]  String              InitiatorAddresses[],
  [in]  UInt16              HostType,
  [in]  Boolean             RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              CreatedMaskingSet,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name for the masking set.

Friendly names are expected to be descriptive, but they are not required to be unique.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*VirtualDiskNames* \[in\]
</dt> <dd>

The list of virtual disks to show to the initiators in the masking set. Each disk must be specified by the identifier that is stored in the **Name** property of its [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object

This parameter has a 1:1 mapping with the *DeviceAccesses* parameter. Both arrays must be the same length, and the elements must be arranged in the same order.

</dd> <dt>

*DeviceAccesses* \[in\]
</dt> <dd>

The level of access that the initiator should have to each virtual disk specified in the *VirtualDiskNames* parameter. This parameter has a 1:1 mapping with the *VirtualDiskNames* parameter. Both arrays must be the same length, and the elements must be arranged in the same order.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read Write** (2)
</dt> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>**Read-Only** (3)
</dt> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>**No Access** (4)
</dt> </dl> </dd> <dt>

*DeviceNumbers* \[in\]
</dt> <dd>

Specifies the order in which the virtual disks should be shown to initiators. This capability is only available if the storage subsystem's **MaskingClientSelectableDeviceNumbers** property is **TRUE**. If specified, this parameter must have a 1:1 mapping with the *VirtualDiskNames* parameter.

</dd> <dt>

*TargetPortAddresses* \[in\]
</dt> <dd>

The target ports to use when showing the virtual disks to initiators. The number of target ports that can be specified depends on the subsystem's **MaskingPortsPerView** property. If **MaskingPortsPerView** is **All target ports share the same view**, this parameter is ignored, and all target ports on the system are associated with this masking set.

</dd> <dt>

*InitiatorAddresses* \[in\]
</dt> <dd>

The initiators to which the virtual disks should be shown. If the subsystem's **MaskingOneInitiatorIdPerView** property is **TRUE**, only one initiator can be specified for this masking set. The list of valid initiator address formats is specified by the subsystem's **MaskingValidInitiatorIdTypes** property.

</dd> <dt>

*HostType* \[in\]
</dt> <dd>

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

Values between 22 and 32767 (inclusive) are reserved for DMTF. Values between 32768 to 65535 (inclusive) are reserved for vendors.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>**Standard** (2)
</dt> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>**Solaris** (3)
</dt> <dt>

<span id="HPUX"></span><span id="hpux"></span>**HPUX** (4)
</dt> <dt>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>**OpenVMS** (5)
</dt> <dt>

<span id="Tru64"></span><span id="tru64"></span><span id="TRU64"></span>**Tru64** (6)
</dt> <dt>

<span id="Netware"></span><span id="netware"></span><span id="NETWARE"></span>**Netware** (7)
</dt> <dt>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>**Sequent** (8)
</dt> <dt>

<span id="AIX"></span><span id="aix"></span>**AIX** (9)
</dt> <dt>

<span id="DGUX"></span><span id="dgux"></span>**DGUX** (10)
</dt> <dt>

<span id="Dynix"></span><span id="dynix"></span><span id="DYNIX"></span>**Dynix** (11)
</dt> <dt>

<span id="Irix"></span><span id="irix"></span><span id="IRIX"></span>**Irix** (12)
</dt> <dt>

<span id="Cisco_iSCSI_Storage_Router"></span><span id="cisco_iscsi_storage_router"></span><span id="CISCO_ISCSI_STORAGE_ROUTER"></span>**Cisco iSCSI Storage Router** (13)
</dt> <dt>

<span id="Linux"></span><span id="linux"></span><span id="LINUX"></span>**Linux** (14)
</dt> <dt>

<span id="Microsoft_Windows"></span><span id="microsoft_windows"></span><span id="MICROSOFT_WINDOWS"></span>**Microsoft Windows** (15)
</dt> <dt>

<span id="OS400"></span><span id="os400"></span>**OS400** (16)
</dt> <dt>

<span id="TRESPASS"></span><span id="trespass"></span>**TRESPASS** (17)
</dt> <dt>

<span id="HI-UX"></span><span id="hi-ux"></span>**HI-UX** (18)
</dt> <dt>

<span id="VMware_ESXi"></span><span id="vmware_esxi"></span><span id="VMWARE_ESXI"></span>**VMware ESXi** (19)
</dt> <dt>

<span id="Microsoft_Windows_Server_2008"></span><span id="microsoft_windows_server_2008"></span><span id="MICROSOFT_WINDOWS_SERVER_2008"></span>**Microsoft Windows Server 2008** (20)
</dt> <dt>

<span id="Microsoft_Windows_Server_2003"></span><span id="microsoft_windows_server_2003"></span><span id="MICROSOFT_WINDOWS_SERVER_2003"></span>**Microsoft Windows Server 2003** (21)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (22..32767)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
</dt> </dl> </dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

</dd> <dt>

*CreatedMaskingSet* \[out\]
</dt> <dd>

If the masking set is created successfully, this parameter receives a string that contains an embedded [**MSFT\_MaskingSet**](msft-maskingset.md) object.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The specified virtual disk could not be found.** (50000)
</dt> <dt>

**The device number specified is not valid.** (52000)
</dt> <dt>

**The HostType requested is not supported.** (52001)
</dt> <dt>

**DeviceAccess must be specified for each virtual disk.** (52002)
</dt> <dt>

**The initiator address specified is not valid** (53000)
</dt> <dt>

**Only one initiator address is acceptable for this operation.** (53001)
</dt> <dt>

**The target port address specified is not valid.** (54000)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





