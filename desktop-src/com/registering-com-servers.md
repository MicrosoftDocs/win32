---
title: Registering COM Servers
description: Registering COM Servers
ms.assetid: aaa09a1b-deb8-424f-a911-ae22d39919d3
ms.topic: article
ms.date: 05/31/2018
---

# Registering COM Servers

After you have defined a class in code (ensuring that it implements [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) or [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2)) and assigned it a CLSID, you need to put information in the registry that will allow COM, on request of a client with the CLSID, to create instances of its objects. This information tells the system, for a given CLSID, where the DLL or EXE code for that class is located and how it is to be launched.

There is more than one way of registering a class in the registry. In addition, there are other ways of "registering" a class with the system when it is running, so that the system is aware that a running object is currently in the system.

See the following topics for more information about registering:

-   [Registering a Class at Installation](registering-a-class-at-installation.md)
-   [Registering a Running EXE Server](registering-a-running-exe-server.md)
-   [Registering Objects in the ROT](registering-objects-in-the-rot.md)
-   [Self-Registration](self-registration.md)
-   [Installing as a Service Application](installing-as-a-service-application.md)

## Related topics

<dl> <dt>

[COM Server Responsibilities](com-server-responsibilities.md)
</dt> </dl>

 

 