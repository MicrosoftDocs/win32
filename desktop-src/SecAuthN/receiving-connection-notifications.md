---
description: Some applications need to receive notification of connection events, either before the event, just after it occurs, or both. You can create a DLL to receive advance and after-the-fact notification of connection events.
ms.assetid: 692eb8f2-1c53-4535-b44d-babb30eecd9c
title: Receiving Connection Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Connection Notifications

Some applications need to receive notification of connection events, either before the event, just after it occurs, or both. You can create a DLL to receive advance and after-the-fact notification of connection events.

An example of an application that needs to receive advance notification of a connection event is the Remote Access Service (RAS). RAS needs to be informed before a connection is made because it may be necessary to establish a modem connection before making the network connection.

Similarly, applications may need to clean up resources after the connection is made, therefore requiring a post-connection notification.

Applications interested in receiving advance and after-the-fact notification of connection events must supply a DLL that exports two functions, [**AddConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-addconnectnotify) and [**CancelConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-cancelconnectnotify).

After you implement these functions, you must register your DLL as described in [Registering to Receive Connection Notifications](registering-to-receive-connection-notifications.md).

 

 



