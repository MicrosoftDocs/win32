---
title: MetricThreshold SetTestCaseKey method
description: Sets the test case key of the MetricThreshold.
ms.assetid: 2A0DE72F-4DB7-4533-8505-FB4FF039BE96
keywords:
- SetTestCaseKey method Access Execution Engine
- SetTestCaseKey method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , SetTestCaseKey method
topic_type:
- apiref
api_name:
- MetricThreshold.SetTestCaseKey
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetricThreshold::SetTestCaseKey method

Sets the test case key of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT SetTestCaseKey(
  [in] LPCWSTR testCaseKey
) = 0;
```



## Parameters

<dl> <dt>

*testCaseKey* \[in\]
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

 

 





