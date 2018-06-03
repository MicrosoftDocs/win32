---
title: TestCase SetSubject method
description: Sets the Subject of the TestCase.
ms.assetid: 656C077D-F35B-4109-B681-84BF94116D45
keywords:
- SetSubject method Access Execution Engine
- SetSubject method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetSubject method
topic_type:
- apiref
api_name:
- TestCase.SetSubject
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

# TestCase::SetSubject method

Sets the [**Subject**](subject.md) of the **TestCase**.

## Syntax


```C++
virtual HRESULT SetSubject(
  [in]            LPCWSTR className,
  [in, optional]  LPCWSTR instanceName,
  [out, optional] Subject **subject
) = 0;
```



## Parameters

<dl> <dt>

*className* \[in\]
</dt> <dd>

The class name of the **Subject**.

</dd> <dt>

*instanceName* \[in, optional\]
</dt> <dd>

The instance name of the **Subject**.

</dd> <dt>

*subject* \[out, optional\]
</dt> <dd>

The **Subject**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **Subject** holds information from element **TestCase/Subject**.

The class name is the value of element **TestCase/Subject/Class/ProgrammaticName**.

The instance name is the value of element **TestCase/Subject/Instance/ProgrammaticName**.

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

 

 





