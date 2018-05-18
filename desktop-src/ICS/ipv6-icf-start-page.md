---
title: IPv6 Internet Connection Firewall
description: The IPv6 Internet Connection Firewall (IPv6 ICF) protects connections on which it is running from unsolicited network traffic.
ms.assetid: '5cd0c1b4-4aee-4571-81d9-ad4b62f45373'
keywords: ["IPv6 Internet Connection Firewall IPv6 ICF", "IPv6 Internet Connection Firewall IPv6 ICF ,start page", "IPv6 firewall", "IPv6, firewall"]
---

# IPv6 Internet Connection Firewall

## Purpose

The IPv6 Internet Connection Firewall (IPv6 ICF) protects connections on which it is running from unsolicited network traffic. The IPv6 ICF API makes it possible to programmatically manage the features of IPv6 ICF, making it possible to open and close ports on an IPv6 ICF network connection.

## Where applicable

The IPv6 ICF API is intended for situations in which a software application or setup program needs to make adjustments to the configuration of the home networking environment in which it runs. For example, a service that needs to receive unsolicited traffic on a connection that is firewalled with IPv6 ICF can use this API to open a port on that connection, and receive the unsolicited traffic.

## Developer audience

The IPv6 ICF API is designed for use by programmers using C/C++, Microsoft Visual Basic development system, Visual Basic Scripting Edition, and Microsoft JScript development software. Programmers should be familiar with networking concepts.

## Run-time requirements

The IPv6 ICF API is supported on Windows XP with Service Pack 1 (SP1) with the Advanced Networking Pack for Windows XP.

**Windows XP with SP2:** Calling the IPv6 ICF APIs produces no result and will return a 'not implemented' result code.

## In this section



| Topic                                                             | Description                                                                                                      |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [Overview](about-ipv6-firewall-configuration.md)<br/>      | General information about IPv6 Internet Connection Firewall.<br/>                                          |
| [Using](using-ipv6-firewall-configuration.md)<br/>         | Sample code that demonstrates how to use IPv6 Internet Connection Firewall.<br/>                           |
| [Reference](ipv6-firewall-configuration-reference.md)<br/> | Documentation for IPv6 Internet Connection Firewall interfaces, structures, and other code elements. <br/> |



 

 

 





