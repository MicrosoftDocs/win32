---
title: Iteration element
description: Receives metric values for a single assessment iteration.
ms.assetid: EB2A453B-4A45-49D3-B292-176B725376AC
keywords:
- Iteration element Access Execution Engine
topic_type:
- apiref
api_name:
- Iteration
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Iteration element

Receives metric values for a single assessment iteration.

## Usage

``` syntax
<Iteration>
  child elements
</Iteration>
```

## Attributes

There are no attributes.

## Child elements



| Element                                         | Description                                                                                                    |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**Activities**](activities.md)<br/>     | A container element for [**Activity**](activity.md) elements.<br/> <br/>                          |
| [**Issues**](issues.md)<br/>             | A container element for one or more issues.<br/> <br/>                                             |
| [**MetricValues**](metricvalues.md)<br/> | A container element for one or more [**MetricValue**](metricvalue.md) elements. <br/> <br/>       |
| [**Ordinal**](ordinal.md)<br/>           | Specifies the order in which **Iteration** nodes should appear in the Job Results file <br/> <br/> |
| [**TestCases**](testcases.md)<br/>       | A container for one or more [**TestCase**](testcase.md) elements.<br/> <br/>                      |
| [**Trace**](trace.md)<br/>               | An optional trace file associated with this iteration.<br/> <br/>                                  |



### Child element sequence

``` syntax
(
  Activities, 
  MetricValues, 
  Issues, 
  TestCases, 
  Ordinal, 
  Trace
)
```

## Parent elements



| Element                                     | Description                                                                           |
|---------------------------------------------|---------------------------------------------------------------------------------------|
| [**Iterations**](iterations.md)<br/> | This is a node that holds one or more &lt;Iteration&gt; nodes.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





