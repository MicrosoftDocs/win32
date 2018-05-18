---
title: AffectedMetricCollection DeleteItem method
description: Deletes a metric reference from the AffectedMetricCollection.
ms.assetid: 'BD911704-9C34-41CC-B53A-6ECB39F436EA'
keywords: ["DeleteItem method Access Execution Engine", "DeleteItem method Access Execution Engine , AffectedMetricCollection interface", "AffectedMetricCollection interface Access Execution Engine , DeleteItem method"]
topic_type:
- apiref
api_name:
- AffectedMetricCollection.DeleteItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# AffectedMetricCollection::DeleteItem method

Deletes a metric reference from the **AffectedMetricCollection**.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The metric reference identifier.

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

 

 





