---
title: IDXCoreAdapter::IsValid
description: Determines whether this DXCore adapter object is still valid.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::IsValid method

Determines whether this DXCore adapter object is still valid. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsValid() = 0;
```

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object is still valid. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
