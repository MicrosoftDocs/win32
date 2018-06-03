---
title: TestCase AddMetricValue method
description: Creates and adds a MetricValue whose value is a UINT.
ms.assetid: 24B3BD46-5B33-44D5-B32C-01A87A2959F8
keywords:
- AddMetricValue method Access Execution Engine
- AddMetricValue method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , AddMetricValue method
topic_type:
- apiref
api_name:
- TestCase.AddMetricValue
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

# TestCase::AddMetricValue method

Creates and adds a [**MetricValue**](metricvalue-struct.md) whose value is a **UINT**.

## Syntax


```C++
virtual HRESULT AddMetricValue(
  [in]  LPCWSTR     programmaticName,
  [in]  UINT        value,
  [out] MetricValue **metricValue
) = 0;
```



## Parameters

<dl> <dt>

*programmaticName* \[in\]
</dt> <dd>

The programmatic name.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The value.

</dd> <dt>

*metricValue* \[out\]
</dt> <dd>

The **MetricValue** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **MetricValue** objects hold information from the **TestCase/MetricValues/MetricValue** elements. The value that this method sets is the value of the **TestCase/MetricValues/MetricValue/Value** element.

The programmatic name is the value of element **MetricValue/ProgrammaticName**.

The value is the value of element **MetricValue/Value**.

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

 

 





