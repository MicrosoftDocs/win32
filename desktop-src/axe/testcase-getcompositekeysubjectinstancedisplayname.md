---
title: TestCase GetCompositeKeySubjectInstanceDisplayName method
description: Returns the composite key subject instance display name of the TestCase.
ms.assetid: '5490210C-BC1C-407E-894C-D59601F3894D'
keywords: ["GetCompositeKeySubjectInstanceDisplayName method Access Execution Engine", "GetCompositeKeySubjectInstanceDisplayName method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetCompositeKeySubjectInstanceDisplayName method"]
topic_type:
- apiref
api_name:
- TestCase.GetCompositeKeySubjectInstanceDisplayName
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetCompositeKeySubjectInstanceDisplayName method

Returns the composite key subject instance display name of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetCompositeKeySubjectInstanceDisplayName(
  [out] LPCWSTR *compositeKeySubjectInstanceDisplayName
) const = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectInstanceDisplayName* \[out\]
</dt> <dd>

The composite key subject instance display name.

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

 

 





