---
title: TestCaseTable element
description: The test case table node defines a table of test cases on a page.
ms.assetid: 8BFEAECB-6A42-4C27-B480-C633376EC1DC
keywords:
- TestCaseTable element Access Execution Engine
topic_type:
- apiref
api_name:
- TestCaseTable
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TestCaseTable element

The test case table node defines a table of test cases on a page.

## Usage

``` syntax
<TestCaseTable>
  child elements
</TestCaseTable>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                                                                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Columns**](columns.md)<br/>             | A collection of the most important metrics gathered by the assessment. <br/> <br/>                                                                                                                |
| [**Description**](description.md)<br/>     | This node contains the description of the test case table. The programmatic name is not necessary, [**Name**](name.md) and [**ToolTip**](tooltip.md) are used to describe the table.<br/> <br/> |
| [**Filter**](filter.md)<br/>               | Describes a filter for the test cases to appear in the table. <br/> <br/>                                                                                                                         |
| [**GroupBy**](groupby.md)<br/>             | The name of one of the columns in the table that specifies how the test cases are initially grouped.<br/> <br/>                                                                                   |
| [**PageLink**](pagelink.md)<br/>           | This node is the main page of the report.<br/> <br/>                                                                                                                                              |
| [**Sort**](sort.md)<br/>                   | The programmatic name of the metric the test case table should initially be sorted by.<br/> <br/>                                                                                                 |
| [**SortAscending**](sortascending.md)<br/> | Specifies whether the initial sort is ascending or descending.<br/> <br/>                                                                                                                         |
| [**TestCaseKey**](testcasekey.md)<br/>     | A real or virtual test case each test case in the table must have listed as a parent.<br/> <br/>                                                                                                  |



### Child element sequence

``` syntax
DescriptionPageLinkColumnsSortSortAscendingGroupByTestCaseKeyFilter
```

## Parent elements



| Element                         | Description                                     |
|---------------------------------|-------------------------------------------------|
| [**Page**](page.md)<br/> | A description of a page.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





