---
title: Issue SetAttributeTestCase method
description: Sets the test case of the Issue.
ms.assetid: FE3173BB-39AC-40E1-B2CC-DF08B54BF690
keywords:
- SetAttributeTestCase method Access Execution Engine
- SetAttributeTestCase method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetAttributeTestCase method
topic_type:
- apiref
api_name:
- Issue.SetAttributeTestCase
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Issue::SetAttributeTestCase method

Sets the test case of the **Issue**.

## Syntax


```C++
virtual HRESULT SetAttributeTestCase(
  [in] LPCWSTR attributeTestCase
) = 0;
```



## Parameters

<dl> <dt>

*attributeTestCase* \[in\]
</dt> <dd>

The test case.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The test case is attribute **TestCase** of element **Issue**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





