---
title: MetricThreshold class
description: This interface provides access to MetricThreshold objects.
ms.assetid: '3E150D5E-EE7A-4036-8592-2F1C6A973F48'
keywords: ["MetricThreshold class Access Execution Engine", "MetricThreshold class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- MetricThreshold
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThreshold class

This interface provides access to **MetricThreshold** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**MetricThreshold** has these types of members:

-   [Methods](#methods)

### Methods

The **MetricThreshold** class has these methods.



| Method                                                                                             | Description                                                                                                                 |
|:---------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**~MetricThreshold**](metricthreshold--metricthreshold.md)                                       | Destructor method.<br/>                                                                                               |
| [**AddMetricThresholdValue**](metricthreshold-addmetricthresholdvalue.md)                         | Creates and adds a [**MetricThresholdValue**](metricthresholdvalue-struct.md) to the **MetricThreshold**.<br/>       |
| [**GetDescriptionProgrammaticName**](metricthreshold-getdescriptionprogrammaticname.md)           | Returns the description programmatic name of the **MetricThreshold**.<br/>                                            |
| [**GetMetricDefinitionProgrammaticName**](metricthreshold-getmetricdefinitionprogrammaticname.md) | Returns the metric definition programmatic name of the **MetricThreshold**.<br/>                                      |
| [**GetMetricThresholdValues**](metricthreshold-getmetricthresholdvalues.md)                       | Returns the [**MetricThresholdValueCollection**](metricthresholdvaluecollection.md) of the **MetricThreshold**.<br/> |
| [**GetOrdinal**](metricthreshold-getordinal.md)                                                   | Returns the ordinal of the **MetricThreshold**.<br/>                                                                  |
| [**GetTarget**](metricthreshold-gettarget.md)                                                     | Returns the target of the **MetricThreshold**.<br/>                                                                   |
| [**GetTestCaseKey**](metricthreshold-gettestcasekey.md)                                           | Returns the test case key of the **MetricThreshold**.<br/>                                                            |
| [**SetDescriptionProgrammaticName**](metricthreshold-setdescriptionprogrammaticname.md)           | Sets the description programmatic name of the **MetricThreshold**.<br/>                                               |
| [**SetMetricDefinitionProgrammaticName**](metricthreshold-setmetricdefinitionprogrammaticname.md) | Sets the metric definition programmatic name of the **MetricThreshold**.<br/>                                         |
| [**SetOrdinal**](metricthreshold-setordinal.md)                                                   | Sets the ordinal of the **MetricThreshold**.<br/>                                                                     |
| [**SetTarget**](metricthreshold-settarget.md)                                                     | Sets the target of the **MetricThreshold**.<br/>                                                                      |
| [**SetTestCaseKey**](metricthreshold-settestcasekey.md)                                           | Sets the test case key of the **MetricThreshold**.<br/>                                                               |



 

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





