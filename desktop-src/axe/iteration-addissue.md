---
title: Iteration AddIssue method
description: Creates and adds an Issue to the Iteration.
ms.assetid: BF8374CC-23FF-4292-822B-A595FCBE177B
keywords:
- AddIssue method Access Execution Engine
- AddIssue method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , AddIssue method
topic_type:
- apiref
api_name:
- Iteration.AddIssue
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

# Iteration::AddIssue method

Creates and adds an [**Issue**](issue-struct.md) to the **Iteration**.

## Syntax


```C++
virtual HRESULT AddIssue(
  [out] Issue **issue
) = 0;
```



## Parameters

<dl> <dt>

*issue* \[out\]
</dt> <dd>

The **Issue** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold information from the **Iteration/Issues/Issue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





