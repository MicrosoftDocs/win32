---
Description: 'The SCM supports handle types to allow access to the following objects.'
ms.assetid: '5ffdd1a9-1a66-4fc4-b35d-4f744bae4897'
title: SCM Handles
---

# SCM Handles

The SCM supports handle types to allow access to the following objects.

-   The database of installed services.
-   A service.
-   The database lock.

An SCManager object represents the database of installed services. It is a container object that holds service objects. The [**OpenSCManager**](openscmanager.md) function returns a handle to an SCManager object on a specified computer. This handle is used when installing, deleting, opening, and enumerating services and when locking the services database.

A service object represents an installed service. The [**CreateService**](createservice.md) and [**OpenService**](openservice.md) functions return handles to installed services.

The [**OpenSCManager**](openscmanager.md), [**CreateService**](createservice.md), and [**OpenService**](openservice.md) functions can request different types of access to SCManager and service objects. The requested access is granted or denied depending on the access token of the calling process and the security descriptor associated with the SCManager or service object.

The [**CloseServiceHandle**](closeservicehandle.md) function closes handles to SCManager and service objects. When you no longer need these handles, be sure to close them.

 

 



