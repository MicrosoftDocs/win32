---
title: MSFT\_MaskingSet class
description: Represents a masking set.
ms.assetid: '2B745820-9347-414A-8D33-36C8DB97385D'
keywords: ["MSFT_MaskingSet class Windows Storage Management API", "MSFT_MaskingSet class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_MaskingSet
- MSFT_MaskingSet.FriendlyName
- MSFT_MaskingSet.Name
- MSFT_MaskingSet.HostType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_MaskingSet class

Represents a masking set.

A masking set is a collection of virtual disks, target ports, and initiator IDs that are used for bulk [**Show**](msft-virtualdisk-show.md) and [**Hide**](msft-virtualdisk-hide.md) operations. When a resource is added to a masking set, it is made available for access to all other resources in the masking set. For example, adding a virtual disk object to a masking set will allow all initiator IDs in the masking set to access the virtual disk object.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_MaskingSet : MSFT_StorageObject
{
  String FriendlyName;
  String Name;
  UInt16 HostType;
};
```

## Members

The **MSFT\_MaskingSet** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MaskingSet** class has these methods.



| Method                                                                 | Description                                                                |
|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**AddInitiatorId**](msft-maskingset-addinitiatorid.md)               | Adds one or more initiator identifiers to the masking set.<br/>      |
| [**AddTargetPort**](msft-maskingset-addtargetport.md)                 | Adds one or more target ports to the masking set.<br/>               |
| [**AddVirtualDisk**](msft-maskingset-addvirtualdisk.md)               | Adds one or more virtual disks to the masking set.<br/>              |
| [**DeleteObject**](msft-maskingset-deleteobject.md)                   | Deletes the masking set instance.<br/>                               |
| [**GetSecurityDescriptor**](msft-maskingset-getsecuritydescriptor.md) | Retrieves the security descriptor for the masking set instance.<br/> |
| [**RemoveInitiatorId**](msft-maskingset-removeinitiatorid.md)         | Removes one or more initiator identifiers from the masking set.<br/> |
| [**RemoveTargetPort**](msft-maskingset-removetargetport.md)           | Removes one or more target ports from the masking set.<br/>          |
| [**RemoveVirtualDisk**](msft-maskingset-removevirtualdisk.md)         | Removes one or more virtual disks from the masking set.<br/>         |
| [**SetFriendlyName**](msft-maskingset-setfriendlyname.md)             | Sets the friendly name for the masking set.<br/>                     |
| [**SetSecurityDescriptor**](msft-maskingset-setsecuritydescriptor.md) | Sets the security descriptor for the masking set object.<br/>        |



 

### Properties

The **MSFT\_MaskingSet** class has these properties.

<dl> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the masking set. It is specified when the masking set is created, and it can be changed using the [**SetFriendlyName**](msft-maskingset-setfriendlyname.md) method.

</dd> <dt>

**HostType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>**Standard** (2)
</dt> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>**Solaris** (3)
</dt> <dt>

<span id="HPUX"></span><span id="hpux"></span>**HPUX**
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

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (22..32767)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
</dt> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly system-defined name for the masking set. This name is unique within the scope of the owning storage subsystem.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





