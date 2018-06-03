---
title: Issue GetAttributeSummary method
description: Returns the summary of the Issue.
ms.assetid: 788EFB3C-D43F-4BD6-9FB3-7A53165C019A
keywords:
- GetAttributeSummary method Access Execution Engine
- GetAttributeSummary method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetAttributeSummary method
topic_type:
- apiref
api_name:
- Issue.GetAttributeSummary
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

# Issue::GetAttributeSummary method

Returns the summary of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAttributeSummary(
  [out] LPCWSTR *attributeSummary
) const = 0;
```



## Parameters

<dl> <dt>

*attributeSummary* \[out\]
</dt> <dd>

The summary.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The summary is attribute **Summary** of element **Issue**.

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

 

 





