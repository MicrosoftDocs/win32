---
description: When creating your own side-by-side assemblies, follow the Guidelines for Creating Side-by-side Assemblies and author any DLL to be included in the assembly according to the guidelines in Authoring a DLL for a Side-by-Side Assembly.
ms.assetid: 0e98bbcd-7e23-4a33-b0fa-1f936d0ef96b
title: Authoring State Storage for Side-by-side Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Authoring State Storage for Side-by-side Assemblies

When creating your own side-by-side assemblies, follow the [Guidelines for Creating Side-by-side Assemblies](guidelines-for-creating-side-by-side-assemblies.md) and author any DLL to be included in the assembly according to the guidelines in [Authoring a DLL for a Side-by-Side Assembly](authoring-a-dll-for-a-side-by-side-assembly.md).

Adhere to the following guidelines for the storage of the state:

-   Design state storage to be forward and backward compatible. Expect the versions to be used in any order: for example, v1, then v3, then v2.
-   Initialize and set the default settings for the assembly in the assembly code. Do not save the defaults settings in the registry.
-   Registry settings must be written on an individual-version basis to isolate multiple assembly versions that may be run at the same time. Design your side-by-side assembly to correctly store and handle the state of the assembly during side-by-side sharing scenarios.
-   Assemblies commonly store state information in registry keys. Author a set of header files and helper functions to provide an easy way to version registry keys containing the assembly state.
-   Any assembly state information saved in the registry must be isolated from other versions of the assembly. State settings stored in the registry must be saved in individual version sections of the registry. This is required in both the HKLM and HKCU parts of the registry. For example, store HKCU state settings for assembly version XXXX under the following registry key:

    **HKCU**\\**MyCompany**\\**MyComponent**\\**VersionXXXX**

-   Any state information stored in the registry by shared assemblies must be saved in individual version sections of the registry. For example, a state setting called EnableSuperCoolFeature might have a value of **TRUE** or **FALSE**. Store the value for a [*shared side-by-side assembly*](s-sbscs-gly.md) as follows:

    **HKEY\_CurrentUser**\\**Software**\\**MyCompany**\\**MyComponent**\\**Version01.01**\\**EnableSuperCoolFeature = TRUE**

-   Any state information stored in the registry by private assemblies must be saved in individual application sections of the registry. This isolates the assembly's state settings to the application. You can use the [**GetModuleFileName**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) function to set up a virtual root. For example, if assembly version XXYY is a private assembly of "SomeApplication," a call to **GetModuleFileName** returns "SomeApplication" and any private state settings for the assembly should be written under the following key:

    **HKCU**\\**MyCompany**\\**MyComponent**\\**VersionXXYY**\\**SomeApplication**

-   Make shared state settings stored in the registry private to the assembly context that runs. You can use the [**GetModuleFileName**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) function to set up a virtual root. This should be done for HKLM and HKCU branches.
-   Ideally, you should adopt a persistence model in which the application persists the state and does not alter the registry. An application should not need to directly touch the component's registry entries. Instead, the assembly should offer API functions that save or restore settings that are side-by-side compatible.
-   Assemblies may save state settings in stores outside the registry to enable the assembly to interact with the global state. Side-by-side assemblies may use the following side-by-side compatible stores:
    -   A protected store (*pstore*)
    -   A WinInet cache
    -   A Microsoft SQL Server

 

 
