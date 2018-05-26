---
title: CIM\_AffectedJobElement class
description: AffectedJobElement represents an association between a Job and the ManagedElement(s) that may be affected by its execution.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b1d947c-d44b-4a4b-9685-465f62b1561b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_AffectedJobElement class iSCSI Software Target API
- CIM_AffectedJobElement class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_AffectedJobElement
- CIM_AffectedJobElement.AffectedElement
- CIM_AffectedJobElement.AffectingElement
- CIM_AffectedJobElement.ElementEffects
- CIM_AffectedJobElement.OtherElementEffectsDescriptions
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_AffectedJobElement class

AffectedJobElement represents an association between a Job and the ManagedElement(s) that may be affected by its execution. It may not be feasible for the Job to describe all of the affected elements. The main purpose of this association is to provide information when a Job requires exclusive use of the 'affected' ManagedElment(s) or when describing that side effects may result.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.15.0"), UMLPackagePath("CIM::System::Processing")]
class CIM_AffectedJobElement
{
  CIM_ManagedElement REF AffectedElement;
  CIM_Job            REF AffectingElement;
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
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

The [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) affected by the execution of the Job.

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Job**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Job that is affecting the ManagedElement.

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_AffectedJobElement.OtherElementEffectsDescriptions")
</dt> </dl>

An enumeration describing the 'effect' on the ManagedElement. This array corresponds to the OtherElementEffectsDescriptions array, where the latter provides details related to the high-level 'effects' enumerated by this property. Additional detail is required if the ElementEffects array contains the value 1, "Other".

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

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_AffectedJobElement.ElementEffects")
</dt> </dl>

Provides details for the 'effect' at the corresponding array position in ElementEffects. This information is required whenever ElementEffects contains the value 1 ("Other").

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





