---
title: TestCase GetSubject method
description: Returns the Subject of the TestCase.
ms.assetid: B7E9774A-51EE-40AF-B7AC-3E782F6B9165
keywords:
- GetSubject method Access Execution Engine
- GetSubject method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetSubject method
topic_type:
- apiref
api_name:
- TestCase.GetSubject
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

# TestCase::GetSubject method

Returns the [**Subject**](subject.md) of the **TestCase**.

## Syntax


```C++
virtual HRESULT GetSubject(
  [out] Subject **subject
) = 0;
```



## Parameters

<dl> <dt>

*subject* \[out\]
</dt> <dd>

The **Subject**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **Subject** holds information from element **TestCase/Subject**.

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

 

 





