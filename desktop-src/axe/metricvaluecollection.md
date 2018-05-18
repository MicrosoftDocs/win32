---
title: MetricValueCollection class
description: This interface provides containers for MetricValue objects.
ms.assetid: '248A9435-8ADF-462C-AD19-DD0F0C04CA1F'
keywords: ["MetricValueCollection class Access Execution Engine", "MetricValueCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- MetricValueCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricValueCollection class

This interface provides containers for [**MetricValue**](metricvalue-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**MetricValueCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **MetricValueCollection** class has these methods.



| Method                                                                         | Description                                                                                                             |
|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**~MetricValueCollection**](metricvaluecollection--metricvaluecollection.md) | Destructor method.<br/>                                                                                           |
| [**AddItem**](metricvaluecollection-additem.md)                               | Overloaded. Creates a [**MetricValue**](metricvalue-struct.md) and adds it to the **MetricValueCollection**<br/> |
| [**Clear**](metricvaluecollection-clear.md)                                   | Deletes all [**MetricValue**](metricvalue-struct.md) objects from the **MetricValueCollection**.<br/>            |
| [**DeleteItem**](metricvaluecollection-deleteitem.md)                         | Deletes a [**MetricValue**](metricvalue-struct.md) from the **MetricValueCollection**.<br/>                      |
| [**GetCount**](metricvaluecollection-getcount.md)                             | Returns a count of the [**MetricValue**](metricvalue-struct.md) objects in the **MetricValueCollection**.<br/>   |
| [**GetItem**](metricvaluecollection-getitem.md)                               | Returns a [**MetricValue**](metricvalue-struct.md) from the **MetricValueCollection**.<br/>                      |



 

## Remarks

A **MetricValueCollection** object holds data from an **Issue/MetricValues**, **Iteration/MetricValues**, or **TestCase/MetricValues** element.

A **MetricValue** object holds data from a **MetricValues/MetricValue** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





