---
description: Describes how the Windows library loader resolves an API set reference to the binary that hosts the implementation.
title: API set loader operation
ms.topic: reference
ms.date: 09/03/2026
---

# API set loader operation

> [!IMPORTANT]
> The info in this topic applies to all versions of Windows 10, and later. We'll refer to those versions here as "Windows", calling out any exceptions where necessary.

[API sets](windows-apisets.md) rely on OS support in the library loader to introduce a module namespace redirection into the library binding process. An [API set contract name](windows-apisets.md#api-set-contract-names) doesn't name a file. The loader performs a run-time redirection from that contract name to the host binary that contains the implementation.

When the loader encounters a dependency on an API set at run time, it consults configuration data in the image to identify the host binary for that API set. This configuration data is called the **API set schema**. The schema is assembled as a property of the OS, and the mapping between API sets and binaries can differ depending on which binaries are included on a given device. The schema is what lets an imported function in a single binary be routed correctly on different devices, even when the module that hosts the implementation has been renamed, split apart, or refactored.

## How imports reach an implementation

A binary can reach an API set implementation in two ways, decided by the name in its import table:

- **Direct API set import.** The binary imports an API set contract name. The loader resolves that name through the API set schema to the host binary on the current device.
- **Legacy module import.** The binary imports a legacy Windows module name, such as *samplefeature.dll*. On an edition that ships that module, the loader binds to it directly. On an edition that has replaced it, a *reverse forwarder* carrying the same name redirects the import to an API set, which the loader then resolves through the schema.

Which of those names ends up in your import table is usually determined by the library you link against rather than by the source you write. See [Windows umbrella libraries](windows-umbrella-libraries.md).

Prefer the API set contract name for code that targets current versions of Windows. The loader resolves it straight to the host, with no forwarder in between. Import the legacy module name when you need a single binary that also runs on Windows versions released before the API set existed. Reverse forwarding keeps that binary working on editions where the legacy module has been replaced.

## Direct API set import

Resolution is a three-step sequence:

1. Your binary imports an API set contract name, or passes one to [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw).
2. The loader looks the contract up in the API set schema on the current device, and finds the host binary that the schema maps it to.
3. The loader loads that host binary and binds the imported function to the host's export.

Because the mapping lives in the schema rather than in the file system, the same import can resolve to different binaries on different devices:

| Device | `api-win-core-samplefeature` maps to |
|---|---|
| A device that includes the feature | *samplefeature.dll* |
| A device that ships a refactored implementation | *samplefeaturecore.dll* |
| A device that doesn't include the feature | Not mapped |

The `samplefeature` names used here are illustrative names for a fictional Windows component.

The consuming binary is unaware of which host it was bound to. That's the point of the mechanism: the contract is stable, while the module that implements it is free to change from one device to the next.

An import of a contract name is resolved in a single operation, with no intermediate forwarder module involved. It's the most efficient form, and the normal path for code written against API sets.

### API set names and the .dll suffix

Because the mappings are kept in the schema rather than on disk, an API set name that ends with **.dll** doesn't refer to a file of that name. The **.dll** part is only a convention required by the loader. The API set name is more like an alias, or a virtual name, for a physical DLL file.

The loader resolves both forms of contract name, a versioned contract name and a contract alias, through the same schema, and both take the **.dll** suffix in a loader operation. For the conventions that govern these names, see [API set contract names](windows-apisets.md#api-set-contract-names).

### Name stability isn't the same as availability

An API set name is stable across Windows devices, in the sense that the same name always identifies the same contract wherever it's recognized. That's a property of the namespace, not a guarantee about any particular device.

A given contract can be absent from a device, or present but not mapped to a host. Nothing about the name tells you which. To find out whether the implementation is actually there, see [Detect API set availability](detect-api-set-availability.md).

## What resolution requires

For a call through an API set to reach an implementation, all of the following have to hold:

- The contract is present in the schema on the current device.
- The schema maps the contract to a host binary, and that host can be loaded.
- The host exports the specific function your binary is calling.

When one of those doesn't hold, where the failure surfaces depends on how you imported the API set:

| Import style | Behavior when the contract can't be resolved |
|---|---|
| Static import | The process fails to start. The loader resolves static imports before any of your code runs. |
| Delay-loaded import | The process starts normally. Resolution is deferred to the first call to the API, where your code can handle the failure. |

A missing export is reported separately from a missing contract; a binary that imports a function the host doesn't export fails with a missing entry point error.

## What a successful load doesn't tell you

Resolution binds a *contract* to a host. It doesn't evaluate the state of an individual capability within that contract.

A contract can organize its individually available capabilities into [named groups](windows-apisets.md#api-set-contract-names). A group can be unavailable on a device even though the contract that carries it resolves normally, because the loader binds at contract granularity and doesn't consult group state when it binds. That's deliberate: refusing to bind a host is fatal to a static import, so the loader takes the permissive path and leaves the finer question to the caller.

The consequence for your code is that a successful load, or a successful **LoadLibrary** call, isn't evidence that a particular capability is available. Ask that question explicitly with an availability query. See [Detect API set availability](detect-api-set-availability.md).

## Optional API sets and delay loading

If your application calls an API set that might not be present, an availability check on its own isn't enough: with a static import the process fails to start, so execution never reaches the check.

To keep the optional code path reachable, either configure the module that carries the optional API for [delay loading](/cpp/build/reference/linker-support-for-delay-loaded-dlls), or resolve the target dynamically with **LoadLibrary** and [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) after an availability query succeeds. For the details of both approaches, see [Detect API set availability](detect-api-set-availability.md).

## Reverse forwarding

While API set names provide a stable namespace for modules across devices, it isn't always practical to convert every binary to this system. An application might have been in common use for many years, and recompiling its binaries might not be feasible. Some applications also need to keep running on systems that were built before specific API sets were introduced.

To accommodate that, editions that don't carry the original modules include a set of *reverse forwarders*: compatibility binaries that carry the module names originally introduced on Windows PCs, and that redirect their exports to API sets.

A full desktop edition ships the original modules, so an import of a legacy module name binds to the module as it always has. On an edition that has replaced that module, the reverse forwarder carrying the same name covers the gap.

The loader operation behaves like this:

1. The loader is presented with a dependency on a legacy Windows PC module name that isn't present on the device.
2. The loader locates a reverse forwarder that carries that module name, and loads it.
3. The reverse forwarder redirects the imported function to an API set.
4. The loader resolves that API set through the schema, as described earlier in this topic.

Conceptually, the mapping looks like this:

Imported DLL: *samplefeature.dll*

- On an edition that has the original module: *samplefeature.dll*
- On an edition that has replaced it: *samplefeature.dll* reverse forwarder -> `api-win-core-samplefeature` -> *samplefeaturecore.dll*

The limit on this path is export coverage. A reverse forwarder carries only the exports that have API set equivalents, so it doesn't necessarily export every function the original module did. A binary that imports a function the reverse forwarder doesn't carry fails to load with a missing entry point error.

Reverse forwarding is also a reason not to treat a successful resolution as proof that an implementation is present. A **GetProcAddress** call against a legacy module name can return a valid function pointer that resolves to a stub returning an error. Query availability explicitly instead. See [Detect API set availability](detect-api-set-availability.md).

> [!NOTE]
> Reverse forwarding covers only a subset of the Win32 API surface. It doesn't allow applications that target desktop versions of Windows to run on all Windows devices. If your binary targets current versions of Windows, the API set contract name is the more direct choice.

## See also

- [Windows API sets](windows-apisets.md)
- [Detect API set availability](detect-api-set-availability.md)
- [Windows umbrella libraries](windows-umbrella-libraries.md)
- [LoadLibrary function](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw)
- [GetProcAddress function](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)
