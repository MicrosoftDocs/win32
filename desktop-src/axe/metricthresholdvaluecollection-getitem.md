---
title: MetricThresholdValueCollection GetItem method
description: Returns a MetricThresholdValue from the MetricThresholdValueCollection.
ms.assetid: '0A488F48-35B2-40AA-8B78-F931ED401290'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , MetricThresholdValueCollection interface", "MetricThresholdValueCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- MetricThresholdValueCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdValueCollection::GetItem method

Returns a **MetricThresholdValue** from the **MetricThresholdValueCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT                  index,
  [out] MetricThresholdValue **metricThresholdValue
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **MetricThresholdValue** identifier.

</dd> <dt>

*metricThresholdValue* \[out\]
</dt> <dd>

The **MetricThresholdValue**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

The **MetricThresholdValueCollection** holds data from element **MetricThreshold/MetricThresholdValues**.

The **MetricThresholdValue** elements hold data from **MetricThresholdValues/MetricThresholdValue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdValueCollection**](metricthresholdvaluecollection.md)
</dt> </dl>

 

 





