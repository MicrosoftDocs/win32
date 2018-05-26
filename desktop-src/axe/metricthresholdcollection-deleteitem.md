---
title: MetricThresholdCollection DeleteItem method
description: Deletes a MetricThreshold from the MetricThresholdCollection.
ms.assetid: 0CA8A6D7-5331-45F0-8726-E3230A88B026
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , MetricThresholdCollection interface
- MetricThresholdCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- MetricThresholdCollection.DeleteItem
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

# MetricThresholdCollection::DeleteItem method

Deletes a [**MetricThreshold**](metricthreshold-struct.md) from the **MetricThresholdCollection**.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **MetricThreshold** identifier.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThresholdCollection** holds data from a **MetricThresholds** element.

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdCollection**](metricthresholdcollection.md)
</dt> </dl>

 

 





