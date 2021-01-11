---
description: Represents an association in which a metric values are collected for a managed element.
ms.assetid: 00752751-bc27-463b-a4ac-4db8e5040077
title: CIM_MetricForME class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MetricForME
- CIM_MetricForME.Antecedent
- CIM_MetricForME.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_MetricForME class

Represents an association in which a metric values are collected for a managed element.

## Syntax

``` syntax
[Association, Abstract, Version("2.7.0"), UMLPackagePath("CIM::Metrics::BaseMetric"), AMENDMENT]
class CIM_MetricForME : CIM_Dependency
{
  CIM_ManagedElement  REF Antecedent;
  CIM_BaseMetricValue REF Dependent;
};
```

## Members

The **CIM\_MetricForME** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MetricForME** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The managed element in the association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BaseMetricValue**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The metric value in the association.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

