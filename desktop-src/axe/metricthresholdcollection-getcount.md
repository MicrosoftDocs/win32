---
title: MetricThresholdCollection GetCount method
description: Returns the count of MetricThreshold objects in the MetricThresholdCollection.
ms.assetid: F1EA165E-D2D7-4FF0-91F3-7F508EE83DEC
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , MetricThresholdCollection interface
- MetricThresholdCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- MetricThresholdCollection.GetCount
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

# MetricThresholdCollection::GetCount method

Returns the count of [**MetricThreshold**](metricthreshold-struct.md) objects in the **MetricThresholdCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The count.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThresholdCollection** holds data from a **MetricThresholds** element.

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdCollection**](metricthresholdcollection.md)
</dt> </dl>

 

 





