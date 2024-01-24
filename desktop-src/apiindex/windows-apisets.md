---
title: Windows API sets
description: API sets are functional groups of Win32 APIs in the core OS. They provide an architectural separation from the host DLL in which a given Win32 API is defined and the functional group to which the API belongs.
ms.topic: article
ms.date: 05/31/2023
---

# Windows API sets

> [!IMPORTANT]
> The info in this topic applies to all versions of Windows 10, and later. We'll refer to those versions here as "Windows", calling out any exceptions where necessary.

All versions of Windows share a common base of operating system (OS) components that's called the *core OS* (in some contexts this common base is also called *OneCore*). In core OS components, Win32 APIs are organized into functional groups called *API sets*.

The purpose of an API set is to provide an architectural separation from the host DLL in which a given Win32 API is implemented, and the functional contract to which the API belongs. The decoupling that API sets provide between implementation and contracts offers many engineering advantages for developers. In particular, using API sets in your code can improve compatibility with Windows devices.

API sets specifically address the following scenarios:

- Although the full breadth of the Win32 API is supported on PCs, only a subset of the Win32 API is available on other Windows devices such as HoloLens, Xbox, and other devices. The API set name provides a query mechanism to cleanly detect whether an API is available on any given device.

- Some Win32 API implementations exist in DLLs with different names across different Windows devices. Using API set names instead of DLL names when detecting API availability and delay loading APIs provide a correct route to the implementation no matter where the API is actually implemented.

For more details, see [API set loader operation](api-set-loader-operation.md) and [Detect API set availability](detect-api-set-availability.md).

## Are API sets and dlls the same thing?

No&mdash;an API set name is a *virtual alias* for a physical `.dll` file. It's an implementation-hiding technique, where you as the caller don't have to know exactly which module is hosting the information.

The technique allows modules to be refactored (split apart, consolidated, renamed, and so on) on different Windows versions and editions. And your apps still link, and still get routed to the correct code at runtime.

So why do API sets have `.dll` in their names? The reason is the way the *DLL loader* is implemented. The loader is the part of the OS that loads DLLs and/or resolves references to DLLs. And at the front end, the loader requires any string passed to [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) to be terminated with ".dll". But after that front end, the loader can strip away that suffix, and query the API set database with the resulting string.

**LoadLibrary** (and delay load) succeeds with an API set name (with the ".dll" in it); but there isn't necessarily an actual file with that name anywhere on the PC.

## Linking umbrella libraries

To make it easier to restrict your code to Win32 APIs that are supported in the core OS, we provide a series of *umbrella libraries*. For example, an umbrella library named `OneCore.lib` provides the exports for the subset of Win32 APIs that are common to all Windows devices.

For more details, see [Windows umbrella libraries](windows-umbrella-libraries.md).

## API set contract names

API sets are identified by a strong contract name that follows these standard conventions recognized by the library loader. 

- The name must begin either with the string **api-** or **ext-**. 
    - Names that begin with **api-** represent APIs that are guaranteed to exist on all Windows versions.
    - Names that begin with **ext-** represent APIs that may not exist on all Windows versions.
- The name must end with the sequence **l\<n\>-\<n\>-\<n\>**, where **n** consists of decimal digits.
- The body of the name can be alphanumeric characters, or dashes (**-**).
- The name is case insensitive.

Here are some examples of API set contract names:

- **api-ms-win-core-ums-l1-1-0**
- **ext-ms-win-com-ole32-l1-1-5**
- **ext-ms-win-ntuser-window-l1-1-0**
- **ext-ms-win-ntuser-window-l1-1-1**

You can use an API set name in the context of a loader operation such as [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [P/Invoke](/dotnet/standard/native-interop/pinvoke) instead of a DLL module name to ensure a correct route to the implementation no matter where the API is actually implemented on the current device. However, when you do this you must append the string **.dll** at the end of the contract name. This is a requirement of the loader to function properly, and is not considered actually a part of the contract name. Although contract names appear similar to DLL names in this context, they are fundamentally different from DLL module names and do not directly refer to a file on disk.

Except for appending the string **.dll** in loader operations, API set contract names should be considered an immutable identifier that corresponds to a specific contract version.

## Identifying API sets for Win32 APIs

To identify whether a particular Win32 API belongs to an API set, review the requirements table in the reference documentation for the API. If the API belongs to an API set, the requirements table in the article lists the API set name and the Windows version in which the API was first introduced to the API set. For examples of APIs that belong to an API set, see these articles:

- [AllowSetForegroundWindow](/windows/win32/api/winuser/nf-winuser-allowsetforegroundwindow)
- [FindWindowsEx](/windows/win32/api/winuser/nf-winuser-findwindowexa)
- [GetClassFile](/windows/win32/api/objbase/nf-objbase-getclassfile)

## In this section

* [API set loader operation](api-set-loader-operation.md)
* [Detect API set availability](detect-api-set-availability.md)
* [Windows umbrella libraries](windows-umbrella-libraries.md)
