---
title: IterationCollection AddItem method
description: Creates an Iteration and adds it to the collection.
ms.assetid: '09FE6A0C-F5CA-4969-81C3-4441D2636865'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , IterationCollection interface", "IterationCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- IterationCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# IterationCollection::AddItem method

Creates an [**Iteration**](iteration-struct.md) and adds it to the collection.

## Syntax


```C++
virtual HRESULT AddItem(
  [out] Iteration **iteration
) = 0;
```



## Parameters

<dl> <dt>

*iteration* \[out\]
</dt> <dd>

The [**Iteration**](iteration-struct.md) that was added.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IterationCollection**](iterationcollection.md)
</dt> </dl>

 

 





