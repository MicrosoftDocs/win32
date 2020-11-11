---
title: Load Balancing Best Practices
description: Load Balancing Best Practices
ms.assetid: 260cf8dd-13b8-4b46-93a6-5333e794c0d3
ms.topic: article
ms.date: 05/31/2018
---

# Load Balancing Best Practices

Several best practices should be followed when setting up and configuring RPC Load balancing.

First, security should be set on incoming and outgoing LBS calls. This means both of the optional [NoSecurity](configuring-load-balancing.md) registry keys should either not be present or should be set to zero.

Second, attention must be paid to the front end load balancing solution used in conjunction with the RPC Load Balancing solution. For example, if the front end load balancer uses simple round robin load balancing, an odd number of servers should exist in the server farm. This is to mitigate the possibility of all connections being forwarded and thus serviced by the same server or servers.

For security, it is commonly desirable to have a firewall control access to RPC Proxy servers. If a port based firewall solution is employed, RPC endpoints must be static in order to limit the number of ports that are opened in the firewall. On Windows Server 2008 and later versions of Windows, RPC provides a mechanism to assign a static port to dynamic endpoints. This is achieved through the RPC netsh firewall commands. An example set of commands to set the LBS interface to the static port of 3010 is:

``` syntax
netsh rpc filter add rule layer=ep_add actiontype=permit

netsh rpc filter add condition field=process_with_if_uuid matchtype=equal data=
3357951c-a1d1-47db-a278-ab945d063d03

netsh rpc filter add condition field=protocol matchtype=equal data=ncacn_ip_tcp

netsh rpc filter add condition field=ep_value matchtype=equal data=w3010

netsh rpc filter add filter
```

The RPC netsh command can be used to set a static endpoint for any dynamic or static interface. This is useful when restricting access to a machine running a port based firewall solution. If the Windows firewall solution is used, the RPC interface can be blocked or enabled without having to assign it to a specific port. For more information, see the [RPC netsh firewall command reference](/previous-versions/windows/it-pro/windows-server-2003/cc784909(v=ws.10)).

 

 