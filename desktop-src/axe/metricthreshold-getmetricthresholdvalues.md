---
title: MetricThreshold GetMetricThresholdValues method
description: Returns the MetricThresholdValueCollection of the MetricThreshold.
ms.assetid: '589E89FD-4CC7-485E-8445-EB83F857E927'
keywords: ["GetMetricThresholdValues method Access Execution Engine", "GetMetricThresholdValues method Access Execution Engine , MetricThreshold interface", "MetricThreshold interface Access Execution Engine , GetMetricThresholdValues method"]
topic_type:
- apiref
api_name:
- MetricThreshold.GetMetricThresholdValues
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThreshold::GetMetricThresholdValues method

Returns the [**MetricThresholdValueCollection**](metricthresholdvaluecollection.md) of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT GetMetricThresholdValues(
  [out] MetricThresholdValueCollection **metricThresholdValues
) = 0;
```



## Parameters

<dl> <dt>

*metricThresholdValues* \[out\]
</dt> <dd>

The **MetricThresholdValueCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The **MetricThresholdValueCollection** holds data from element **MetricThreshold/MetricThresholdValues**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThreshold**](metricthreshold-struct.md)
</dt> </dl>

 

 





