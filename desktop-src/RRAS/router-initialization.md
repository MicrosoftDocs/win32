---
title: Router Initialization
description: Configuration information for the router, the router managers and the routing protocols/clients is divided into global information and per interface information and is stored in the registry and the router's phone-book file, Router.pbk.
ms.assetid: c54541c1-6508-448a-a211-5fca634a184a
keywords:
- routers RRAS , initialization
ms.topic: article
ms.date: 05/31/2018
---

# Router Initialization

Configuration information for the router, the router managers and the routing protocols/clients is divided into global information and per interface information and is stored in the registry and the router's phone-book file, Router.pbk.

When the router process starts, DIM (Dynamic Interface Manager) reads the router configuration from the registry. DIM creates the interfaces that are specified by the interface information.

DIM also retrieves the global router manager information. DIM starts the router managers that correspond to this information, and passes them the information. For example, if DIM finds global information for the IP router manager in the registry, DIM starts the IP router manager and passes it the global information. If no global information is present in the registry for a particular router manager, DIM does not start that router manager.

The router managers examine the global information received from DIM. If the router manager finds information specific to a particular client within the global information, the router manager loads the DLL for the client (for example IpNAT.dll) and initializes the client by calling the client's [**RegisterProtocol**](/windows/desktop/api/Routprot/nc-routprot-pregister_protocol) and [**StartProtocol**](/windows/desktop/api/Routprot/nc-routprot-pstart_protocol) functions. The router manager passes the client-specific global information to the client in the call to [**StartProtocol**](/windows/desktop/api/Routprot/nc-routprot-pstart_protocol).

At each stage, the information being passed to the next entity is opaque to the entity preceding it. That is, DIM does not interpret the global information for the IP Router Manager, beyond the fact that the information is meant for the IP Router Manager. Similarly, the IP Router Manager does not interpret the OSPF specific information beyond the fact that it is OSPF information.

 

 




