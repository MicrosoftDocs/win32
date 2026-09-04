---
title: Windows API sets
description: API sets are functional groups of Win32 APIs in the core OS. They provide an architectural separation between the host DLL in which a given Win32 API is implemented and the functional contract to which the API belongs.
ms.topic: concept-article
ms.date: 09/03/2026
---

# Windows API sets

> [!IMPORTANT]
> The info in this topic applies to all versions of Windows 10, and later. We'll refer to those versions here as "Windows", calling out any exceptions where necessary.

All versions of Windows share a common base of operating system (OS) components that's called the *core OS* (in some contexts this common base is also called *OneCore*). In core OS components, Win32 APIs are organized into functional groups called *API sets*.

The purpose of an API set is to provide an architectural separation between the host DLL in which a given Win32 API is implemented, and the functional contract to which the API belongs. The decoupling that API sets provide between implementation and contracts offers many engineering advantages for developers. In particular, using API sets in your code can improve compatibility with Windows devices.

API sets specifically address the following scenarios:

- Although the full breadth of the Win32 API is supported on PCs, only a subset of the Win32 API is available on other Windows devices such as HoloLens, Xbox, and other devices. An API set name gives you a stable thing to ask about, so that your app can detect at run time whether a capability is available on the current device. The query itself is performed by the [IsApiSetImplemented](/windows/win32/api/apiquery2/nf-apiquery2-isapisetimplemented) function.

- Some Win32 API implementations exist in DLLs with different names across different Windows devices. Using API set names instead of DLL names when detecting API availability and delay loading APIs provides a correct route to the implementation no matter where the API is actually implemented.

For more details, see [API set loader operation](api-set-loader-operation.md) and [Detect API set availability](detect-api-set-availability.md).

## Are API sets and DLLs the same thing?

No&mdash;an API set name identifies a *contract*, not a file. At run time the loader resolves that contract through the API set schema on the current device, and routes the reference to the DLL that hosts the implementation. It's an implementation-hiding technique, where you as the caller don't have to know exactly which module is hosting the information.

The technique allows modules to be refactored (split apart, consolidated, renamed, and so on) on different Windows versions and editions. And your apps still link, and still get routed to the correct code at run time.

So why do API sets have `.dll` in their names? The reason is the way the *DLL loader* is implemented. The loader is the part of the OS that loads DLLs and/or resolves references to DLLs. And at the front end, the loader requires any string passed to [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) to be terminated with ".dll". But after that front end, the loader can strip away that suffix, and query the API set schema with the resulting string.

You can pass an API set name (with the ".dll" in it) to **LoadLibrary**, or use it as a delay-load target. The operation succeeds when the schema on the current device maps that contract to a usable host; there isn't necessarily an actual file with that name anywhere on the PC. If the contract isn't mapped on the current device, a direct **LoadLibrary** fails. A delay-loaded reference behaves differently: the process still loads, and the absence surfaces later, when the API is called.

Either way, a successful link or load isn't by itself evidence that an implementation is present. To determine that, see [Detect API set availability](detect-api-set-availability.md).

## Linking umbrella libraries

To make it easier to restrict your code to Win32 APIs that are supported in the core OS, we provide a series of *umbrella libraries*. An umbrella library lets you link a single library instead of identifying the individual import library for each API that you call.

For more details, and to choose the umbrella library that matches what you're targeting, see [Windows umbrella libraries](windows-umbrella-libraries.md).

## API set contract names

API sets are identified by a contract name that follows conventions recognized by the library loader.

All contract names share these conventions:

- The name begins either with the string **api-** or **ext-**.
- The body of the name can be alphanumeric characters, or dashes (**-**). A tilde (**~**) appears only as the separator before a group name.
- The name is case insensitive.

Two forms of contract name are in use, and you can encounter either one.

A *versioned contract name* ends with the sequence **l\<n\>-\<n\>-\<n\>**, where **n** consists of decimal digits&mdash;for example, `ext-ms-win-core-samplefeature-l1-1-0`. The trailing numbers identify one specific version of the contract, and a name in this form should be considered an immutable identifier for that version.

A *contract alias* carries no version&mdash;for example, `api-win-core-samplefeature`. It identifies the contract itself rather than one version of it. When a contract organizes its individually available capabilities into *named groups*, a group is addressed by appending the group name to the contract alias, separated by a tilde: `api-win-core-samplefeature~AdvancedOperations`.

The `samplefeature` names used here are illustrative names for a fictional Windows component.

### The api- and ext- prefixes

The prefix is a naming convention. It was originally intended to distinguish contracts that are present on every qualifying edition (**api-**) from contracts that might be absent (**ext-**). That distinction wasn't consistently applied, and a contract's role can change over time without the contract being renamed.

The loader assigns no significance to the prefix; it resolves **api-** and **ext-** names by the same rules. Don't infer availability from the prefix. Query it instead&mdash;see [Detect API set availability](detect-api-set-availability.md).

### Using a contract name

Two different kinds of operation take a contract name, and they take it in different forms.

*Loader operations*&mdash;such as [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) or [P/Invoke](/dotnet/standard/native-interop/pinvoke)&mdash;take the name with the string **.dll** appended. Use a contract name in these operations instead of a DLL module name to ensure a correct route to the implementation no matter where the API is actually implemented on the current device. The **.dll** suffix is a requirement of the loader to function properly, and is not considered actually a part of the contract name. Although contract names appear similar to DLL names in this context, they are fundamentally different from DLL module names and do not directly refer to a file on disk.

*Availability queries* take the name without a **.dll** suffix, in the form that matches how the API is addressed:

| API surface | Query form | Example |
|---|---|---|
| Named group | `<contract>~<group>` | `api-win-core-samplefeature~AdvancedOperations` |
| Default group | Contract alias, without `~Default` | `api-win-core-samplefeature` |
| Versioned contract | Complete versioned contract name | `ext-ms-win-core-samplefeature-l1-1-0` |

A group name can't be combined with a versioned contract name.

## Identifying API sets for Win32 APIs

To identify whether a particular Win32 API belongs to an API set, review the requirements table in the reference documentation for the API. If the API belongs to an API set, the requirements table in the article lists the API set name and the Windows version in which the API was first introduced to the API set. For examples of APIs that belong to an API set, see these articles:

- [AllowSetForegroundWindow](/windows/win32/api/winuser/nf-winuser-allowsetforegroundwindow)
- [FindWindowEx](/windows/win32/api/winuser/nf-winuser-findwindowexa)
- [GetClassFile](/windows/win32/api/objbase/nf-objbase-getclassfile)

If the API's header supplies an `Is<APIName>Present` helper function, prefer that helper when you test for availability. It already contains the correct name for the API set or group that carries the API. For more info, see [Detect API set availability](detect-api-set-availability.md).

## In this section

* [API set loader operation](api-set-loader-operation.md)
* [Detect API set availability](detect-api-set-availability.md)
* [Windows umbrella libraries](windows-umbrella-libraries.md)
