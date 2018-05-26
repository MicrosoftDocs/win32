---
title: MetricValue GetValue method
description: Returns the value of the MetricValue for a type ULONGLONG value.
ms.assetid: 132C8F89-D246-4024-A075-B253D98737F2
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetricValue::GetValue method

Returns the value of the **MetricValue** for a type **ULONGLONG** value.

## Syntax


```C++
virtual HRESULT GetValue(
  [out] ULONGLONG *value
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

 

 





