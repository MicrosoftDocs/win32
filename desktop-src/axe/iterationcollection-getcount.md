---
title: IterationCollection GetCount method
description: Returns the count of Iteration objects in the collection.
ms.assetid: C25751AF-EAC7-4384-B178-A5964D351553
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , IterationCollection interface
- IterationCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- IterationCollection.GetCount
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

# IterationCollection::GetCount method

Returns the count of [**Iteration**](iteration-struct.md) objects in the collection.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The count of [**Iteration**](iteration-struct.md) objects.

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

[**IterationCollection**](iterationcollection.md)
</dt> </dl>

 

 





