---
title: CIM\_VirtualSystemSettingData class
description: Describes the virtual aspects of a virtual system through a set of virtualization specific properties. CIM\_VirtualSystemSettingData is also used as the top level class of virtual system configurations.
ms.assetid: '728f4173-29f4-493d-8889-8fdf3c982d06'
keywords: ["CIM_VirtualSystemSettingData class Hyper-V", "CIM_VirtualSystemSettingData class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemSettingData
- CIM_VirtualSystemSettingData.Caption
- CIM_VirtualSystemSettingData.Description
- CIM_VirtualSystemSettingData.SettingType
- CIM_VirtualSystemSettingData.SystemName
- CIM_VirtualSystemSettingData.InstanceID
- CIM_VirtualSystemSettingData.ElementName
- CIM_VirtualSystemSettingData.VirtualSystemType
- CIM_VirtualSystemSettingData.AutoActivate
- CIM_VirtualSystemSettingData.OtherVirtualSystemType
- CIM_VirtualSystemSettingData.CreationTime
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_VirtualSystemSettingData class

Describes the virtual aspects of a virtual system through a set of virtualization specific properties. **CIM\_VirtualSystemSettingData** is also used as the top level class of virtual system configurations.

Virtual system configurations model configuration information about virtual systems and their components. A virtual system configuration consists of one top-level **CIM\_VirtualSystemSettingData** instance that aggregates a number of [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances that are associated using the [**CIM\_ConcreteComponent**](cim-concretecomponent.md) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Experimental, Abstract, Version("2.13.0"), AMENDMENT]
class CIM_VirtualSystemSettingData : CIM_SettingData
{
  string   Caption;
  string   Description;
  uint16   SettingType;
  string   SystemName;
  string   InstanceID;
  string   ElementName;
  uint16   VirtualSystemType;
  boolean  AutoActivate;
  string   OtherVirtualSystemType;
  datetime CreationTime;
};
```

## Members

The **CIM\_VirtualSystemSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VirtualSystemSettingData** class has these properties.

<dl> <dt>

**AutoActivate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag that indicates whether the virtual system is automatically started when the virtualization platform is started.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when the virtual system configuration was created.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ElementName")
</dt> </dl>

The display name of the virtual system. A associated instance of CIM\_EnabledLogicalELementCapabilities indicates whether ElementName is modifiable or not.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Key. For more information about the format, see the base class. Be aware that when used as an input element InstanceID must not be set by the client; instead, the implementation assigns a name, using implementation dependent rules.

</dd> <dt>

**OtherVirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_VirtualSystemSettingData**.**VirtualSystemType**")
</dt> </dl>

Designates the type of the virtual system if VirtualSystemType is set to 1 - Other.

</dd> <dt>

**SettingType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes a usage context of the instance.

<dt>

<span id="Input"></span><span id="input"></span><span id="INPUT"></span>

<span id="Input"></span><span id="input"></span><span id="INPUT"></span>**Input** (1)


</dt> <dd>

Input designates an instance reflecting the virtual aspects of a input virtual system configuration

</dd> <dt>

<span id="Recorded"></span><span id="recorded"></span><span id="RECORDED"></span>

<span id="Recorded"></span><span id="recorded"></span><span id="RECORDED"></span>**Recorded** (2)


</dt> <dd>

Recorded designates an instance reflecting the virtual aspects of a virtual system definition

</dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>**Current** (3)


</dt> <dd>

Current designates an instance reflecting a virtual aspects of a currently active virtual

</dd> <dt>

<span id="Capability"></span><span id="capability"></span><span id="CAPABILITY"></span>

<span id="Capability"></span><span id="capability"></span><span id="CAPABILITY"></span>**Capability** (4)


</dt> <dd>

Capability designates an instance reflecting virtual system capabilities.

</dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>**Snapshot** (5)


</dt> <dd>

Snapshot designates an instance reflecting virtual aspects of a snapshot of a virtual system.

</dd> </dl>

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

SystemName shall reflect a unique name for the system as it is used within the virtualization platform. Be aware that the SystemName is neither the hostname assigned to the operating system instance running within the virtual system, nor is it an IP address or MAC address assigned to any of its network ports.

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_VirtualSystemSettingData**.**OtherVirtualSystemType**")
</dt> </dl>

The type of the virtual system.

> [!Note]  
> If the virtual system type is unknown, this value must be set to "DMTF:unknown".

 

This property is formatted using the following Augmented Backus–Naur Form (ABNF) format:

vs-type = dmtf-value / other-org-value / legacy-value; dmtf-value = "DMTF:" defining-org ":" org-vs-type; other-org-value = defining-org ":" org-vs-type;

The value of the above ABNF format are:

-   *dmtf-value* — a property value defined by DMTF and is defined in the description of this property.
-   *other-org-value* — is a property value defined by a business entity other than DMTF and is not defined in the description of this property.
-   *legacy-value* — a property value defined by a business entity other than DMTF and is not defined in the description of this property. These values are permitted but recommended to be deprecated over time.
-   *defining-org* — an identifier for the business entity that defines the virtual system type. It should include a copyrighted, trademarked, or a unique name that is owned by the business entity. It should not be "DMTF" and shall not contain a colon.
-   *org-vs-type* — an identifier for the virtual system type within the defining business entity. It should be unique within defining-org. org-vs-type may use any character allowed for CIM strings, except the following: U0000-U001F (Unicode C0 controls), U0020 (space), U007F (Unicode C0 controls), or U0080-U009F (Unicode C1 controls).
-   If there is a need to structure the value into segments, the segments should be separated with a single colon.
-   The values of this property should be processed case sensitively. They are intended to be processed programmatically, instead of being a display name, and should be short.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Reserved_General"></span><span id="reserved_general"></span><span id="RESERVED_GENERAL"></span>

**Reserved General** (2..100)


</dt> <dd></dd> <dt>

<span id="EMC_vmWare"></span><span id="emc_vmware"></span><span id="EMC_VMWARE"></span>

**EMC vmWare** (101)


</dt> <dd></dd> <dt>

<span id="Reserved_EMC"></span><span id="reserved_emc"></span><span id="RESERVED_EMC"></span>

**Reserved EMC** (102..199)


</dt> <dd></dd> <dt>

<span id="IBM_Power_-_IVM"></span><span id="ibm_power_-_ivm"></span><span id="IBM_POWER_-_IVM"></span>

**IBM Power - IVM** (201)


</dt> <dd></dd> <dt>

<span id="IBM_Power_-_VIOS"></span><span id="ibm_power_-_vios"></span><span id="IBM_POWER_-_VIOS"></span>

**IBM Power - VIOS** (202)


</dt> <dd></dd> <dt>

<span id="IBM_Power_-_i5_OS"></span><span id="ibm_power_-_i5_os"></span><span id="IBM_POWER_-_I5_OS"></span>

**IBM Power - i5/OS** (203)


</dt> <dd></dd> <dt>

<span id="IBM_System_z_-_LPAR_ESA_390"></span><span id="ibm_system_z_-_lpar_esa_390"></span><span id="IBM_SYSTEM_Z_-_LPAR_ESA_390"></span>

**IBM System z - LPAR ESA/390** (204)


</dt> <dd></dd> <dt>

<span id="IBM_System_z_-_LPAR_ESA_390_TPF"></span><span id="ibm_system_z_-_lpar_esa_390_tpf"></span><span id="IBM_SYSTEM_Z_-_LPAR_ESA_390_TPF"></span>

**IBM System z - LPAR ESA/390 TPF** (205)


</dt> <dd></dd> <dt>

<span id="IBM_System_z_-_LPAR_CF"></span><span id="ibm_system_z_-_lpar_cf"></span><span id="IBM_SYSTEM_Z_-_LPAR_CF"></span>

**IBM System z - LPAR CF** (206)


</dt> <dd></dd> <dt>

<span id="IBM_System_z_-_LPAR_Linux"></span><span id="ibm_system_z_-_lpar_linux"></span><span id="IBM_SYSTEM_Z_-_LPAR_LINUX"></span>

**IBM System z - LPAR Linux** (207)


</dt> <dd></dd> <dt>

<span id="IBM_System_z_-_z_VM_ESA"></span><span id="ibm_system_z_-_z_vm_esa"></span><span id="IBM_SYSTEM_Z_-_Z_VM_ESA"></span>

**IBM System z - z/VM ESA** (208)


</dt> <dd></dd> <dt>

<span id="IBM_System_z_-_z_VM_XA"></span><span id="ibm_system_z_-_z_vm_xa"></span><span id="IBM_SYSTEM_Z_-_Z_VM_XA"></span>

**IBM System z - z/VM XA** (209)


</dt> <dd></dd> <dt>

<span id="IBM_SYstem_z_-_z_VM_XC"></span><span id="ibm_system_z_-_z_vm_xc"></span><span id="IBM_SYSTEM_Z_-_Z_VM_XC"></span>

**IBM SYstem z - z/VM XC** (210)


</dt> <dd></dd> <dt>

<span id="Reserved_IBM"></span><span id="reserved_ibm"></span><span id="RESERVED_IBM"></span>

**Reserved IBM** (211..299)


</dt> <dd></dd> <dt>

<span id="Microsoft_VirtualServer"></span><span id="microsoft_virtualserver"></span><span id="MICROSOFT_VIRTUALSERVER"></span>

**Microsoft VirtualServer** (301)


</dt> <dd></dd> <dt>

<span id="Reserved_Microsoft"></span><span id="reserved_microsoft"></span><span id="RESERVED_MICROSOFT"></span>

**Reserved Microsoft** (301..399)


</dt> <dd></dd> <dt>

<span id="XenSoft_-_Xen"></span><span id="xensoft_-_xen"></span><span id="XENSOFT_-_XEN"></span>

**XenSoft - Xen** (401)


</dt> <dd></dd> <dt>

<span id="Reserved_XenSoft"></span><span id="reserved_xensoft"></span><span id="RESERVED_XENSOFT"></span>

**Reserved XenSoft** (401-499)


</dt> <dd></dd> <dt>

<span id="Reserved_Other_Vendors"></span><span id="reserved_other_vendors"></span><span id="RESERVED_OTHER_VENDORS"></span>

**Reserved Other Vendors** (501..65535)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

 





