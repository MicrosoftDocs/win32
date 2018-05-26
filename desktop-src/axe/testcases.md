---
title: TestCases element
description: A container for one or more TestCase elements. TestCases enables multiple metrics to apply to a single item.
ms.assetid: 8B377587-9150-49BA-AABC-E6DC219E2DD9
keywords:
- TestCases element Access Execution Engine
topic_type:
- apiref
api_name:
- TestCases
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TestCases element

A container for one or more [**TestCase**](testcase.md) elements. **TestCases** enables multiple metrics to apply to a single item. For example, a driver verification assessment could use multiple tests to verify a given driver.

## Usage

``` syntax
<TestCases>
  child elements
</TestCases>
```

## Attributes

There are no attributes.

## Child elements



| Element                                 | Description                                |
|-----------------------------------------|--------------------------------------------|
| [**TestCase**](testcase.md)<br/> | An individual test.<br/> <br/> |



### Child element sequence

``` syntax
TestCase
```

## Parent elements



| Element                                   | Description                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------|
| [**Iteration**](iteration.md)<br/> | Receives metric values for a single assessment iteration.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





