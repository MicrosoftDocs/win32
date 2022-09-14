---
title: DXCoreAdapterMemoryBudget
description: Describes the memory budget for an adapter.
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreAdapterMemoryBudget structure

Specifies the <em>AdapterMemoryBudget</em> adapter state, which retrieves or requests the adapter memory budget on the adapter. Setting (requesting) a budget represents the minimum required physical memory to reserve, in bytes, on the adapter. We recommend that you set an adapter reservation in order to denote the amount of physical memory that your application can't go without. This value helps the operating system (OS) to quickly minimize the impact of large memory-pressure situations.

When calling [QueryState](./nf-dxcore_interface-idxcoreadapter-querystate.md), the <em>AdapterMemoryBudget</em> adapter state has type <a href="/windows/win32/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudgetnodesegmentgroup">DXCoreAdapterMemoryBudgetNodeSegmentGroup</a> for *inputStateDetails*, and type **DXCoreAdapterMemoryBudget** for *outputBuffer*.

When calling [SetState](./nf-dxcore_interface-idxcoreadapter-setstate.md), the <em>AdapterMemoryBudget</em> adapter state has type <a href="/windows/win32/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudgetnodesegmentgroup">DXCoreAdapterMemoryBudgetNodeSegmentGroup</a> for *inputStateDetails*, and type **uint64_t** for *inputData*.

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

### currentUsage

Type: **uint64_t**

Specifies your applicaton's current adapter memory usage, in bytes.

### availableForReservation

Type: **uint64_t**

Specifies the amount of adapter memory, in bytes, that your application has available for reservation. To reserve this adapter memory, your application should call [IDXCoreAdapter::SetState](./nf-dxcore_interface-idxcoreadapter-setstate.md) with *state* set to [DXCoreAdapterState::AdapterMemoryBudget](./ne-dxcore_interface-dxcoreadapterstate.md).

### currentReservation

Type: **uint64_t**

Specifies the amount of adapter memory, in bytes, that is reserved by your application. The OS uses the reservation as a hint to determine your application's minimum working set. Your application should attempt to ensure that its adapter memory usage can be trimmed to meet this requirement.

## See also

[DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
