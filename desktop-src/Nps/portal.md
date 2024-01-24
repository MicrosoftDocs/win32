---
title: Network Policy Server
description: Network Policy Server (NPS) is the Microsoft implementation of a Remote Authentication Dial-in User Service (RADIUS) server and proxy.
ms.assetid: d0eb41cb-e9c0-4a60-aeac-77d1dd90a75b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# Network Policy Server

## Purpose

Network Policy Server (NPS) is the Microsoft implementation of a Remote Authentication Dial-in User Service (RADIUS) server and proxy. It is the successor of Internet Authentication Service (IAS).

As a RADIUS server, NPS performs authentication, authorization, and accounting for wireless, authenticating switch, and remote access dial-up and virtual private network (VPN) connections.

NPS is also a health evaluator server for Network Access Protection (NAP). NPS performs authentication and authorization of network connection attempts and, based on configured system health policies, evaluates computer health compliance and determines how to limit a noncompliant computer's network access or communication. This is a new feature specific to NPS only; IAS does not support it. See [Internet Authentication Service and Network Policy Server](internet-authentication-service-vs-network-policy-server.md) for a complete list of features new to NPS.

NPS includes two API sets: NPS Extensions API and Server Data Objects (SDO) API. Both NPS Extensions API and SDO API are also supported by the precursor of NPS, the Internet Authentication Service.

NPS Extensions API can be used to extend the authentication, authorization, and accounting methods offered by NPS and previously by IAS.

Server Data Objects API can be used to manipulate the network policy configuration on a computer that runs NPS or IAS.

> [!Note]  
> Network policies in NPS are equivalent to remote access policies in IAS.

## Developer audience

The NPS Extensions API is designed for use by programmers using C/C++ development software. Programmers should be familiar with networking concepts and the RADIUS protocol. RADIUS is documented in [RFC 2865](https://www.ietf.org/rfc/rfc2865.txt) and [RFC 2866](https://www.ietf.org/rfc/rfc2866.txt).

The Server Data Objects API is designed for use by programmers using C/C++ or Visual Basic development software. Programmers should be familiar with [Remote Access Service](/windows/desktop/RRAS/remote-access-request-for-comments) (RAS) and the RADIUS protocol.

## Run-time requirements

NPS Extensions API is supported on Windows Server 2008 with the installation of the Microsoft Commercial Internet Service (MCIS).

Server Data Objects API is supported on Windows Server 2008.

NPS is available on Windows Server 2008 with the installation of the Microsoft Commercial Internet Service (MCIS).

## In this section

- General information regarding RADIUS, IAS, and NPS: [Overview](about-network-policy-server.md)
- API for implementing extension DLLs used for authentication, authorization, and accounting: [Network Policy Server Extensions API](ias-extensions.md)
- API for managing the network policy configuration: [Server Data Objects API](server-data-objects.md)
- Samples of stored procedures used for managing NPS (IAS) logging: [SQL Programmability](sql-programmability.md)

## Related topics

- [TechNet: Network Policy Server](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831683(v=ws.11))
- [Network Policy Server (NPS)](/windows-server/networking/technologies/nps/nps-top)
- [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
