---
title: IDXCoreAdapter::IsQueryStateSupported
description: Determines whether this DXCore adapter object and the current operating system (OS) support querying the value of the specified adapter state.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::IsQueryStateSupported method

Determines whether this DXCore adapter object and the current operating system (OS) support querying the value of the specified adapter state.

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsQueryStateSupported( 
  DXCoreAdapterState property) = 0;
```

## Parameters

### state

Type: **[DXCoreAdapterState](/windows/win32/api/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate)**

The kind of state item that you're querying about support for. See the table in [DXCoreAdapterState](/windows/win32/api/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about each adapter state kind.

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object and the current operating system (OS) support querying the specified adapter state. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore reference](../dxcore-reference.md), [DXCore adapter attribute GUIDs](../dxcore-adapter-attribute-guids.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
