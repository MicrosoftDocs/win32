---
title: Subject SetClass method
description: Sets the class name of the Subject.
ms.assetid: 0C4BC81E-9518-4789-8F13-6C1D88CBEF88
keywords:
- SetClass method Access Execution Engine
- SetClass method Access Execution Engine , Subject interface
- Subject interface Access Execution Engine , SetClass method
topic_type:
- apiref
api_name:
- Subject.SetClass
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

# Subject::SetClass method

Sets the class name of the **Subject**.

## Syntax


```C++
virtual HRESULT SetClass(
  [in] LPCWSTR name
) = 0;
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The class name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Subject** objects hold information from the **Iteration/TestCases/TestCase/Subject** elements.

The class name is the value of element **Subject/Class/ProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Subject**](subject.md)
</dt> </dl>

 

 





