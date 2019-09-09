---
title: IDXCoreAdapterList::IsAdapterPreferenceSupported
description: Determines whether a specified [DXCoreAdapterPreference](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference) value is understood by the OS.
ms.localizationpriority: low
ms.topic: article
ms.date: 09/03/2019
---

# IDXCoreAdapterList::IsAdapterPreferenceSupported method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Determines whether a specified [DXCoreAdapterPreference](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference) value is understood by the current operating system (OS). You can call **IsAdapterPreferenceSupported** before calling [IDXCoreAdapterList::Sort](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterlist-sort).

## Syntax

```cpp
bool IsAdapterPreferenceSupported(
  DXCoreAdapterPreference preference
);
```

## Parameters

### preference

Type: **[DXCoreAdapterPreference](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference)**

A [DXCoreAdapterPreference](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterpreference) value that will be checked to see whether it's supported by the OS.

## Returns

Type: **bool**

Returns `true` if the sort type is understood by the current OS. Otherwise, returns `false`.

## See also

[IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)