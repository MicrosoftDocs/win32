---
title: Issue SetIssueTitle method
description: Sets the title of the Issue.
ms.assetid: 777DE9DA-7AC0-4A02-B45D-CAF72B4FB9D7
keywords:
- SetIssueTitle method Access Execution Engine
- SetIssueTitle method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetIssueTitle method
topic_type:
- apiref
api_name:
- Issue.SetIssueTitle
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

# Issue::SetIssueTitle method

Sets the title of the **Issue**.

## Syntax


```C++
virtual HRESULT SetIssueTitle(
  [in] LPCWSTR issueTitle
) = 0;
```



## Parameters

<dl> <dt>

*issueTitle* \[in\]
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

 

 





