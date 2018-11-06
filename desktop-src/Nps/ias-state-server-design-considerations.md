---
title: State Server Design Considerations
description: Depending on your design, you may need a server to track the users that are currently logged onto the network.
ms.assetid: 2f8d268b-5518-4ad2-aed6-5971c913db6d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# State Server Design Considerations

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

Depending on your design, you may need a server to track the users that are currently logged onto the network. The main challenge with the state server is keeping the information in the state server database in-sync with who is actually logged on. If the information in the state server is out of sync, users may succeed in having multiple sessions when they aren't authorized to do so. Also, users who do not have multiple sessions could be inadvertently penalized.

The following should be taken into consideration in implementing the state server:

-   The state server must make the decision online in a few seconds. For this reason the state server requires a scaleable infrastructure that can support many updates and queries per second. Relational databases are not appropriate for such large queries with simultaneous updates. Relational databases are primarily built to keep data consistent and to provide a consistent view of the data to all consumers. They are not built for quick updates.
-   Transactional consistency on updates between multiple objects is not important. This is because the state server can tolerate a small window of opportunity. However, transactional consistency of a single update is important to reduce the chances of leaving the state server in an inconsistent state if one of the RADIUS servers is shut down in the middle of the update.
-   Persistence (saving the state of the network to persistent storage) is not important because the persistent information will quickly fall out of sync with the actual state of the network.
-   If ISDN or other forms of multilink are supported on the network, the state server should be able to handle scenarios that use these features.

One possible design is to implement both an Authentication Extension DLL and an Authorization Extension DLL. Each of these DLLs can communicate over the network with a database. The Authorization Extension DLL can update the database with information about who is currently logged onto the network. The Authentication Extension DLL can query the database for this information to decide whether to accept or reject a particular user's authentication request; if the user is already logged on, the request is rejected.

The advantage of having the Authorization Extension DLL update the state-server database is that the Authorization Extension DLL has access to more information about the authenticated user. The Authorization Extension DLL has access to all of the authorization attributes from the NPS Authorization mechanism. For example, some users may have authorizations that allow them to have multiple sessions. The state server should treat such users as a special case.

 

 




