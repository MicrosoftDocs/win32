---
title: DXCoreAdapterMemoryBudgetNodeSegmentGroup
description: Describes a memory segment group for an adapter.
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreAdapterMemoryBudgetNodeSegmentGroup structure

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

Specifies the device's physical adapter for which the adapter memory information is queried. For single-adapter operation, set this to zero. If there are multiple adapter nodes, then set this to the index of the node (the device's physical adapter) for which you want to query for adapter memory information (see [Multi-adapter systems](../../direct3d12/multi-engine.md)).

### segmentGroup

Type: **[DXCoreSegmentGroup](./ne-dxcore_interface-dxcoresegmentgroup.md)**

Specifies the adapter memory segment grouping that you want to query about.

## See also

[DXCore Reference](../dxcore-reference.md)

[Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)

[Multi-adapter systems](../../direct3d12/multi-engine.md)
