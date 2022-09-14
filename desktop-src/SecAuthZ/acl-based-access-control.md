---
description: Just as the system uses security descriptors to control access to securable objects, a server can use security descriptors to control access to its private objects. For more information about the Windows security model, see Access Control Model.
ms.assetid: d6219438-711a-4eda-a893-9095bce3a07d
title: ACL-based Access Control
ms.topic: article
ms.date: 05/31/2018
---

# ACL-based Access Control

Just as the system uses [security descriptors](security-descriptors.md) to control access to securable objects, a server can use security descriptors to control access to its private objects. For more information about the Windows security model, see [Access Control Model](access-control-model.md).

A protected server can [create a security descriptor](security-descriptors-for-private-objects.md) with a DACL that specifies the types of access allowed for various [trustees](trustees.md). In a simple case, the server could create a single security descriptor to [control access to all of the server's data and functionality](checking-access-to-private-objects.md). For a finer granularity of protection, the server could create security descriptors for each of its private objects, or for different types of functionality.

For example, when a client asks the server to create a new object in a database, the server could create a security descriptor for the new private object. The server could then store the security descriptor with the private object in the database. When a client tries to access the object, the server retrieves the security descriptor to check the client's access rights. It is important to note that there is nothing in a security descriptor that associates it with the object or functionality it is protecting. Instead, it is up to the protected server to maintain the association.

Access to the private object can also be audited. Refer to [Auditing Access to Private Objects](auditing-access-to-private-objects.md) for a description of this.

 

 



