---
title: TestCase SetToolTip method
description: Sets the tooltip of the TestCase.
ms.assetid: CE126280-9144-41B3-85C3-82A057A81E23
keywords:
- SetToolTip method Access Execution Engine
- SetToolTip method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetToolTip method
topic_type:
- apiref
api_name:
- TestCase.SetToolTip
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

# TestCase::SetToolTip method

Sets the tooltip of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetToolTip(
  [in] LPCWSTR tooltip
) = 0;
```



## Parameters

<dl> <dt>

*tooltip* \[in\]
</dt> <dd>

The tooltip.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The tooltip is the value of element **TestCase/ToolTip**.

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

 

 





