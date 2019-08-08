---
UID: NS:dxcore_interface.DXCoreAdapterMemoryBudgetNodeSegmentGroup
title: DXCoreAdapterMemoryBudgetNodeSegmentGroup
description: Describes a memory segment group for an adapter.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/06/2019
ms.keywords: DXCoreAdapterMemoryBudgetNodeSegmentGroup structure, dxcore_interface.dxcoreadaptermemorybudgetnodesegmentgroup
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
 - DXCoreAdapterMemoryBudgetNodeSegmentGroup
---

# DXCoreAdapterMemoryBudgetNodeSegmentGroup structure

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Describes a memory segment group for an adapter.

## -struct-fields

### nodeIndex

Type: **uint32_t**

Specifies the device's physical adapter for which the adapter memory information is queried. For single-adapter operation, set this to zero. If there are multiple adapter nodes, then set this to the index of the node (the device's physical adapter) for which you want to query for adapter memory information (see [Multi-adapter](/windows/desktop/direct3d12/multi-engine)).

### segmentGroup

Type: **[DXCoreSegmentGroup](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoresegmentgroup)**

Specifies the adapter memory segment grouping that you want to query about.

## See also

[DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters), [Multi-adapter](/windows/desktop/direct3d12/multi-engine)