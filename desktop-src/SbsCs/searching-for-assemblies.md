---
Description: 'There are two methods by which a hosting application can search for side-by-side assemblies.'
ms.assetid: 'f34f8f39-f03c-4adf-afa8-9cb9ed48d149'
title: Searching for Assemblies
---

# Searching for Assemblies

There are two methods by which a hosting application can search for side-by-side assemblies.

Hosted modules can register themselves with the hosting application by extending some shared configuration information. The application can then use this configuration information to load the assemblies required for the new functionality. This could be done by calling [**CreateActCtx**](createactctx.md) on manifests specified in the registration data, followed by calling [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) or [**CoCreateInstance**](_com_cocreateinstance) to get into the new module. Note that with this method, the new components have to update some shared application state to indicate their presence.

The hosting application can actively search for the assemblies on startup using [**FindFirstFile**](https://msdn.microsoft.com/library/windows/desktop/aa364418) and [**FindNextFile**](https://msdn.microsoft.com/library/windows/desktop/aa364428) to look for DLLs or manifests in a specified location, and then use [**CreateActCtx**](createactctx.md) to access the information. This method requires no registration of the component.

 

 



