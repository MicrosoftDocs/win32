---
title: TestCase GetKey method
description: Returns the key of the TestCase.
ms.assetid: BA1E3724-F36E-477D-830B-12CC1B049408
keywords:
- GetKey method Access Execution Engine
- GetKey method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetKey method
topic_type:
- apiref
api_name:
- TestCase.GetKey
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TestCase::GetKey method

Returns the key of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetKey(
  [out] LPCWSTR *key
) const = 0;
```



## Parameters

<dl> <dt>

*key* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





