---
title: TestCase SetCompositeKeyActivityClass method
description: Sets the composite key activity class of the TestCase.
ms.assetid: 6FA63565-1102-4537-AD92-509425672EA9
keywords:
- SetCompositeKeyActivityClass method Access Execution Engine
- SetCompositeKeyActivityClass method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetCompositeKeyActivityClass method
topic_type:
- apiref
api_name:
- TestCase.SetCompositeKeyActivityClass
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

# TestCase::SetCompositeKeyActivityClass method

Sets the composite key activity class of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetCompositeKeyActivityClass(
  [in] LPCWSTR compositeKeyActivityClass
) = 0;
```



## Parameters

<dl> <dt>

*compositeKeyActivityClass* \[in\]
</dt> <dd>

The composite key activity class.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

This method is deprecated.

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

 

 





