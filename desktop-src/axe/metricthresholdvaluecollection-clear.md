---
title: MetricThresholdValueCollection Clear method
description: Deletes all MetricThresholdValue objects from the MetricThresholdValueCollection.
ms.assetid: EC5AEC77-79C7-4BD7-830F-74014D49E47E
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , MetricThresholdValueCollection interface
- MetricThresholdValueCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- MetricThresholdValueCollection.Clear
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

# MetricThresholdValueCollection::Clear method

Deletes all **MetricThresholdValue** objects from the **MetricThresholdValueCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValueCollection** holds data from element **MetricThreshold/MetricThresholdValues**.

The **MetricThresholdValue** elements hold data from **MetricThresholdValues/MetricThresholdValue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdValueCollection**](metricthresholdvaluecollection.md)
</dt> </dl>

 

 





