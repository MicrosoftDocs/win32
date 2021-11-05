---
title: IUpdateOrchestratorUpdateCollection::get_Count method
description: Gets the number of updates contained in the collection.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdateCollection::get_Count method

Gets the number of updates contained in the collection.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdateCollection::get_Count(
    [out, retval] ULONG* pcCount);
```

## Parameters

`pcCount`


## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorUpdateCollection](iupdateorchestratorupdatecollection.md)

[IUpdateOrchestratorUpdateCollection::get_Item](iupdateorchestratorupdatecollection-get-item.md)