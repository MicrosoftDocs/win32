---
title: Iteration AddMetricThreshold method
description: Creates and adds a MetricThreshold to the Iteration.
ms.assetid: D5D1C1D6-4483-4650-95E8-7E619CF6BC9D
keywords:
- AddMetricThreshold method Access Execution Engine
- AddMetricThreshold method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , AddMetricThreshold method
topic_type:
- apiref
api_name:
- Iteration.AddMetricThreshold
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

# Iteration::AddMetricThreshold method

Creates and adds a [**MetricThreshold**](metricthreshold-struct.md) to the **Iteration**.

## Syntax


```C++
virtual HRESULT AddMetricThreshold(
  [in]            LPCWSTR         descriptionProgrammaticName,
  [in]            LPCWSTR         metricDefinitionProgrammaticName,
  [out, optional] MetricThreshold **metricThreshold
) = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[in\]
</dt> <dd>

The description programmatic name.

</dd> <dt>

*metricDefinitionProgrammaticName* \[in\]
</dt> <dd>

The metric definition programmatic name.

</dd> <dt>

*metricThreshold* \[out, optional\]
</dt> <dd>

The **MetricThreshold** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThreshold** objects hold information from the **Iteration/MetricThresholds/MetricThreshold** elements.

The description programmatic name is the value of element **Iteration/MetricThresholds/MetricThreshold/Description**.

The metric definition programmatic name is the value of element **Iteration/MetricThresholds/MetricThreshold/MetricDefintionProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





