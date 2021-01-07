---
description: Lists the diagnostic procedures to use when troubleshooting WSDAPI applications.
ms.assetid: befe4234-8d3a-4fc5-9a7d-faca94964af6
title: Troubleshooting Other WSDAPI Applications
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting Other WSDAPI Applications

Applications can directly call into WSDAPI interfaces and functions to perform device discovery and metadata exchange. The message patterns used by these applications vary.

The goal of this troubleshooting guide is to help WSDAPI application developers successfully implement a device proxy. This guide is not intended to help troubleshoot all aspects of WSDAPI. If the device proxy has been successfully created and the client and host can see each other on the network, then this guide cannot address the application's problems. To troubleshoot these application problems, follow the instructions in [Enabling WSDAPI Tracing](enabling-wsdapi-tracing.md) and contact Microsoft support for further assistance.

## Troubleshooting clients calling WSDCreateDeviceProxy

Applications call [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy) to create and initialize an instance of the [**IWSDDeviceProxy**](/windows/desktop/api/WsdClient/nn-wsdclient-iwsddeviceproxy) interface. This device proxy object can be used to advertise services on a device and also to exchange metadata.

An application calling [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy) always uses the following messages.

-   [Get](get--metadata-exchange--http-request-and-message.md)
-   [GetResponse](getresponse--metadata-exchange--message.md)

An application calling [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy) sometimes uses the following messages.

-   [Resolve](resolve-message.md)
-   [ResolveMatches](resolvematches-message.md)

[Resolve](resolve-message.md) and [ResolveMatches](resolvematches-message.md) messages are generated when a logical device address (that is, a device address of the form urn:uuid:{guid}) is passed to *pszDeviceId*. These messages are not generated when a physical device address is passed to *pszDeviceId*. When Resolve and ResolveMatches messages are used, they are sent before the [Get](get--metadata-exchange--http-request-and-message.md) and [GetResponse](getresponse--metadata-exchange--message.md) messages.

The following diagnostic procedures should be used (in order) to help identify problems with an application calling [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy) with a physical device address.

1.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
2.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
3.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
4.  [Inspect network traces for HTTP metadata exchange](inspecting-network-traces-for-http-metadata-exchange.md).

The following diagnostic procedures should be used (in order) to help identify problems with an application calling [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy) with a logical device address.

1.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
2.  [Use a generic host and client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).
3.  [Use WSD Debug Client to verify multicast traffic](using-wsddebug-client-to-verify-multicast-traffic.md).
4.  [Inspect network traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).
5.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
6.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
7.  [Inspect network traces for HTTP metadata exchange](inspecting-network-traces-for-http-metadata-exchange.md).

Verify that [Resolve](resolve-message.md) and [ResolveMatches](resolvematches-message.md) messages are generated and meet traffic requirements. It is not necessary to look for [Probe](probe-message.md) or [ProbeMatches](probematches-message.md) messages in the WSD Debug Client output or in the network traces.

## Troubleshooting clients calling WSDCreateDeviceProxyAdvanced

Applications call [**WSDCreateDeviceProxyAdvanced**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxyadvanced) to create and initialize an instance of the [**IWSDDeviceProxy**](/windows/desktop/api/WsdClient/nn-wsdclient-iwsddeviceproxy) interface. Unlike [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy), **WSDCreateDeviceProxyAdvanced** has a *pDeviceAddress* parameter that is used to define the device transport address. If this transport address is specified, then logical address resolution is not required and [Resolve](resolve-message.md) and [ResolveMatches](resolvematches-message.md) messages are not generated.

If *pDeviceAddress* is set to **NULL** and *pszDeviceId* is a logical address, then address resolution is required and [Resolve](resolve-message.md) and [ResolveMatches](resolvematches-message.md) messages are generated.

The following diagnostic procedures should be used (in order) to help identify problems with an application calling [**WSDCreateDeviceProxyAdvanced**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxyadvanced) with a non-**NULL***pDeviceAddress* parameter. These procedures can also be used when *pDeviceAddress* is **NULL** and *pszDeviceId* is a physical address.

1.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
2.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
3.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
4.  [Inspect network traces for HTTP metadata exchange](inspecting-network-traces-for-http-metadata-exchange.md).

The following diagnostic procedures should be used (in order) to help identify problems with an application calling [**WSDCreateDeviceProxyAdvanced**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxyadvanced) with *pDeviceAddress* set to **NULL** and with *pszDeviceId* set to a logical address.

1.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
2.  [Use a generic host and client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).
3.  [Use WSD Debug Client to verify multicast traffic](using-wsddebug-client-to-verify-multicast-traffic.md).
4.  [Inspect network traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).
5.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
6.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
7.  [Inspect network traces for HTTP metadata exchange](inspecting-network-traces-for-http-metadata-exchange.md).

Verify that [Resolve](resolve-message.md) and [ResolveMatches](resolvematches-message.md) messages are generated and meet traffic requirements. It is not necessary to look for [Probe](probe-message.md) or [ProbeMatches](probematches-message.md) messages in the WSD Debug Client output or in the network traces.

## Troubleshooting clients using the IWSDiscoveryProvider interface

Applications calling into the [**IWSDiscoveryProvider**](/windows/desktop/api/WsdDisco/nn-wsddisco-iwsdiscoveryprovider) interface do not perform metadata exchange. This interface is only used for discovery. The message patterns and troubleshooting procedures are different for each method called on the **IWSDiscoveryProvider** interface.

When an application calls [**IWSDiscoveryProvider::SearchByType**](/windows/desktop/api/WsdDisco/nf-wsddisco-iwsdiscoveryprovider-searchbytype), a [Probe](probe-message.md) message is generated. The Probe message is sent by UDP multicast to port 3702. A [ProbeMatches](probematches-message.md) message is generated in response. The ProbeMatches message is sent by UDP unicast and it originates from port 3702.

When an application calls [**IWSDiscoveryProvider::SearchById**](/windows/desktop/api/WsdDisco/nf-wsddisco-iwsdiscoveryprovider-searchbyid), a [Resolve](resolve-message.md) message is generated. A Resolve message is sent by UDP multicast to port 3702. A [ResolveMatches](resolvematches-message.md) message is generated in response. The ResolveMatches is sent by UDP unicast and it originates from port 3702.

The following diagnostic procedures should be used (in order) to help identify problems with an application calling [**IWSDiscoveryProvider::SearchByType**](/windows/desktop/api/WsdDisco/nf-wsddisco-iwsdiscoveryprovider-searchbytype) or [**IWSDiscoveryProvider::SearchById**](/windows/desktop/api/WsdDisco/nf-wsddisco-iwsdiscoveryprovider-searchbyid). Verify that the messages generated by the called API satisfy the traffic requirements.

1.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
2.  [Use a generic host and client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).
3.  [Use WSD Debug Client to verify multicast traffic](using-wsddebug-client-to-verify-multicast-traffic.md).
4.  [Inspect network traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).

If an application calls [**IWSDiscoveryProvider::SearchByAddress**](/windows/desktop/api/WsdDisco/nf-wsddisco-iwsdiscoveryprovider-searchbyaddress), then it is a directed discovery application. For more troubleshooting information, see [Troubleshooting Applications Using Directed Discovery](troubleshooting-applications-using-directed-discovery.md).

## Related topics

<dl> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



