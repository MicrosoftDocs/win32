---
title: AffectedMetricCollection Clear method
description: Deletes all metric references from the AffectedMetricCollection.
ms.assetid: 8A615655-91D1-4BFB-9086-D29556814BCA
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , AffectedMetricCollection interface
- AffectedMetricCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- AffectedMetricCollection.Clear
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

# AffectedMetricCollection::Clear method

Deletes all metric references from the **AffectedMetricCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

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

 

 





