---
title: MSISCSITARGET\_AffectedJobElement class
description: Represents an association between a job and the managed elements that might be affected by its execution.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b97e693d-8394-40ab-8a25-b0e943a26b47
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_AffectedJobElement class iSCSI Software Target API
- MSISCSITARGET_AffectedJobElement class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_AffectedJobElement
- MSISCSITARGET_AffectedJobElement.AffectedElement
- MSISCSITARGET_AffectedJobElement.AffectingElement
- MSISCSITARGET_AffectedJobElement.ElementEffects
- MSISCSITARGET_AffectedJobElement.OtherElementEffectsDescriptions
api_location:
- WTWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSISCSITARGET\_AffectedJobElement class

Represents an association between a job and the managed elements that might be affected by its execution. It might not be feasible for the job to describe all of the affected elements. The main purpose of this association is to provide information when a job requires exclusive use of the specified managed elements or when side effects must be documented that might occur as a result.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_AffectedJobElement : CIM_AffectedJobElement
{
  CIM_ManagedElement REF AffectedElement;
  CIM_Job            REF AffectingElement;
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
};
```

## Members

The **MSISCSITARGET\_AffectedJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_AffectedJobElement** class has these properties.

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

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

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

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

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

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

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

This property is inherited from [**CIM\_AffectedJobElement**](cim-affectedjobelement.md).

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                 |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WTWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**CIM\_AffectedJobElement**](cim-affectedjobelement.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663)
</dt> </dl>

 

 





