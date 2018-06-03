---
title: TestCase class
description: This interface provides access to the TestCase elements of an AssessmentResult.
ms.assetid: F1B99126-443E-462B-9069-924580F843D7
keywords:
- TestCase class Access Execution Engine
- TestCase class Access Execution Engine , described
topic_type:
- apiref
api_name:
- TestCase
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# TestCase class

This interface provides access to the **TestCase** elements of an **AssessmentResult**.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**TestCase** has these types of members:

-   [Methods](#methods)

### Methods

The **TestCase** class has these methods.



| Method                                                                                                  | Description                                                                                                 |
|:--------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**~TestCase**](testcase--testcase.md)                                                                 | Destructor method.<br/>                                                                               |
| [**AddIssue**](testcase-addissue.md)                                                                   | Creates and adds an [**Issue**](issue-struct.md) to the **TestCase**.<br/>                           |
| [**AddMetricThreshold**](testcase-addmetricthreshold.md)                                               | Creates and adds a [**MetricThreshold**](metricthreshold-struct.md) to the **TestCase**.<br/>        |
| [**AddMetricValue**](testcase-addmetricvalue.md)                                                       | Overloaded. Creates and adds a [**MetricValue**](metricvalue-struct.md) to the **TestCase**.<br/>    |
| [**AddParent**](testcase-addparent.md)                                                                 | Adds a parent to the **TestCase.**<br/>                                                               |
| [**DeleteSubject**](testcase-deletesubject.md)                                                         | Deletes the [**Subject**](subject.md) from the **TestCase**.<br/>                                    |
| [**GetActivityReference**](testcase-getactivityreference.md)                                           | Returns the activity reference of the **TestCase.**<br/>                                              |
| [**GetCompositeKeyActivityClass**](testcase-getcompositekeyactivityclass.md)                           | Returns the composite key activity class of the **TestCase.**<br/>                                    |
| [**GetCompositeKeyActivityInstance**](testcase-getcompositekeyactivityinstance.md)                     | Returns the composite key activity instance of the **TestCase.**<br/>                                 |
| [**GetCompositeKeySubjectClass**](testcase-getcompositekeysubjectclass.md)                             | Returns the composite key subject class of the **TestCase.**<br/>                                     |
| [**GetCompositeKeySubjectClassDisplayName**](testcase-getcompositekeysubjectclassdisplayname.md)       | Returns the composite key subject class display name of the **TestCase.**<br/>                        |
| [**GetCompositeKeySubjectInstance**](testcase-getcompositekeysubjectinstance.md)                       | Returns the composite key subject instance of the **TestCase.**<br/>                                  |
| [**GetCompositeKeySubjectInstanceDisplayName**](testcase-getcompositekeysubjectinstancedisplayname.md) | Returns the composite key subject instance display name of the **TestCase.**<br/>                     |
| [**GetIssues**](testcase-getissues.md)                                                                 | Returns the [**IssueCollection**](issuecollection.md) for the **TestCase**.<br/>                     |
| [**GetKey**](testcase-getkey.md)                                                                       | Returns the key of the **TestCase.**<br/>                                                             |
| [**GetMetricThresholds**](testcase-getmetricthresholds.md)                                             | Returns the [**MetricThresholdCollection**](metricthresholdcollection.md) for the **TestCase**.<br/> |
| [**GetMetricValues**](testcase-getmetricvalues.md)                                                     | Returns the [**MetricValueCollection**](metricvaluecollection.md) of the **TestCase.**<br/>          |
| [**GetName**](testcase-getname.md)                                                                     | Returns the name of the **TestCase.**<br/>                                                            |
| [**GetParents**](testcase-getparents.md)                                                               | Returns the [**ParentCollection**](parentcollection.md) of the **TestCase.**<br/>                    |
| [**GetSubject**](testcase-getsubject.md)                                                               | Returns the [**Subject**](subject.md) of the **TestCase**.<br/>                                      |
| [**GetToolTip**](testcase-gettooltip.md)                                                               | Returns the tooltip of the **TestCase.**<br/>                                                         |
| [**SetActivityReference**](testcase-setactivityreference.md)                                           | Sets the activity reference of the **TestCase.**<br/>                                                 |
| [**SetCompositeKeyActivityClass**](testcase-setcompositekeyactivityclass.md)                           | Sets the composite key activity class of the **TestCase.**<br/>                                       |
| [**SetCompositeKeyActivityInstance**](testcase-setcompositekeyactivityinstance.md)                     | Sets the composite key activity instance of the **TestCase.**<br/>                                    |
| [**SetCompositeKeySubjectClass**](testcase-setcompositekeysubjectclass.md)                             | Sets the composite key subject class of the **TestCase.**<br/>                                        |
| [**SetCompositeKeySubjectClassDisplayName**](testcase-setcompositekeysubjectclassdisplayname.md)       | Sets the composite key subject class display name of the **TestCase.**<br/>                           |
| [**SetCompositeKeySubjectInstance**](testcase-setcompositekeysubjectinstance.md)                       | Sets the composite key subject instance of the **TestCase.**<br/>                                     |
| [**SetCompositeKeySubjectInstanceDisplayName**](testcase-setcompositekeysubjectinstancedisplayname.md) | Sets the composite key subject instance display name of the **TestCase.**<br/>                        |
| [**SetKey**](testcase-setkey.md)                                                                       | Sets the key of the **TestCase.**<br/>                                                                |
| [**SetName**](testcase-setname.md)                                                                     | Sets the name of the **TestCase.**<br/>                                                               |
| [**SetSubject**](testcase-setsubject.md)                                                               | Overloaded. Sets the [**Subject**](subject.md) of the **TestCase**.<br/>                             |
| [**SetToolTip**](testcase-settooltip.md)                                                               | Sets the tooltip of the **TestCase.**<br/>                                                            |



 

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





