---
title: TestCase SetCompositeKeyActivityInstance method
description: Sets the composite key activity instance of the TestCase.
ms.assetid: 8D703D5E-A7B1-4B64-9A0B-51F1CA449972
keywords:
- SetCompositeKeyActivityInstance method Access Execution Engine
- SetCompositeKeyActivityInstance method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetCompositeKeyActivityInstance method
topic_type:
- apiref
api_name:
- TestCase.SetCompositeKeyActivityInstance
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

# TestCase::SetCompositeKeyActivityInstance method

Sets the composite key activity instance of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetCompositeKeyActivityInstance(
  [in] LPCWSTR compositeKeyActivityInstance
) = 0;
```



## Parameters

<dl> <dt>

*compositeKeyActivityInstance* \[in\]
</dt> <dd>

The composite key activity instance.

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

 

 





