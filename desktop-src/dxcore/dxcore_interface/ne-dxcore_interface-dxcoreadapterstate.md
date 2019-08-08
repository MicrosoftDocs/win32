---
UID: NE:dxcore_interface.DXCoreAdapterState
title: DXCoreAdapterState
description: Defines constants that specify kinds of DXCore adapter states.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/11/2019
ms.keywords: DXCoreAdapterState enumeration, dxcore_interface.dxcoreadapterstate
ms.localizationpriority: low
ms.topic: enumeration
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: enumeration
req.ddi-compliance: 
req.dll: dxcore.dll
req.header: dxcore_interface.h
req.idl: 
req.include-header: dxcore.h
req.irql: 
req.kmdf-ver: 
req.lib: dxcore.lib
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: Windows 10 (Build 18936)
req.target-min-winversvr: 
req.target-type: Windows
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
 - kbsyntax
api_type:
 - HeaderDef
api_location:
 - dxcore.dll
api_name:
 - DXCoreAdapterState
---

## Description

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

# DXCoreAdapterState enum

Defines constants that specify kinds of DXCore adapter states. Pass one of these constants to the [IDXCoreAdapter::QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate) method to retrieve the adapter state item for a state kind; pass a constant to the [IDXCoreAdapter::SetState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate) method to set an adapter's info for a state item.

## Enum fields

### IsDriverUpdateInProgress

Specifies the <em>IsDriverUpdateInProgress</em> adapter state, which when `true` indicates that a driver update has been initiated on the adapter but it has not yet completed. If the driver update has already completed, then the adapter will have been invalidated, and your [QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate) call will return a <b>HRESULT</b> of <b>DXGI_ERROR_DEVICE_REMOVED</b>.

When calling [QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate), the <em>IsDriverUpdateInProgress</em> state item has type <b>uint8_t</b>, representing a Boolean value.

<b>Important</b>. This state item is not supported for [SetState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate).

### AdapterMemoryBudget

Specifies the <em>AdapterMemoryBudget</em> adapter state, which retrieves or requests the adapter memory budget on the adapter.

When calling [QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate), the <em>AdapterMemoryBudget</em> adapter state has type <a href="/windows/desktop/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudgetnodesegmentgroup">DXCoreAdapterMemoryBudgetNodeSegmentGroup</a> for *inputStateDetails*, and type <a href="/windows/desktop/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudget">DXCoreAdapterMemoryBudget</a> for *outputBuffer*.

<b>Important</b>. This state item is not supported for [SetState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate).

### AdapterMemoryReservation

Specifies the <em>AdapterMemoryReservation</em> adapter state, which represents the minimum required physical memory to set, in bytes, on the adapter. We recommend that you set an adapter reservation in order to denote the amount of physical memory that your application can't go without. This value helps the operating system (OS) to quickly minimize the impact of large memory-pressure situations.

When calling [SetState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate), the <em>AdapterMemoryReservation</em> adapter state has type <a href="/windows/desktop/dxcore/dxcore_interface/ns-dxcore_interface-dxcoreadaptermemorybudgetnodesegmentgroup">DXCoreAdapterMemoryBudgetNodeSegmentGroup</a> for *inputStateDetails*, and type **uint64_t** for *inputData*.

<b>Important</b>. This state item is not supported for [QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate).

## See also

[IDXCoreAdapter::QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate), [IDXCoreAdapter::SetState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)
