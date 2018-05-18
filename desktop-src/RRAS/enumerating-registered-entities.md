---
title: Enumerating Registered Entities
description: After a client has registered, the client can obtain a list of all the other clients that have registered with the routing table manager. Some clients must perform certain operations if the presence of a particular type of client is detected.
ms.assetid: 'd94de573-7c1e-4179-a41f-5836d2c5d44a'
---

# Enumerating Registered Entities

After a client has registered, the client can obtain a list of all the other clients that have registered with the routing table manager. Some clients must perform certain operations if the presence of a particular type of client is detected.

The client can call the [**RtmGetRegisteredEntities**](rtmgetregisteredentities.md) function. A buffer of [**RTM\_ENTITY\_INFO**](rtm-entity-info.md) structures is returned. After the client has processed this information, the client should call [**RtmReleaseEntities**](rtmreleaseentities.md) to release the handles in the **RTM\_ENTITY\_INFO** structures.

If the routing table manager client supplied a callback function in the call to [**RtmRegisterEntity**](rtmregisterentity.md), the client is notified when any other clients register or unregister.

For sample code that shows how to use these functions, see [Enumerate the Registered Entities](enumerate-the-registered-entities.md) and [Use the Event Notification Callback](use-the-event-notification-callback.md).

 

 




