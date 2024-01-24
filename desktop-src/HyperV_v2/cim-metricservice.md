---
description: Manages metrics for managed elements.
ms.assetid: df249d0c-960b-47d6-9590-f0fd08ddec18
title: CIM_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MetricService
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_MetricService class

Manages metrics for managed elements.

## Syntax

``` syntax
[Abstract, Version("2.23.0"), UMLPackagePath("CIM::Metrics::BaseMetric"), AMENDMENT]
class CIM_MetricService : CIM_Service
{
};
```

## Members

The **CIM\_MetricService** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_MetricService** class has these methods.



| Method                                                                   | Description                                                                                                                                                                         |
|:-------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ControlMetrics**](cim-metricservice-controlmetrics.md)               | Enables and disables the collection of metrics.<br/>                                                                                                                          |
| [**ControlMetricsByClass**](cim-metricservice-controlmetricsbyclass.md) | Enables and disables the collection of metrics for a class.<br/>                                                                                                              |
| [**ControlSampleTimes**](cim-metricservice-controlsampletimes.md)       | Specifies when metrics are gathered.<br/>                                                                                                                                     |
| [**GetMetricValues**](cim-metricservice-getmetricvalues.md)             | Retrieves a filtered list of metric values.<br/>                                                                                                                              |
| [**ShowMetrics**](cim-metricservice-showmetrics.md)                     | Indicates whether metric collection is enabled for the specified managed elements, and indicates the metrics that are available for collection for each managed element.<br/> |
| [**ShowMetricsByClass**](cim-metricservice-showmetricsbyclass.md)       | Indicates which metrics are available for collection for all instances of a CIM class.<br/>                                                                                   |



 

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

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 




