---
title: TestCase SetActivityReference method
description: Sets the activity reference of the TestCase.
ms.assetid: 624D34D7-BE30-466F-AE3F-11D0A672EFDD
keywords:
- SetActivityReference method Access Execution Engine
- SetActivityReference method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetActivityReference method
topic_type:
- apiref
api_name:
- TestCase.SetActivityReference
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

# TestCase::SetActivityReference method

Sets the activity reference of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetActivityReference(
  [in] LPCWSTR activityReference
) = 0;
```



## Parameters

<dl> <dt>

*activityReference* \[in\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





