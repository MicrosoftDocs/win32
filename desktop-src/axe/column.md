---
title: Column element
description: The column node describes a column of metric values.
ms.assetid: 'A6C14E8A-2755-4A65-B6A4-7DD675D6C005'
keywords: ["Column element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Column
api_type:
- Schema
---

# Column element

The column node describes a column of metric values.

## Usage

``` syntax
<Column>
  child elements
</Column>
```

## Attributes

There are no attributes.

## Child elements



| Element                                               | Description                                                                                                                                                                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Charted**](charted.md)<br/>                 | If this column is part of a group or the overview presentation hints columns, the value (True \| False) defines whether this column is charted by default or not. This field is optional.<br/> <br/>      |
| [**Hidden**](hidden--column-.md)<br/>          | If this column is part of a "TestCaseTable", the value (True \| False) defines the initial visibility of the column. "True" specifies the column is initially visible. This field is optional.<br/> <br/> |
| [**Metric**](metric.md)<br/>                   | Contains the programmatic name of a metric definition. This field is required.<br/> <br/>                                                                                                                 |
| **PageLink**<br/>                               | Defines an link from this column to another report page. This field is optional.<br/> <br/>                                                                                                               |
| **TestCaseKey**<br/>                            | If present, the Metric value is loaded from the specified test case rather than the current test case. This field is optional.<br/> <br/>                                                                 |
| [**TestCaseName**](testcasename.md)<br/>       | If **TestCaseKey** is present, gives a human-readable localizable name of the test case. This field is optional.<br/> <br/>                                                                               |
| [**TestCaseToolTip**](testcasetooltip.md)<br/> | The test case tooltip.<br/> <br/>                                                                                                                                                                         |



### Child element sequence

``` syntax
MetricPageLinkHiddenChartedTestCaseKeyTestCaseNameTestCaseToolTip
```

## Parent elements



| Element                               | Description                                                                                                           |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**Columns**](columns.md)<br/> | A collection of the most important metrics gathered by the assessment. This field is optional.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**AXE Assessment Manifest**](axeassessmentmanifest.md)
</dt> </dl>

 

 





