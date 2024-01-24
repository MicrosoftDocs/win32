---
description: Represents the association between a job and the managed elements that may be affected by its execution.
ms.assetid: 81849DE4-9039-426F-B7B1-45BB31A9132C
title: Msvm_AffectedStorageJobElement class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_AffectedStorageJobElement
- Msvm_AffectedStorageJobElement.AffectedElement
- Msvm_AffectedStorageJobElement.AffectingElement
- Msvm_AffectedStorageJobElement.ElementEffects
- Msvm_AffectedStorageJobElement.OtherElementEffectsDescriptions
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_AffectedStorageJobElement class

Represents the association between a job and the managed elements that may be affected by its execution.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_AffectedStorageJobElement : CIM_AffectedJobElement
{
  CIM_ManagedElement REF AffectedElement;
  Msvm_StorageJob    REF AffectingElement;
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
};
```

## Members

The **Msvm\_AffectedStorageJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_AffectedStorageJobElement** class has these properties.

<dl> <dt>

**AffectedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The managed element affected by the execution of the job. This property is inherited from [**CIM\_AffectedJobElement**](/previous-versions//cc150663(v=vs.85)).

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_StorageJob**](msvm-storagejob.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\_AffectedJobElement.AffectingElement")
</dt> </dl>

The job that is affecting the affected element. This property is inherited from [**CIM\_AffectedJobElement**](/previous-versions//cc150663(v=vs.85)).

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration that describes the effect on the managed element. This array corresponds to the **OtherElementEffectsDescriptions** property array, where the latter provides details related to the high-level effects enumerated by this property. Additional detail is required if the **ElementEffects** property array contains the value 1, (Other). This property is inherited from [**CIM\_AffectedJobElement**](/previous-versions//cc150663(v=vs.85)).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Exclusive_Use"></span><span id="exclusive_use"></span><span id="EXCLUSIVE_USE"></span>**Exclusive Use** (2)
</dt> <dt>

<span id="Performance_Impact"></span><span id="performance_impact"></span><span id="PERFORMANCE_IMPACT"></span>**Performance Impact** (3)
</dt> <dt>

<span id="Element_Integrity_"></span><span id="element_integrity_"></span><span id="ELEMENT_INTEGRITY_"></span>**Element Integrity** (4 )
</dt> </dl>

</dd> <dt>

**OtherElementEffectsDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides details for the effect at the corresponding array position in the **ElementEffects** property array. This information is required whenever the corresponding element in the **ElementEffects** property array contains the value 1 (Other). This property is inherited from [**CIM\_AffectedJobElement**](/previous-versions//cc150663(v=vs.85)).

</dd> </dl>

## Remarks

Access to the **Msvm\_AffectedStorageJobElement** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_AffectedJobElement**](cim-affectedjobelement.md)
</dt> <dt>

[**CIM\_AffectedJobElement**](/previous-versions//cc150663(v=vs.85))
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

