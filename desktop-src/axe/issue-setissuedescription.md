---
title: Issue SetIssueDescription method
description: Sets the description of the Issue.
ms.assetid: 9143F307-2CE2-41A8-8229-67AFDB0D7284
keywords:
- SetIssueDescription method Access Execution Engine
- SetIssueDescription method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetIssueDescription method
topic_type:
- apiref
api_name:
- Issue.SetIssueDescription
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

# Issue::SetIssueDescription method

Sets the description of the **Issue**.

## Syntax


```C++
virtual HRESULT SetIssueDescription(
  [in] LPCWSTR issueDescription
) = 0;
```



## Parameters

<dl> <dt>

*issueDescription* \[in\]
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

 

 





