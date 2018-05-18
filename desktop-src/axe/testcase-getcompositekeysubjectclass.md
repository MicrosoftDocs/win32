---
title: TestCase GetCompositeKeySubjectClass method
description: Returns the composite key subject class of the TestCase.
ms.assetid: '7AA75296-51F6-4029-8C45-A15D46F95499'
keywords: ["GetCompositeKeySubjectClass method Access Execution Engine", "GetCompositeKeySubjectClass method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetCompositeKeySubjectClass method"]
topic_type:
- apiref
api_name:
- TestCase.GetCompositeKeySubjectClass
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetCompositeKeySubjectClass method

Returns the composite key subject class of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetCompositeKeySubjectClass(
  [out] LPCWSTR *compositeKeySubjectClass
) const = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectClass* \[out\]
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

 

 





