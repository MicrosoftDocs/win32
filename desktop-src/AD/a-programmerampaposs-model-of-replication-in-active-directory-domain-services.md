---
title: A Programmer's Model of Replication in Active Directory Domain Services
description: The following is a description of the replication model for Active Directory Domain Services.
ms.assetid: 45baf7ff-9474-4f86-81c8-03336901fec2
ms.tgt_platform: multiple
keywords:
- A Programmer's Model of Active Directory Replication AD
- A Programmer's Model of Replication in Active Directory Domain Services
ms.topic: article
ms.date: 05/31/2018
---

# A Programmer's Model of Replication in Active Directory Domain Services

The following is a description of the replication model for Active Directory Domain Services.

All updates to the Active Directory Domain Controller (DC) are performed using LDAP requests that create, modify, or delete one object for each request. A single request can set or modify multiple attributes on an object.

An update request is processed as an atomic transaction at some DC. Either the entire update happens or none of it does. If the requester receives a successful response to an update request, that entire request has succeeded (committed). This is called an "originating write." Multiple LDAP requests cannot be grouped into a single larger transaction.

In an originating write, a DC computes a "stamp" for each new or modified attribute value, and attaches this stamp to the value so when the value is replicated, the stamp is replicated too. The new stamp is unique, and in case of an update, the new stamp is larger than the stamp on the old value at that DC.

Occasionally, a DC selects the set of objects that have changed since the last time the DC performed replication. Then, for each object, it sends a single message to all other DCs that contain all the current values of attributes changed since the last time the object was replicated. Replication messages are reliable and are delivered in order, but may require more time to be delivered.

When one DC receives a replication message from another DC, it processes it as follows: For each modified attribute, if the stamp on the value in the replication message is larger than the stamp on the current value, the DC applies the update; otherwise the DC discards the update. Each replication message is applied as an atomic transaction, just like an originating write.

That is the Active Directory Domain Services replication model. Key properties of this model include:

-   An originating write to a single object is atomic.
-   When replicating changes, either all the changes made by an originating write are sent or none of them are.
-   A replicated write to a single object is atomic, but conflicts are resolved attribute-by-attribute.

The model does not guarantee the replication ordering of changes made to different objects. Do not write applications that assume that changes are replicated in originating-write order. The model does not guarantee that if an attribute of an object is changed twice, both values will be replicated; Replication sends only the current value at the time of replication.

The model differs from reality in several ways that only affect performance. For example, the Active Directory Server sends replication messages containing the changes to multiple objects, but processes the contents of such a multi-object message as if it were a series of single-object messages. The Active Directory Server does not perform point-to-point replication as described in the model, but instead performs a more complex and more efficient transitive replication that is functionally equivalent to the model.

 

 




