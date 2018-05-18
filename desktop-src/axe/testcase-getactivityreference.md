---
title: TestCase GetActivityReference method
description: Returns the activity reference of the TestCase.
ms.assetid: '6BAE8DAC-394E-4A20-84DE-8FFE562250CB'
keywords: ["GetActivityReference method Access Execution Engine", "GetActivityReference method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetActivityReference method"]
topic_type:
- apiref
api_name:
- TestCase.GetActivityReference
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetActivityReference method

Returns the activity reference of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetActivityReference(
  [out] LPCWSTR *activityReference
) const = 0;
```



## Parameters

<dl> <dt>

*activityReference* \[out\]
</dt> <dd>

The activity reference.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The activity reference is the value of element **TestCase/ActivityReference**.

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

 

 





