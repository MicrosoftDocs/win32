---
description: The Hyper-V metrics API defines the following programming elements.
ms.assetid: 00235614-9FCB-4161-B03D-9D557050153B
title: Hyper-V metrics API reference
ms.topic: reference
ms.date: 05/31/2018
---

# Hyper-V metrics API reference

The Hyper-V metrics API defines the following programming elements.

## In this section



| Topic                                                                                    | Description                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_AggregationMetricDefinition**](msvm-aggregationmetricdefinition.md)<br/> | Represents the definition aspects of a metric that is derived from another metric value.<br/>                                                                                                                                                                                                                             |
| [**Msvm\_AggregationMetricValue**](msvm-aggregationmetricvalue.md)<br/>           | Represents the instance value of a metric defined by an instance of the [**Msvm\_AggregationMetricDefinition**](msvm-aggregationmetricdefinition.md) class.<br/>                                                                                                                                                         |
| [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md)<br/>               | Represents the definition aspects of a metric.<br/>                                                                                                                                                                                                                                                                       |
| [**Msvm\_BaseMetricValue**](msvm-basemetricvalue.md)<br/>                         | Represents a metric value defined by an instance of the [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) class.<br/>                                                                                                                                                                                       |
| [**Msvm\_MetricCollectionDependency**](msvm-metriccollectiondependency.md)<br/>   | Represents the association between two metric definitions or two metric values.<br/>                                                                                                                                                                                                                                      |
| [**Msvm\_MetricDefForME**](msvm-metricdefforme.md)<br/>                           | Defines the association between an [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) and a [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) to define metrics for the latter. The metrics definition is given context by the ManagedElement, which is why the definition is dependent on the element.<br/> |
| [**Msvm\_MetricForME**](msvm-metricforme.md)<br/>                                 | This association links a managed element to the metric values being maintained for it.<br/>                                                                                                                                                                                                                               |
| [**Msvm\_MetricInstance**](msvm-metricinstance.md)<br/>                           | Represents an association of metric value objects with their metrics definitions.<br/>                                                                                                                                                                                                                                    |
| [**Msvm\_MetricService**](msvm-metricservice.md)<br/>                             | Provides the ability to manage metrics.<br/>                                                                                                                                                                                                                                                                              |
| [**Msvm\_MetricServiceCapabilities**](msvm-metricservicecapabilities.md)<br/>     | Describes the capabilities of the associated [**Msvm\_MetricService**](msvm-metricservice.md) instance.<br/>                                                                                                                                                                                                             |
| [**Msvm\_MetricServiceSettingData**](msvm-metricservicesettingdata.md)<br/>       | Represents the settings for the metric service. The properties for this class cannot be modified directly. The client must call the [**ModifyServiceSettings**](modifyservicesettings-msvm-metricservice.md) method to modify any of these properties.<br/>                                                              |



 

 

