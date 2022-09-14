---
title: Managing DNS Servers
description: Learn about managing DNS Servers. A DNS Server is a computer that completes the process of name resolution in DNS.
ms.assetid: 9ac68e35-112a-44d3-918d-2caea47b6e52
ms.topic: article
ms.date: 05/31/2018
---

# Managing DNS Servers

A DNS Server is a computer that completes the process of name resolution in DNS. DNS Servers contain files, called *zone files*, that enable them to resolve names to IP addresses (or vice versa). When queried, a DNS Server responds in one of three ways:

-   The server returns the requested name-resolution or IP-resolution information.
-   The server returns a pointer to another DNS Server that can service the request.
-   The server indicates that it does not have the requested information.

DNS Servers might, during the course of preparing to return the requested resolution information, query other DNS Servers. But beyond that, DNS Servers do not perform any operations other than those mentioned in the previous list.

There are three main kinds of DNS Servers — primary servers, secondary servers, and caching servers. See [DNS Servers](dns-servers.md) for more information on these DNS Servers.

## Administration Steps

The DNS WMI Provider enables the administration of DNS Servers from the server itself, or from remote hosts. The general steps necessary to administer a DNS Server using the DNS WMI Provider are:

-   Connecting to the DNS WMI Provider
-   Getting a server instance
-   Listing or modifying a server property, or using a method

To illustrate how to implement those administration steps, examples are provided. The following tasks are linked to their associated scripting samples.

-   [Stopping a DNS Server](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Starting a DNS Server](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Restarting a DNS Server](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Adding an IP Address](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Removing an IP Address](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Listing DNS Server Properties](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Displaying DNS Server Property Types](dns-wmi-provider-samples-managing-a-dns-server.md)
-   [Modifying DNS Server Properties](dns-wmi-provider-samples-managing-a-dns-server.md)

 

 




