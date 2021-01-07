---
description: The system uses objects and handles to regulate access to system resources for two main reasons.
ms.assetid: 122acb9e-2a1b-480b-9207-5cc6bbe6b6d4
title: About Handles and Objects
ms.topic: article
ms.date: 05/31/2018
---

# About Handles and Objects

The system uses objects and handles to regulate access to system resources for two main reasons. First, the use of objects ensures that Microsoft can update system functionality, as long as the original object interface is maintained. When subsequent versions of the system are released, you can use the updated object with little or no additional work.

Secondly, the use of objects enables you to take advantage of Windows security. Each object has its own access-control list (ACL) that specifies the actions a process can perform on the object. The system examines an object's ACL each time an application creates a handle to the object. For more information, see [Access Control](/windows/desktop/SecAuthZ/access-control).

-   [Object Manager](object-manager.md)
-   [Object Interface](object-interface.md)
-   [Object Namespaces](/windows/desktop/Sync/object-namespaces)
-   [Handle Limitations](handle-limitations.md)
-   [Handle Inheritance](handle-inheritance.md)

 

 
