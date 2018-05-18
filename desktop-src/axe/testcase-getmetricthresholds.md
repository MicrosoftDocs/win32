---
title: TestCase GetMetricThresholds method
description: Returns the MetricThresholdCollection for the TestCase.
ms.assetid: 'D00EB39B-D93F-498A-9F2B-3C3F49E00ECF'
keywords: ["GetMetricThresholds method Access Execution Engine", "GetMetricThresholds method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetMetricThresholds method"]
topic_type:
- apiref
api_name:
- TestCase.GetMetricThresholds
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetMetricThresholds method

Returns the [**MetricThresholdCollection**](metricthresholdcollection.md) for the **TestCase**.

## Syntax


```C++
virtual HRESULT GetMetricThresholds(
  [out] MetricThresholdCollection **metricThresholds
) = 0;
```



## Parameters

<dl> <dt>

*metricThresholds* \[out\]
</dt> <dd>

The **MetricThresholdCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **MetricThresholdCollection** holds information from element **TestCase/MetricThresholds**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





