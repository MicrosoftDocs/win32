---
title: DXCoreSegmentGroup
description: Defines constants that specify an adapter's memory segment grouping.
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreSegmentGroup enum

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

[DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
