---
title: CIM\_MetricForME class
description: Represents an association in which a metric values are collected for a managed element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2f95ce39-ffa8-4ed6-a6c5-b59b3b1e7e4e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_MetricForME class
- CIM_MetricForME class, described
topic_type:
- apiref
api_name:
- CIM_MetricForME
- CIM_MetricForME.Antecedent
- CIM_MetricForME.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_MetricForME class

Represents an association in which a metric values are collected for a managed element.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.7.0"), UMLPackagePath("CIM::Metrics::BaseMetric")]
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

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The managed element in the association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BaseMetricValue**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The metric value in the association.

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

 

 





