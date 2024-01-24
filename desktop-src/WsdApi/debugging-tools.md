---
description: A debugging toolset built on Web Services on Devices API (WSDAPI) is available in the Windows SDK and the Windows Driver Kit (WDK).
ms.assetid: bd7efa8b-4f12-4b19-a7df-fa34c6a3444a
title: Debugging Tools
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Tools

A debugging toolset built on Web Services on Devices API (WSDAPI) is available in the Windows SDK and the Windows Driver Kit (WDK). These tools can be used to test the functionality of custom applications written on WSDAPI, or devices and clients written using other Device Profile for Web Services (DPWS) stacks.

The WSD Debug Host (wsddebug\_host.exe) and WSD Debug Client (wsddebug\_client.exe) tools can be used to inspect the characteristics of DPWS clients or hosts. They can also be used to troubleshoot connectivity or configuration problems. For more information, see [WSDAPI Troubleshooting Guide](wsdapi-troubleshooting-guide.md). These tools are only available in the SDK. SDK tools are located in the following directory: \<Windows SDK Install Folder>\\Bin.

The [WSDAPI Basic Interoperability Tool (WSDBIT)](https://msdn.microsoft.com/library/cc264250.aspx) can be used to test SOAP-level or transport-level interoperability (that is, ensuring messages are well-formed). This tool is only available in the WDK.

## The WSD Debug Client

The WSD Debug Client (wsddebug\_client.exe) provides an interactive console that can be used to send and receive WS-Discovery messages, and to obtain metadata. It can also be used to generate and consume raw multicast messages.

The WSD Debug Client operates in one of three modes: multicast, discovery, and metadata.



| Mode      | Description                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multicast | In Multicast mode, the WSD Debug Client sends and receives unformatted multicast messages on UDP port 3702, as defined in WS-Discovery. The user may save these SOAP messages in a text file, and may modify and rebroadcast the messages with the WSD Debug Client.                                                                                                                                 |
| Discovery | In Discovery mode, the WSD Debug Client sends and receives formatted WS-Discovery messages. It can display received [Hello](hello-message.md), [Bye](bye-message.md), [ProbeMatches](probematches-message.md), and [ResolveMatches](resolvematches-message.md) messages. It can send [Probe](probe-message.md) messages over UDP or HTTP, and [Resolve](resolve-message.md) messages over UDP. |
| Metadata  | In addition to implementing all of the features of Discovery mode, Metadata mode also attempts to retrieve metadata from devices.                                                                                                                                                                                                                                                                    |



 

For more information, see [Using a Generic Host and Client for HTTP Metadata Exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md), [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md), and [Using WSD Debug Client to Verify Multicast Traffic](using-wsddebug-client-to-verify-multicast-traffic.md).

## The WSD Debug Host

The WSD Debug Host (wsddebug\_host.exe) provides an interactive console used to announce the host, respond to client requests, and print diagnostic information.

The WSD Debug Host operates in one of two modes: discovery and metadata.



| Mode      | Description                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Discovery | In Discovery mode, the WSD Debug Host prints formatted WS-Discovery messages. It also sends [Hello](hello-message.md) and [Bye](bye-message.md) messages, and automatically responds to [Probe](probe-message.md) and [Resolve](resolve-message.md) messages. |
| Metadata  | In addition to implementing all of the features of Discovery mode, Metadata mode advertises a metadata service and allows clients to connect and perform metadata exchange.                                                                                       |



 

For more information, see [Using a Generic Host and Client for HTTP Metadata Exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md) and [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).

## Related topics

<dl> <dt>

[WSD Application Development on Windows](wsd-application-development-on-windows.md)
</dt> <dt>

[WSDAPI Development Tools](wsdapi-development-tools.md)
</dt> <dt>

[WSDAPI Troubleshooting Guide](wsdapi-troubleshooting-guide.md)
</dt> </dl>

 

 



