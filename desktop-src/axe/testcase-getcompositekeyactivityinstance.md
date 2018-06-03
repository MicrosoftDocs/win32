---
title: TestCase GetCompositeKeyActivityInstance method
description: Returns the composite key activity instance of the TestCase.
ms.assetid: 05431C6B-B76F-46EE-94C9-78426E5FAA6B
keywords:
- GetCompositeKeyActivityInstance method Access Execution Engine
- GetCompositeKeyActivityInstance method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetCompositeKeyActivityInstance method
topic_type:
- apiref
api_name:
- TestCase.GetCompositeKeyActivityInstance
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

# TestCase::GetCompositeKeyActivityInstance method

Returns the composite key activity instance of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetCompositeKeyActivityInstance(
  [out] LPCWSTR *compositeKeyActivityInstance
) const = 0;
```



## Parameters

<dl> <dt>

*compositeKeyActivityInstance* \[out\]
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

 

 





