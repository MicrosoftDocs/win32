---
title: IDXCoreAdapter::IsAttributeSupported
description: Determines whether this DXCore adapter object supports the specified adapter attribute.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::IsAttributeSupported method

Determines whether this DXCore adapter object supports the specified adapter attribute.

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsAttributeSupported( 
  REFGUID attributeGUID) = 0;
```

## Parameters

### attributeGUID

Type: **REFGUID**

A reference to an adapter attribute GUID. For a list of attribute GUIDs, see [DXCore adapter attribute GUIDs](../dxcore-adapter-attribute-guids.md).

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object supports the specified adapter attribute. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [DXCore adapter attribute GUIDs](../dxcore-adapter-attribute-guids.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
