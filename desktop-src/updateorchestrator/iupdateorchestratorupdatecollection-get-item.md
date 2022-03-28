---
title: IUpdateOrchestratorUpdateCollection::get_Item method
description: Gets the update with the given index.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdateCollection::get_Item method

Gets the update with the given index.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdateCollection::get_Item(
        [in] ULONG ulIndex,
        [out, retval] IUpdateOrchestratorUpdate** update);

```
## Parameters

`ulIndex`

`update`


## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorUpdateCollection](iupdateorchestratorupdatecollection.md)

[IUpdateOrchestratorUpdateCollection::get_Count](iupdateorchestratorupdatecollection-get-count.md)