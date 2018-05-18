---
title: TestCaseCollection GetCount method
description: Returns the count of TestCase objects in the TestCaseCollection.
ms.assetid: 'F2796971-C399-4B89-9211-A98AE90AD2B5'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , TestCaseCollection interface", "TestCaseCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- TestCaseCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCaseCollection::GetCount method

Returns the count of [**TestCase**](testcase-struct.md) objects in the **TestCaseCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The count.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCaseCollection**](testcasecollection.md)
</dt> </dl>

 

 





