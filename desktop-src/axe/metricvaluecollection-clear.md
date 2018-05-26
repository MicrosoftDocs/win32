---
title: MetricValueCollection Clear method
description: Deletes all MetricValue objects from the MetricValueCollection.
ms.assetid: 6E3A3024-0063-41AD-B932-A3852401BFB9
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , MetricValueCollection interface
- MetricValueCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- MetricValueCollection.Clear
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

# MetricValueCollection::Clear method

Deletes all [**MetricValue**](metricvalue-struct.md) objects from the **MetricValueCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

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

 

 





