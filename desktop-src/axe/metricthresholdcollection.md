---
title: MetricThresholdCollection class
description: This interface provides containers for MetricThreshold objects.
ms.assetid: 'DEF8170A-510A-406B-A220-30776C448063'
keywords: ["MetricThresholdCollection class Access Execution Engine", "MetricThresholdCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- MetricThresholdCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdCollection class

This interface provides containers for [**MetricThreshold**](metricthreshold-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**MetricThresholdCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **MetricThresholdCollection** class has these methods.



| Method                                                                                     | Description                                                                                                                     |
|:-------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**~MetricThresholdCollection**](metricthresholdcollection--metricthresholdcollection.md) | Destructor method.<br/>                                                                                                   |
| [**AddItem**](metricthresholdcollection-additem.md)                                       | Creates and adds a [**MetricThreshold**](metricthreshold-struct.md) to the **MetricThresholdCollection**.<br/>           |
| [**Clear**](metricthresholdcollection-clear.md)                                           | Deletes all [**MetricThreshold**](metricthreshold-struct.md) objects from the **MetricThresholdCollection**.<br/>        |
| [**DeleteItem**](metricthresholdcollection-deleteitem.md)                                 | Deletes a [**MetricThreshold**](metricthreshold-struct.md) from the **MetricThresholdCollection**.<br/>                  |
| [**GetCount**](metricthresholdcollection-getcount.md)                                     | Returns the count of [**MetricThreshold**](metricthreshold-struct.md) objects in the **MetricThresholdCollection**.<br/> |
| [**GetItem**](metricthresholdcollection-getitem.md)                                       | Returns a [**MetricThreshold**](metricthreshold-struct.md) from the **MetricThresholdCollection**.<br/>                  |



 

## Remarks

A **MetricThresholdCollection** holds data from a **MetricThresholds** element.

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





