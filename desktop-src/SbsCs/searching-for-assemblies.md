---
description: There are two methods by which a hosting application can search for side-by-side assemblies.
ms.assetid: f34f8f39-f03c-4adf-afa8-9cb9ed48d149
title: Searching for Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Searching for Assemblies

There are two methods by which a hosting application can search for side-by-side assemblies.

Hosted modules can register themselves with the hosting application by extending some shared configuration information. The application can then use this configuration information to load the assemblies required for the new functionality. This could be done by calling [**CreateActCtx**](/windows/desktop/api/Winbase/nf-winbase-createactctxa) on manifests specified in the registration data, followed by calling [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get into the new module. Note that with this method, the new components have to update some shared application state to indicate their presence.

The hosting application can actively search for the assemblies on startup using [**FindFirstFile**](/windows/desktop/api/fileapi/nf-fileapi-findfirstfilea) and [**FindNextFile**](/windows/desktop/api/fileapi/nf-fileapi-findnextfilea) to look for DLLs or manifests in a specified location, and then use [**CreateActCtx**](/windows/desktop/api/Winbase/nf-winbase-createactctxa) to access the information. This method requires no registration of the component.

 

 
