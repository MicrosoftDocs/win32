---
title: Using the Remote Desktop Virtualization API
description: Developers can use this API to customize the logic that RD Connection Broker uses to determine the best destination for an incoming client connection.
ms.assetid: b25eb87e-dac4-49ce-890e-b39c7e9e3408
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , using the virtualization API
ms.topic: article
ms.date: 05/31/2018
---

# Using the Remote Desktop Virtualization API

The Terminal Services Session Directory (TS  Session Directory) role service allows terminal servers to store user and session information in a database called a session directory. When a user connects to a terminal server in a farm, TS Session Directory determines whether the user already has a session running on a terminal server and if so, it redirects the user to that terminal server.

In Windows Server 2008, the TS Session Directory role service was expanded and renamed Terminal Services Session Broker (TS Session Broker). In addition to maintaining a directory of existing sessions, TS Session Broker can also broker incoming connections. When TS Session Broker receives an incoming connection from a user, it checks its database to determine whether the user has an existing session on a terminal server. If so, TS Session Broker redirects the connection to that same terminal server. If not, TS Session Broker determines which terminal server has the fewest connections and redirects the connection to that server.

Beginning with Windows Server 2008, Microsoft also released a public application programming interface (API) for monitoring and interacting with sessions on terminal servers. This API is described in [Remote Desktop Connection Broker Plug-in Reference](/windows/desktop/TermServ/terminal-services-virtualization-api-reference). Using this API, developers can create custom policy plug-ins that override the standard redirection logic of TS Session Broker. The custom plug-ins can redirect sessions to terminal servers, as well as virtual machines, virtual desktops, blade servers, and physical desktops.

In Windows Server 2008 R2, the architecture of Remote Desktop Connection Broker (RD Connection Broker) (formerly known as TS Session Broker) was expanded to support connections to virtual machines. The new architecture supports session management for virtual machines through the Remote Desktop Virtualization API. Developers can use this API to customize the logic that RD Connection Broker uses to determine the best destination for an incoming client connection.

Remote Desktop Virtualization API offers several benefits to developers:

-   The interfaces for working with physical terminal servers are similar to those for working with virtual machines.
-   Developers can replace all or part of the standard redirection logic. Developers can build on the code that ships with the product and do not have to write everything from scratch.
-   No additional management agent is required on the managing server or within the session.
-   TS Session Broker plug-ins developed for use with Windows Server 2008 are still supported.
-   The API also allows developers to create user interfaces for administration of both Remote Desktop Session Host (RD Session Host) servers (formerly known as "terminal servers") and virtual machines.

## Related topics

<dl> <dt>

[Remote Desktop Virtualization API Reference](terminal-services-virtualization-api-reference.md)
</dt> <dt>

[Remote Desktop Connection Broker Plug-in Reference](/windows/desktop/TermServ/terminal-services-virtualization-api-reference)
</dt> </dl>

 

 