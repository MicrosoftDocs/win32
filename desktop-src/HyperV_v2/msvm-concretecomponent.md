---
Description: A generic association used to establish part of relationships between managed elements.
ms.assetid: 4D237D68-0A63-4A19-B6AD-E3C781090994
title: Msvm\_ConcreteComponent class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ConcreteComponent
- Msvm_ConcreteComponent.GroupComponent
- Msvm_ConcreteComponent.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ConcreteComponent class

A generic association used to establish 'part of' relationships between managed elements. [**CIM\_ConcreteComponent**](https://msdn.microsoft.com/library/cc150665) is defined as a concrete subclass of the abstract [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class, to be used in place of many specific subclasses of component that add no semantics (that is subclasses that do not clarify the type of composition, update cardinalities, or add or remove qualifiers.)

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ConcreteComponent : CIM_ConcreteComponent
{
  CIM_ManagedElement REF GroupComponent;
  CIM_ManagedElement REF PartComponent;
};
```

## Members

The **Msvm\_ConcreteComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ConcreteComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent element in the association. This property is inherited from [**CIM\_ConcreteComponent**](https://msdn.microsoft.com/library/cc150665).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The child element in the association. This property is inherited from [**CIM\_ConcreteComponent**](https://msdn.microsoft.com/library/cc150665).

</dd> </dl>

## Remarks

Access to the **Msvm\_ConcreteComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ConcreteComponent**](cim-concretecomponent.md)
</dt> <dt>

[**CIM\_ConcreteComponent**](https://msdn.microsoft.com/library/cc150665)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 




