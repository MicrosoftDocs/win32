---
title: MetricValueCollection GetItem method
description: Returns a MetricValue from the MetricValueCollection.
ms.assetid: F4CEAB50-ACD6-4533-94B4-48B1A921E270
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , MetricValueCollection interface
- MetricValueCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- MetricValueCollection.GetItem
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

# MetricValueCollection::GetItem method

Returns a [**MetricValue**](metricvalue-struct.md) from the **MetricValueCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT         index,
  [out] MetricValue **metricValue
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **MetricValue** identifier.

</dd> <dt>

*metricValue* \[out\]
</dt> <dd>

The **MetricValue**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

A **MetricValueCollection** holds data from an **Issue/MetricValues**, **Iteration/MetricValues**, or **TestCase/MetricValues** element.

A **MetricValue** object holds data from a **MetricValues/MetricValue** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricValueCollection**](metricvaluecollection.md)
</dt> </dl>

 

 





