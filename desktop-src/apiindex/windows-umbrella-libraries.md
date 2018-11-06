---
Description: An &\#0034;umbrella&\#0034; library is a single static-link library that exports a subset of Win32 APIs. For example, an umbrella lib named OneCore.lib provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices.
ms.assetid: A323B5D1-3235-4BBA-96BF-A7DFEBB85C89
title: Windows "umbrella" libraries
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbHowTo
api_name: 
api_type: 
api_location: 
---

# Windows "umbrella" libraries

An "umbrella" library is a single static-link library that exports a subset of Win32 APIs. For example, an umbrella lib named OneCore.lib provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices.

The APIs in an umbrella lib may be implemented across a range of modules (whether that's an [API set](#what-is-an-api-set) or a DLL), but the umbrella lib abstracts that detail away from you, making your app more portable across operating system versions. Simply link your classic desktop app or driver with the umbrella lib that contains the set of APIs that you're interested in, and that's all you need to do. The topics in this section document the sets of APIs exported by some useful umbrella libs for developing Windows 10 apps.

## What is an API set?

An API set is a strong name for a list of Win32 APIs. The convention for assigning a strong name to an API set is to use what appears to be a dll name. But the purpose of an API set is to provide architectural separation between the API set's name and its associated host DLL implementation for improved portability of your app, so you should think of an API set's name as just a unique character string, and not as a DLL name. For delay load, you use the name of the API set.

API sets rely on operating system support in the library loader to effectively introduce a namespace redirection component into the library binding process. Subject to various inputs, including the API set name and the binding (import) context, the library loader performs a runtime redirection of the reference to a target host binary that houses the appropriate implementation of the API set.

The decoupling between implementation and interface contracts provided by API sets offers many engineering advantages, but can also potentially reduce the number of DLLs loaded in a process.

## In this section



| Topic                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OneCore.lib umbrella library (by module)](umbrella-lib-onecore.md)<br/>                | For convenience, an umbrella library named OneCore.lib is provided in the Microsoft Windows Software Development Kit (SDK), which provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices. Link your classic desktop app or driver with OneCore.lib (and no other libraries) to access these APIs. If you link your app or driver to OneCore.lib, and you only call Win32 APIs in that library, then your app or driver will load successfully on all Windows 10 devices.<br/>                                            |
| [OneCore.lib umbrella library (alphabetical)](umbrella-lib-onecore-alpha.md)<br/>       | For convenience, an umbrella library named OneCore.lib is provided in the Windows SDK, which provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices. Link your classic Desktop app or driver with OneCore.lib (and no other libraries) to access these APIs. If you link your app or driver to OneCore.lib, and you only call Win32 APIs in that library, then your app or driver will load successfully on all Windows 10 devices.<br/>                                                                                 |
| [OneCoreUap.lib umbrella library (by module)](umbrella-lib-onecoreuap.md)<br/>          | For convenience, an umbrella library named OneCoreUap.lib is provided in the Windows SDK, which provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices that support the Universal Windows Platform (UWP). Link your classic Desktop app or driver with OneCoreUap.lib (and no other libraries) to access these APIs. If you link your app or driver to OneCoreUap.lib, and you only call Win32 APIs in that library, then your app or driver will load successfully on all Windows 10 devices that support the UWP.<br/> |
| [OneCoreUap.lib umbrella library (alphabetical)](umbrella-lib-onecoreuap-alpha.md)<br/> | For convenience, an umbrella library named OneCoreUap.lib is provided in the Windows SDK, which provides the exports for the subset of Win32 APIs that are common to all Windows 10 devices that support the UWP. Link your classic Desktop app or driver with OneCoreUap.lib (and no other libraries) to access these APIs. If you link your app or driver to OneCoreUap.lib, and you only call Win32 APIs in that library, then your app or driver will load successfully on all Windows 10 devices that support the UWP.<br/>                              |



 

 

 




