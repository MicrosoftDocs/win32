---
description: Represents an association between a system and one of the elements that compose it.
ms.assetid: 728f25bf-3d52-4b1c-bf72-51e8ed0a4e72
title: CIM_SystemComponent class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SystemComponent
- CIM_SystemComponent.GroupComponent
- CIM_SystemComponent.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_SystemComponent class (Hyper-V management)

Represents an association between a system and one of the elements that compose it.

## Syntax

``` syntax
[Association, Aggregation, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_SystemComponent : CIM_Component
{
  CIM_System               REF GroupComponent;
  CIM_ManagedSystemElement REF PartComponent;
};
```

## Members

The **CIM\_SystemComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent")
</dt> </dl>

The [**CIM\_System**](cim-system.md) that contains the **PartComponent**.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

The child [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) that is a component of the system.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

