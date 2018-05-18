---
title: Iteration AddMetricValue methods
description: Creates and adds a MetricValue to the Iteration.
ms.assetid: 'C3149792-2521-4A9C-87FF-8B6B30CD3901'
keywords: ["AddMetricValue methods Access Execution Engine"]
topic_type:
- apiref
api_location:
- AxeCore.dll
api_type:
- DllExport
---

# Iteration::AddMetricValue methods

Creates and adds a [**MetricValue**](metricvalue-struct.md) to the **Iteration**.

### Overload list



| Method                                                                                   | Description                                                                   |
|:-----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**AddMetricValue(programmaticName,value,metricValue)**](iteration-addmetricvalue-1.md) | Creates and adds a **MetricValue** whose value is a **LPCWSTR**.<br/>   |
| [**AddMetricValue(programmaticName,value,metricValue)**](iteration-addmetricvalue-2.md) | Creates and adds a **MetricValue** whose value is an **INT**.<br/>      |
| [**AddMetricValue(programmaticName,value,metricValue)**](iteration-addmetricvalue-3.md) | Creates and adds a **MetricValue** whose value is a **UINT**.<br/>      |
| [**AddMetricValue(programmaticName,value,metricValue)**](iteration-addmetricvalue-4.md) | Creates and adds a **MetricValue** whose value is a **LONGLONG**.<br/>  |
| [**AddMetricValue(programmaticName,value,metricValue)**](iteration-addmetricvalue-5.md) | Creates and adds a **MetricValue** whose value is a **ULONGLONG**.<br/> |
| [**AddMetricValue(programmaticName,value,metricValue)**](iteration-addmetricvalue-6.md) | Creates and adds a **MetricValue** whose value is a **DOUBLE**.<br/>    |



## Remarks

The **MetricValue** objects hold information from the **Iteration/MetricValues/MetricValue** elements. The value that this method sets is the value of the **Iteration/MetricValues/MetricValue/Value** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





