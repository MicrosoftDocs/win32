---
title: Filter element
description: Describes a filter for the test cases to appear in the table.
ms.assetid: 22F3DB5B-670F-4A6D-92C3-3744C642A9B0
keywords:
- Filter element Access Execution Engine
topic_type:
- apiref
api_name:
- Filter
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Filter element

Describes a filter for the test cases to appear in the table.

## Usage

``` syntax
<Filter>
  text
</Filter>
```

## Attributes

There are no attributes.

## Text value

The Filter node describes a filter for the test cases to appear in the table. Each non-leaf node under the Filter node describes a binary operation, and each leaf node describes a value. Valid binary operations include: And, Or, Equal, GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual, NotEqual, and Contains ( a case-insensitive string contains operation). Valid leaf nodes include &lt;Metric&gt;programmaticName&lt;/Metric&gt;, defining a metric value, and &lt;Constant&gt;constant&lt;/Constant&gt;, defining a constant.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                                              |
|---------------------------------------------------|------------------------------------------------------------------------------------------|
| [**TestCaseTable**](testcasetable.md)<br/> | The test case table node defines a table of test cases on a page.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





