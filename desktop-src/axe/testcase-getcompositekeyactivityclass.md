---
title: TestCase GetCompositeKeyActivityClass method
description: Returns the composite key activity class of the TestCase.
ms.assetid: 1FBF582D-845F-41AF-921A-529648874B2A
keywords:
- GetCompositeKeyActivityClass method Access Execution Engine
- GetCompositeKeyActivityClass method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetCompositeKeyActivityClass method
topic_type:
- apiref
api_name:
- TestCase.GetCompositeKeyActivityClass
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

# TestCase::GetCompositeKeyActivityClass method

Returns the composite key activity class of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetCompositeKeyActivityClass(
  [out] LPCWSTR *compositeKeyActivityClass
) const = 0;
```



## Parameters

<dl> <dt>

*compositeKeyActivityClass* \[out\]
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

 

 





