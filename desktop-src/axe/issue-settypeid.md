---
title: Issue SetTypeID method
description: Sets the type ID of the Issue.
ms.assetid: 3B05C08A-D8CE-47AD-A360-EC9956C29A99
keywords:
- SetTypeID method Access Execution Engine
- SetTypeID method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetTypeID method
topic_type:
- apiref
api_name:
- Issue.SetTypeID
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

# Issue::SetTypeID method

Sets the type ID of the **Issue**.

## Syntax


```C++
virtual HRESULT SetTypeID(
  [in] LPCWSTR typeID
) = 0;
```



## Parameters

<dl> <dt>

*typeID* \[in\]
</dt> <dd>

The type ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The type ID is the value of element **Issue/TypeID**.

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

 

 





