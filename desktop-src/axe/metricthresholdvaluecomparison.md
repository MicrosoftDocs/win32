---
title: MetricThresholdValueComparison enumeration
description: Specifies how AXE compares metric values.
ms.assetid: 65920F73-2A5F-4D51-A9F9-354FA0466FAD
keywords:
- MetricThresholdValueComparison enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- MetricThresholdValueComparison
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MetricThresholdValueComparison enumeration

Specifies how AXE compares metric values.

## Syntax


```C++
typedef enum _MetricThresholdValueComparison { 
  MetricThresholdValueComparison_NotSet                       = 0,
  MetricThresholdValueComparisonAbsolute,
  MetricThresholdValueComparisonOffset,
  MetricThresholdValueComparisonPercent,
  MetricThresholdValueComparisonTrueIsPass,
  MetricThresholdValueComparisonFalseIsPass,
  MetricThresholdValueComparisonContainsStringIsPass,
  MetricThresholdValueComparisonContainsStringIsFail,
  MetricThresholdValueComparisonIsStringIsPass,
  MetricThresholdValueComparisonIsStringIsFail,
  MetricThresholdValueComparisonRegularExpressionMatchIsPass,
  MetricThresholdValueComparisonRegularExpressionMatchIsFail,
  MetricThresholdValueComparison_Max
} MetricThresholdValueComparison;
```



## Constants

<dl> <dt>

<span id="MetricThresholdValueComparison_NotSet"></span><span id="metricthresholdvaluecomparison_notset"></span><span id="METRICTHRESHOLDVALUECOMPARISON_NOTSET"></span>**MetricThresholdValueComparison\_NotSet**
</dt> <dd>

No comparison method specified.

</dd> <dt>

<span id="MetricThresholdValueComparisonAbsolute"></span><span id="metricthresholdvaluecomparisonabsolute"></span><span id="METRICTHRESHOLDVALUECOMPARISONABSOLUTE"></span>**MetricThresholdValueComparisonAbsolute**
</dt> <dd>

Indicates that the [**MetricThreshold**](metricthreshold.md) target is not used and the [**MetricValue**](metricvalue.md) is compared directly with the [**MetricThresholdValue**](metricthresholdvalue.md). This is only valid for floating point and integral numeric types.

</dd> <dt>

<span id="MetricThresholdValueComparisonOffset"></span><span id="metricthresholdvaluecomparisonoffset"></span><span id="METRICTHRESHOLDVALUECOMPARISONOFFSET"></span>**MetricThresholdValueComparisonOffset**
</dt> <dd>

Indicates that the **MetricThresholdValue** is treated as an offset from the **MetricThreshold** target value. This is only valid for floating point and integral numeric types.

</dd> <dt>

<span id="MetricThresholdValueComparisonPercent"></span><span id="metricthresholdvaluecomparisonpercent"></span><span id="METRICTHRESHOLDVALUECOMPARISONPERCENT"></span>**MetricThresholdValueComparisonPercent**
</dt> <dd>

Indicates that the **MetricThresholdValue** is treated as a percent offset from the **MetricThreshold**. Target value. This is only valid for floating point and integral numeric types.

</dd> <dt>

<span id="MetricThresholdValueComparisonTrueIsPass"></span><span id="metricthresholdvaluecomparisontrueispass"></span><span id="METRICTHRESHOLDVALUECOMPARISONTRUEISPASS"></span>**MetricThresholdValueComparisonTrueIsPass**
</dt> <dd>

Indicates that the **MetricValue** is considered to pass if its boolean value is **true**. This is valid for boolean, numeric and string types. For integral numeric types, zero is considered false, and non-zero is true. For floating point types, zero and NaN are considered false, and all other values true. For string types, false is assumed if the string is null, empty (zero length) or consists of all white space characters.

</dd> <dt>

<span id="MetricThresholdValueComparisonFalseIsPass"></span><span id="metricthresholdvaluecomparisonfalseispass"></span><span id="METRICTHRESHOLDVALUECOMPARISONFALSEISPASS"></span>**MetricThresholdValueComparisonFalseIsPass**
</dt> <dd>

