---
title: Issue GetAffectedMetrics method
description: Returns the AffectedMetricCollection of the Issue.
ms.assetid: B089FF28-358A-4DE3-954A-553D4DF92BF4
keywords:
- GetAffectedMetrics method Access Execution Engine
- GetAffectedMetrics method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetAffectedMetrics method
topic_type:
- apiref
api_name:
- Issue.GetAffectedMetrics
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

# Issue::GetAffectedMetrics method

Returns the [**AffectedMetricCollection**](affectedmetriccollection.md) of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAffectedMetrics(
  [out] AffectedMetricCollection **affectedMetrics
) = 0;
```



## Parameters

<dl> <dt>

*affectedMetrics* \[out\]
</dt> <dd>

The **AffectedMetricCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The **AffectedMetricCollection** holds data from element **Issue/AffectedMetrics**.

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

 

 





