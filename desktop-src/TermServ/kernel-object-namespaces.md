---
title: Kernel object namespaces
description: Remote Desktop Services uses multiple namespaces for kernel objects; a global namespace is used primarily by services in client/server applications.
ms.assetid: 771e0bbf-bd73-4e87-aa1e-945c1287b517
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Kernel object namespaces

A Remote Desktop Services server has multiple namespaces for the following named kernel objects: events, semaphores, mutexes, waitable timers, file-mapping objects, and job objects. There is a global namespace used primarily by services in client/server applications. In addition, each client session has a separate namespace for these objects, such as in Windows Vista.

The separate client session namespaces enable multiple clients to run the same applications without interfering with each other. For processes started under a client session, the system uses the session namespace by default. However, these processes can use the global namespace by prepending the "Global\\" prefix to the object name. For example, the following code calls [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa) and creates an event object named CSAPP in the global namespace:

> [!Note]  
> The global namespace is not available for Windows Store apps.

 

`CreateEvent( NULL, FALSE, FALSE, "Global\\CSAPP" );`

Service applications in a Remote Desktop Services environment use the global namespace by default.

Session zero is only used for hosting services, and there is no console session, unlike previous versions of Windows.

The global namespace enables processes on multiple client sessions to communicate with a service application. For example, a client/server application might use a mutex object for synchronization. The server module can create the mutex object in the global namespace. Then a client session can use the "Global\\" prefix to open the mutex object.

Another use of the global namespace is for applications that use named objects to detect that there is already an instance of the application running in the system across all sessions. This named object must be created or opened in the global namespace instead of the per-session namespace. The more common case of running the application once per session is supported by default because the named object is created in a per session namespace.

In addition to the "Global\\" prefix, client processes can use the "Local\\" prefix to explicitly create an object in their session namespace. These keywords are case sensitive.

The "Session\\" prefix is reserved for system use and you should not use it in names of kernel objects.

Fast user switching is implemented by using Remote Desktop Services sessions. The first user to log on uses session one, the next user to log on uses session two, and so on. Kernel object names must follow the guidelines outlined for Remote Desktop Services so that applications can support multiple users.

The creation of a file-mapping object in the global namespace, by using [**CreateFileMapping**](/windows/desktop/api/winbase/nf-winbase-createfilemappinga), from a session other than session zero is a privileged operation. Because of this, an application running in an arbitrary Remote Desktop Session Host (RD Session Host) server session must have [SeCreateGlobalPrivilege](/windows/desktop/SecAuthZ/authorization-constants) enabled in order to create a file-mapping object in the global namespace successfully. The privilege check is limited to the creation of file-mapping objects, and does not apply to opening existing ones. For example, if a service or the system creates a file-mapping object, any process running in any session can access that file-mapping object provided that the user has the necessary access.

 

 