---
title: Iteration class
description: This interface provides access to the Iterations element of an AssessmentResult.
ms.assetid: FE18AA62-3E43-4490-8B7C-C415DAB479E4
keywords:
- Iteration class Access Execution Engine
- Iteration class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Iteration
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

# Iteration class

This interface provides access to the **Iterations** element of an **AssessmentResult**.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Iteration** has these types of members:

-   [Methods](#methods)

### Methods

The **Iteration** class has these methods.



| Method                                                                             | Description                                                                                                  |
|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| [**~Iteration**](iteration--iteration.md)                                         | Destructor method.<br/>                                                                                |
| [**AddActivity**](iteration-addactivity.md)                                       | Creates and adds an [**Activity**](activity-struct.md) to the **Iteration**.<br/>                     |
| [**AddIssue**](iteration-addissue.md)                                             | Creates and adds an [**Issue**](issue-struct.md) to the **Iteration**.<br/>                           |
| [**AddMetricThreshold**](iteration-addmetricthreshold.md)                         | Creates and adds a [**MetricThreshold**](metricthreshold-struct.md) to the **Iteration**.<br/>        |
| [**AddMetricValue**](iteration-addmetricvalue.md)                                 | Overloaded. Creates and adds a [**MetricValue**](metricvalue-struct.md) to the **Iteration**.<br/>    |
| [**AddTestCase**](iteration-addtestcase.md)                                       | Creates and adds a [**TestCase**](testcase-struct.md) to the **Iteration**.<br/>                      |
| [**ClearTrace**](iteration-cleartrace.md)                                         | Clear the trace for the **Iteration**.<br/>                                                            |
| [**GetActivities**](iteration-getactivities.md)                                   | Returns the [**ActivityCollection**](activitycollection.md) for the **Iteration**.<br/>               |
| [**GetDescriptionDisplayName**](iteration-getdescriptiondisplayname.md)           | Returns the description display name of the **Iteration**.<br/>                                        |
| [**GetDescriptionProgrammaticName**](iteration-getdescriptionprogrammaticname.md) | Returns the description programmatic name of the **Iteration**.<br/>                                   |
| [**GetIssues**](iteration-getissues.md)                                           | Returns the [**IssueCollection**](issuecollection.md) for the **Iteration**.<br/>                     |
| [**GetMetricThresholds**](iteration-getmetricthresholds.md)                       | Returns the [**MetricThresholdCollection**](metricthresholdcollection.md) for the **Iteration**.<br/> |
| [**GetMetricValues**](iteration-getmetricvalues.md)                               | Returns the [**MetricValueCollection**](metricvaluecollection.md) for the **Iteration**.<br/>         |
| [**GetOrdinal**](iteration-getordinal.md)                                         | Returns the ordinal value of the **Iteration**.<br/>                                                   |
| [**GetTestCases**](iteration-gettestcases.md)                                     | Returns the [**TestCaseCollection**](testcasecollection.md) for the **Iteration**.<br/>               |
| [**GetTrace**](iteration-gettrace.md)                                             | Returns the [**Trace**](trace-struct.md) object of the **Iteration**.<br/>                            |
| [**GetTraceFile**](iteration-gettracefile.md)                                     | Returns the trace file name for the **Iteration**.<br/>                                                |
| [**GetTraceLink**](iteration-gettracelink.md)                                     | Returns the trace link for the **Iteration**.<br/>                                                     |
| [**GetTraceName**](iteration-gettracename.md)                                     | Returns the trace name for the **Iteration**.<br/>                                                     |
| [**GetTraceToolTip**](iteration-gettracetooltip.md)                               | Returns the trace tooltip for the **Iteration**.<br/>                                                  |
| [**SetDescriptionDisplayName**](iteration-setdescriptiondisplayname.md)           | Sets the description display name of the **Iteration**.<br/>                                           |
| [**SetDescriptionProgrammaticName**](iteration-setdescriptionprogrammaticname.md) | Sets the description programmatic name of the **Iteration**.<br/>                                      |
| [**SetOrdinal**](iteration-setordinal.md)                                         | Sets the ordinal value of the **Iteration**.<br/>                                                      |
| [**SetTrace**](iteration-settrace.md)                                             | Overloaded. Sets values for the [**Trace**](trace-struct.md) object of the **Iteration**.<br/>        |
| [**SetTraceFile**](iteration-settracefile.md)                                     | Sets the trace file name for the **Iteration**.<br/>                                                   |
| [**SetTraceLink**](iteration-settracelink.md)                                     | Sets the trace link for the **Iteration**.<br/>                                                        |
| [**SetTraceName**](iteration-settracename.md)                                     | Sets the trace name for the **Iteration**.<br/>                                                        |
| [**SetTraceToolTip**](iteration-settracetooltip.md)                               | Sets the trace tooltip for the **Iteration**.<br/>                                                     |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





