---
title: Issue GetClassProgrammaticName method
description: Returns the programmatic name of the class of the Issue.
ms.assetid: FDF72E13-4D2D-4858-9586-012D4CD009CC
keywords:
- GetClassProgrammaticName method Access Execution Engine
- GetClassProgrammaticName method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetClassProgrammaticName method
topic_type:
- apiref
api_name:
- Issue.GetClassProgrammaticName
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

# Issue::GetClassProgrammaticName method

Returns the programmatic name of the class of the **Issue**.

## Syntax


```C++
virtual HRESULT GetClassProgrammaticName(
  [out] LPCWSTR *classProgrammaticName
) const = 0;
```



## Parameters

<dl> <dt>

*classProgrammaticName* \[out\]
</dt> <dd>

The programmatic name of the class.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The programmatic name of the class is the value of element **Issue/Class/ProgrammaticName**.

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

 

 





