---
title: TestCase AddIssue method
description: Creates and adds an Issue to the TestCase.
ms.assetid: A79A53E5-A81A-4770-A332-383111C94E6D
keywords:
- AddIssue method Access Execution Engine
- AddIssue method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , AddIssue method
topic_type:
- apiref
api_name:
- TestCase.AddIssue
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

# TestCase::AddIssue method

Creates and adds an [**Issue**](issue-struct.md) to the **TestCase**.

## Syntax


```C++
virtual HRESULT AddIssue(
  [out] Issue **issue
) = 0;
```



## Parameters

<dl> <dt>

*issue* \[out\]
</dt> <dd>

The **Issue** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **Issue** objects hold information from the **TestCase/Issues/Issue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





