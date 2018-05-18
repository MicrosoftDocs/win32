---
title: Issue element
description: This element holds information about a single issue.
ms.assetid: '0BFC67EF-9DF3-4EE5-871C-658C0049C2CB'
keywords: ["Issue element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Issue
api_type:
- Schema
---

# Issue element

This element holds information about a single issue. Examples of issues would be a missing driver or a PNP device that won’t go into sleep mode.

## Usage

``` syntax
<Issue
  Known = "text"
  ID = "text">
  child elements
</Issue>
```

## Attributes



| Attribute            | Type            | Required      | Description                                                                                      |
|----------------------|-----------------|---------------|--------------------------------------------------------------------------------------------------|
| **ID**<br/>    | text<br/> | No<br/> | A cross reference for a related issue. <br/> <br/>                                   |
| **Known**<br/> | text<br/> | No<br/> | This holds a case-insensitive value of "Yes", "No", "True", or "False" . <br/> <br/> |



## Child elements



| Element                                                 | Description                                                                                             |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**AffectedMetrics**](affectedmetrics.md)<br/>   | Enables a metric value to be related to an issue.<br/> <br/>                                |
| [**Class**](class--issue-.md)<br/>               | The issue class.<br/> <br/>                                                                 |
| [**EqualityID**](equalityid.md)<br/>             | The issue equality identifier.<br/> <br/>                                                   |
| [**Impact**](impact.md)<br/>                     | Describes the impact of the issue.<br/> <br/>                                               |
| [**IssueDescription**](issuedescription.md)<br/> | Brief description of the issue.<br/> <br/>                                                  |
| [**IssueTitle**](issuetitle.md)<br/>             | Short name for the issue. <br/> <br/>                                                       |
| [**IssueToolTip**](issuetooltip.md)<br/>         | A tool tip for the UI to display.<br/> <br/>                                                |
| [**MetricValues**](metricvalues.md)<br/>         | A container element for one or more [**MetricValue**](metricvalue.md) elements.<br/> <br/> |
| [**Solution**](solution.md)<br/>                 | Holds information about a solution for a single issue.<br/> <br/>                           |
| [**SolutionData**](solutiondata.md)<br/>         | Contains XML that is specific to a solution or assessment.<br/> <br/>                       |
| [**TypeID**](typeid.md)<br/>                     | The issue type identifier.<br/> <br/>                                                       |



### Child element sequence

``` syntax
(
  AffectedMetrics, 
  Class, 
  EqualityID, 
  Impact, 
  IssueTitle, 
  IssueDescription, 
  IssueToolTip, 
  MetricValues, 
  Solution, 
  SolutionData, 
  TypeID
)
```

## Parent elements



| Element                             | Description                                                         |
|-------------------------------------|---------------------------------------------------------------------|
| [**Issues**](issues.md)<br/> | A container element for one or more issues. <br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





