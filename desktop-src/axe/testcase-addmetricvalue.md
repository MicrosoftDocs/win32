---
title: TestCase AddMetricValue methods
description: Creates and adds a MetricValue to the TestCase.
ms.assetid: 'D2E86EFB-11E8-4788-ACF4-64B237E0E248'
keywords: ["AddMetricValue methods Access Execution Engine"]
topic_type:
- apiref
api_location:
- AxeCore.dll
api_type:
- DllExport
---

# TestCase::AddMetricValue methods

Creates and adds a [**MetricValue**](metricvalue-struct.md) to the **TestCase**.

### Overload list



| Method                                                                                  | Description                                                                   |
|:----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**AddMetricValue(programmaticName,value,metricValue)**](testcase-addmetricvalue-1.md) | Creates and adds a **MetricValue** whose value is a **LPCWSTR**.<br/>   |
| [**AddMetricValue(programmaticName,value,metricValue)**](testcase-addmetricvalue-2.md) | Creates and adds a **MetricValue** whose value is an **INT**.<br/>      |
| [**AddMetricValue(programmaticName,value,metricValue)**](testcase-addmetricvalue-3.md) | Creates and adds a **MetricValue** whose value is a **UINT**.<br/>      |
| [**AddMetricValue(programmaticName,value,metricValue)**](testcase-addmetricvalue-4.md) | Creates and adds a **MetricValue** whose value is a **LONGLONG**.<br/>  |
| [**AddMetricValue(programmaticName,value,metricValue)**](testcase-addmetricvalue-5.md) | Creates and adds a **MetricValue** whose value is a **ULONGLONG**.<br/> |
| [**AddMetricValue(programmaticName,value,metricValue)**](testcase-addmetricvalue-6.md) | Creates and adds a **MetricValue** whose value is a **DOUBLE**.<br/>    |



## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **MetricValue** objects hold information from the **TestCase/MetricValues/MetricValue** elements. The value that this method sets is the value of the **TestCase/MetricValues/MetricValue/Value** element.

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

 

 





