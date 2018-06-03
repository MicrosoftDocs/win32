---
title: MSFTSM\_Namespace class
description: Provides a domain, in other words a container, in which the instances of a class are guaranteed to be unique per the KEY qualifier definitions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f3014e71-4bba-4fba-86ba-08e3661feac5
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSM_Namespace class iSCSI Software Target API
- MSFTSM_Namespace class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSM_Namespace
- MSFTSM_Namespace.Caption
- MSFTSM_Namespace.Description
- MSFTSM_Namespace.ElementName
- MSFTSM_Namespace.SystemCreationClassName
- MSFTSM_Namespace.SystemName
- MSFTSM_Namespace.ObjectManagerCreationClassName
- MSFTSM_Namespace.ObjectManagerName
- MSFTSM_Namespace.CreationClassName
- MSFTSM_Namespace.Name
- MSFTSM_Namespace.ClassInfo
- MSFTSM_Namespace.DescriptionOfClassInfo
- MSFTSM_Namespace.ClassType
- MSFTSM_Namespace.ClassTypeVersion
- MSFTSM_Namespace.DescriptionOfClassType
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFTSM\_Namespace class

Provides a domain, in other words a container, in which the instances of a class are guaranteed to be unique per the KEY qualifier definitions. It is named relative to the [**MSFTSM\_ObjectManager**](msftsm-objectmanager.md) implementation that provides such a domain.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), Provider("MSiSCSITargetProv")]
class MSFTSM_Namespace : CIM_Namespace
{
  string Caption;
  string Description;
  string ElementName;
  string SystemCreationClassName;
  string SystemName;
  string ObjectManagerCreationClassName;
  string ObjectManagerName;
  string CreationClassName;
  string Name;
  uint16 ClassInfo;
  string DescriptionOfClassInfo;
  uint16 ClassType;
  string ClassTypeVersion;
  string DescriptionOfClassType;
};
```

## Members

The **MSFTSM\_Namespace** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_Namespace** class has these properties.

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

**ClassInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_Namespace.ClassType"), [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Namespace.DescriptionOfClassInfo")
</dt> </dl>

Enumeration indicating the organization/schema of the Namespace's objects. For example, they may be instances of classes of a specific CIM version.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="CIM_1.0"></span><span id="cim_1.0"></span>

**CIM 1.0** (2)


</dt> <dd></dd> <dt>

<span id="CIM_2.0"></span><span id="cim_2.0"></span>

**CIM 2.0** (3)


</dt> <dd></dd> <dt>

<span id="CIM_2.1"></span><span id="cim_2.1"></span>

**CIM 2.1** (4)


</dt> <dd></dd> <dt>

<span id="CIM_2.2"></span><span id="cim_2.2"></span>

**CIM 2.2** (5)


</dt> <dd></dd> <dt>

<span id="CIM_2.3"></span><span id="cim_2.3"></span>

**CIM 2.3** (6)


</dt> <dd></dd> <dt>

<span id="CIM_2.4"></span><span id="cim_2.4"></span>

**CIM 2.4** (7)


</dt> <dd></dd> <dt>

<span id="CIM_2.5"></span><span id="cim_2.5"></span>

**CIM 2.5** (8)


</dt> <dd></dd> <dt>

<span id="CIM_2.6"></span><span id="cim_2.6"></span>

**CIM 2.6** (9)


</dt> <dd></dd> <dt>

<span id="CIM_2.7"></span><span id="cim_2.7"></span>

**CIM 2.7** (10)


</dt> <dd></dd> <dt>

<span id="CIM_2.8"></span><span id="cim_2.8"></span>

**CIM 2.8** (11)


</dt> <dd></dd> <dt>

<span id="DMI_Recast"></span><span id="dmi_recast"></span><span id="DMI_RECAST"></span>

**DMI Recast** (200)


</dt> <dd></dd> <dt>

<span id="SNMP_Recast"></span><span id="snmp_recast"></span><span id="SNMP_RECAST"></span>

**SNMP Recast** (201)


</dt> <dd></dd> <dt>

<span id="CMIP_Recast"></span><span id="cmip_recast"></span><span id="CMIP_RECAST"></span>

**CMIP Recast** (202)


</dt> <dd></dd> </dl>

</dd> <dt>

**ClassType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Namespace.DescriptionOfClassType", "CIM\_Namespace.ClassTypeVersion")
</dt> </dl>

Enumeration indicating the schema of the Namespace's objects. For example, they may be instances of classes of a specific CIM version or a mapping from another standard, such as SNMP. If 'Other' is selected, the DescriptionOfClassType property MUST be populated.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="CIM"></span><span id="cim"></span>

**CIM** (2)


</dt> <dd></dd> <dt>

<span id="DMI_Recast"></span><span id="dmi_recast"></span><span id="DMI_RECAST"></span>

**DMI Recast** (200)


</dt> <dd></dd> <dt>

<span id="SNMP_Recast"></span><span id="snmp_recast"></span><span id="SNMP_RECAST"></span>

**SNMP Recast** (201)


</dt> <dd></dd> <dt>

<span id="CMIP_Recast"></span><span id="cmip_recast"></span><span id="CMIP_RECAST"></span>

**CMIP Recast** (202)


</dt> <dd></dd> </dl>

</dd> <dt>

**ClassTypeVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Namespace.DescriptionOfClassType", "CIM\_Namespace.ClassType")
</dt> </dl>

The version of the objects in this namespace. The string representing the version MUST be in the form:

M + "." + N + "." + U

Where:

M - The major version (in numeric form)

N - The minor version (in numeric form)

U - The update (e.g. errata, patch, ..., in numeric form)

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

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

**DescriptionOfClassInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_Namespace.DescriptionOfClassType"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Namespace.ClassInfo")
</dt> </dl>

A string providing more detail (beyond the general classification in ClassInfo) for the object hierarchy of the Namespace.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**DescriptionOfClassType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Namespace.ClassType", "CIM\_Namespace.ClassTypeVersion")
</dt> </dl>

A string providing more detail (beyond the general classification in ClassInfo) for the object hierarchy of the Namespace.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

A string to uniquely identify the Namespace within the ObjectManager.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**ObjectManagerCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManager.CreationClassName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping ObjectManager's CreationClassName.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**ObjectManagerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManager.Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping ObjectManager's Name.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManager.SystemCreationClassName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping System's CreationClassName.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ObjectManager.SystemName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping System's Name.

This property is inherited from [**CIM\_Namespace**](cim-namespace.md).

</dd> </dl>

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

[**CIM\_Namespace**](cim-namespace.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





