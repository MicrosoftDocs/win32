---
title: Show method of the MSFT\_VirtualDisk class
description: Shows a virtual disk to an initiator.
ms.assetid: '6B2649E0-669B-4E8A-9DC5-78287ECE5625'
keywords: ["Show method Windows Storage Management API", "Show method Windows Storage Management API , MSFT_VirtualDisk class", "MSFT_VirtualDisk class Windows Storage Management API , Show method"]
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Show
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Show method of the MSFT\_VirtualDisk class

Shows a virtual disk to an initiator.

This operation is also known as "exposing" or "unmasking" a virtual disk.

## Syntax


```mof
UInt32 Show(
  [in]  String              TargetPortAddresses[],
  [in]  String              InitiatorAddress,
  [in]  UInt16              HostType,
  [in]  Boolean             RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*TargetPortAddresses* \[in\]
</dt> <dd>

An array of target port addresses from which the virtual disk should be shown.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*InitiatorAddress* \[in\]
</dt> <dd>

The address of the initiator to which the virtual disk should be shown.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*HostType* \[in\]
</dt> <dd>

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
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

**Cache out of date** (40003)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The HostType requested is not supported.** (52001)
</dt> <dt>

**The initiator address specified is not valid** (53000)
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

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





