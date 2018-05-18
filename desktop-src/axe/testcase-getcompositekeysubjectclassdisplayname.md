---
title: TestCase GetCompositeKeySubjectClassDisplayName method
description: Returns the composite key subject class display name of the TestCase.
ms.assetid: '2487C9E4-36B4-4A4E-86E6-C5A09C51BA71'
keywords: ["GetCompositeKeySubjectClassDisplayName method Access Execution Engine", "GetCompositeKeySubjectClassDisplayName method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetCompositeKeySubjectClassDisplayName method"]
topic_type:
- apiref
api_name:
- TestCase.GetCompositeKeySubjectClassDisplayName
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetCompositeKeySubjectClassDisplayName method

Returns the composite key subject class display name of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetCompositeKeySubjectClassDisplayName(
  [out] LPCWSTR *compositeKeySubjectClassDisplayName
) const = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectClassDisplayName* \[out\]
</dt> <dd>

The composite key subject class display name.

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

 

 





