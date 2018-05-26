---
title: MetricThreshold SetMetricDefinitionProgrammaticName method
description: Sets the metric definition programmatic name of the MetricThreshold.
ms.assetid: 175E583B-00B4-4CEB-9914-F489DB7E27FD
keywords:
- SetMetricDefinitionProgrammaticName method Access Execution Engine
- SetMetricDefinitionProgrammaticName method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , SetMetricDefinitionProgrammaticName method
topic_type:
- apiref
api_name:
- MetricThreshold.SetMetricDefinitionProgrammaticName
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

# MetricThreshold::SetMetricDefinitionProgrammaticName method

Sets the metric definition programmatic name of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT SetMetricDefinitionProgrammaticName(
  [in] LPCWSTR metricDefinitionProgrammaticName
) = 0;
```



## Parameters

<dl> <dt>

*metricDefinitionProgrammaticName* \[in\]
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

 

 





