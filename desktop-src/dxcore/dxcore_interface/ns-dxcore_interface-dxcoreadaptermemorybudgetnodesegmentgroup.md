---
title: DXCoreAdapterMemoryBudgetNodeSegmentGroup
description: Describes a memory segment group for an adapter.
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# DXCoreAdapterMemoryBudgetNodeSegmentGroup structure

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Describes a memory segment group for an adapter.

## Syntax

```cpp
struct DXCoreAdapterMemoryBudgetNodeSegmentGroup
{
  uint32_t nodeIndex;
  DXCoreSegmentGroup segmentGroup;
};
```

## Members

### nodeIndex

Type: **uint32_t**

Specifies the device's physical adapter for which the adapter memory information is queried. For single-adapter operation, set this to zero. If there are multiple adapter nodes, then set this to the index of the node (the device's physical adapter) for which you want to query for adapter memory information (see [Multi-adapter systems](/windows/win32/direct3d12/multi-engine)).

### segmentGroup

Type: **[DXCoreSegmentGroup](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoresegmentgroup)**

Specifies the adapter memory segment grouping that you want to query about.

## See also

[DXCore Reference](/windows/win32/dxcore/dxcore-reference)

[Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

[Multi-adapter systems](/windows/win32/direct3d12/multi-engine)