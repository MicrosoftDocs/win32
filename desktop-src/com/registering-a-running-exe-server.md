---
title: Registering a Running EXE Server
description: Registering a Running EXE Server
ms.assetid: 277f44bb-72b7-4409-955d-2cd53bc99467
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registering a Running EXE Server

When an executable (EXE) server is launched, it should call [**CoRegisterClassObject**](/windows/win32/combaseapi/nf-combaseapi-coregisterclassobject?branch=master), which registers the CLSID for the server in what is called the class table (a different table than the running object table). When a server is registered in the class table, it allows the service control manager (SCM) to determine that it is not necessary to launch the class again, because the server is already running. Only if the server is not listed in the class table will the SCM check the registry for appropriate values and launch the server associated with the given CLSID.

You pass [**CoRegisterClassObject**](/windows/win32/combaseapi/nf-combaseapi-coregisterclassobject?branch=master) the CLSID for the class and a pointer to its [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) interface. Clients who subsequently call [**CoGetClassObject**](/windows/win32/combaseapi/nf-combaseapi-cogetclassobject?branch=master) with this CLSID will retrieve a pointer to their requested interface, as long as security does not forbid it. (See [Instance Creation Helper Functions](instance-creation-helper-functions.md) for a description of several instance creation and activation functions.)

The server for a class object should call [**CoRevokeClassObject**](/windows/win32/combaseapi/nf-combaseapi-corevokeclassobject?branch=master) to revoke the class object (remove its registration) when all of the following are true:

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

 

 




