---
title: TestCase element
description: An individual test.
ms.assetid: 8AD4BD72-9BE7-424E-8C01-303A5F8AA7DF
keywords:
- TestCase element Access Execution Engine
topic_type:
- apiref
api_name:
- TestCase
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TestCase element

An individual test.

## Usage

``` syntax
<TestCase>
  child elements
</TestCase>
```

## Attributes

There are no attributes.

## Child elements



| Element                                         | Description                                                                                             |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Issues**](issues.md)<br/>             | A container element for one or more issues.<br/> <br/>                                      |
| [**Key**](key.md)<br/>                   | Identifies all the metrics under this test case.<br/> <br/>                                 |
| [**MetricValues**](metricvalues.md)<br/> | A container element for one or more [**MetricValue**](metricvalue.md) elements.<br/> <br/> |



### Child element sequence

``` syntax
(
  MetricValues, 
  Issues, 
  Key
)
```

## Parent elements



| Element                                   | Description                                                               |
|-------------------------------------------|---------------------------------------------------------------------------|
| [**TestCases**](testcases.md)<br/> | A container for one or more **TestCase** elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





