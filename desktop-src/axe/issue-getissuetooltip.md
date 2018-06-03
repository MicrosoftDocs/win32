---
title: Issue GetIssueToolTip method
description: Returns the tooltip of the Issue.
ms.assetid: CB605DED-1756-40DA-9DD8-328B4DB04EA4
keywords:
- GetIssueToolTip method Access Execution Engine
- GetIssueToolTip method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetIssueToolTip method
topic_type:
- apiref
api_name:
- Issue.GetIssueToolTip
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

# Issue::GetIssueToolTip method

Returns the tooltip of the **Issue**.

## Syntax


```C++
virtual HRESULT GetIssueToolTip(
  [out] LPCWSTR *issueToolTip
) const = 0;
```



## Parameters

<dl> <dt>

*issueToolTip* \[out\]
</dt> <dd>

The tooltip.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The tooltip is the value of element **Issue/IssueToolTip**.

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

 

 





