---
title: IDXCoreAdapterList::GetAdapterCount
description: Retrieves the number of adapters in a DXCore adapter list object.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterList::GetAdapterCount method

Retrieves the number of adapters in a DXCore adapter list object. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Syntax

```cpp
virtual uint32_t STDMETHODCALLTYPE GetAdapterCount() = 0;
```

## Returns

Type: **uint32_t**

Returns the number of adapter items in the list.

## See also

[IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
