---
description: Defines the association between an Msvm\_BaseMetricDefinition and a CIM\_ManagedElement to define metrics for the latter. The metrics definition is given context by the ManagedElement, which is why the definition is dependent on the element.
ms.assetid: 528d9b1a-089d-48ae-b5a6-40bc9d09191c
title: Msvm_MetricDefForME class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricDefForME
- Msvm_MetricDefForME.Antecedent
- Msvm_MetricDefForME.Dependent
- Msvm_MetricDefForME.MetricCollectionEnabled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_MetricDefForME class

Defines the association between an [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) and a [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) to define metrics for the latter. The metrics definition is given context by the ManagedElement, which is why the definition is dependent on the element.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MetricDefForME : CIM_MetricDefForME
{
  CIM_ManagedElement       REF Antecedent;
  CIM_BaseMetricDefinition REF Dependent;
  uint16                       MetricCollectionEnabled = 2;
};
```

## Members

The **Msvm\_MetricDefForME** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MetricDefForME** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) class that represents the managed element that can have metrics of the type defined by **Dependent** applied to it. This property is inherited from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) class that represents the metric definition that the **Antecedent** can have applied to it. This property is inherited from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**MetricCollectionEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the metric defined by **Dependent** is being collected for the **Antecedent**. This will be one of the following values.



| Value                                                                                                                                                                                                                                                               | Meaning                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>2</dt> </dl>                                         | The metric is being collected.<br/>                                |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>3</dt> </dl>                                     | The metric is not being collected.<br/>                            |
| <span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span><dl> <dt>**Reserved**</dt> <dt>4</dt> </dl>                                     |                                                                          |
| <span id="PartiallyEnabled"></span><span id="partiallyenabled"></span><span id="PARTIALLYENABLED"></span><dl> <dt>**PartiallyEnabled**</dt> <dt>32768</dt> </dl> | The metric is being collected for some, but not all, devices.<br/> |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

