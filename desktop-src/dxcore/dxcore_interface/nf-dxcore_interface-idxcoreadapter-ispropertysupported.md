---
title: IDXCoreAdapter::IsPropertySupported
description: Determines whether this DXCore adapter object and the current operating system (OS) support the specified adapter property.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::IsPropertySupported method

Determines whether this DXCore adapter object and the current operating system (OS) support the specified adapter property.

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsPropertySupported( 
  DXCoreAdapterProperty property) = 0;
```

## Parameters

### property

Type: **[DXCoreAdapterProperty](./ne-dxcore_interface-dxcoreadapterproperty.md)**

The type of property that you're querying about support for. See the table in [DXCoreAdapterProperty](./ne-dxcore_interface-dxcoreadapterproperty.md) for more info about each adapter property.

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object and the current operating system (OS) support the specified adapter property. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [DXCore adapter attribute GUIDs](../dxcore-adapter-attribute-guids.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
