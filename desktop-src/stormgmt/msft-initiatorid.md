---
title: MSFT\_InitiatorId class
description: Represents an initiator identifier.
ms.assetid: 446877F7-C9A3-40D5-A17E-D3DBBF341B9B
keywords:
- MSFT_InitiatorId class Windows Storage Management API
- MSFT_InitiatorId class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_InitiatorId
- MSFT_InitiatorId.InitiatorAddress
- MSFT_InitiatorId.Type
- MSFT_InitiatorId.HostType
- MSFT_InitiatorId.OtherHostTypeDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_InitiatorId class

Represents an initiator identifier.

This object represents the storage subsystem's view of an initiator port. This is used in conjunction with a target port to establish which initiator port is allowed access to the subsystem's virtual disks.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_InitiatorId : MSFT_StorageObject
{
  String InitiatorAddress;
  UInt16 Type;
  UInt16 HostType[];
  String OtherHostTypeDescription[];
};
```

## Members

The **MSFT\_InitiatorId** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_InitiatorId** class has these methods.



| Method                                                | Description                                                |
|:------------------------------------------------------|:-----------------------------------------------------------|
| [**DeleteObject**](msft-initiatorid-deleteobject.md) | Deletes an instance of an initiator identifier.<br/> |



 

### Properties

The **MSFT\_InitiatorId** class has these properties.

<dl> <dt>

**HostType**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array of values specifying the operating system, version, driver, and other host environment factors.

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

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (22..32767)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
</dt> </dl>

</dd> <dt>

**InitiatorAddress**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The address or unique identifier for the corresponding initiator port.

</dd> <dt>

**OtherHostTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ( "Indexed" ), [**ModelCorrespondence {"CIM\_StorageClientSettingData.ClientTypes"}**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If the corresponding entry in the **HostType** array is **Other**, the entry in this property contains a string describing the host operating system information.

If the corresponding entry in the **HostType** array is not **Other**, the entry in this property allows variations or qualifications of **ClientTypes** for example, different versions of Solaris.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The type of identifier that is used in the **InitiatorAddress** property.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="PortWWN"></span><span id="portwwn"></span><span id="PORTWWN"></span>**PortWWN** (2)
</dt> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>**NodeWWN** (3)
</dt> <dt>

<span id="HostName"></span><span id="hostname"></span><span id="HOSTNAME"></span>**HostName** (4)
</dt> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>**iSCSI Name** (5)
</dt> <dt>

<span id="SwitchWWN"></span><span id="switchwwn"></span><span id="SWITCHWWN"></span>**SwitchWWN** (6)
</dt> <dt>

<span id="SASAddress"></span><span id="sasaddress"></span><span id="SASADDRESS"></span>**SASAddress** (7)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





