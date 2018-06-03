---
title: MetricThreshold SetTarget method
description: Sets the target of the MetricThreshold.
ms.assetid: DF3CDAAA-599D-4332-9E41-6293E21DDC8C
keywords:
- SetTarget method Access Execution Engine
- SetTarget method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , SetTarget method
topic_type:
- apiref
api_name:
- MetricThreshold.SetTarget
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

# MetricThreshold::SetTarget method

Sets the target of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT SetTarget(
  [in] LPCWSTR target
) = 0;
```



## Parameters

<dl> <dt>

*target* \[in\]
</dt> <dd>

The target.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The target is the value of element **MetricThreshold/Target**.

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

 

 





