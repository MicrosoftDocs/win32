---
title: Iteration GetMetricValues method
description: Returns the MetricValueCollection for the Iteration.
ms.assetid: E342A576-4B46-401F-9047-1AF211A0077A
keywords:
- GetMetricValues method Access Execution Engine
- GetMetricValues method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , GetMetricValues method
topic_type:
- apiref
api_name:
- Iteration.GetMetricValues
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

# Iteration::GetMetricValues method

Returns the [**MetricValueCollection**](metricvaluecollection.md) for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetMetricValues(
  [out] MetricValueCollection **metricValues
) = 0;
```



## Parameters

<dl> <dt>

*metricValues* \[out\]
</dt> <dd>

The **MetricValueCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricValueCollection** holds information from element **Iteration/MetricValues**.

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

 

 





