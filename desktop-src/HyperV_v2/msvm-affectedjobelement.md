---
Description: 'Represents an association between a job and the managed element that may be affected by its execution.'
ms.assetid: '125A4976-A4E3-4D7A-A43B-86045C3B00AE'
title: 'Msvm\_AffectedJobElement class'
---

# Msvm\_AffectedJobElement class

Represents an association between a job and the managed element that may be affected by its execution.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_AffectedJobElement : CIM_AffectedJobElement
{
  CIM_ManagedElement REF AffectedElement;
  Msvm_ConcreteJob   REF AffectingElement;
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
};
```

## Members

The **Msvm\_AffectedJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_AffectedJobElement** class has these properties.

<dl> <dt>

**AffectedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The managed element affected by the execution of the job. This property is inherited from [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663).

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ConcreteJob**](msvm-concretejob.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The job that is affecting the managed element. This property is inherited from [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663).

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration that describes the effect on the managed element. This property is inherited from [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663).

</dd> <dt>

**OtherElementEffectsDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides details for the effect at the corresponding array position in **ElementEffects**. This property is inherited from [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663).

</dd> </dl>

## Remarks

Access to the **Msvm\_AffectedJobElement** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_AffectedJobElement**](cim-affectedjobelement.md)
</dt> <dt>

[**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 




