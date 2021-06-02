---
description: The purpose of this topic is to describe the discovery functionality implemented by WSDAPI but not otherwise described in the DPWS or WS-Discovery specifications.
ms.assetid: ae7eff53-c932-4cba-9e71-c60f308f0e2d
title: Additional WS-Discovery Functionality
ms.topic: article
ms.date: 05/31/2018
---

# Additional WS-Discovery Functionality

In some cases, the [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS) and related specifications do not explicitly define implementation functionality. For example, the [WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf) specification does not define client and host behavior in multi-homed environments. When WSDAPI was implemented, some discovery functionality was added beyond the functionality defined in the specification.

WSDAPI also implements selected portions of WS-Discovery v1.1 CD1 for communicating with a discovery proxy over HTTP.

The purpose of this topic is to describe the discovery functionality implemented by WSDAPI but not otherwise described in the DPWS or WS-Discovery specifications.

## IPv6 addresses and the soap.udp URI format

SOAP-over-UDP and WS-Discovery do not explicitly describe how a literal IPv6 address is represented in the soap.udp URI format. [RFC 2396](https://www.ietf.org/rfc/rfc2396.txt), entitled "Uniform Resource Identifiers (URI): Generic Syntax", indicates that literal IPv6 addresses are not supported by the soap.udp URI format.

For simplicity, WSDAPI recognizes IPv6 addresses enclosed in square brackets in the soap.udp scheme. For example, the address `soap.udp://[2001:abcd:0001:0002:0003:0004:0005:0032]:3702` is recognized by WSDAPI. This is similar to how IPv6 addresses are handled in HTTP.

## Hello and XAddrs

WSDAPI's DPWS hosting object will never send a WS-Discovery [Hello](hello-message.md) message with [XAddrs](xaddr-validation-rules.md) in the message body. A client will always send a [Resolve](resolve-message.md) message after receiving a Hello message if the client needs to get the XAddrs.

There are two benefits of this approach. First, a device built on WSDAPI will never expose XAddrs that disclose the IP addresses of private networks. Secondly, a device built on WSDAPI only exposes XAddrs that are accessible to the client, which means that IPv6 addresses are never sent to an IPv4 client.

When a [Probe](probe-message.md) or Resolve message is received, only a single XAddr is sent in response. The sent XAddr corresponds to the local address on which the request was received. If the request was received across subnets over IPv6, WSDAPI will provide a global IPv6 address in the response.

## Preferred addresses

A device can provide multiple XAddrs in a [Hello](hello-message.md), [ProbeMatch](probematches-message.md), or [ResolveMatch](resolvematches-message.md) message. A service can also be available at multiple endpoints with different transport addresses. In these cases, WSDAPI will try to communicate with the device on the first usable address it finds. An address is usable if it is from an available protocol, such as IPv4 on a machine where IPv4 is installed or IPv6 on a machine where IPv6 is installed. Additionally, if the address came from a device or service that is not on the local subnet, it is usable only if it is IPv4, IPv6 site local, or IPv6 link local.

## WSDL in metadata exchange

Devices and services built on WSDAPI do not provide their WSDL in metadata exchange unless extended by the application to provide this information. By default, WSDL provision is not part of the programming model.

## APP\_MAX\_DELAY

DPWS defines APP\_MAX\_DELAY, the random interval to delay between receiving a [Probe](probe-message.md) and sending a [ProbeMatch](probematches-message.md), as 5,000 milliseconds. Windows Firewall requires that the multicast request/unicast response model for UDP will only work within the 4 second firewall window. As a result, WSDAPI will transmit responses in 2,500 ms or less, instead of the 5,000 ms window described by APP\_MAX\_DELAY.

## IANA port reservations

WSDAPI uses TCP port 5357 for HTTP traffic and TCP port 5358 for HTTPS traffic by default. These ports are reserved for lower privilege processes through a URL reservation in HTTP.sys, and are also reserved with IANA.

## UDP port sharing

WSDAPI uses port sharing. Unicast messages sent to port 3702 may not be properly handled by all WSDAPI-based applications. If an application binds exclusively to port 3702, it may prevent WSDAPI-based applications from using that port correctly.

## WS-Discovery v1.1 CD1 Proxy

WSDAPI will search for and communicate with a discovery proxy that implements the WS-Discovery v1.1 CD1 managed mode protocol. WS-Discovery v1.1 CD1 is the first revision of WS-Discovery to include an explicit description of an HTTP protocol for communication between a proxy and a client or device.

To limit the number of concurrent versions used in multicast requests, WSDAPI sends a WS-Discovery Probe request in the 2005/04 namespace, but searches for the WS-Discovery v1.1 CD1 DiscoveryProxy type. If a proxy responds, WSDAPI will send an HTTP Probe or Resolve request to the specified proxy endpoint as defined in WS-Discovery v1.1 CD1.

 

 



