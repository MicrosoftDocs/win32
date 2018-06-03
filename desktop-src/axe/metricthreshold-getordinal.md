---
title: MetricThreshold GetOrdinal method
description: Returns the ordinal of the MetricThreshold.
ms.assetid: 46251675-01E7-49EC-9A6A-85442490F110
keywords:
- GetOrdinal method Access Execution Engine
- GetOrdinal method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , GetOrdinal method
topic_type:
- apiref
api_name:
- MetricThreshold.GetOrdinal
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

# MetricThreshold::GetOrdinal method

Returns the ordinal of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT GetOrdinal(
  [out] UINT *ordinal
) const = 0;
```



## Parameters

<dl> <dt>

*ordinal* \[out\]
</dt> <dd>

The ordinal.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The ordinal is the value of element **MetricThreshold/Ordinal**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThreshold**](metricthreshold-struct.md)
</dt> </dl>

 

 





