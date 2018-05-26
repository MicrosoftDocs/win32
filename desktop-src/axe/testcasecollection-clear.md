---
title: TestCaseCollection Clear method
description: Deletes all TestCase objects from the TestCaseCollection.
ms.assetid: 101BA829-05C9-415F-B73B-C6A71F975349
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , TestCaseCollection interface
- TestCaseCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- TestCaseCollection.Clear
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

# TestCaseCollection::Clear method

Deletes all [**TestCase**](testcase-struct.md) objects from the **TestCaseCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCaseCollection**](testcasecollection.md)
</dt> </dl>

 

 





