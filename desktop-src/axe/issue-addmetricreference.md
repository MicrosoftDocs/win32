---
title: Issue AddMetricReference method
description: Creates and adds a metric reference to the Issue.
ms.assetid: '68B75CD4-5BE1-4D12-B38B-BDBA403427A1'
keywords: ["AddMetricReference method Access Execution Engine", "AddMetricReference method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , AddMetricReference method"]
topic_type:
- apiref
api_name:
- Issue.AddMetricReference
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::AddMetricReference method

Creates and adds a metric reference to the **Issue**.

## Syntax


```C++
virtual HRESULT AddMetricReference(
  [in] LPCWSTR metricReference
) = 0;
```



## Parameters

<dl> <dt>

*metricReference* \[in\]
</dt> <dd>

The metric reference.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The metric reference is the value of the **Issue/AffectedMetrics/MetricReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





