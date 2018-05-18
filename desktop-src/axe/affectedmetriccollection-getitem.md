---
title: AffectedMetricCollection GetItem method
description: Returns a metric reference from the AffectedMetricCollection.
ms.assetid: '077FA405-B473-431D-9994-6BEAD5906A77'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , AffectedMetricCollection interface", "AffectedMetricCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- AffectedMetricCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# AffectedMetricCollection::GetItem method

Returns a metric reference from the **AffectedMetricCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT     index,
  [out] LPCWSTR *metricReference
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The metric reference identifier.

</dd> <dt>

*metricReference* \[out\]
</dt> <dd>

The metric reference.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





