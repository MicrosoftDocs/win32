---
Description: The SCM supports handle types to allow access to the following objects.
ms.assetid: 5ffdd1a9-1a66-4fc4-b35d-4f744bae4897
title: SCM Handles
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCM Handles

The SCM supports handle types to allow access to the following objects.

-   The database of installed services.
-   A service.
-   The database lock.

An SCManager object represents the database of installed services. It is a container object that holds service objects. The [**OpenSCManager**](/windows/win32/Winsvc/nf-winsvc-openscmanagera?branch=master) function returns a handle to an SCManager object on a specified computer. This handle is used when installing, deleting, opening, and enumerating services and when locking the services database.

A service object represents an installed service. The [**CreateService**](/windows/win32/Winsvc/nf-winsvc-createservicea?branch=master) and [**OpenService**](/windows/win32/Winsvc/nf-winsvc-openservicea?branch=master) functions return handles to installed services.

The [**OpenSCManager**](/windows/win32/Winsvc/nf-winsvc-openscmanagera?branch=master), [**CreateService**](/windows/win32/Winsvc/nf-winsvc-createservicea?branch=master), and [**OpenService**](/windows/win32/Winsvc/nf-winsvc-openservicea?branch=master) functions can request different types of access to SCManager and service objects. The requested access is granted or denied depending on the access token of the calling process and the security descriptor associated with the SCManager or service object.

The [**CloseServiceHandle**](/windows/win32/Winsvc/nf-winsvc-closeservicehandle?branch=master) function closes handles to SCManager and service objects. When you no longer need these handles, be sure to close them.

 

 



