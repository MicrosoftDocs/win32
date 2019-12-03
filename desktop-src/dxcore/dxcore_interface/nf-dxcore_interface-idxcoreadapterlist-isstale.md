---
title: IDXCoreAdapterList::IsStale
description: Determines whether changes to this system have resulted in this DXCore adapter list object becoming out of date.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterList::IsStale method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Determines whether changes to this system have resulted in this DXCore adapter list object becoming out of date. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsStale() = 0;
```

## Returns

Type: **bool**

Returns `true` if, since generating the list, changes to system conditions have occurred that would cause this adapter list to become stale. Otherwise, returns `false`.

## Remarks

You can poll **IsStale** to determine whether changing system conditions have led to this list becoming out of date. If **IsStale** returns `true` once, then it returns `true` for the remaining lifetime of the DXCore adapter list object. A stale list object is still considered stale even if system conditions return to a state that matches the list (the same conditions obtain now as did when the list was first generated).

## See also

[IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
