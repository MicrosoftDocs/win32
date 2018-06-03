---
title: Issue AddCategory method
description: Creates and adds a category to the Issue.
ms.assetid: 4DB8846D-C771-44BD-B6EC-0554A34AA60C
keywords:
- AddCategory method Access Execution Engine
- AddCategory method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , AddCategory method
topic_type:
- apiref
api_name:
- Issue.AddCategory
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

# Issue::AddCategory method

Creates and adds a category to the **Issue**.

## Syntax


```C++
virtual HRESULT AddCategory(
  [in] LPCWSTR category
) = 0;
```



## Parameters

<dl> <dt>

*category* \[in\]
</dt> <dd>

The category.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The category is the value of element **Issue/Categories/Category**.

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

 

 





