---
title: TestCase GetParents method
description: Returns the ParentCollection of the TestCase.
ms.assetid: 'E8D99E9C-9433-4B17-A088-14463C7C9354'
keywords: ["GetParents method Access Execution Engine", "GetParents method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetParents method"]
topic_type:
- apiref
api_name:
- TestCase.GetParents
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetParents method

Returns the [**ParentCollection**](parentcollection.md) of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetParents(
  [out] ParentCollection **parents
) = 0;
```



## Parameters

<dl> <dt>

*parents* \[out\]
</dt> <dd>

The **ParentCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **ParentCollection** holds information from element **TestCase/Parents**.

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

 

 





