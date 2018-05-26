---
title: Issue GetMetricValues method
description: Returns the MetricValueCollection of the Issue.
ms.assetid: BCF85EDB-2F76-4C39-B39B-18EEC1FE7D72
keywords:
- GetMetricValues method Access Execution Engine
- GetMetricValues method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetMetricValues method
topic_type:
- apiref
api_name:
- Issue.GetMetricValues
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

# Issue::GetMetricValues method

Returns the [**MetricValueCollection**](metricvaluecollection.md) of the **Issue**.

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

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The **MetricValueCollection** holds data from element **Issue/MetricValues**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





