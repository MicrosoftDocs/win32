---
description: Activation contexts enable COM objects to be used without requiring that they be registered.
ms.assetid: e6ec7b8b-8032-4dff-8f96-07ae3ffc286d
title: Creating Registration-Free COM Objects
ms.topic: article
ms.date: 05/31/2018
---

# Creating Registration-Free COM Objects

Activation contexts enable COM objects to be used without requiring that they be registered. This enables your application to have multiple components with different functionality based upon their version rather than their registry information. Multiple components can expose the same COM object with the same GUID but have different functionality based on the version.

When an application requests a GUID from [**CLSIDFromProgID**](/windows/win32/api/combaseapi/nf-combaseapi-clsidfromprogid), COM first searches for the mapping from progid to CLSID in the active activation context. When an application uses [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to obtain an instance interface pointer, COM searches in the active activation context to find which DLL will host the CLSID. If the activation context does not contain the required information, COM then searches for the information in the registry using the usual method.

Note that because activation contexts are per-thread, COM marshals the activation context of the creating thread over to the host thread and activates it before calling [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**DllGetClassObject**](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject) on the host thread. This functionality is already present in Windows, client code is not required to do anything to implement this.

COM classes can be exported by hosted components without going through the registry. Multiple components can expose the same ProgID for different COM objects, and your hosting application should only find the proper activation context and then use [**CLSIDFromProgID**](/windows/win32/api/combaseapi/nf-combaseapi-clsidfromprogid) and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get the hosted object's interface pointers.

 

 
