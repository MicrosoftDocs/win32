---
title: MetricValues element
description: A container element for one or more MetricValue elements.
ms.assetid: 'BCF85EDB-2F76-4C39-B39B-18EEC1FE7D72'
keywords: ["MetricValues element Access Execution Engine"]
topic_type:
- apiref
api_name:
- MetricValues
api_type:
- Schema
---

# MetricValues element

A container element for one or more [**MetricValue**](metricvalue.md) elements.

## Usage

``` syntax
<MetricValues>
  child elements
</MetricValues>
```

## Attributes

There are no attributes.

## Child elements



| Element                                       | Description                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| [**MetricValue**](metricvalue.md)<br/> | This element describes a single metric value.<br/> <br/> |



### Child element sequence

``` syntax
MetricValue
```

## Parent elements



| Element                                   | Description                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------|
| [**Issue**](issue.md)<br/>         | This element holds information about a single issue.<br/> <br/>      |
| [**Iteration**](iteration.md)<br/> | Receives metric values for a single assessment iteration.<br/> <br/> |
| [**TestCase**](testcase.md)<br/>   | An individual test.<br/> <br/>                                       |



## Examples

This example shows the hierarchy with irrelevant element omitted.

``` syntax
<AssessmentResult>
    <Iterations>
        <Iteration>
            <MetricValues>
            <MetricValue>  ...  </MetricValue>
            <MetricValue>  ...  </MetricValue>
            <MetricValue>  ...  </MetricValue>
            </MetricValues>
        </Iteration>
    </Iterations>
</AssessmentResult>
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





