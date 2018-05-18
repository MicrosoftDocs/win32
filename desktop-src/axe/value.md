---
title: Value element
description: This element contains a value.
ms.assetid: 'fa2a998d-b2fd-4884-894a-4b2566134a6e'
keywords: ["Value element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Value
api_type:
- Schema
---

# Value element

This element contains a value.

## Usage

``` syntax
<Value>
  text
</Value>
```

## Attributes

There are no attributes.

## Text value

One-line (200 characters) providing the value. This can be the value for the parameter or the value for the metric threshold. At job run time, the execution engine checks these values and returns an error for the assessment if the text cannot be converted to the specified parameter data type.

## Child elements

There are no child elements.

## Parent elements



| Element                                                         | Description                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**Flag**](flag.md)<br/>                                 | Describes a flag.<br/> <br/>                                              |
| [**MetricThresholdValue**](metricthresholdvalue.md)<br/> | This node contains the data defining a metric threshold value.<br/> <br/> |
| [**MetricValue**](metricvalue.md)<br/>                   | Describes a single metric value.<br/> <br/>                               |
| [**ParameterValue**](parametervalue.md)<br/>             | This element describes a single assessment parameter.<br/> <br/>          |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





