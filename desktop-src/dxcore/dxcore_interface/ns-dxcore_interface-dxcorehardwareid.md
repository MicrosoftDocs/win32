---
title: DXCoreHardwareID
description: Represents the PnP hardware ID parts for an adapter.
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
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

[DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)