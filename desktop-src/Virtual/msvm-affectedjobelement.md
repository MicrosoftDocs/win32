---
title: Msvm\_AffectedJobElement class
description: Represents an association between a job and the managed element that may be affected by its execution.
ms.assetid: d8b3a9e3-e69a-446c-91a5-569beac023a6
keywords:
- Msvm_AffectedJobElement class Hyper-V
- Msvm_AffectedJobElement class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_AffectedJobElement
- Msvm_AffectedJobElement.AffectedElement
- Msvm_AffectedJobElement.ElementEffects
- Msvm_AffectedJobElement.OtherElementEffectsDescriptions
- Msvm_AffectedJobElement.AffectingElement
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
  Msvm_ConcreteJob   REF AffectingElement;
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

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The managed element affected by the execution of the job.

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ConcreteJob**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_affectedJobElement.AffectingElement")
</dt> </dl>

The job that is affecting the managed element.

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_AffectedJobElement**](cim-affectedjobelement.md).**OtherElementEffectsDescriptions**")
</dt> </dl>

The effect the job has on the managed element.

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Exclusive_Use"></span><span id="exclusive_use"></span><span id="EXCLUSIVE_USE"></span>

**Exclusive Use** (2)


</dt> <dd></dd> <dt>

<span id="Performance_Impact"></span><span id="performance_impact"></span><span id="PERFORMANCE_IMPACT"></span>

**Performance Impact** (3)


</dt> <dd></dd> <dt>

<span id="Element_Integrity"></span><span id="element_integrity"></span><span id="ELEMENT_INTEGRITY"></span>

**Element Integrity** (4)


</dt> <dd></dd> <dt>

<span id="Create"></span><span id="create"></span><span id="CREATE"></span>

**Create** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherElementEffectsDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_AffectedJobElement**](cim-affectedjobelement.md).**ElementEffects**")
</dt> </dl>

Additional details for corresponding "1" (Other) values in the **ElementEffects** array.

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_AffectedJobElement** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_AffectedJobElement**](cim-affectedjobelement.md)
</dt> <dt>

[**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/mt445944)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





