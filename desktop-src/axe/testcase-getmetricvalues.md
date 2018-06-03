---
title: TestCase GetMetricValues method
description: Returns the MetricValueCollection of the TestCase.
ms.assetid: 3278FE5D-217A-496F-8973-6EC3C19B0134
keywords:
- GetMetricValues method Access Execution Engine
- GetMetricValues method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetMetricValues method
topic_type:
- apiref
api_name:
- TestCase.GetMetricValues
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TestCase::GetMetricValues method

Returns the [**MetricValueCollection**](metricvaluecollection.md) of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetMetricValues(
  [out] MetricValueCollection **metricValues
) const = 0;
```



## Parameters

<dl> <dt>

*metricValues* \[out\]
</dt> <dd>

The **MetricValueCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **MetricValueCollection** holds information from element **TestCase/MetricValues**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





