---
title: DXCoreAdapterMemoryBudget
description: Describes the memory budget for an adapter.
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# DXCoreAdapterMemoryBudget structure

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Describes the memory budget for an adapter.

## Syntax

```cpp
struct DXCoreAdapterMemoryBudget
{
  uint64_t budget;
  uint64_t currentUsage;
  uint64_t availableForReservation;
  uint64_t currentReservation;
};
```

## Members

### budget

Type: **uint64_t**

Specifies the OS-provided adapter memory budget, in bytes, that your application should target. If *currentUsage* is greater than *budget*, then your application may incur stuttering or performance penalties due to background activity by the OS, which is intended to provide other applications with a fair usage of adapter memory.

### budget

Type: **uint64_t**

Specifies your applicaton's current adapter memory usage, in bytes.

### availableForReservation

Type: **uint64_t**

Specifies the amount of adapter memory, in bytes, that your application has available for reservation. To reserve this adapter memory, your application should call [IDXCoreAdapter::SetState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate) with *state* set to [DXCoreAdapterState::AdapterMemoryBudget](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate).

### availableForReservation

Type: **uint64_t**

Specifies the amount of adapter memory, in bytes, that is reserved by your application. The OS uses the reservation as a hint to determine your application's minimum working set. Your application should attempt to ensure that its adapter memory usage can be trimmed to meet this requirement.

## See also

[DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)