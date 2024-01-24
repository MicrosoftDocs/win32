---
title: IDXCoreAdapter
description: The **IDXCoreAdapter** interface implements methods for retrieving details about an adapter item.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter interface

The **IDXCoreAdapter** interface implements methods for retrieving details about an adapter item. **IDXCoreAdapter** inherits from the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Remarks

An adapter's properties are established at the time the adapter starts, and they're immutable for the lifetime of the adapter. This is in contrast to an adapter's state, which can be queried or set, and the values of which can change over time.

## See also

[DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
