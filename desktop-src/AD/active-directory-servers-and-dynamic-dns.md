---
title: Active Directory Servers and Dynamic DNS
description: The Active Directory servers publish their addresses such that clients can find them knowing only the domain name.
ms.assetid: b4928d53-2629-4ddb-bb43-ce7a187b41e2
ms.tgt_platform: multiple
keywords:
- dynamic DNS Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Active Directory Servers and Dynamic DNS

The Active Directory servers publish their addresses such that clients can find them knowing only the domain name. Active Directory servers are published using the Service Resource Records (SRV RRs) in DNS. The SRV RR is a DNS record used to map the name of a service to the address of a server that offers the service. The name of a SRV RR is in this form:


```C++
<service>.<protocol>.<domain>
```



Active Directory servers offer the LDAP service over the TCP protocol so that published names are "ldap.tcp.&lt;domain&gt;". Thus, the SRV RR for fabrikam.com is "ldap.tcp.fabrikam.com". Additional data about the SRV RR indicates the priority and weight for the server, enabling clients to choose the best server for their needs.

When an Active Directory server is installed, it uses Dynamic DNS to publish itself. Because TCP/IP addresses are subject to change, servers periodically verify their registrations to be sure they are correct, and update them if necessary.

Dynamic DNS is a recent addition to the DNS standard. Dynamic DNS defines a protocol for dynamically updating a DNS server with new data. Prior to Dynamic DNS, administrators were required to manually configure the records stored by DNS servers.

 

 




