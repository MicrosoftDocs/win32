---
title: Issue AddSolutionLink method
description: Creates and adds a solution Link to the Issue.
ms.assetid: '254C190C-A7A0-4AC7-AFA5-2A80F683356E'
keywords: ["AddSolutionLink method Access Execution Engine", "AddSolutionLink method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , AddSolutionLink method"]
topic_type:
- apiref
api_name:
- Issue.AddSolutionLink
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::AddSolutionLink method

Creates and adds a solution [**Link**](link-struct.md) to the **Issue**.

## Syntax


```C++
virtual HRESULT AddSolutionLink(
  [in, optional]  LPCWSTR solutionLinkTitle,
  [in, optional]  LPCWSTR solutionLinkValue,
  [out, optional] Link    **solutionLink
) = 0;
```



## Parameters

<dl> <dt>

*solutionLinkTitle* \[in, optional\]
</dt> <dd>

The solution link title.

</dd> <dt>

*solutionLinkValue* \[in, optional\]
</dt> <dd>

The solution link value, a URI.

</dd> <dt>

*solutionLink* \[out, optional\]
</dt> <dd>

The solution **Link** object that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The solution **Link** objects hold data from the **Issue/Solution/Links/Link** elements.

The solution link title is the value of element **Link/LinkTitle**.

The solution link value is the value of element **Link/LinkURI**.

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

 

 





