---
title: DXCoreAdapterState
description: Defines constants that specify kinds of DXCore adapter states.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreAdapterState enum

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Defines constants that specify kinds of DXCore adapter states. Pass one of these constants to the [IDXCoreAdapter::QueryState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate) method to retrieve the adapter state item for a state kind; pass a constant to the [IDXCoreAdapter::SetState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate) method to set an adapter's info for a state item.

## Syntax

```cpp
enum class DXCoreAdapterState : uint32_t
{
  IsDriverUpdateInProgress = 0,
  AdapterMemoryBudget = 1
};
```

## Constants

### IsDriverUpdateInProgress

Specifies the <em>IsDriverUpdateInProgress</em> adapter state, which when `true` indicates that a driver update has been initiated on the adapter but it has not yet completed. If the driver update has already completed, then the adapter will have been invalidated, and your [QueryState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate) call will return a <b>HRESULT</b> of <b>DXGI_ERROR_DEVICE_REMOVED</b>.

When calling [QueryState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate), the <em>IsDriverUpdateInProgress</em> state item has type <b>uint8_t</b>, representing a Boolean value.

<b>Important</b>. This state item is not supported for [SetState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate).

### AdapterMemoryBudget

Specifies the <em>AdapterMemoryBudget</em> adapter state, which retrieves or requests the adapter memory budget on the adapter.

When calling [QueryState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate), the <em>AdapterMemoryBudget</em> adapter state has type <a href="/windows/win32/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudgetnodesegmentgroup">DXCoreAdapterMemoryBudgetNodeSegmentGroup</a> for *inputStateDetails*, and type <a href="/windows/win32/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudget">DXCoreAdapterMemoryBudget</a> for *outputBuffer*.

<b>Important</b>. This state item is not supported for [SetState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate).

## See also

[IDXCoreAdapter::QueryState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate), [IDXCoreAdapter::SetState](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)