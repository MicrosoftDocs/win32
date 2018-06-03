---
title: Issue SetSolutionDescription method
description: Sets the solution description of the Issue.
ms.assetid: 75F533D6-7494-427B-B8CE-A6E1149327D7
keywords:
- SetSolutionDescription method Access Execution Engine
- SetSolutionDescription method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetSolutionDescription method
topic_type:
- apiref
api_name:
- Issue.SetSolutionDescription
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

# Issue::SetSolutionDescription method

Sets the solution description of the **Issue**.

## Syntax


```C++
virtual HRESULT SetSolutionDescription(
  [in] LPCWSTR solutionDescription
) = 0;
```



## Parameters

<dl> <dt>

*solutionDescription* \[in\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





