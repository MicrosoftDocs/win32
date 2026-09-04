---
description: An umbrella library is a single library that covers a selected subset of Win32 APIs, so you can link one library instead of identifying the module that implements each API.
title: Windows umbrella libraries
ms.topic: concept-article
ms.date: 09/03/2026
ms.assetid: A323B5D1-3235-4BBA-96BF-A7DFEBB85C89
---

# Windows umbrella libraries

> [!IMPORTANT]
> The info in this topic applies to all versions of Windows 10, and later. We'll refer to those versions here as "Windows", calling out any exceptions where necessary.

An *umbrella library* is a single library that you link, and that covers a selected subset of Win32 APIs. For example, an umbrella library named **OneCore.lib** covers the subset of Win32 APIs that are common to all Windows devices.

The APIs in an umbrella library might be implemented across a range of modules (where a module is either an [API set](windows-apisets.md) or a DLL). But the umbrella library abstracts that detail away from you, making your app more portable across operating system versions. In your desktop app or driver, link the umbrella library that covers the set of APIs that you're interested in, and that's all you need to do.

## What an umbrella library covers

An umbrella library covers a *selected* subset of APIs. It isn't a complete index of every API in every module it draws from, and a given API isn't necessarily present in every umbrella library.

The set of APIs a library covers is also specific to the Windows SDK version you build against. A later SDK can add coverage that an earlier one doesn't have.

For both of those reasons, treat the reference page for an individual API as the authority on which library to link. The **Requirements** table on that page names the library for that API.

## Available libraries

| Library | Description |
|-|-|
| OneCore.lib | Covers the subset of Win32 APIs that are common to all Windows devices. Link `OneCore.lib` (and no other Win32 umbrella library) to reach those APIs. If you link `OneCore.lib`, and you call only Win32 APIs that it covers, then your desktop app or driver loads successfully on all Windows devices. |
| OneCore_apiset.lib | The API set variant of `OneCore.lib`. Where an API set name is available for an API, it resolves through a [direct API set import](api-set-loader-operation.md#direct-api-set-import), so no intermediate forwarder module is involved at load time. A binary that links it isn't guaranteed to run as-is on versions of Windows released before the API sets it imports. |
| OneCoreUAP.lib | Covers the subset of Win32 APIs that are common to all Windows devices that support the Windows Runtime (WinRT). Link `OneCoreUAP.lib` (and no other Win32 umbrella library) to reach those APIs. If you link `OneCoreUAP.lib`, and you call only Win32 APIs that it covers, then your desktop app or driver loads successfully on all Windows devices that support WinRT. |
| OneCoreUAP_apiset.lib | The API set variant of `OneCoreUAP.lib`. Where an API set name is available for an API, it resolves through a [direct API set import](api-set-loader-operation.md#direct-api-set-import), so no intermediate forwarder module is involved at load time. A binary that links it isn't guaranteed to run as-is on versions of Windows released before the API sets it imports. |

Don't combine two of these libraries in one binary. Each one exists to confine your binary to a particular API surface, and linking a second library can bind you to APIs outside that surface.

## Choosing between a library and its API set variant

For an API that both variants cover, the two reach the same implementation at run time. What differs is the name that ends up in your binary's import table, and therefore the range of Windows versions the binary can run on.

- Link the plain library (`OneCore.lib`, `OneCoreUAP.lib`) when you need a single binary that also runs on versions of Windows released before the relevant API sets existed. It imports legacy Windows module names, and [reverse forwarding](api-set-loader-operation.md#reverse-forwarding) redirects those imports on editions that no longer carry the original modules.
- Link the API set variant (`OneCore_apiset.lib`, `OneCoreUAP_apiset.lib`) when your binary targets current versions of Windows. It prefers an API set name wherever one is available for the API, so that import resolves directly to the binary that hosts the implementation, with no forwarder in between. That's the more efficient form. Where no API set name applies, it uses the module name, the same as the plain library does.

Neither choice changes which APIs you can call. It changes how your imports are named, and how far back your binary can run.

## See also

- [Windows API sets](windows-apisets.md)
- [API set loader operation](api-set-loader-operation.md)
- [Detect API set availability](detect-api-set-availability.md)
