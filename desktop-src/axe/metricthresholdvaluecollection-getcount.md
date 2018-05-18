---
title: MetricThresholdValueCollection GetCount method
description: Returns the count of MetricThresholdValue objects in the MetricThresholdValueCollection.
ms.assetid: 'D6D1CEC8-1C62-47EF-B5C6-1FCC53650C27'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , MetricThresholdValueCollection interface", "MetricThresholdValueCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- MetricThresholdValueCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdValueCollection::GetCount method

Returns the count of **MetricThresholdValue** objects in the **MetricThresholdValueCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
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

 

 





