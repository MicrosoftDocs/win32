---
title: Issue SetIssueToolTip method
description: Sets the tooltip of the Issue.
ms.assetid: '12EC811A-693A-41E1-9C45-8B66627E3A71'
keywords: ["SetIssueToolTip method Access Execution Engine", "SetIssueToolTip method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , SetIssueToolTip method"]
topic_type:
- apiref
api_name:
- Issue.SetIssueToolTip
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::SetIssueToolTip method

Sets the tooltip of the **Issue**.

## Syntax


```C++
virtual HRESULT SetIssueToolTip(
  [in] LPCWSTR issueToolTip
) = 0;
```



## Parameters

<dl> <dt>

*issueToolTip* \[in\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





