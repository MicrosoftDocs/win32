---
title: IDXCoreAdapter
description: The **IDXCoreAdapter** interface implements methods for retrieving details about an adapter item.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **IDXCoreAdapter** interface implements methods for retrieving details about an adapter item. **IDXCoreAdapter** inherits from the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Remarks

An adapter's properties are established at the time the adapter starts, and they're immutable for the lifetime of the adapter. This is in contrast to an adapter's state, which can be queried or set, and the values of which can change over time.

## See also

[DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)