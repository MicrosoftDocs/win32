---
title: TestCase GetToolTip method
description: Returns the tooltip of the TestCase.
ms.assetid: '0C46C6F0-C24A-4AD5-8C80-30E258D5A566'
keywords: ["GetToolTip method Access Execution Engine", "GetToolTip method Access Execution Engine , TestCase interface", "TestCase interface Access Execution Engine , GetToolTip method"]
topic_type:
- apiref
api_name:
- TestCase.GetToolTip
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCase::GetToolTip method

Returns the tooltip of the **TestCase.**

## Syntax


```C++
virtual HRESULT GetToolTip(
  [out] LPCWSTR *tooltip
) const = 0;
```



## Parameters

<dl> <dt>

*tooltip* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





