---
title: TestCase GetCompositeKeySubjectInstance method
description: Returns the composite key subject instance of the TestCase.
ms.assetid: '96A45B07-1BE8-47DF-8B25-9162370794DF'
keywords: ["GetCompositeKeySubjectInstance method Access Execution Engine", "GetCompositeKeySubjectInstance method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetCompositeKeySubjectInstance method"]
topic_type:
- apiref
api_name:
- TestCase.GetCompositeKeySubjectInstance
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetCompositeKeySubjectInstance method

Returns the composite key subject instance of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetCompositeKeySubjectInstance(
  [out] LPCWSTR *compositeKeySubjectInstance
) const = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectInstance* \[out\]
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

 

 





