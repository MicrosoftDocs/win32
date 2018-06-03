---
title: Issue GetAttributeID method
description: Returns the ID of the Issue.
ms.assetid: 849FCC62-F432-4066-8B9D-A8ACBD7414B3
keywords:
- GetAttributeID method Access Execution Engine
- GetAttributeID method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetAttributeID method
topic_type:
- apiref
api_name:
- Issue.GetAttributeID
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

# Issue::GetAttributeID method

Returns the ID of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAttributeID(
  [out] LPCWSTR *attributeID
) const = 0;
```



## Parameters

<dl> <dt>

*attributeID* \[out\]
</dt> <dd>

The ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The ID is attribute **ID** of element **Issue**.

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

 

 





