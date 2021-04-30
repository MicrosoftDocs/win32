---
description: "Learn more about: WS-Discovery Specification Compliance"
ms.assetid: b795a385-b48d-4a16-9d91-e48bca120572
title: WS-Discovery Specification Compliance
ms.topic: article
ms.date: 05/31/2018
---

# WS-Discovery Specification Compliance

[WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf) describes how to perform the following tasks:

-   Announce the availability of services on the local subnet
-   Search for services on the subnet
-   Locate a previously referenced service

To accomplish this, WS-Discovery defines two one-way messages, [Hello](hello-message.md) and [Bye](bye-message.md), and two bidirectional search messages, [Probe](probe-message.md) and [Resolve](resolve-message.md).

WS-Discovery also provides addresses and a reserved port for IPv4 and IPv6 link local discovery. The specification also allows for alternate bindings to be defined elsewhere, such as the Probe over HTTP binding defined in the [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS).

The WS-Discovery specification describes elective functionality by using the terms MAY or SHOULD in a given implementation recommendation or restriction. Omitted functionality may be functionality described as REQUIRED in the WS-Discovery specification that was not implemented by WSDAPI, or it may be functionality that WSDAPI implemented in a method other in the one specified in the WS-Discovery specification.

This topic describes how WS-Discovery restrictions, requirements, and elective functionality are handled by the WSDAPI implementation. This topic is best read in tandem with the WS-Discovery specification.

## WS-Discovery and SOAP-over-UDP Support

In SOAP-over-UDP, Section 3.2 specifies that the UDP message must fit in a 64K datagram. WSDAPI will accept 64K UDP messages, but the DPWS constraint of MAX\_ENVELOPE\_SIZE (32K) will constrain the message size. As required by [WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf), WSDAPI supports the message patterns described in Section 4.

WSDAPI may be configured to support the security model in Sections 7 and 8. When so configured, WSDAPI will sign outbound WS-Discovery messages and will validate signatures on inbound messages.

WSDAPI implements the retransmission algorithm defined in Appendix I as amended by DPWS Appendix I.

In WS-Discovery, WSDAPI uses the addresses specified in section 2.4. WSDAPI extends APP\_MAX\_DELAY from section 2.4, but not to the extent as defined in DPWS Appendix I. For more information about APP\_MAX\_DELAY, see [Additional WS-Discovery Functionality](additional-ws-discovery-functionality.md).

WS-Discovery describes the `uuid:` URI format recommendation in section 2.6, but WSDAPI overrides this recommendation. Instead, WSDAPI uses the `urn:uuid:` URI format described in DPWS.

Section 3 of WS-Discovery describes how a client interacts with a discovery proxy. WSDAPI does not recognize this interaction and ignores announcements from discovery proxies. In Windows 7, WSDAPI implements a private extension to the WS-Discovery protocol, WS-Discovery Remote Extensions, to allow discovery clients to search for services spread across many different networks by sending requests to centralized proxies.For more information, see [Additional WS-Discovery Functionality](additional-ws-discovery-functionality.md).

Section 4.1, paragraph 3 of WS-Discovery requires that a timer must elapse before a [Hello](hello-message.md) message is sent. The hosting API does not wait before sending a Hello message. If a scenario requires a delay before a Hello message is sent, then the application developer must implement a wait.

WSDAPI implements all of the messages described in WS-Discovery Sections 4, 5, and 6. WSDAPI also enforces the MATCH\_TIMEOUT described in Section 7 as amended by DPWS Appendix I. WSDAPI only protects against "Replay" from the secure considerations in Section 9.

WSDAPI does implement application sequencing as described in WS-Discovery Appendix I.

 

 



