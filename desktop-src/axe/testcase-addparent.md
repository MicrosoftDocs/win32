---
title: TestCase AddParent method
description: Adds a parent to the TestCase.
ms.assetid: 37FFF787-07EB-4EBD-9CE6-DD933C1BE576
keywords:
- AddParent method Access Execution Engine
- AddParent method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , AddParent method
topic_type:
- apiref
api_name:
- TestCase.AddParent
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

# TestCase::AddParent method

Adds a parent to the **TestCase.**

## Syntax


```C++
virtual HRESULT AddParent(
  [in] LPCWSTR parent
) = 0;
```



## Parameters

<dl> <dt>

*parent* \[in\]
</dt> <dd>

The parent.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The parent is the value of element **TestCase/Parents/Parent**.

A **TestCase** should have only one parent.

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

 

 





