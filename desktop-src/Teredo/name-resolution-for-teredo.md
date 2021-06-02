---
title: Name Resolution For Teredo
ms.assetid: eb0cf6d5-f093-46f6-8995-d01971de8241
description: "Learn more about: Name Resolution For Teredo"
ms.topic: article
ms.date: 05/31/2018
---

# Name Resolution For Teredo

The Teredo interface currently utilizes the following protocols for name resolution:

## Domain Name System

The Domain Name System (DNS) is currently the most prominent name resolution technology on the Internet. Most web servers register URL addresses with DNS servers. However, the addresses of a home network are not registered with DNS servers since most home users obtain IP addresses via Dynamic Host Configuration Protocol (DHCP) from their Internet Service Provider. DHCP leases are of relatively short duration and take anywhere from 48 to 72 hours to propagate a name throughout the DNS cloud. As a result DNS has proven to be an ineffective method of obtaining a home user's public IP address. A Teredo address includes the public IPv4 address and hence inherits at least the same volatility of the IPv4 addresses. Hence, Teredo addresses are currently not registered in DNS.

## Peer Name Resolution Protocol

The Peer Name Resolution Protocol (PNRP) is a distributed DNS technology that stores IP addresses on thousands of user machines that are a part of a PNRP cloud. Using Windows Vista, any home user can choose to become a member of a PNRP cloud and advertise their Teredo IPv6 address on the PNRP network. Unlike addresses given to DNS servers, addresses on the PNRP network often take less than a minute to propagate. Since Teredo addresses can change frequently (external IPv4 address provided by the ISP can change or the external port used by the user's internet gateway device can change), PNRP has proven to be an effective mechanism for home users. PNRP names, addresses ending with ".pnrp.net" are based on a unique system properties that do not change. As a result a PNRP name is a reliable way to connect to a home user. The [**WSAConnectByName**](/windows/desktop/api/winsock2/nf-winsock2-wsaconnectbynamea) API can be used to obtain IP address using PNRP technology (DNS names ending with ".pnrp.net") and establish connection with other hosts.

 

 
