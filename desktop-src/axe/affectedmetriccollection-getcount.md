---
title: AffectedMetricCollection GetCount method
description: Returns the count of metric references in the AffectedMetricCollection.
ms.assetid: 2F3B89C5-7848-44ED-AEA0-C9911D9EB3FD
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , AffectedMetricCollection interface
- AffectedMetricCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- AffectedMetricCollection.GetCount
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

# AffectedMetricCollection::GetCount method

Returns the count of metric references in the **AffectedMetricCollection**.

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

An **AffectedMetricCollection** object holds data from element **Issue/AffectedMetrics**.

A metric reference is the value of an **Issue/AffectedMetrics/MetricReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**AffectedMetricCollection**](affectedmetriccollection.md)
</dt> </dl>

 

 





