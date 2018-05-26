---
title: Comparison element
description: Specifies how AXE compares metric values.
ms.assetid: 70DF348C-02CC-4C83-B107-001FA4A595DD
keywords:
- Comparison element Access Execution Engine
topic_type:
- apiref
api_name:
- Comparison
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Comparison element

Specifies how AXE compares metric values. This element maps to the [**MetricThresholdValueComparison**](metricthresholdvaluecomparison.md) enumeration.

## Usage

``` syntax
<Comparison>
  child elements
</Comparison>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Absolute**](absolute.md)<br/>                                         | Indicates that the [**MetricThreshold**](metricthreshold.md) target is not used and the [**MetricValue**](metricvalue.md) is compared directly with the [**MetricThresholdValue**](metricthresholdvalue.md). This is only valid for floating point and integral numeric types.<br/> <br/>                                                                                                                                                             |
| [**ContainsStringIsFail**](containsstringisfail.md)<br/>                 | Indicates that the **MetricValue** is considered to fail if the string contains the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings.<br/> <br/>                                                                                                                                                                                                                     |
| [**ContainsStringIsPass**](containsstringispass.md)<br/>                 | Indicates that the **MetricValue** is considered to pass if the string contains the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings.<br/> <br/>                                                                                                                                                                                                                     |
| [**FalseIsPass**](falseispass.md)<br/>                                   | Indicates that the **MetricValue** is considered to pass if its boolean value is **false**. This is valid for boolean, numeric and string types. For integral numeric types, zero is considered false, and non-zero is true. For floating point types, zero and NaN are considered false, and all other values true. For string types, false is assumed if the string is null, empty (zero length) or consists of all white space characters.<br/> <br/> |
| [**IsStringIsFail**](isstringisfail.md)<br/>                             | Indicates that the **MetricValue** is considered to fail if the **MetricValue** is a string or is not equivalent to the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings. This is only valid for string types.<br/> <br/>                                                                                                                                            |
| [**IsStringIsPass**](isstringispass.md)<br/>                             | Indicates that the **MetricValue** is considered to pass if the **MetricValue** is a string and is equivalent to the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings. This is only valid for string types.<br/> <br/>                                                                                                                                               |
| [**Offset**](offset.md)<br/>                                             | Indicates that the **MetricThresholdValue** is treated as an offset from the **MetricThreshold** target value. This is only valid for floating point and integral numeric types.<br/> <br/>                                                                                                                                                                                                                                                              |
| [**Percent**](percent.md)<br/>                                           | Indicates that the **MetricThresholdValue** is treated as a percent offset from the **MetricThreshold**. Target value. This is only valid for floating point and integral numeric types.<br/> <br/>                                                                                                                                                                                                                                                      |
| [**RegularExpressionMatchIsFail**](regularexpressionmatchisfail.md)<br/> | Indicates that the **MetricValue** is considered to fail if the **MetricValue** is a string matched by the regular expression in the **MetricThresholdValue**. This is only valid for string types.<br/> <br/>                                                                                                                                                                                                                                           |
| [**RegularExpressionMatchIsPass**](regularexpressionmatchispass.md)<br/> | Indicates that the **MetricValue** is considered to pass if the **MetricValue** is a string matched by the regular expression in the **MetricThresholdValue**. This is only valid for string types.<br/> <br/>                                                                                                                                                                                                                                           |
| [**TrueIsPass**](trueispass.md)<br/>                                     | Indicates that the **MetricValue** is considered to pass if its boolean value is **true**. This is valid for boolean, numeric and string types. For integral numeric types, zero is considered false, and non-zero is true. For floating point types, zero and NaN are considered false, and all other values true. For string types, false is assumed if the string is null, empty (zero length) or consists of all white space characters.<br/> <br/>  |



### Child element sequence

``` syntax
AbsoluteOffsetPercentTrueIsPassFalseIsPassContainsStringIsPassContainsStringIsFailIsStringIsPassIsStringIsFailRegularExpressionMatchIsPassRegularExpressionMatchIsFail
```

## Parent elements



| Element                                                         | Description                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**MetricThresholdValue**](metricthresholdvalue.md)<br/> | This node contains the data defining a metric threshold value.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





