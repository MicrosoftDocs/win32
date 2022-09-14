---
title: DXCoreHardwareID
description: Represents the PnP hardware ID parts for an adapter.
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreHardwareID structure

Represents the PnP hardware ID parts for an adapter.

## Syntax

```cpp
struct DXCoreHardwareID
{
  uint32_t vendorID;
  uint32_t deviceID;
  uint32_t subSysID;
  uint32_t revision;
};
```

## Members

### vendorId

Type: **uint32_t\***

The PCI ID of the adapter's hardware vendor.

### deviceId

Type: **uint32_t\***

The PCI ID of the adapter's hardware device.

### subSysId

Type: **uint32_t\***

The PCI ID of the adapter's hardware subsystem.

### revision

Type: **uint32_t\***

The PCI ID of the adapter's revision number.

## See also

[DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
