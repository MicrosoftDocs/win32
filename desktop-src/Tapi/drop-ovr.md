---
description: Dropping or disconnecting a session terminates communication. The application has the option of sending user-user information at the time of the disconnect, if the service provider supports it.
ms.assetid: dc348bb2-d564-40f8-afe3-5473c5769fa4
title: Drop
ms.topic: article
ms.date: 05/31/2018
---

# Drop

Dropping or disconnecting a session terminates communication. The application has the option of sending user-user information at the time of the disconnect, if the service provider supports it.

The usual reasons for dropping a session is a user has requested a disconnect or the other end of the session has dropped. A drop operation may also be called when TAPI offers a session to the application. If the service provider supports this, the effect is that the application rejects the call.

When invoking a drop operation, related sessions can sometimes be affected as well. For example, dropping a conference call can drop all individual participants. State change messages are sent to the application for all calls whose state is affected.

In various bridged or party-line configurations when multiple parties are on the call, a drop operation may not actually clear the call. For example, in a bridged situation, the call may not be dropped because the status of other stations on the call may govern. Instead, the call may simply be changed to the inactive state while remaining connected at other stations.

Following a drop operation, the session identifier and most resources associated with the session will remain usable for most query operations. When an application no longer requires these resources, it must [terminate the session](terminate-a-session-ovr.md) in order to avoid memory leaks.

**TAPI 2.x:** See [**lineDrop**](/windows/win32/api/tapi/nf-tapi-linedrop).

**TAPI 3.x:** See [**ITBasicCallControl::Disconnect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-disconnect).

 

 
