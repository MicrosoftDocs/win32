---
title: TestCase SetCompositeKeySubjectInstance method
description: Sets the composite key subject instance of the TestCase.
ms.assetid: 'D1CC8E8D-9EA4-4772-BC3E-1D131EE27D34'
keywords: ["SetCompositeKeySubjectInstance method Access Execution Engine", "SetCompositeKeySubjectInstance method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , SetCompositeKeySubjectInstance method"]
topic_type:
- apiref
api_name:
- TestCase.SetCompositeKeySubjectInstance
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::SetCompositeKeySubjectInstance method

Sets the composite key subject instance of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetCompositeKeySubjectInstance(
  [in] LPCWSTR compositeKeySubjectInstance
) = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectInstance* \[in\]
</dt> <dd>

The composite key subject instance.

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

 

 





