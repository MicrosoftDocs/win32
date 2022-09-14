---
title: Registering COM Applications
description: Registering COM Applications
ms.assetid: 64ab5b42-2fdb-4d06-bd58-fd76f27f7da4
ms.topic: article
ms.date: 05/31/2018
---

# Registering COM Applications

The registry is a system database that contains information about the configuration of system hardware and software as well as about users of the system. Any Windows-based program can add information to the registry and read information back from the registry. Clients search the registry for interesting components to use.

The registry maintains information about all the COM objects installed in the system. Whenever an application creates an instance of a COM component, the registry is consulted to resolve either the CLSID or ProgID of the component into the pathname of the server DLL or EXE that contains it. After determining the component's server, Windows either loads the server into the process space of the client application (in-process components) or starts the server in its own process space (local and remote servers). The server creates an instance of the component and returns to the client a reference to one of the component's interfaces.

For more information about the Windows registry, see the following topics:

-   [Registry Hierarchy](registry-hierarchy.md)
-   [Classes and Servers](classes-and-servers.md)
-   [Classifying Components](classifying-components.md)
-   [Using OleView](using-oleview.md)
-   [Registering Components](registering-components.md)
-   [Checking Registration](checking-registration.md)
-   [Unknown User Types](unknown-user-types.md)
-   [COM Registry Keys](com-registry-keys.md)

 

 




