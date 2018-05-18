---
title: MetricThresholdCollection GetItem method
description: Returns a MetricThreshold from the MetricThresholdCollection.
ms.assetid: '0DC862B6-5565-4DAD-BA08-3FDC77C55335'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , MetricThresholdCollection interface", "MetricThresholdCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- MetricThresholdCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdCollection::GetItem method

Returns a [**MetricThreshold**](metricthreshold-struct.md) from the **MetricThresholdCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT             index,
  [out] MetricThreshold **metricThreshold
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **MetricThreshold** identifier.

</dd> <dt>

*metricThreshold* \[out\]
</dt> <dd>

The **MetricThreshold**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

A **MetricThresholdCollection** holds data from a **MetricThresholds** element.

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdCollection**](metricthresholdcollection.md)
</dt> </dl>

 

 





