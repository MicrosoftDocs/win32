---
title: Registering a Class at Installation
description: If a class is intended to be available to clients at any time, as most applications are, you usually register it through an installation and setup program.
ms.assetid: 6d78c2ce-56d8-4866-9801-35125ec9cac4
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Class at Installation

If a class is intended to be available to clients at any time, as most applications are, you usually register it through an installation and setup program. This means putting information about the application into the registry, including how and where its objects are to be instantiated. This information must be registered for all CLSIDs. Other information is optional. Tools such as Regsvr32 make it simple to write a setup program that registers servers at installation.

If you are not relying on system defaults, there are two important keys in the registry: the CLSID and the AppID. Among the important pieces of information under these keys is how the object is to be instantiated. Objects can be designated as in-process, out-of-process local, or out-of-process remote.

Under the AppID key are several values that define information specific to that application. Among these are [RemoteServerName](remoteservername.md) and [ActivateAtStorage](activateatstorage.md), both of which can be used to permit a client to create an object, with the client having no built-in knowledge of the location of the server. (For more information about remote instantiation, see [Locating a Remote Object](locating-a-remote-object.md) and [Instance Creation Helper Functions](instance-creation-helper-functions.md).)

A server can also be installed as a service, or to run under a specific user account. For more information, see [Installing as a Service Application](installing-as-a-service-application.md).

A server or ROT object that is not a service or running under a specific user account can be referred to as an "activate as activator" server. For these servers, the security context and the window station/desktop of the client must match the server's. A client attempting to connect to a remote server is considered to have a **NULL** window station/desktop, so only the server security context is compared in this instance. (For more information about SIDs, see [Security in COM](security-in-com.md).) COM caches the window station/desktop of a process when the process first connects to the distributed COM service. Therefore, COM clients and servers should not change their window station or thread desktops of the process after calling [**CoInitialize**](/windows/desktop/api/Objbase/nf-objbase-coinitialize) or [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex).

When a class is registered as in-process, a call to [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) to create its class object is automatically passed by COM to the [**DllGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-dllgetclassobject) function, which the class must implement to give the calling object a pointer to its class object.

Classes implemented in executables can specify that COM should execute their process and wait for the process to register their class object's [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface through a call to the [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) function.

## Related topics

<dl> <dt>

[COM Registry Keys](com-registry-keys.md)
</dt> <dt>

[Installing as a Service Application](installing-as-a-service-application.md)
</dt> <dt>

[Registering a Running EXE Server](registering-a-running-exe-server.md)
</dt> <dt>

[Registering Components](registering-components.md)
</dt> <dt>

[Registering Objects in the ROT](registering-objects-in-the-rot.md)
</dt> <dt>

[Self-Registration](self-registration.md)
</dt> </dl>

 

 