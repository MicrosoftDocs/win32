---
title: ResultSnippet GetIterations method
description: Returns a pointer to the IterationCollection object that contains the Iterations for this ResultSnippet object.
ms.assetid: B60BB4E8-A835-4413-85C1-D618E208D402
keywords:
- GetIterations method Access Execution Engine
- GetIterations method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , GetIterations method
topic_type:
- apiref
api_name:
- ResultSnippet.GetIterations
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

# ResultSnippet::GetIterations method

Returns a pointer to the [**IterationCollection**](iterationcollection.md) object that contains the [**Iteration**](iteration-struct.md)s for this [**ResultSnippet**](resultsnippet.md) object.

## Syntax


```C++
virtual HRESULT GetIterations(
  [out] IterationCollection **iterations
) = 0;
```



## Parameters

<dl> <dt>

*iterations* \[out\]
</dt> <dd>

A double pointer that receives the pointer to the [**IterationCollection**](iterationcollection.md) object.

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

 

 





