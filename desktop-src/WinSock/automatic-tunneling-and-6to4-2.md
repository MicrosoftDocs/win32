---
description: Automatic tunneling with IPv4-compatible addresses and 6to4 both work through a route for a prefix that is on-link to interface \#2. The 32 bits following the prefix are extracted and used as an IPv4 destination address for the encapsulated packet.
ms.assetid: 92261a1b-2b7f-4a76-b98a-2631dc303618
title: IPv6 Automatic Tunneling and 6to4
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Automatic Tunneling and 6to4

Automatic tunneling with IPv4-compatible addresses and 6to4 both work through a route for a prefix that is on-link to interface \#2. The 32 bits following the prefix are extracted and used as an IPv4 destination address for the encapsulated packet.

Automatic tunneling uses the ::/96 prefix, which is enabled by default. It can be disabled by removing the route for ::/96.

6to4 uses the 2002::/16 prefix, which is not enabled by default.

 

 



