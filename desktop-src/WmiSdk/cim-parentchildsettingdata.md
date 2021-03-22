---
description: An association between an instance of CIM\_VirtualSystemSettingData and the CIM\_VirtualSystemSettingData instance which represents the most recent snapshot upon which this object is based.
ms.assetid: f6e93c22-077b-4604-8d0d-9584b1f4dce1
ms.tgt_platform: multiple
title: CIM_ParentChildSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ParentChildSettingData
- Root\CIMV2.CIM_ParentChildSettingData.Antecedent
- Root\CIMV2.CIM_ParentChildSettingData.Dependent
- Root\CIMV2.CIM_ParentChildSettingData.Parent
- Root\CIMV2.CIM_ParentChildSettingData.Child
api_type: 
- Schema
api_location: 
- Root\CIMV2
---

# CIM\_ParentChildSettingData class

An association between an instance of [**CIM\_VirtualSystemSettingData**](/previous-versions/windows/desktop/clushyperv/cim-virtualsystemsettingdata) and the **CIM\_VirtualSystemSettingData** instance which represents the most recent snapshot upon which this object is based.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class CIM_ParentChildSettingData : CIM_Dependency
{
  CIM_ManagedSystemElement     REF Antecedent;
  CIM_ManagedSystemElement     REF Dependent;
  CIM_VirtualSystemSettingData REF Parent;
  CIM_VirtualSystemSettingData REF Child;
};
```

## Members

The **CIM\_ParentChildSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ParentChildSettingData** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the independent object in this association.

This property is inherited from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The setting data for the virtual system which represents the child of the Parent.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the object that is dependent on the **Antecedent** property.

This property is inherited from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The snapshot setting data upon which the Child setting data is based.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------------|------------------------|
| Namespace<br/> | Root\\CIMV2<br/> |



## See also

<dl> <dt>

[**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency)
</dt> </dl>

 

