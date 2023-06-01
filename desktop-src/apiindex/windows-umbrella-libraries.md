---
title: Windows umbrella libraries
description: An umbrella library is a single static-link library that exports a subset of Win32 APIs. For example, an umbrella lib named OneCore.lib provides the exports for the subset of Win32 APIs that are common to all Windows devices.
ms.topic: article
ms.date: 05/31/2023
ms.assetid: A323B5D1-3235-4BBA-96BF-A7DFEBB85C89
---

# Windows umbrella libraries

> [!IMPORTANT]
> The info in this topic applies to all versions of Windows 10, and later. We'll refer to those versions here as "Windows", calling out any exceptions where necessary.

An *umbrella library* is a single static-link library that exports a subset of Win32 APIs. For example, an umbrella library named **OneCore.lib** provides the exports for the subset of Win32 APIs that are common to all Windows devices.

The APIs in an umbrella library might be implemented across a range of modules (where a module is either an [API set](windows-apisets.md) or a DLL). But the umbrella library abstracts that detail away from you, making your app more portable across operating system versions. In your desktop app or driver, simply link the umbrella library that contains the set of APIs that you're interested in, and that's all you need to do.

| Library | Description |
|-|-|
| OneCore.lib | Provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices, and later. Link `OneCore.lib` (and no other libraries) to access those APIs. If you link `OneCore.lib`, and you call only Win32 APIs in that library, then your desktop app or driver will load successfully on all Windows 10 devices, and later. |
| OneCore_apiset.lib | Provides the same coverage as `OneCore.lib`, but uses [API set direct forwarding](api-set-loader-operation.md#direct-forwarding). Linking `OneCore_apiset.lib` will be compatible only with the Windows version, or later, relevant to the SDK version you're targeting. |
| OneCoreUap.lib | Provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices, and later, that support the Windows Runtime (WinRT). Link `OneCoreUap.lib` (and no other libraries) to access those APIs. If you link `OneCore.lib`, and you call only Win32 APIs in that library, then your desktop app or driver will load successfully on all Windows 10 devices, and later, that support the UWP. |
| OneCoreUAP_apiset.lib | Provides the same coverage as `OneCoreUAP.lib`, but uses [API set direct forwarding](api-set-loader-operation.md#direct-forwarding). Linking `OneCoreUAP_apiset.lib` will be compatible only with the Windows version, or later, relevant to the SDK version you're targeting. |
