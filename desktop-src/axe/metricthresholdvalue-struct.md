---
title: MetricThresholdValue class
description: This interface provides access to MetricThresholdValue objects.
ms.assetid: B19E4E1F-3BFE-46F0-9681-67235BB6D65C
keywords:
- MetricThresholdValue class Access Execution Engine
- MetricThresholdValue class Access Execution Engine , described
topic_type:
- apiref
api_name:
- MetricThresholdValue
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetricThresholdValue class

This interface provides access to **MetricThresholdValue** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**MetricThresholdValue** has these types of members:

-   [Methods](#methods)

### Methods

The **MetricThresholdValue** class has these methods.



| Method                                                                                        | Description                                                                           |
|:----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**~MetricThresholdValue**](metricthresholdvalue--metricthresholdvalue.md)                   | Destructor method.<br/>                                                         |
| [**GetComparison**](metricthresholdvalue-getcomparison.md)                                   | Returns the comparison setting of the **MetricThresholdValue**.<br/>            |
| [**GetDescriptionProgrammaticName**](metricthresholdvalue-getdescriptionprogrammaticname.md) | Returns the description programmatic name of the **MetricThresholdValue**.<br/> |
| [**GetInclusion**](metricthresholdvalue-getinclusion.md)                                     | Returns the inclusion setting of the **MetricThresholdValue**.<br/>             |
| [**GetValue**](metricthresholdvalue-getvalue.md)                                             | Returns the value of the **MetricThresholdValue**.<br/>                         |
| [**GetValueType**](metricthresholdvalue-getvaluetype.md)                                     | Returns the value type of the **MetricThresholdValue**.<br/>                    |
| [**SetComparison**](metricthresholdvalue-setcomparison.md)                                   | Sets the comparison setting of the **MetricThresholdValue**.<br/>               |
| [**SetDescriptionProgrammaticName**](metricthresholdvalue-setdescriptionprogrammaticname.md) | Sets the description programmatic name of the **MetricThresholdValue**.<br/>    |
| [**SetInclusion**](metricthresholdvalue-setinclusion.md)                                     | Sets the inclusion setting of the **MetricThresholdValue**.<br/>                |
| [**SetValue**](metricthresholdvalue-setvalue.md)                                             | Sets the value of the **MetricThresholdValue**.<br/>                            |
| [**SetValueType**](metricthresholdvalue-setvaluetype.md)                                     | Sets the value type of the **MetricThresholdValue**.<br/>                       |



 

## Remarks

The **MetricThresholdValue** objects hold data from the **MetricThreshold/MetricThresholdValues/MetricThresholdValue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





