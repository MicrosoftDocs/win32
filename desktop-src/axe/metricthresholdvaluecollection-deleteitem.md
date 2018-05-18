---
title: MetricThresholdValueCollection DeleteItem method
description: Deletes a MetricThresholdValue from the MetricThresholdValueCollection.
ms.assetid: 'D1053F7C-90FB-4BEC-876A-7859F745D8E2'
keywords: ["DeleteItem method Access Execution Engine", "DeleteItem method Access Execution Engine , MetricThresholdValueCollection interface", "MetricThresholdValueCollection interface Access Execution Engine , DeleteItem method"]
topic_type:
- apiref
api_name:
- MetricThresholdValueCollection.DeleteItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdValueCollection::DeleteItem method

Deletes a **MetricThresholdValue** from the **MetricThresholdValueCollection**.

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

The **MetricThresholdValue** identifier.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

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

 

 





