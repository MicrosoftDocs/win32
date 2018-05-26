---
title: IterationCollection GetItem method
description: Returns an Iteration object from the collection.
ms.assetid: F346DACC-E5F5-47E2-9C25-A8DBAAB1FCE4
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , IterationCollection interface
- IterationCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- IterationCollection.GetItem
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

# IterationCollection::GetItem method

Returns an [**Iteration**](iteration-struct.md) object from the collection.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT       index,
  [out] Iteration **iteration
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The identifier of the [**Iteration**](iteration-struct.md) object.

</dd> <dt>

*iteration* \[out\]
</dt> <dd>

The [**Iteration**](iteration-struct.md) object.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





