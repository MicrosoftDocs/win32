---
UID: NE:dxcore_interface.DXCoreSegmentGroup
title: DXCoreSegmentGroup
description: Defines constants that specify an adapter's memory segment grouping.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/11/2019
ms.keywords: DXCoreAdapterState enumeration, dxcore_interface.dxcoresegmentgroup
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
 - DXCoreSegmentGroup
---

# DXCoreSegmentGroup enum

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Defines constants that specify an adapter's memory segment grouping.

## Enum fields

### Local

Specifies a grouping of segments that is considered local to the adapter, and represents the fastest memory available to the GPU. Your application should target the local segment group as the target size for its working set.

### NonLocal

Specifies a grouping of segments that is considered non-local to the adapter, and may have slower performance than the local segment group.

## See also

[DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)