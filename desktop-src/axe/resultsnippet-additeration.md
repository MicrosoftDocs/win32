---
title: ResultSnippet AddIteration method
description: Creates and returns an Iteration for use by this ResultSnippet object.
ms.assetid: 242F8A09-54AD-4566-AD8C-5C8F57E1EF92
keywords:
- AddIteration method Access Execution Engine
- AddIteration method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , AddIteration method
topic_type:
- apiref
api_name:
- ResultSnippet.AddIteration
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

# ResultSnippet::AddIteration method

Creates and returns an [**Iteration**](iteration.md) for use by this [**ResultSnippet**](resultsnippet.md) object.

## Syntax


```C++
virtual HRESULT AddIteration(
  [out] Iteration **iteration
) = 0;
```



## Parameters

<dl> <dt>

*iteration* \[out\]
</dt> <dd>

A double pointer that receives a pointer to the created [**Iteration**](resultsnippet-getiterations.md).

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ResultSnippet**](resultsnippet.md)
</dt> </dl>

 

 





