---
description: This association links a managed element to the metric values being maintained for it.
ms.assetid: 89b43736-90ae-49e0-a0ed-7918ddec8558
title: Msvm_MetricForME class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricForME
- Msvm_MetricForME.Antecedent
- Msvm_MetricForME.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_MetricForME class

This association links a managed element to the metric values being maintained for it.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MetricForME : CIM_MetricForME
{
  CIM_ManagedElement  REF Antecedent;
  CIM_BaseMetricValue REF Dependent;
};
```

## Members

The **Msvm\_MetricForME** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MetricForME** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) class that represents the managed element that has metrics defined by **Dependent** maintained for it. This property is inherited from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: ****CIM\_BaseMetricValue****
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the **CIM\_BaseMetricValue** class that represents the metric that the **Antecedent** has collected for it. This property is inherited from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

