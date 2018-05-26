---
title: TestCase GetName method
description: Returns the name of the TestCase.
ms.assetid: D2D0748E-0923-47D1-BB72-06B9E449AF9C
keywords:
- GetName method Access Execution Engine
- GetName method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetName method
topic_type:
- apiref
api_name:
- TestCase.GetName
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

# TestCase::GetName method

Returns the name of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetName(
  [out] LPCWSTR *name
) const = 0;
```



## Parameters

<dl> <dt>

*name* \[out\]
</dt> <dd>

The name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The name is the value of element **TestCase/Name**.

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

 

 





