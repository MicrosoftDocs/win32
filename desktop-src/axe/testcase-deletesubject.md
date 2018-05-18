---
title: TestCase DeleteSubject method
description: Deletes the Subject from the TestCase.
ms.assetid: 'B9A4EF34-B7EE-4548-98BC-2879E96DDF88'
keywords: ["DeleteSubject method Access Execution Engine", "DeleteSubject method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , DeleteSubject method"]
topic_type:
- apiref
api_name:
- TestCase.DeleteSubject
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::DeleteSubject method

Deletes the [**Subject**](subject.md) from the **TestCase**.

## Syntax


```C++
virtual HRESULT DeleteSubject() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **Subject** holds information from element **TestCase/Subject**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





