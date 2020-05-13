---
title: IDXCoreAdapter::IsAttributeSupported
description: Determines whether this DXCore adapter object supports the specified adapter attribute.
ms.localizationpriority: low
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

### attributeGUID

Type: **REFGUID**

A reference to an adapter attribute GUID. For a list of attribute GUIDs, see [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids).

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object supports the specified adapter attribute. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
