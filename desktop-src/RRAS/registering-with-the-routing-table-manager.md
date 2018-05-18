---
title: Registering with the Routing Table Manager
description: Before a client can access the routing table, it first must register with the routing table manager using the RtmRegisterEntity function.
ms.assetid: '9bdbe138-d31b-42bb-9c51-5f1c5e8a4ca7'
keywords: ["Routing Table Manager Version 2 RRAS , registering"]
---

# Registering with the Routing Table Manager

Before a client can access the routing table, it first must register with the routing table manager using the [**RtmRegisterEntity**](rtmregisterentity.md) function.

When a client registers, it passes to the routing table manager an [**RTM\_ENTITY\_INFO**](rtm-entity-info.md) structure. This structure contains the information that uniquely identifies a client, the address family, and the instance of the routing table manager with which the client is registering. A client can also establish the [**RTM\_EVENT\_CALLBACK**](rtm-event-callback.md) callback. The routing table manager will use this callback to notify the client of events such as change notifications and client registrations.

The routing table manager completes its registration processing and returns a handle to the client. The client must use this handle for all subsequent calls to RTMv2 functions.

The [**RtmRegisterEntity**](rtmregisterentity.md) function that is used in RTMv2 is analogous to the [**RtmRegisterClient**](rtmregisterclient.md) function that is used in RTMv1. The **RtmRegisterClient** function is obsolete, except for clients using IPX.

Once a client has finished interacting with the routing table manager, it must call [**RtmDeregisterEntity**](rtmderegisterentity.md). The routing table manager destroys the handle associated with the client. To avoid memory leaks, the client must ensure that it releases all handles and deletes all the routes and next hops that it owns before calling **RtmDeregisterEntity**.

For sample code that shows how to use these functions, see [Register with the Routing Table Manager](register-with-the-routing-table-manager.md) and [Use the Event Notification Callback](use-the-event-notification-callback.md).

 

 




