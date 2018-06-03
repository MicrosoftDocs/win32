---
title: Issue AddMetricValue method
description: Creates and adds a MetricValue whose value is a UINT.
ms.assetid: D1F9645F-927D-4A3B-973F-FCBF372E434B
keywords:
- AddMetricValue method Access Execution Engine
- AddMetricValue method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , AddMetricValue method
topic_type:
- apiref
api_name:
- Issue.AddMetricValue
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

# Issue::AddMetricValue method

Creates and adds a [**MetricValue**](metricvalue-struct.md) whose value is a **UINT**.

## Syntax


```C++
virtual HRESULT AddMetricValue(
  [in]            LPCWSTR     programmaticName,
  [in]            UINT        value,
  [out, optional] MetricValue **metricValue
) = 0;
```



## Parameters

<dl> <dt>

*programmaticName* \[in\]
</dt> <dd>

The programmatic name.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The value.

</dd> <dt>

*metricValue* \[out, optional\]
</dt> <dd>

The **MetricValue** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The programmatic name is the value of element **MetricValue/ProgrammaticName**.

The value is the value of element **MetricValue/Value**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





