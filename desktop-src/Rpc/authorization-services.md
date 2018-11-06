---
title: Authorization Services
description: An authorization service is the method that the SSP uses to authorize access to a remote procedure. SSPs can provide more than one authorization service. However, they usually select one as a default.
ms.assetid: 5ea3cde9-96e9-4208-bb61-d0f98f23b90c
ms.topic: article
ms.date: 05/31/2018
---

# Authorization Services

An authorization service is the method that the SSP uses to authorize access to a remote procedure. SSPs can provide more than one authorization service. However, they usually select one as a default.

Your application can use the default authorization method for the current SSP, or it can specify one. At present, Microsoft RPC supports two methods of authorization. One is for the server to provide authorization based on the name of the client program. The other is for the server to compare the client's authentication credentials against the server's access control list (ACL).

For a list of authorization services, see [Authorization-Service Constants](authorization-service-constants.md).

> [!Note]  
> It is recommended that developers use RPC\_C\_AUTHZ\_NONE.

 

 

 




