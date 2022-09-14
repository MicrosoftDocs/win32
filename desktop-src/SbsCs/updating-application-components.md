---
description: Side-by-side private assemblies can be used to create components that can be easily updated without also updating the hosting application.
ms.assetid: 5a45ee79-3ae1-4e9b-a77e-d4209fb23fa8
title: Updating Application Components
ms.topic: article
ms.date: 05/31/2018
---

# Updating Application Components

Side-by-side private assemblies can be used to create components that can be easily updated without also updating the hosting application. This allows an updating service to install the application's updated components, restart the application, and have the application use the changes. When using application manifests, the functionality of components hosted by an application can be updated without having to change the hosting application's code.

This method can be used to update the version of an application's resources. For example, if an application contains an assembly, the application's manifest can specify a dependency on this assembly. The application can get the assembly by calling [**SearchPath**](/windows/desktop/api/processenv/nf-processenv-searchpathw) to find and load the files it requires. An updater simply has to bring down the newest bits for the assembly, which can exist side-by-side with an earlier version of the assembly.

 

 
