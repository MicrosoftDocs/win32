---
title: MetricValue SetValue method
description: Sets a value of type DOUBLE to the MetricValue.
ms.assetid: 1FA01E9A-C913-49FA-80F4-230784DD7A98
keywords:
- SetValue method Access Execution Engine
- SetValue method Access Execution Engine , MetricValue interface
- MetricValue interface Access Execution Engine , SetValue method
topic_type:
- apiref
api_name:
- MetricValue.SetValue
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

# MetricValue::SetValue method

Sets a value of type **DOUBLE** to the **MetricValue**.

## Syntax


```C++
virtual HRESULT SetValue(
  [in] DOUBLE value
) const = 0;
```



## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

The value.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricValue** object holds data from an **Issue/MetricValues/MetricValue**, **Iteration/MetricValues/MetricValue**, or **TestCase/MetricValues/MetricValue** element.

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

[**MetricValue**](metricvalue-struct.md)
</dt> </dl>

 

 





