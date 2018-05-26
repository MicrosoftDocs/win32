---
title: Issue GetEqualityID method
description: Returns the equality ID of the Issue.
ms.assetid: C17FEFBA-7C36-405C-B5BF-1DBD66E9BE91
keywords:
- GetEqualityID method Access Execution Engine
- GetEqualityID method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetEqualityID method
topic_type:
- apiref
api_name:
- Issue.GetEqualityID
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

# Issue::GetEqualityID method

Returns the equality ID of the **Issue**.

## Syntax


```C++
virtual HRESULT GetEqualityID(
  [out] LPCWSTR *equalityID
) const = 0;
```



## Parameters

<dl> <dt>

*equalityID* \[out\]
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

 

 





