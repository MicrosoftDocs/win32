---
title: MetricThreshold GetMetricDefinitionProgrammaticName method
description: Returns the metric definition programmatic name of the MetricThreshold.
ms.assetid: F3BD33B7-6F2F-4F7B-9EEE-CEBCC1B07B9F
keywords:
- GetMetricDefinitionProgrammaticName method Access Execution Engine
- GetMetricDefinitionProgrammaticName method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , GetMetricDefinitionProgrammaticName method
topic_type:
- apiref
api_name:
- MetricThreshold.GetMetricDefinitionProgrammaticName
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

# MetricThreshold::GetMetricDefinitionProgrammaticName method

Returns the metric definition programmatic name of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT GetMetricDefinitionProgrammaticName(
  [out] LPCWSTR *metricDefinitionProgrammaticName
) const = 0;
```



## Parameters

<dl> <dt>

*metricDefinitionProgrammaticName* \[out\]
</dt> <dd>

The metric definition programmatic name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The metric definition programmatic name is the value of element **MetricThreshold/MetricDefinitionProgrammaticName**.

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

 

 





