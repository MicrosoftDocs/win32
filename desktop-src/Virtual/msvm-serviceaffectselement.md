---
title: Msvm\_ServiceAffectsElement class
description: Associates a virtual computer system instance with the management service that controls its state.
ms.assetid: 1078857e-0eb1-4e6c-b9b1-4a9efbe44cc9
keywords:
- Msvm_ServiceAffectsElement class Hyper-V
- Msvm_ServiceAffectsElement class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ServiceAffectsElement
- Msvm_ServiceAffectsElement.AffectedElement
- Msvm_ServiceAffectsElement.AffectingElement
- Msvm_ServiceAffectsElement.ElementEffects
- Msvm_ServiceAffectsElement.OtherElementEffectsDescriptions
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

# Msvm\_ServiceAffectsElement class

Associates a virtual computer system instance with the management service that controls its state.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ServiceAffectsElement : CIM_ServiceAffectsElement
{
  CIM_ManagedElement REF AffectedElement;
  CIM_Service        REF AffectingElement;
  uint16                 ElementEffects[];
  string                 OtherElementEffectsDescriptions[];
};
```

## Members

The **Msvm\_ServiceAffectsElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ServiceAffectsElement** class has these properties.

<dl> <dt>

**AffectedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the virtual computer system.

This property is inherited from [**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md).

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Service**](cim-service.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the service that controls the virtual computer system.

This property is inherited from [**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md).

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md).**OtherElementEffectsDescriptions**")
</dt> </dl>

The effect on the managed element. This array corresponds to the **OtherElementEffectsDescriptions** array.

This property is set to 5 (Manages).

This property is inherited from [**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md).

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

<span id="Manages"></span><span id="manages"></span><span id="MANAGES"></span>

**Manages** (5)


</dt> <dd></dd> <dt>

<span id="Consumes"></span><span id="consumes"></span><span id="CONSUMES"></span>

**Consumes** (6)


</dt> <dd></dd> <dt>

<span id="Enhances_Integrity"></span><span id="enhances_integrity"></span><span id="ENHANCES_INTEGRITY"></span>

**Enhances Integrity** (7)


</dt> <dd></dd> <dt>

<span id="Degrades_Integrity"></span><span id="degrades_integrity"></span><span id="DEGRADES_INTEGRITY"></span>

**Degrades Integrity** (8)


</dt> <dd></dd> <dt>

<span id="Enhances_Performance"></span><span id="enhances_performance"></span><span id="ENHANCES_PERFORMANCE"></span>

**Enhances Performance** (9)


</dt> <dd></dd> <dt>

<span id="Degrades_Performance"></span><span id="degrades_performance"></span><span id="DEGRADES_PERFORMANCE"></span>

**Degrades Performance** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**OtherElementEffectsDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md).**ElementEffects**")
</dt> </dl>

Each item in the array provides additional information for the corresponding item in the **ElementEffects** array. A description is required for any item in the **ElementEffects** array that is set to **Other** ("1").

This property is set to **NULL**.

This property is inherited from [**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ServiceAffectsElement** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md)
</dt> <dt>

[**CIM\_ServiceAffectsElement**](https://msdn.microsoft.com/library/mt146250)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





