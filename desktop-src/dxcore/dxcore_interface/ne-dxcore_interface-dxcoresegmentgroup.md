---
title: DXCoreSegmentGroup
description: Defines constants that specify an adapter's memory segment grouping.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreSegmentGroup enum

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Defines constants that specify an adapter's memory segment grouping.

## Syntax

```cpp
enum class DXCoreSegmentGroup : uint32_t
{
  Local = 0,
  NonLocal = 1
};
```

## Constants

### Local

Specifies a grouping of segments that is considered local to the adapter, and represents the fastest memory available to the GPU. Your application should target the local segment group as the target size for its working set.

### NonLocal

Specifies a grouping of segments that is considered non-local to the adapter, and may have slower performance than the local segment group.

## See also

[DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)