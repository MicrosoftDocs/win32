---
title: TestCase SetKey method
description: Sets the key of the TestCase.
ms.assetid: 'ED88C71D-A943-4381-9E80-50A9E62088A5'
keywords: ["SetKey method Access Execution Engine", "SetKey method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , SetKey method"]
topic_type:
- apiref
api_name:
- TestCase.SetKey
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::SetKey method

Sets the key of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetKey(
  [in] LPCWSTR key
) = 0;
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

The key.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The key is the value of element **TestCase/Key**.

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

 

 





