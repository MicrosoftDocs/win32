---
description: An umbrella library is a single static-link library that exports a subset of Win32 APIs. For example, an umbrella lib named OneCore.lib provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices.
ms.assetid: A323B5D1-3235-4BBA-96BF-A7DFEBB85C89
title: Windows umbrella libraries
ms.topic: article
ms.date: 10/14/2020
---

# Windows umbrella libraries

An *umbrella library* is a single static-link library that exports a subset of Win32 APIs. For example, an umbrella library named **OneCore.lib** provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices.

The APIs in an umbrella library may be implemented across a range of modules (whether that's an [API set](windows-apisets.md) or a DLL), but the umbrella library abstracts that detail away from you, making your app more portable across operating system versions. Simply link your desktop app or driver with the umbrella library that contains the set of APIs that you're interested in, and that's all you need to do. 

| Library | Description |
|------------------------|-------------------------|
| OneCore.lib | This library provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices. Link your desktop app or driver with OneCore.lib (and no other libraries) to access these APIs. If you link your app or driver to OneCore.lib, and you only call Win32 APIs in that library, then your app or driver will load successfully on all Windows 10 devices.         |
| OneCore_apiset.lib | This library provides the same coverage as OneCore.lib, but uses [API set direct forwarding](api-set-loader-operation.md#direct-forwarding). Note that using this library will be compatible only with the Windows 10 version as specified by the SDK version you're targeting, or greater.  |
| OneCoreUap.lib | This library provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices that support the Windows Runtime (WinRT). Link your desktop app or driver with OneCoreUap.lib (and no other libraries) to access these APIs. If you link your app or driver to OneCoreUap.lib, and you only call Win32 APIs in that library, then your app or driver will load successfully on all Windows 10 devices that support the UWP. |
| OneCoreUAP_apiset.lib | This library provides the same coverage as OneCoreUAP.lib, but uses the [API set direct forwarding](api-set-loader-operation.md#direct-forwarding) technique. Note that using this library will be compatible only with the Windows 10 version as specified by the SDK you're targeting, or greater.  |
