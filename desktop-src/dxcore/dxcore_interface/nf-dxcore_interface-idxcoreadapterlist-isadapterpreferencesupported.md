---
title: IDXCoreAdapterList::IsAdapterPreferenceSupported
description: Determines whether a specified [DXCoreAdapterPreference](/windows/win32/api/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference) value is understood by the OS.
ms.topic: reference
ms.date: 09/03/2019
---

# IDXCoreAdapterList::IsAdapterPreferenceSupported method

## Description

Determines whether a specified [DXCoreAdapterPreference](/windows/win32/api/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference) value is understood by the current operating system (OS). You can call **IsAdapterPreferenceSupported** before calling [IDXCoreAdapterList::Sort](./nf-dxcore_interface-idxcoreadapterlist-sort.md).

## Syntax

```cpp
bool IsAdapterPreferenceSupported(
  DXCoreAdapterPreference preference
);
```

## Parameters

### preference

Type: **[DXCoreAdapterPreference](/windows/win32/api/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference)**

A [DXCoreAdapterPreference](/windows/win32/api/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference) value that will be checked to see whether it's supported by the OS.

## Returns

Type: **bool**

Returns `true` if the sort type is understood by the current OS. Otherwise, returns `false`.

## See also

[IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [DXCore reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
