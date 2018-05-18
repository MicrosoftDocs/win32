---
title: MetricValue SetProgrammaticName method
description: Sets the programmatic name of the MetricValue.
ms.assetid: '15934519-5F44-44A6-B5BD-75C4F1159D6B'
keywords: ["SetProgrammaticName method Access Execution Engine", "SetProgrammaticName method Access Execution Engine , MetricValue interface", "MetricValue interface Access Execution Engine , SetProgrammaticName method"]
topic_type:
- apiref
api_name:
- MetricValue.SetProgrammaticName
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricValue::SetProgrammaticName method

Sets the programmatic name of the **MetricValue**.

## Syntax


```C++
virtual HRESULT SetProgrammaticName(
  [in] LPCWSTR programmaticName
) = 0;
```



## Parameters

<dl> <dt>

*programmaticName* \[in\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricValue**](metricvalue-struct.md)
</dt> </dl>

 

 





