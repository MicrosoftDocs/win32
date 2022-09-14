---
title: IDXCoreAdapter::IsValid
description: Determines whether this DXCore adapter object is still valid.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::IsValid method

Determines whether this DXCore adapter object is still valid. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsValid() = 0;
```

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object is still valid. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
