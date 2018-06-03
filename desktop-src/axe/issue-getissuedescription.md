---
title: Issue GetIssueDescription method
description: Returns the description of the Issue.
ms.assetid: AF65927E-F5B0-4179-B257-7FED0B1EC819
keywords:
- GetIssueDescription method Access Execution Engine
- GetIssueDescription method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetIssueDescription method
topic_type:
- apiref
api_name:
- Issue.GetIssueDescription
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

# Issue::GetIssueDescription method

Returns the description of the **Issue**.

## Syntax


```C++
virtual HRESULT GetIssueDescription(
  [out] LPCWSTR *issueDescription
) const = 0;
```



## Parameters

<dl> <dt>

*issueDescription* \[out\]
</dt> <dd>

The description.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The description is the value of element **Issue/IssueDescription**.

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

 

 





