---
title: Issue SetAttributeKnown method
description: Sets the value of attribute Known of the Issue.
ms.assetid: E5717D0B-527C-4F9C-902C-947AB1657029
keywords:
- SetAttributeKnown method Access Execution Engine
- SetAttributeKnown method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetAttributeKnown method
topic_type:
- apiref
api_name:
- Issue.SetAttributeKnown
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

# Issue::SetAttributeKnown method

Sets the value of attribute **Known** of the **Issue**.

## Syntax


```C++
virtual HRESULT SetAttributeKnown(
  [in] LPCWSTR attributeKnown
) = 0;
```



## Parameters

<dl> <dt>

*attributeKnown* \[in\]
</dt> <dd>

The value of attribute **Known**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

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

 

 





