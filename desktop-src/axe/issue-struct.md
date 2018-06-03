---
title: Issue class
description: This interface provides access to Issue objects.
ms.assetid: 644C4859-9804-4AF9-93EB-6A5BB08B3299
keywords:
- Issue class Access Execution Engine
- Issue class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Issue
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

# Issue class

This interface provides access to **Issue** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Issue** has these types of members:

-   [Methods](#methods)

### Methods

The **Issue** class has these methods.



| Method                                                                               | Description                                                                                                           |
|:-------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**~Issue**](issue--issue.md)                                                       | Destructor method.<br/>                                                                                         |
| [**AddAnalysisLink**](issue-addanalysislink.md)                                     | Creates and adds an analysis [**Link**](link-struct.md) to the **Issue**.<br/>                                 |
| [**AddCategory**](issue-addcategory.md)                                             | Creates and adds a category to the **Issue**.<br/>                                                              |
| [**AddImpactRelatedActivityReference**](issue-addimpactrelatedactivityreference.md) | Creates and adds an impact-related [**ActivityReference**](activityreference-struct.md) to the **Issue**.<br/> |
| [**AddMetricReference**](issue-addmetricreference.md)                               | Creates and adds a metric reference to the **Issue**.<br/>                                                      |
| [**AddMetricValue**](issue-addmetricvalue.md)                                       | Overloaded. Creates and adds a [**MetricValue**](metricvalue-struct.md) to the **Issue**.<br/>                 |
| [**AddSolutionLink**](issue-addsolutionlink.md)                                     | Creates and adds a solution [**Link**](link-struct.md) to the **Issue**.<br/>                                  |
| [**GetAffectedMetrics**](issue-getaffectedmetrics.md)                               | Returns the [**AffectedMetricCollection**](affectedmetriccollection.md) of the **Issue**.<br/>                 |
| [**GetAnalysisLinks**](issue-getanalysislinks.md)                                   | Returns the analysis [**LinkCollection**](linkcollection.md) of the **Issue**.<br/>                            |
| [**GetAttributeID**](issue-getattributeid.md)                                       | Returns the ID of the **Issue**.<br/>                                                                           |
| [**GetAttributeKnown**](issue-getattributeknown.md)                                 | Returns the value of attribute **Known** of the **Issue**.<br/>                                                 |
| [**GetAttributeParentID**](issue-getattributeparentid.md)                           | Returns the parent ID of the **Issue**.<br/>                                                                    |
| [**GetAttributeSummary**](issue-getattributesummary.md)                             | Returns the summary of the **Issue**.<br/>                                                                      |
| [**GetAttributeTestCase**](issue-getattributetestcase.md)                           | Returns the test case of the **Issue**.<br/>                                                                    |
| [**GetCategories**](issue-getcategories.md)                                         | Returns the [**CategoryCollection**](categorycollection.md) of the **Issue**.<br/>                             |
| [**GetClassDisplayName**](issue-getclassdisplayname.md)                             | Returns the display name of the class of the **Issue**.<br/>                                                    |
| [**GetClassProgrammaticName**](issue-getclassprogrammaticname.md)                   | Returns the programmatic name of the class of the **Issue**.<br/>                                               |
| [**GetEqualityID**](issue-getequalityid.md)                                         | Returns the equality ID of the **Issue**.<br/>                                                                  |
| [**GetImpactAttributeSeverity**](issue-getimpactattributeseverity.md)               | Returns the impact severity of the **Issue**.<br/>                                                              |
| [**GetImpactRelatedActivities**](issue-getimpactrelatedactivities.md)               | Returns the impact [**RelatedActivityCollection**](relatedactivitycollection.md) of the **Issue**.<br/>        |
| [**GetIssueDescription**](issue-getissuedescription.md)                             | Returns the description of the **Issue**.<br/>                                                                  |
| [**GetIssueTitle**](issue-getissuetitle.md)                                         | Returns the title of the **Issue**.<br/>                                                                        |
| [**GetIssueToolTip**](issue-getissuetooltip.md)                                     | Returns the tooltip of the **Issue**.<br/>                                                                      |
| [**GetMetricValues**](issue-getmetricvalues.md)                                     | Returns the [**MetricValueCollection**](metricvaluecollection.md) of the **Issue**.<br/>                       |
| [**GetSolutionDescription**](issue-getsolutiondescription.md)                       | Returns the solution description of the **Issue**.<br/>                                                         |
| [**GetsolutionLinks**](issue-getsolutionlinks.md)                                   | Returns the solution [**LinkCollection**](linkcollection.md) of the **Issue**.<br/>                            |
| [**GetTypeID**](issue-gettypeid.md)                                                 | Returns the type ID of the **Issue**.<br/>                                                                      |
| [**SetAttributeID**](issue-setattributeid.md)                                       | Sets the ID of the **Issue**.<br/>                                                                              |
| [**SetAttributeKnown**](issue-setattributeknown.md)                                 | Sets the value of attribute **Known** of the **Issue**.<br/>                                                    |
| [**SetAttributeParentID**](issue-setattributeparentid.md)                           | Sets the parent ID of the **Issue**.<br/>                                                                       |
| [**SetAttributeSummary**](issue-setattributesummary.md)                             | Sets the summary of the **Issue**.<br/>                                                                         |
| [**SetAttributeTestCase**](issue-setattributetestcase.md)                           | Sets the test case of the **Issue**.<br/>                                                                       |
| [**SetClassDisplayName**](issue-setclassdisplayname.md)                             | Sets the display name of the class of the **Issue**.<br/>                                                       |
| [**SetClassProgrammaticName**](issue-setclassprogrammaticname.md)                   | Sets the programmatic name of the class of the **Issue**.<br/>                                                  |
| [**SetEqualityID**](issue-setequalityid.md)                                         | Sets the equality ID of the **Issue**.<br/>                                                                     |
| [**SetImpactAttributeSeverity**](issue-setimpactattributeseverity.md)               | Sets the impact severity of the **Issue**.<br/>                                                                 |
| [**SetIssueDescription**](issue-setissuedescription.md)                             | Sets the description of the **Issue**.<br/>                                                                     |
| [**SetIssueTitle**](issue-setissuetitle.md)                                         | Sets the title of the **Issue**.<br/>                                                                           |
| [**SetIssueToolTip**](issue-setissuetooltip.md)                                     | Sets the tooltip of the **Issue**.<br/>                                                                         |
| [**SetSolutionDescription**](issue-setsolutiondescription.md)                       | Sets the solution description of the **Issue**.<br/>                                                            |
| [**SetTypeID**](issue-settypeid.md)                                                 | Sets the type ID of the **Issue**.<br/>                                                                         |



 

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





