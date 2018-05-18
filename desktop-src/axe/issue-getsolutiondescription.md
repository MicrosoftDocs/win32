---
title: Issue GetSolutionDescription method
description: Returns the solution description of the Issue.
ms.assetid: 'AB490B90-5B33-41F0-AC94-4CF3C787D6A6'
keywords: ["GetSolutionDescription method Access Execution Engine", "GetSolutionDescription method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , GetSolutionDescription method"]
topic_type:
- apiref
api_name:
- Issue.GetSolutionDescription
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::GetSolutionDescription method

Returns the solution description of the **Issue**.

## Syntax


```C++
virtual HRESULT GetSolutionDescription(
  [out] LPCWSTR *solutionDescription
) const = 0;
```



## Parameters

<dl> <dt>

*solutionDescription* \[out\]
</dt> <dd>

The solution description.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The solution description is the value of element **Issue/Solution/Description**.

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

 

 





