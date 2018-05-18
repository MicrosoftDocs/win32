---
title: MetricThresholdValueCollection class
description: This interface provides containers for MetricThresholdValue objects.
ms.assetid: '2D8A86AD-8554-47B2-9C74-65EDBD9BC243'
keywords: ["MetricThresholdValueCollection class Access Execution Engine", "MetricThresholdValueCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- MetricThresholdValueCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdValueCollection class

This interface provides containers for [**MetricThresholdValue**](metricthresholdvalue-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**MetricThresholdValueCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **MetricThresholdValueCollection** class has these methods.



| Method                                                                                                    | Description                                                                                                 |
|:----------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**~MetricThresholdValueCollection**](metricthresholdvaluecollection--metricthresholdvaluecollection.md) | Destructor method.<br/>                                                                               |
| [**AddItem**](metricthresholdvaluecollection-additem.md)                                                 | Creates and adds a **MetricThresholdValue** to the **MetricThresholdValueCollection**.<br/>           |
| [**Clear**](metricthresholdvaluecollection-clear.md)                                                     | Deletes all **MetricThresholdValue** objects from the **MetricThresholdValueCollection**.<br/>        |
| [**DeleteItem**](metricthresholdvaluecollection-deleteitem.md)                                           | Deletes a **MetricThresholdValue** from the **MetricThresholdValueCollection**.<br/>                  |
| [**GetCount**](metricthresholdvaluecollection-getcount.md)                                               | Returns the count of **MetricThresholdValue** objects in the **MetricThresholdValueCollection**.<br/> |
| [**GetItem**](metricthresholdvaluecollection-getitem.md)                                                 | Returns a **MetricThresholdValue** from the **MetricThresholdValueCollection**.<br/>                  |



 

## Remarks

The **MetricThresholdValueCollection** holds data from element **MetricThreshold/MetricThresholdValues**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





