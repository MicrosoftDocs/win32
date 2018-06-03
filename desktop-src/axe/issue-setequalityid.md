---
title: Issue SetEqualityID method
description: Sets the equality ID of the Issue.
ms.assetid: DD00D1AD-DEFF-4AA1-9538-69BC2468AFA9
keywords:
- SetEqualityID method Access Execution Engine
- SetEqualityID method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetEqualityID method
topic_type:
- apiref
api_name:
- Issue.SetEqualityID
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

# Issue::SetEqualityID method

Sets the equality ID of the **Issue**.

## Syntax


```C++
virtual HRESULT SetEqualityID(
  [in] LPCWSTR equalityID
) = 0;
```



## Parameters

<dl> <dt>

*equalityID* \[in\]
</dt> <dd>

The equality ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The equality ID is the value of element **Issue/EqualityID**.

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

 

 





