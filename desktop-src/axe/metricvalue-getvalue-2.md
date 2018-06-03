---
title: MetricValue GetValue method
description: Returns the value of the MetricValue for a type INT value.
ms.assetid: AE8A8C2F-72C1-41FA-B1FB-AA877F04706E
keywords:
- GetValue method Access Execution Engine
- GetValue method Access Execution Engine , MetricValue interface
- MetricValue interface Access Execution Engine , GetValue method
topic_type:
- apiref
api_name:
- MetricValue.GetValue
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

# MetricValue::GetValue method

Returns the value of the **MetricValue** for a type **INT** value.

## Syntax


```C++
virtual HRESULT GetValue(
  [out] INT *value
) const = 0;
```



## Parameters

<dl> <dt>

*value* \[out\]
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

 

 





