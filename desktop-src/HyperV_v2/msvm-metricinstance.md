---
description: Represents an association of metric value objects with their metrics definitions.
ms.assetid: 98ad9390-78b4-4c18-b068-d05efa2f1866
title: Msvm_MetricInstance class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricInstance
- Msvm_MetricInstance.Antecedent
- Msvm_MetricInstance.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_MetricInstance class

Represents an association of metric value objects with their metrics definitions. This association ties an instance of [**Msvm\_BaseMetricValue**](msvm-basemetricvalue.md) to its [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MetricInstance : CIM_MetricInstance
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **Msvm\_MetricInstance** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MetricInstance** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: ****CIM\_ManagedElement****
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A reference to an instance of the [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) class that represents the metrics definitions.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: ****CIM\_ManagedElement****
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A reference to an instance of the [**Msvm\_BaseMetricValue**](msvm-basemetricvalue.md) class that represents the metrics that are dependent on the **Antecedent**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




