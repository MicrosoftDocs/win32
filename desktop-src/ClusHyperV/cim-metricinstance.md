---
title: CIM\_MetricInstance class
description: Represents an association between an instance of a metric value and a metric definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47c5aaed-e3c7-4dbe-b102-23c85907ba15
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_MetricInstance class
- CIM_MetricInstance class, described
topic_type:
- apiref
api_name:
- CIM_MetricInstance
- CIM_MetricInstance.Antecedent
- CIM_MetricInstance.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_MetricInstance class

Represents an association between an instance of a metric value and a metric definition.An instance of [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) must not exist without being associated with a corresponding [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.7.0"), UMLPackagePath("CIM::Metrics::BaseMetric")]
class CIM_MetricInstance : CIM_Dependency
{
  CIM_BaseMetricDefinition REF Antecedent;
  CIM_BaseMetricValue      REF Dependent;
};
```

## Members

The **CIM\_MetricInstance** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MetricInstance** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BaseMetricDefinition**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The definition of the metric value.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BaseMetricValue**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The metric value that is associated with the metric definition.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





