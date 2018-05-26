---
title: Issue GetIssueTitle method
description: Returns the title of the Issue.
ms.assetid: FB033F5D-BF7C-4D1B-BCBD-C22E91C9478C
keywords:
- GetIssueTitle method Access Execution Engine
- GetIssueTitle method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetIssueTitle method
topic_type:
- apiref
api_name:
- Issue.GetIssueTitle
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

# Issue::GetIssueTitle method

Returns the title of the **Issue**.

## Syntax


```C++
virtual HRESULT GetIssueTitle(
  [out] LPCWSTR *issueTitle
) const = 0;
```



## Parameters

<dl> <dt>

*issueTitle* \[out\]
</dt> <dd>

The title.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The title is the value of element **Issue/IssueTitle**.

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

 

 





