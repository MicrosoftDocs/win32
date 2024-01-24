---
description: This topic describes how WSDAPI implements the elective functionality in the Devices Profile for Web Services (DPWS) specification. It also describes which DPWS functionality was omitted from the WSDAPI implementation.
ms.assetid: 54d51e56-8022-4696-b488-4b3a226224d8
title: DPWS Specification Compliance
ms.topic: article
ms.date: 05/31/2018
---

# DPWS Specification Compliance

This topic describes how WSDAPI implements the elective functionality in the [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS) specification. It also describes which DPWS functionality was omitted from the WSDAPI implementation.

The DPWS specification provides a consistent way to message with devices. It also adds specific restrictions and recommendations that simplify the process of supporting web services on embedded hardware.

The DPWS specification describes elective functionality by using the terms MAY or SHOULD in a given implementation recommendation or restriction. Omitted functionality may be functionality described as REQUIRED in the DPWS specification that was not implemented by WSDAPI, or it may be functionality that WSDAPI implemented in a method other in the one specified in the DPWS specification.

This topic follows the layout of the DPWS section by section. Each section describes how specific restrictions, requirements, and elective functionality are handled by the WSDAPI implementation. This topic is best read in tandem with the DPWS specification.

## DPWS 3.0 Messaging

### DPWS 3.1 URI formats

Restrictions R0025 and R0027 constrain URIs to MAX\_URI\_SIZE octets. WSDAPI enforces both of these restrictions as specified.

### DPWS 3.2 UDP messaging

Recommendation R0029 suggests that UDP packets larger than the maximum transfer unit (MTU) for UDP should not be sent. WSDAPI does not implement this recommendation, and will allow implementations to send and receive discovery messages that are larger than the MTU.

### DPWS 3.3 HTTP messaging

R0001 requires that services support chunked transfer. WSDAPI accepts chunked data in request messages, and will send chunked data in request messages.

R0012 and R0013 describe required portions of the SOAP HTTP binding. For R0012, WSDAPI implements the SOAP HTTP binding, but will not begin reading the HTTP response until WSDAPI has finished sending the HTTP request. WSDAPI does implement the required message exchange pattern in R0013, does implement the optional responding SOAP node in R0014, and does not implement the optional web method feature in R0015. WSDAPI also supports the requirements in R0030 and R0017.

### DPWS 3.4 SOAP Envelope

WSDAPI supports R0034, and enforces R0003 and R0026 by default. More specifically, in accordance with R0003 and R0026, if WSDAPI receives a SOAP envelope that is larger than MAX\_ENVELOPE\_SIZE over HTTP it is rejected and the connection is closed.

### DPWS 3.5 WS-Addressing

R0004 reflects the recommended use of the device API in WSDAPI, and is supported by the client API in WSDAPI. Since this is a recommendation, WSDAPI will allow clients and devices to use URIs other than `urn:uuid` URIs for their device endpoints to ensure maximum compatibility. Since the device API in WSDAPI does not persist state between initializations, it is up to application developers using the device API in WSDAPI to ensure R0005 and R0006 are properly supported. The client API in WSDAPI will assume that device identities are unique and persisted, and functionality building on the client API in WSDAPI (such as PnP-X) will require this in order to properly recognize the device across device reboots.

R0007 recommends against the use of reference properties in endpoint references. WSDAPI will still recognize and accept endpoints with reference properties, and developers may choose to use them, but by default WSDAPI will not populate them in endpoints it creates. Similarly, with R0042, when WSDAPI creates service endpoints it will use a HTTP or HTTPS transport address, but will not require devices use HTTP or HTTPS transport addresses in their service endpoints. The behavior of the client when attempting to communicate with a service that does not use HTTP or HTTPS is undefined.

On faults, R0031 constrains the reply endpoint and describes the fault to send if the fault is not anonymous. WSDAPI forces the reply endpoint to use the correct value when sending messages, and will fault correctly if WSDAPI receives a request message with the incorrect reply endpoint. R0041 gives implementations the option to drop a fault if the reply endpoint is invalid. Rather than drop the fault, WSDAPI will send the fault back on the request channel, addressed to the anonymous endpoint, as a "best effort" to communicate with the client.

Lastly, there are two restrictions on SOAP headers, R0019 and R0040, both of which WSDAPI complies with and enforces on received messages.

### DPWS 3.6 Attachments

WSDAPI supports attachments and complies with R0022. WSDAPI also complies with R0037. When sending attachments, WSDAPI will always set the Content Transfer Encoding to "binary" for all MIME parts. However, WSDAPI does not enforce R0036. The behavior of WSDAPI when receiving a MIME part with a Content Transfer Encoding not set to "binary" is undefined.

DPWS also defines MIME part ordering clauses. For R0038, WSDAPI will enforce part ordering and will reject a MIME message if the SOAP envelope is not the first MIME part. For R0039, WSDAPI will always send the SOAP envelope as the first MIME part.

