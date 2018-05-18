---
title: Issue AddMetricValue methods
description: Creates and adds a MetricValue to the Issue.
ms.assetid: '8CEC3D70-A064-42DF-8B4D-FDAAFB8BF0B8'
keywords: ["AddMetricValue methods Access Execution Engine"]
topic_type:
- apiref
api_location:
- AxeCore.dll
api_type:
- DllExport
---

# Issue::AddMetricValue methods

Creates and adds a [**MetricValue**](metricvalue-struct.md) to the **Issue**.

### Overload list



| Method                                                                               | Description                                                                   |
|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**AddMetricValue(programmaticName,value,metricValue)**](issue-addmetricvalue-1.md) | Creates and adds a **MetricValue** whose value is a **LPCWSTR**.<br/>   |
| [**AddMetricValue(programmaticName,value,metricValue)**](issue-addmetricvalue-2.md) | Creates and adds a **MetricValue** whose value is an **INT**.<br/>      |
| [**AddMetricValue(programmaticName,value,metricValue)**](issue-addmetricvalue-3.md) | Creates and adds a **MetricValue** whose value is a **UINT**.<br/>      |
| [**AddMetricValue(programmaticName,value,metricValue)**](issue-addmetricvalue-4.md) | Creates and adds a **MetricValue** whose value is a **LONGLONG**.<br/>  |
| [**AddMetricValue(programmaticName,value,metricValue)**](issue-addmetricvalue-5.md) | Creates and adds a **MetricValue** whose value is a **ULONGLONG**.<br/> |
| [**AddMetricValue(programmaticName,value,metricValue)**](issue-addmetricvalue-6.md) | Creates and adds a **MetricValue** whose value is a **DOUBLE**.<br/>    |



## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The **MetricValue** objects hold data from the **Issue/MetricValues/MetricValue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





