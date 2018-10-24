---
Description: Microsoft has implemented an array of extensions to the Navigator Auto-Config File Format in order to add IPv6 support in the WinINet and WinHTTP WPAD helper functions.
ms.assetid: 40116a01-b18f-432a-8542-b56b3f55c692
title: IPv6 Extensions to Navigator Auto-Config File Format
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Extensions to Navigator Auto-Config File Format

Microsoft has implemented an array of extensions to the Navigator Auto-Config File Format in order to add IPv6 support in the WinINet and WinHTTP WPAD helper functions.

The explosion of the Internet in the late 1990’s has caused an unexpected scarcity of IPv4 addresses, with the pool depleting on a daily basis. IPv6 provides a solution to this problem and although it is currently not widely deployed, its use will definitely become more prevalent in the future. [WPAD](http://go.microsoft.com/fwlink/p/?linkid=201408) is a protocol that allows web clients to automatically detect what the correct proxy configuration should be for their outgoing traffic. This is very useful for corporate deployments because it allows IT administrators to setup complex scripts that can route traffic for all clients to specific proxies based on the target server the clients are attempting to connect to. WinINet and WinHTTP support WPAD helper functions as defined by the [Navigator Proxy Auto-Config (PAC) File Format specification](http://go.microsoft.com/fwlink/p/?linkid=84541), which has become a defacto standard. Unfortunately this specification was written in 1996 and does not define what the function behaviors should be when a WPAD script is deployed in an IPv6 capable network.

Since IPv6 is the wave of the future, all Windows components now support dual stack (IPv4 and IPv6) and IPv6 only networks. In order to support IPv6 without affecting existing deployment, Microsoft added 6 new helper class functions as an extension to the Navigator Proxy Auto-Config (PAC) File Format specification and also added a new IPv6 capable function called **FindProxyForURLEx** that administrators can implement in the WPAD script.

<dl> <dt>

[IPv6-Aware Proxy Helper API Definitions](ipv6-aware-proxy-helper-api-definitions.md)
</dt> <dd></dd> <dt>

[Differences Between IPv6-Aware WPAD Helper Functions and Legacy WPAD Helper Functions](differences-between-ipv6-aware-wpad-helper-functions-and-legacy-wpad-helper-functions.md)
</dt> <dd></dd> </dl>

> [!Note]  
> This functionality requires Windows Internet Explorer 7 or greater.

 

 

 



