---
title: MetricThreshold GetTestCaseKey method
description: Returns the test case key of the MetricThreshold.
ms.assetid: F20B3055-333D-4025-BC1F-423C67B9F97B
keywords:
- GetTestCaseKey method Access Execution Engine
- GetTestCaseKey method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , GetTestCaseKey method
topic_type:
- apiref
api_name:
- MetricThreshold.GetTestCaseKey
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

# MetricThreshold::GetTestCaseKey method

Returns the test case key of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT GetTestCaseKey(
  [out] LPCWSTR *testCaseKey
) const = 0;
```



## Parameters

<dl> <dt>

*testCaseKey* \[out\]
</dt> <dd>

The test case key.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The test case key is the value of element **MetricThreshold/TestCaseKey**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThreshold**](metricthreshold-struct.md)
</dt> </dl>

 

 





