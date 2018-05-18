---
title: CIM\_AffectedJobElement class
description: Represents an association between a job and the CIM\_ManagedElement objects that may be affected by its execution.
ms.assetid: '2b2aa04e-b1a3-454e-844d-37f61c2a3916'
keywords: ["CIM_AffectedJobElement class Hyper-V", "CIM_AffectedJobElement class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_AffectedJobElement
- CIM_AffectedJobElement.AffectedElement
- CIM_AffectedJobElement.AffectingElement
- CIM_AffectedJobElement.ElementEffects
- CIM_AffectedJobElement.OtherElementEffectsDescriptions
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_AffectedJobElement class

Represents an association between a job and the **CIM\_ManagedElement** objects that may be affected by its execution. It may not be feasible for the job to describe all of the affected elements. The main purpose of this association is to provide information when a job requires exclusive use of the affected managed elements or when describing the side effects that may result.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.7.0"), AMENDMENT]
class CIM_AffectedJobElement
{
  CIM_ManagedElement REF AffectedElement;
  CIM_Job            REF AffectingElement;
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
};
```

## Members

The **CIM\_AffectedJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AffectedJobElement** class has these properties.

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

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Job**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The job that is affecting the managed element.

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_AffectedJobElement**.**OtherElementEffectsDescriptions**")
</dt> </dl>

The effect the job has on the managed element.

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

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_AffectedJobElement**.**ElementEffects**")
</dt> </dl>

Additional details for corresponding "1" (Other) values in the **ElementEffects** array.

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



 

 





