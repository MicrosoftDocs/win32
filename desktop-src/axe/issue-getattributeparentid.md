---
title: Issue GetAttributeParentID method
description: Returns the parent ID of the Issue.
ms.assetid: 0E1C5DF1-C298-43B1-BEC9-8832DE36E51C
keywords:
- GetAttributeParentID method Access Execution Engine
- GetAttributeParentID method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetAttributeParentID method
topic_type:
- apiref
api_name:
- Issue.GetAttributeParentID
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

# Issue::GetAttributeParentID method

Returns the parent ID of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAttributeParentID(
  [out] LPCWSTR *attributeParentID
) const = 0;
```



## Parameters

<dl> <dt>

*attributeParentID* \[out\]
</dt> <dd>

The parent ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The parent ID is attribute **parentID** of element **Issue**.

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

 

 





