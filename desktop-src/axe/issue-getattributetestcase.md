---
title: Issue GetAttributeTestCase method
description: Returns the test case of the Issue.
ms.assetid: 8AD4BD72-9BE7-424E-8C01-303A5F8AA7DF
keywords:
- GetAttributeTestCase method Access Execution Engine
- GetAttributeTestCase method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetAttributeTestCase method
topic_type:
- apiref
api_name:
- Issue.GetAttributeTestCase
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

# Issue::GetAttributeTestCase method

Returns the test case of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAttributeTestCase(
  [out] LPCWSTR *attributeTestCase
) const = 0;
```



## Parameters

<dl> <dt>

*attributeTestCase* \[out\]
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

 

 





