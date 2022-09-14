---
description: Describes how Windows 10 uses API sets in loader operations. 
title: API set loader operation
ms.topic: article
ms.date: 10/14/2020
---

# API set loader operation

[API sets](windows-apisets.md) rely on OS support in the library loader to effectively introduce a module namespace redirection into the library binding process. The [API set contract name](windows-apisets.md#api-set-contract-names) is used by library loader to perform a runtime redirection of the reference to a target host binary that houses the appropriate implementation of the API set.

When the loader encounters a dependency on an API set at run time, the loader consults configuration data in the image to identify the host binary for an API set. This configuration data is called the **API set schema**. The schema is assembled as a property of the OS, and the mapping between API sets and binaries may differ depending on which binaries are included in a given device. The schema enables an imported function in a single binary to be routed correctly on different devices, even if the module names of the binary host have been renamed or completely refactored on different Windows devices.

Windows 10 supports two standard techniques to consume and interface with API sets: **direct forwarding** and **reverse forwarding**.

### Direct forwarding

In this configuration, the consuming code imports an API set module name directly. This import is resolved in a single operation, and is the most efficient method with the least overhead. Conceptually, this resolution may point to different binaries on different Windows 10 devices, as is shown in the following example:

Imported API set: **api-feature1-l1-1-0.dll**
-  Windows PC -> **feature1.dll**
-  HoloLens -> **feature1_holo.dll**
-  IoT -> **feature1_iot.dll**

Because the mappings are kept in a custom schema data repository, it means that an API set name that ends with **.dll** does not directly refer to a file on disk. The **.dll** part of the API set name is only a convention required by the loader. The API set name is more like an alias or a virtual name for a physical DLL file. This makes the name portable across the entire range of Windows 10 devices.

### Reverse forwarding

While API set names provide a stable namespace for modules across devices, it is not always practical to convert every binary to this new system. For example, an application may have been in common use for many years, and recompiling the application's binaries may not be feasible. Additionally, some applications may need to continue to run on systems built before specific API sets were introduced.

To accommodate this level of compatibility, a system of *forwarders* are provided on all Windows 10 devices that cover a subset of the Win32 API surface. These forwarders use the module names that were introduced on Windows PCs, and leverage the API Set system to provide compatibility across all Windows 10 devices.

The loader operation behaves like this:

1.  On a device other than a Windows PC, the loader is presented a legacy Windows PC module name dependency that is not present on the device.
2.  The loader locates an API set forwarder for this module and loads it into memory.
3.  The forwarder has a mapping for the API set for the given function being called.
4.  The loader finds the proper host binary for the given device.

Conceptually, the mapping looks like:

Imported DLL: **feature1.dll**
- Windows PC -> **feature1.dll**
- HoloLens -> **feature1.dll** forwarder -> **api-feature1-l1-1-0.dll** -> **feature1_holo.dll**
- IoT -> **feature1.dll** forwarder -> **api-feature1-l1-1-0.dll** -> **feature1_iot.dll**

The end result is functionally the same as [direct forwarding](#direct-forwarding), but it accomplishes it in a way that maximizes application compatibility.

> [!NOTE]
> Reverse forwarding provides coverage only for a subset of the Win32 API surface. It does not allow applications that target desktop versions of Windows 10 to run on all Windows 10 devices.
