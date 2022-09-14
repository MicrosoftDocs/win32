---
title: Registering a Running EXE Server
description: Registering a Running EXE Server
ms.assetid: 277f44bb-72b7-4409-955d-2cd53bc99467
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Running EXE Server

When an executable (EXE) server is launched, it should call [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject), which registers the CLSID for the server in what is called the class table (a different table than the running object table). When a server is registered in the class table, it allows the service control manager (SCM) to determine that it is not necessary to launch the class again, because the server is already running. Only if the server is not listed in the class table will the SCM check the registry for appropriate values and launch the server associated with the given CLSID.

You pass [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) the CLSID for the class and a pointer to its [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. Clients who subsequently call [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) with this CLSID will retrieve a pointer to their requested interface, as long as security does not forbid it. (See [Instance Creation Helper Functions](instance-creation-helper-functions.md) for a description of several instance creation and activation functions.)

The server for a class object should call [**CoRevokeClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-corevokeclassobject) to revoke the class object (remove its registration) when all of the following are true:

-   There are no existing instances of the object definition.
-   There are no locks on the class object.
-   The application providing services to the class object is not under user control (not visible to the user on the display).

## Related topics

<dl> <dt>

[Installing as a Service Application](installing-as-a-service-application.md)
</dt> <dt>

[Registering a Class at Installation](registering-a-class-at-installation.md)
</dt> <dt>

[Registering Objects in the ROT](registering-objects-in-the-rot.md)
</dt> <dt>

[Self-Registration](self-registration.md)
</dt> </dl>

 

 




