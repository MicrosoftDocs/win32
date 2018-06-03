---
title: Issue GetSolutionLinks method
description: Returns the solution LinkCollection of the Issue.
ms.assetid: B8C35072-8226-469E-89CD-B39C0592215B
keywords:
- GetSolutionLinks method Access Execution Engine
- GetSolutionLinks method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetSolutionLinks method
topic_type:
- apiref
api_name:
- Issue.GetSolutionLinks
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

# Issue::GetSolutionLinks method

Returns the solution [**LinkCollection**](linkcollection.md) of the **Issue**.

## Syntax


```C++
virtual HRESULT GetSolutionLinks(
  [out] LinkCollection **solutionLinks
) = 0;
```



## Parameters

<dl> <dt>

*solutionLinks* \[out\]
</dt> <dd>

The solution **LinkCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The solution **LinkCollection** holds data from element **Issue/Solution/Links**.

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

 

 





