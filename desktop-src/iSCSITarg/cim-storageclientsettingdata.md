---
title: CIM\_StorageClientSettingData class
description: This class models host environment factors that influence the behavior of Storage Systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '63d64153-6cc1-4422-8d9b-df3e5d8ae7e5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_StorageClientSettingData class iSCSI Software Target API", "CIM_StorageClientSettingData class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_StorageClientSettingData
- CIM_StorageClientSettingData.Caption
- CIM_StorageClientSettingData.Description
- CIM_StorageClientSettingData.InstanceID
- CIM_StorageClientSettingData.ElementName
- CIM_StorageClientSettingData.ClientTypes
- CIM_StorageClientSettingData.OtherClientTypeDescriptions
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_StorageClientSettingData class

This class models host environment factors that influence the behavior of Storage Systems. For example, a disk array has different SCSI responses for clients (initiators) configured as AIX verses HPUX. Instances of this setting class can be associated via ElementSettingData to a storage system's LogicalPort, ProtocolController, or Volume instances when these elements have host awareness. These associations are created by the management instrumentation provider to reflect the current configuration. A client deletes/creates these associations to request changes in element host-awareness. This settings class can also be associated with StorageHardwareID instances when that HW ID is configured with host information. An instance of this setting may include several ClientType values if the storage system treats them identically. The storage system exposes all supported setting instances to a WBEM Enumerate request; the client uses the returned settings to determine which types are available.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("2.31.0"), UMLPackagePath("CIM::User::StorageHardwareID")]
class CIM_StorageClientSettingData : CIM_SettingData
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint16 ClientTypes[];
  string OtherClientTypeDescriptions[];
};
```

## Members

The **CIM\_StorageClientSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageClientSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ClientTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageClientSettingData.OtherClientTypeDescriptions")
</dt> </dl>

This enumeration defines operating system, version, driver, and other host environment factors that influence the behavior exposed by storage systems. Values in this array are combined with data from the OtherClientTypeDescriptions property to provide complete information on the host environment.

"Microsoft Windows" indicates generic Windows operating system. To utilize features of a specific Windows operating system, use the corresponding value for that Windows operating system, for example, "Microsoft Windows Server 2008".

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>

**Standard** (2)


</dt> <dd></dd> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>

**Solaris** (3)


</dt> <dd></dd> <dt>

<span id="HPUX"></span><span id="hpux"></span>

**HPUX** (4)


</dt> <dd></dd> <dt>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>

**OpenVMS** (5)


</dt> <dd></dd> <dt>

<span id="Tru64"></span><span id="tru64"></span><span id="TRU64"></span>

**Tru64** (6)


</dt> <dd></dd> <dt>

<span id="Netware"></span><span id="netware"></span><span id="NETWARE"></span>

**Netware** (7)


</dt> <dd></dd> <dt>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>

**Sequent** (8)


</dt> <dd></dd> <dt>

<span id="AIX"></span><span id="aix"></span>

**AIX** (9)


</dt> <dd></dd> <dt>

<span id="DGUX"></span><span id="dgux"></span>

**DGUX** (10)


</dt> <dd></dd> <dt>

<span id="Dynix"></span><span id="dynix"></span><span id="DYNIX"></span>

**Dynix** (11)


</dt> <dd></dd> <dt>

<span id="Irix"></span><span id="irix"></span><span id="IRIX"></span>

**Irix** (12)


</dt> <dd></dd> <dt>

<span id="Cisco_iSCSI_Storage_Router"></span><span id="cisco_iscsi_storage_router"></span><span id="CISCO_ISCSI_STORAGE_ROUTER"></span>

**Cisco iSCSI Storage Router** (13)


</dt> <dd></dd> <dt>

<span id="Linux"></span><span id="linux"></span><span id="LINUX"></span>

**Linux** (14)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows"></span><span id="microsoft_windows"></span><span id="MICROSOFT_WINDOWS"></span>

**Microsoft Windows** (15)


</dt> <dd></dd> <dt>

<span id="OS400"></span><span id="os400"></span>

**OS400** (16)


</dt> <dd></dd> <dt>

<span id="TRESPASS"></span><span id="trespass"></span>

**TRESPASS** (17)


</dt> <dd></dd> <dt>

<span id="HI-UX"></span><span id="hi-ux"></span>

**HI-UX** (18)


</dt> <dd></dd> <dt>

<span id="VMware_ESXi"></span><span id="vmware_esxi"></span><span id="VMWARE_ESXI"></span>

**VMware ESXi** (19)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows_Server_2008"></span><span id="microsoft_windows_server_2008"></span><span id="MICROSOFT_WINDOWS_SERVER_2008"></span>

**Microsoft Windows Server 2008** (20)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows_Server_2003"></span><span id="microsoft_windows_server_2003"></span><span id="MICROSOFT_WINDOWS_SERVER_2003"></span>

**Microsoft Windows Server 2003** (21)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>22–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

For DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**OtherClientTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageClientSettingData.ClientTypes")
</dt> </dl>

When the the corresponding array entry in ClientTypes\[\] is "Other", this entry provides a string describing the manufacturer and OS/Environment. When the corresponding ClientTypes\[\] entry is not "Other", this entry allows variations or qualifications of ClientTypes - for example, different versions of Solaris.

</dd> </dl>

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

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

 





