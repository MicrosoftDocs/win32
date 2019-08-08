---
UID: NS:dxcore_interface.DXCoreAdapterMemoryBudget
title: DXCoreAdapterMemoryBudget
description: Describes the memory budget for an adapter.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/06/2019
ms.keywords: DXCoreAdapterMemoryBudget structure, dxcore_interface.dxcoreadaptermemorybudget
ms.localizationpriority: low
ms.topic: structure
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: structure
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
 - DXCoreAdapterMemoryBudget
---

# DXCoreAdapterMemoryBudget structure

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Describes the memory budget for an adapter.

## -struct-fields

### budget

Type: **uint64_t**

Specifies the OS-provided adapter memory budget, in bytes, that your application should target. If *currentUsage* is greater than *budget*, then your application may incur stuttering or performance penalties due to background activity by the OS, which is intended to provide other applications with a fair usage of adapter memory.

### budget

Type: **uint64_t**

Specifies your applicaton's current adapter memory usage, in bytes.

### availableForReservation

Type: **uint64_t**

Specifies the amount of adapter memory, in bytes, that your application has available for reservation. To reserve this adapter memory, your application should call [IDXCoreAdapter::SetState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-setstate) with *state* set to [DXCoreAdapterState::AdapterMemoryBudget](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate).

### availableForReservation

Type: **uint64_t**

Specifies the amount of adapter memory, in bytes, that is reserved by your application. The OS uses the reservation as a hint to determine your application's minimum working set. Your application should attempt to ensure that its adapter memory usage can be trimmed to meet this requirement.

## See also

[DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)