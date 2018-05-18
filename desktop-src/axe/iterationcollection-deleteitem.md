---
title: IterationCollection DeleteItem method
description: Deletes an Iteration object from the collection.
ms.assetid: 'F9F3C897-1A80-43B2-89A8-6172AE2E21F3'
keywords: ["DeleteItem method Access Execution Engine", "DeleteItem method Access Execution Engine , IterationCollection interface", "IterationCollection interface Access Execution Engine , DeleteItem method"]
topic_type:
- apiref
api_name:
- IterationCollection.DeleteItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# IterationCollection::DeleteItem method

Deletes an [**Iteration**](iteration-struct.md) object from the collection.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The identifier of the [**Iteration**](iteration-struct.md) object.

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

 

 





