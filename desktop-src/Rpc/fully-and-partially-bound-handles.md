---
title: Fully and Partially Bound Handles
description: When you use dynamic endpoints, the run-time libraries obtain endpoint information as they need it.
ms.assetid: 13f2f783-2c10-4122-ba4d-a97b9c0378c1
ms.topic: article
ms.date: 05/31/2018
---

# Fully and Partially Bound Handles

When you use dynamic endpoints, the run-time libraries obtain endpoint information as they need it. The run-time libraries make the distinction between a *fully bound handle* (one that includes endpoint information) and a *partially bound handle* (one that does not include endpoint information).

The client run-time library must convert the partially bound handle to a fully bound handle before the client can bind to the server. The client run-time library tries to convert the partially bound handle for the client application by obtaining the endpoint information as shown:

-   From the client's interface specification
-   From an endpoint-mapping service running on the server

If the client tries to use a partially bound handle when the endpoint information is not available in the interface specification and the server's endpoint-mapper does not have information about the server endpoint, the client will not have enough information to make its remote procedure call and that call will fail. To prevent this, you must register the endpoint in the endpoint mapper when your distributed application uses partially bound handles. For more information about the endpoint mapper, see [Specifying Dynamic Endpoints](specifying-endpoints.md).

When a remote procedure call fails, the client application can call [**RpcBindingReset**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingreset) to remove out-of-date endpoint information. When the client tries to call the remote procedure, the client run-time library again tries to convert the fully bound handle to a partially bound handle. This is useful when the server has been stopped and restarted using a different dynamic endpoint.

 

 




