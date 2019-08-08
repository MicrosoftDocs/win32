---
UID: NS:dxcore_interface.DXCoreHardwareID
title: DXCoreHardwareID
description: Represents the PnP hardware ID parts for an adapter.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/06/2019
ms.keywords: DXCoreHardwareID structure, dxcore_interface.dxcorehardwareid
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
 - DXCoreHardwareID
---

# DXCoreHardwareID structure

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Represents the PnP hardware ID parts for an adapter.

## -struct-fields

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

[DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)