Indicates that the **MetricValue** is considered to pass if its boolean value is **false**. This is valid for boolean, numeric and string types. For integral numeric types, zero is considered false, and non-zero is true. For floating point types, zero and NaN are considered false, and all other values true. For string types, false is assumed if the string is null, empty (zero length) or consists of all white space characters.

</dd> <dt>

<span id="MetricThresholdValueComparisonContainsStringIsPass"></span><span id="metricthresholdvaluecomparisoncontainsstringispass"></span><span id="METRICTHRESHOLDVALUECOMPARISONCONTAINSSTRINGISPASS"></span>**MetricThresholdValueComparisonContainsStringIsPass**
</dt> <dd>

Indicates that the **MetricValue** is considered to pass if the string contains the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings.

</dd> <dt>

<span id="MetricThresholdValueComparisonContainsStringIsFail"></span><span id="metricthresholdvaluecomparisoncontainsstringisfail"></span><span id="METRICTHRESHOLDVALUECOMPARISONCONTAINSSTRINGISFAIL"></span>**MetricThresholdValueComparisonContainsStringIsFail**
</dt> <dd>

Indicates that the **MetricValue** is considered to fail if the string contains the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings.

</dd> <dt>

<span id="MetricThresholdValueComparisonIsStringIsPass"></span><span id="metricthresholdvaluecomparisonisstringispass"></span><span id="METRICTHRESHOLDVALUECOMPARISONISSTRINGISPASS"></span>**MetricThresholdValueComparisonIsStringIsPass**
</dt> <dd>

Indicates that the **MetricValue** is considered to pass if the **MetricValue** is a string and is equivalent to the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings. This is only valid for string types.

</dd> <dt>

<span id="MetricThresholdValueComparisonIsStringIsFail"></span><span id="metricthresholdvaluecomparisonisstringisfail"></span><span id="METRICTHRESHOLDVALUECOMPARISONISSTRINGISFAIL"></span>**MetricThresholdValueComparisonIsStringIsFail**
</dt> <dd>

Indicates that the **MetricValue** is considered to fail if the **MetricValue** is a string or is not equivalent to the **MetricThresholdValue**. String comparison is ordinal, insensitive to case, and ignores leading and trailing spaces in both strings. This is only valid for string types.

</dd> <dt>

<span id="MetricThresholdValueComparisonRegularExpressionMatchIsPass"></span><span id="metricthresholdvaluecomparisonregularexpressionmatchispass"></span><span id="METRICTHRESHOLDVALUECOMPARISONREGULAREXPRESSIONMATCHISPASS"></span>**MetricThresholdValueComparisonRegularExpressionMatchIsPass**
</dt> <dd>

Indicates that the **MetricValue** is considered to pass if the **MetricValue** is a string matched by the regular expression in the **MetricThresholdValue**. This is only valid for string types.

</dd> <dt>

<span id="MetricThresholdValueComparisonRegularExpressionMatchIsFail"></span><span id="metricthresholdvaluecomparisonregularexpressionmatchisfail"></span><span id="METRICTHRESHOLDVALUECOMPARISONREGULAREXPRESSIONMATCHISFAIL"></span>**MetricThresholdValueComparisonRegularExpressionMatchIsFail**
</dt> <dd>

Indicates that the **MetricValue** is considered to fail if the **MetricValue** is a string matched by the regular expression in the **MetricThresholdValue**. This is only valid for string types.

</dd> <dt>

<span id="MetricThresholdValueComparison_Max"></span><span id="metricthresholdvaluecomparison_max"></span><span id="METRICTHRESHOLDVALUECOMPARISON_MAX"></span>**MetricThresholdValueComparison\_Max**
</dt> <dd>

Invalid comparison specification (the value of this member is one larger than the largest valid member).

</dd> </dl>

## Remarks

This enumeration maps to the [**Comparison**](comparison.md) element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





