---
title: Out-of-Band Signaling
description: Cooperating applications that share common data using the directory can use out-of-band signaling to avoid both version skew and partial updates.
ms.assetid: 82960273-5cda-44d2-bc17-d604f34f5a9b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Out-of-Band Signaling

Cooperating applications that share common data using the directory can use out-of-band signaling to avoid both version skew and partial updates. Put simply, the cooperating applications use a mechanism separate from directory replication to inform each other of changes in the shared common data. Out-of-band signaling is most effective when used in combination with a versioning mechanism—this allows the partner detecting the change to notify remote partners what version of the shared data to wait for.

Returning to the RPC example given in the "Version Skew" section of [Replication Behavior in Active Directory Domain Services](replication-behavior-in-active-directory-domain-services.md), the RPC server could call back into connected clients to inform them of the move to a new server: "I am going to move. Please stand by, replication will bring you the new address shortly" so that the client can handle the transition period.

Applications that require identical policies to be in force in order to communicate with each other can use out-of-band signaling to ensure that a new policy is not employed until all involved parties have received it. For example, if the Internet Protocol security (IPsec) policy between two machines is changed, an agent on the source machine could contact an agent on the destination machine to negotiate the application of the changed policy, with the source machine delaying application until the destination machine has received the new policy as well.

 

 




