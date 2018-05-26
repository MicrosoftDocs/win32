---
Description: Associates the Msvm\_VirtualSystemReferencePoint to the corresponding Msvm\_VirtualSystem objects.
ms.assetid: 5a9cb099-c0ae-4088-a64c-f2720a6cb9c8
title: Msvm\_ReferencePointOfVirtualSystem class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ReferencePointOfVirtualSystem class

Associates the [**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md) to the corresponding [**Msvm\_VirtualSystem**](msvm-virtualsystemresourcecomponent.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReferencePointOfVirtualSystem : CIM_Dependency
{
  Msvm_ComputerSystem              REF Antecedent;
  Msvm_VirtualSystemReferencePoint REF Dependent;
};
```

## Members

The **Msvm\_ReferencePointOfVirtualSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReferencePointOfVirtualSystem** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

An [**Msvm\_ComputerSystem**](msvm-computersystem.md) that represents the independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemReferencePoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

An [**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md) that represents the object that is dependent on the **Antecedent**.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




