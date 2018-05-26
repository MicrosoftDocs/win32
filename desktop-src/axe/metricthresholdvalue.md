---
title: MetricThresholdValue element
description: This node contains the data defining a metric threshold value.
ms.assetid: 45C2F19D-0B8F-44A6-B068-C79ED93F397E
keywords:
- MetricThresholdValue element Access Execution Engine
topic_type:
- apiref
api_name:
- MetricThresholdValue
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetricThresholdValue element

This node contains the data defining a metric threshold value.

## Usage

``` syntax
<MetricThresholdValue>
  child elements
</MetricThresholdValue>
```

## Attributes

There are no attributes.

## Child elements



| Element                                       | Description                                                                              |
|-----------------------------------------------|------------------------------------------------------------------------------------------|
| [**Comparison**](comparison.md)<br/>   | The value of this node maps to the AXE object model enumeration.<br/> <br/>  |
| [**Description**](description.md)<br/> | This node contains the description of the metric threshold value.<br/> <br/> |
| [**Inclusion**](https://msdn.microsoft.com/library/windows/desktop/hh437683)<br/>     | The value of this node maps to the AXE object model enumeration.<br/> <br/>  |
| [**Value**](value.md)<br/>             | This node contains the value for the metric threshold.<br/> <br/>            |
| [**ValueType**](valuetype.md)<br/>     | This node contains the type of the metric threshold value. <br/> <br/>       |



### Child element sequence

``` syntax
(
  Description, 
  ValueType, 
  Value, 
  Comparison, 
  Inclusion
)
```

## Parent elements



| Element                             | Description                                                             |
|-------------------------------------|-------------------------------------------------------------------------|
| [**Target**](target.md)<br/> | This is the target value for a metric threshold.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





