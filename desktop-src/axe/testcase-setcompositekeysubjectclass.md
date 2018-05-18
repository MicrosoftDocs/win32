---
title: TestCase SetCompositeKeySubjectClass method
description: Sets the composite key subject class of the TestCase.
ms.assetid: '46323094-E1A3-4B09-A372-012F0540B86A'
keywords: ["SetCompositeKeySubjectClass method Access Execution Engine", "SetCompositeKeySubjectClass method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , SetCompositeKeySubjectClass method"]
topic_type:
- apiref
api_name:
- TestCase.SetCompositeKeySubjectClass
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::SetCompositeKeySubjectClass method

Sets the composite key subject class of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetCompositeKeySubjectClass(
  [in] LPCWSTR compositeKeySubjectClass
) = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectClass* \[in\]
</dt> <dd>

The composite key subject class.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

This method is deprecated.

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

 

 





