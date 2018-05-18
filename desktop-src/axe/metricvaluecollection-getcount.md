---
title: MetricValueCollection GetCount method
description: Returns a count of the MetricValue objects in the MetricValueCollection.
ms.assetid: '194A706B-5C58-40D9-8DF6-DD2B119DF720'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , MetricValueCollection interface", "MetricValueCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- MetricValueCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricValueCollection::GetCount method

Returns a count of the [**MetricValue**](metricvalue-struct.md) objects in the **MetricValueCollection**.

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

A **MetricValueCollection** holds data from an **Issue/MetricValues**, **Iteration/MetricValues**, or **TestCase/MetricValues** element.

A **MetricValue** object holds data from a **MetricValues/MetricValue** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricValueCollection**](metricvaluecollection.md)
</dt> </dl>

 

 





