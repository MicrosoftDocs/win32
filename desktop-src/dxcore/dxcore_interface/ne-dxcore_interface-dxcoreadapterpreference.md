---
title: DXCoreAdapterPreference
description: Defines constants that specify DXCore adapter preferences to be used as list-sorting criteria.
ms.localizationpriority: low
ms.topic: reference
ms.date: 09/03/2019
---

# DXCoreAdapterPreference enum

## Description

Defines constants that specify DXCore adapter preferences to be used as list-sorting criteria. You can sort a DXCore adapter list by passing an array of **DXCoreAdapterPreference** to [IDXCoreAdapterList::Sort](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterlist-sort).

## Syntax

```cpp
enum class DXCoreAdapterPreference : uint32_t
{
  Hardware = 0,
  MinimumPower = 1,
  HighPerformance = 2
};
```

## Enum fields

### Hardware

Specifies a preference for hardware adapters (as opposed to software adapters).

### MinimumPower

Specifies a preference for the minimum-powered GPU (such as an integrated graphics processor, or iGPU).

### HighPerformance

Specifies a preference for the highest-performance GPU, such as an external graphics processor (xGPU), if available, or discrete graphics processor (dGPU) if available.

## See also

[IDXCoreAdapterList::Sort](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterlist-sort), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)