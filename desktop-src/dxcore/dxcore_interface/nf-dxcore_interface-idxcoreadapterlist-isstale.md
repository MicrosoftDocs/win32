---
title: IDXCoreAdapterList::IsStale
description: Determines whether changes to this system have resulted in this DXCore adapter list object becoming out of date.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterList::IsStale method

Determines whether changes to this system have resulted in this DXCore adapter list object becoming out of date. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsStale() = 0;
```

## Returns

Type: **bool**

Returns `true` if, since generating the list, changes to system conditions have occurred that would cause this adapter list to become stale. Otherwise, returns `false`.

## Remarks

You can poll **IsStale** to determine whether changing system conditions have led to this list becoming out of date. If **IsStale** returns `true` once, then it returns `true` for the remaining lifetime of the DXCore adapter list object. A stale list object is still considered stale even if system conditions return to a state that matches the list (the same conditions obtain now as did when the list was first generated).

## See also

[IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
