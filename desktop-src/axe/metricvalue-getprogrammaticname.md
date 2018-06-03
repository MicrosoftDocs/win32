---
title: MetricValue GetProgrammaticName method
description: Returns the programmatic name of the MetricValue.
ms.assetid: E979A5D1-C4A8-4464-8C9C-5851E16095A8
keywords:
- GetProgrammaticName method Access Execution Engine
- GetProgrammaticName method Access Execution Engine , MetricValue interface
- MetricValue interface Access Execution Engine , GetProgrammaticName method
topic_type:
- apiref
api_name:
- MetricValue.GetProgrammaticName
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MetricValue::GetProgrammaticName method

Returns the programmatic name of the **MetricValue**.

## Syntax


```C++
virtual HRESULT GetProgrammaticName(
  [out] LPCWSTR *programmaticName
) const = 0;
```



## Parameters

<dl> <dt>

*programmaticName* \[out\]
</dt> <dd>

The programmatic name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricValue** object holds data from an **Issue/MetricValues/MetricValue**, **Iteration/MetricValues/MetricValue**, or **TestCase/MetricValues/MetricValue** element.

The programmatic name is the value of element **MetricValue/ProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricValue**](metricvalue-struct.md)
</dt> </dl>

 

 





