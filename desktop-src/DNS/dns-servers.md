---
title: DNS Servers
description: Learn about DNS Servers. A DNS Server is a computer that completes the process of name resolution in DNS.
ms.assetid: c7ce6e46-491c-482e-8d72-a79b911c3f68
keywords:
- DNS Servers
ms.topic: article
ms.date: 05/31/2018
---

# DNS Servers

A *DNS Server* is a computer that completes the process of name resolution in DNS. DNS Servers contain [*zone files*](z-gly.md) that enable them to resolve names to IP addresses and IP addresses to names. When queried, a DNS Server will respond in one of three ways:

-   The server returns the requested name-resolution or IP-resolution data.
-   The server returns a pointer to another DNS Server that can service the request.
-   The server indicates that it does not have the requested data.

DNS Servers might, during the course of preparing to return the requested resolution data, query other DNS Servers, but beyond that, DNS Servers do not perform any other operations.

There are three main kinds of DNS Servers — primary servers, secondary servers, and caching servers.

## Primary Server

The *primary server* is the authoritative server for the zone. All administrative tasks associated with the zone (such as creating subdomains within the zone, or other similar administrative tasks) must be performed on the primary server. In addition, any changes associated with the zone or any modifications or additions to RRs in the zone files must be made on the primary server. For any given zone, there is one primary server, except when you integrate Active Directory services and Microsoft DNS Server.

## Secondary Servers

*Secondary servers* are backup DNS Servers. Secondary servers receive all of their zone files from the primary server zone files in a zone transfer. Multiple secondary servers can exist for any given zone — as many as necessary to provide [*load balancing*](l-gly.md), [*fault tolerance*](f-gly.md), and traffic reduction. Additionally, any given DNS Server can be a secondary server for multiple zones.

In addition to primary and secondary DNS Servers, additional DNS Server roles can be used when such servers are appropriate for a DNS infrastructure. These additional servers are caching servers and [*forwarders*](f-gly.md).

## Caching Servers

[*Caching servers*](c-gly.md), also known as caching-only servers, perform as their name suggests; they provide only cached-query service for DNS responses. Rather than maintaining zone files like other secondary servers do, caching DNS Servers perform queries, cache the answers, and return the results to the querying client. The primary difference between caching servers and other secondary servers is that other secondary servers maintain zone files (and do zone transfers when appropriate, thereby generating network traffic associated with the transfer), caching servers do not.

 

 




