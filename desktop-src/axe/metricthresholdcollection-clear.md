---
title: MetricThresholdCollection Clear method
description: Deletes all MetricThreshold objects from the MetricThresholdCollection.
ms.assetid: '8C7CFEB0-548F-4F47-A33A-85B8ACA08EBF'
keywords: ["Clear method Access Execution Engine", "Clear method Access Execution Engine , MetricThresholdCollection interface", "MetricThresholdCollection interface Access Execution Engine , Clear method"]
topic_type:
- apiref
api_name:
- MetricThresholdCollection.Clear
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdCollection::Clear method

Deletes all [**MetricThreshold**](metricthreshold-struct.md) objects from the **MetricThresholdCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

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

 

 





