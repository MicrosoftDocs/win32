---
title: AffectedMetricCollection AddItem method
description: Creates and adds a metric reference to the AffectedMetricCollection.
ms.assetid: '970DB2F0-95D1-4ACF-A531-76A76E986EE2'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , AffectedMetricCollection interface", "AffectedMetricCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- AffectedMetricCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# AffectedMetricCollection::AddItem method

Creates and adds a metric reference to the **AffectedMetricCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in] LPCWSTR metricReference
) = 0;
```



## Parameters

<dl> <dt>

*metricReference* \[in\]
</dt> <dd>

The metric reference.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

An **AffectedMetricCollection** object holds data from element **Issue/AffectedMetrics**.

A metric reference is the value of an **Issue/AffectedMetrics/MetricReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**AffectedMetricCollection**](affectedmetriccollection.md)
</dt> </dl>

 

 





