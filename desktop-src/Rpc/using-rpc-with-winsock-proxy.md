---
title: Using RPC with Winsock Proxy
description: Using RPC with Winsock Proxy
ms.assetid: d36e2737-f6a0-40ce-92e0-058976c08eb6
ms.topic: article
ms.date: 05/31/2018
---

# Using RPC with Winsock Proxy

The release of Microsoft Internet Access Server included Winsock Proxy, an enhanced version of Windows Sockets API version 1.1. Winsock Proxy lets a Windows Sockets application, running on a private network client, behave as if it were directly connected to a remote Internet server application. The Microsoft Proxy Server acts as the host for this connection. This means that all application-level communications are channeled through a single secured computer—the gateway computer running Microsoft Proxy Server.

Ordinarily, for datagram-packet transfers, the RPC transport DLL bypasses the [**sendto**](/windows/desktop/api/winsock/nf-winsock-sendto) and [**recvfrom**](/windows/desktop/api/winsock/nf-winsock-recvfrom) functions provided in Wsock32.dll, and communicates directly with the underlying device driver. This improves the speed of packet transfers but makes Winsock Proxy features unavailable to the application.

Each network protocol provider to have an associated GUID. The RPC run-time library compares the UDP and IPX GUIDs to the well known Microsoft identifiers. If they don't match, RPC automatically uses Winsock.

Another feature of Winsock Proxy is its ability to emulate the TCP transport protocol over the Novell SPX transport when the SPX client computer does not have TCP installed. To use this feature with RPC applications, edit the system registry on each client computer to add this entry:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Rpc\ClientProtocols
   ncacn_ip_tcp = "rpcltccm.dll"<dl>
<dt>

   Data type
</dt>
<dd>   REG_SZ</dd>
</dl>
   ncadg_ip_udp = "rpcltccm.dll"<dl>
<dt>

   Data type
</dt>
<dd>   REG_SZ</dd>
</dl>
```

Edit the registry on each server computer to add this entry:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Rpc\ServerProtocols
   ncacn_ip_tcp = "rpcltscm.dll"<dl>
<dt>

   Data type
</dt>
<dd>   REG_SZ</dd>
</dl>
   ncadg_ip_udp = "rpcltscm.dll"<dl>
<dt>

   Data type
</dt>
<dd>   REG_SZ</dd>
</dl>
```

For more information about RPC transport protocols see [Specifying Protocol Sequences](specifying-protocol-sequences.md). For more information about Winsock Proxy, see the product documentation for Microsoft Internet Access Server.

Windows 2000 does not implement the **ClientProtocols** and **ServerProtocols** registry entries. Microsoft provides all well known transports as part of the run-time library. Therefore, these entries are not necessary.

 

 