## DPWS 4.0 Discovery

R1013 and R1001 differentiate device discovery and service discovery. WSDAPI complies with R1013. The hosting implementation complies with R1001, but WSDAPI does not enforce this recommendation on the client.

DPWS also provides guidance on types and scope matching rules. WSDAPI supports all of the scope matching rules defined in [WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf) except LDAP. WSDAPI also provides an extensible model for defining custom scope matching rules, thus complying with R1019. The hosting API will also always provide the `wsdp:Device` type in discovery per R1020, but the client API does not require it be present. Other applications built on WSDAPI, such as PnP-X, do have a hard requirement for the `wsdp:Device` type to be present in discovery.

To facilitate discovery and binding, WSDAPI supports R1009 and R1016. Per R1018, WSDAPI will ignore multicast UDP not sent to the anonymous address. R1015, R1021, and R1022 define a HTTP binding for the Probe message, which WSDAPI supports as described.

## DPWS 5.0 Description

WSDAPI enforces R2044 on the client. On the hosting side, WSDAPI will only ever provide the `wsx:Metadata` element in the SOAP envelope body. R2045 allows devices to support a subset of the [WS-Transfer](https://specs.xmlsoap.org/ws/2004/09/transfer/WS-Transfer.pdf) functionality. The hosting API will always generate the `wsa:ActionNotSupported` fault.

### DPWS 5.1 Characteristics

DPWS describes basic characteristics for the device. In addition to the restrictions described in this topic, length limits are defined for specific strings and URIs. WSDAPI does enforce the length limits in this DPWS section 5.1, either before sending the message or after parsing its contents.

DPWS also describes the required metadata sections and cycling of the metadata version. The client implementation enforces the presence of ThisModel and ThisDevice metadata. The hosting implementation also properly manages the metadata version and always provides these sections, complying with R2038, R2012, R2001, R2039, R2014, and R2002.

### DPWS 5.2 Hosting

This section describes the hierarchy of services and relationship metadata. WSDAPI does not enforce the uniqueness of the ServiceId as described in this section on either the client or the device side.

WSDAPI does comply with R2040, and it is possible for the hosting implementation to send a metadata response with no relationship section if there are no hosted services. The client implementation correctly accepts the metadata response.

R2029 allows for multiple relationship sections in a metadata response, which WSDAPI will correctly accept. R2030 and R2042 describe management of the metadata version, which is implemented correctly in the hosting API.

### DPWS 5.3 WSDL

If a service provides Web Services Description Language (WSDL) data, client implementations can get the service definition and manipulate the service on the fly. This is used by late bound clients. The WSDAPI client implementation will accept WSDL provided from a service, but the client does not validate it and the client does not provide a late bound programming model. The hosting implementation can be used to provide WSDL, but the host is not required to do so as the service level metadata is not managed by the host itself.

### DPWS 5.4 WS-Policy

DPWS describes Policy assertions to be used for devices. Since WSDAPI does not provide and does not interpret WSDL, it cannot recognize and enforce policy embedded in WSDL data.

## DPWS 6.0 Eventing

### DPWS 6.1 Subscription

DPWS requires support for Push delivery. WSDAPI implements Push delivery on the service side, thus complying with R3009 and R3010, and will only accept the Push delivery mode on the client side. R3017 and R3018 require specific faults from the service if it does not recognize the `NotifyTo` or `EndTo` addresses. WSDAPI does not validate these addresses upfront and will not generate these faults. However, the client implementation will recognize these faults correctly. Similarly, R3019 is optional and WSDAPI does not implement this recommendation, but the client implementation will correctly recognize the `SubscriptionEnd` message and will notify the application of a delivery failure.

### DPWS 6.1.1 Filtering

WSDAPI complies with R3008 and implements the `Action` filter. In compliance with R3011 and R3012, WSDAPI will not generate the faults in the stated conditions. WSDAPI also implements the fault described R3020 if it does not recognize the actions on which it is asked to filter.

### DPWS 6.2 Subscription Duration and Renewal

WSDAPI complies with R3005, R3006, and R3016. WSDAPI will always use `xs:duration` but will accept `xs:dateTime` if provided, and thus will not issue the optional fault in R3013. WSDAPI supports `GetStatus` and will not issue the `wsa:ActionNotSupported` fault per R3015. WSDAPI accept the `wsa:ActionNotSupported` fault if a service responds to a `GetStatus` request with it.

## DPWS 7.0 Security

DPWS describes a recommended security model for devices. WSDAPI does not implement these recommendations as described, and does not enforce the restrictions in this section as described.

## DPWS Appendix I

DPWS amends global constants from other specifications to suit devices. WSDAPI uses the constants from this section, and overrides the default constants in the [WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf) implementation with these constants. Applications using WSDAPI for WS-Discovery will be bound to the constants defined in DPWS, not the constants defined in [WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf).

 

 



