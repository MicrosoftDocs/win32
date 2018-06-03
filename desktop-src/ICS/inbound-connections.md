---
title: Inbound Connections
description: Inbound Connections
ms.assetid: f32c41ef-c37c-477b-9599-c65c7a6ef068
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Inbound Connections

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. It is unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

There are two different methods to permit inbound connection attempts through the firewall for a port and protocol pair.

-   [INetFwV6Mgr::OpenGlobalPort](inetfwv6mgr-openglobalport.md)
-   [INetFwV6Connection::OpenPort](inetfwv6connection-openport.md)

A GlobalPort is a setting that grants access to a specific port and protocol pair across all interfaces or connections on the machine, even those that may be added in the future. A standard port setting applies to a specific port/protocol pair on only one specific connection. To instruct the firewall to allow inbound traffic to the port and protocol pair for any IPv6 connection-type that the machine has (including any that may be added in the future), use the [INetFwV6Mgr::OpenGlobalPort](inetfwv6mgr-openglobalport.md) method. To restrict this setting to a specific connection-type, use the [INetFwV6Connection::OpenPort](inetfwv6connection-openport.md) method.

When determining whether the firewall should allow traffic through on a connection for a port/protocol pair, the following rules are checked, in order:

-   If [INetFwV6Connection::OpenPort](inetfwv6connection-openport.md) has been called on the connection, the traffic is allowed.
-   If [INetFwV6Mgr::OpenGlobalPort](inetfwv6mgr-openglobalport.md) has been called for the port/protocol pair and [INetFwV6Connection::IgnoreGlobalPort](inetfwv6connection-ignoreglobalport.md) has not been called for the connection, the traffic is allowed.
-   Otherwise, since the port has not been opened, or opened globally but the connection has been specifically instructed to ignore the global setting, the traffic is allowed.

[INetFwV6Connection](inetfwv6connection.md) methods that query or alter the settings of a port/protocol pair are affect any global settings unless they specifically mention Global in the name of the method. This means that if the developer wishes to determine whether traffic is allowed on a given connection and port/protocol pair, it is not enough to merely query the [INetFwV6Connection::IsPortOpen](inetfwv6connection-isportopen.md) method. The developer must also examine whether the pair exists in the GlobalPort settings of the [INetFwV6Mgr](inetfwv6mgr.md), and whether this connection has been instructed to ignore the global setting. The [Querying an ICF Port](querying-an-icf-port.md) example illustrates this process in detail.

 

 




