---
Description: There are two ways to determine the diagnostic procedure to use.
ms.assetid: d6877063-6cf9-48dc-8208-0f3fc85b6d6b
title: Getting Started with WSDAPI Troubleshooting
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with WSDAPI Troubleshooting

This troubleshooting guide contains a set of [diagnostic procedures](wsdapi-diagnostic-procedures.md) that can be used to help identify the cause of application problems. Once the cause of the problem has been successfully identified, the suggested solutions in the diagnostic procedure can be applied in order to resolve the problem.

There are two ways to determine the diagnostic procedure to use. One way is to go to the troubleshooting page for the type of client to view a step-by-step list of diagnostic procedures to use to troubleshoot the client. The other way is to go to the troubleshooting quick reference below to view summary tables that show common problems with WSDAPI applications and the procedures to use to diagnose the problems.

## Troubleshooting by Type of Client

The following topics show the relevant diagnostic procedures by type of client. These topics also show the message patterns associated with the client type.

-   [Troubleshooting WSDAPI Applications Using Directed Discovery](troubleshooting-applications-using-directed-discovery.md)
-   [Troubleshooting Function Discovery Clients](troubleshooting-function-discovery-clients.md)
-   [Troubleshooting People Near Me/Meetings Near Me](troubleshooting-people-near-me-meetings-near-me.md)
-   [Troubleshooting the Add Printer Wizard](troubleshooting-the-add-printer-wizard.md)
-   [Troubleshooting the Network Explorer](troubleshooting-the-network-explorer.md)
-   [Troubleshooting the Projector Wizard](troubleshooting-the-projector-wizard.md)
-   [Troubleshooting Other WSDAPI Applications](troubleshooting-wsdapi-applications.md)

## Troubleshooting Quick Reference

The following tables show some problems that can prevent WSDAPI clients and hosts from seeing each other on the network and from exchanging device metadata. The tables also show the diagnostic procedures to run and the criteria to use to evaluate whether the application suffers from a particular problem.

### Network environment problems



| Problem                                                                                                                                                                                              | Diagnostic Procedure                                                                                                                                                                                                                             | Problem Identification                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The firewall blocks Network Discovery traffic.                                                                                                                                                       | [Inspecting Adapter and Firewall Settings](inspecting-adapter-and-firewall-settings.md)                                                                                                                                                         | Enabling the Network Discovery exception on the firewall solves the problem.                                                                                                                      |
| Firewall exceptions specific to the application are blocking messages.                                                                                                                               | [Inspecting Adapter and Firewall Settings](inspecting-adapter-and-firewall-settings.md)                                                                                                                                                         | Disabling the firewall solves the problem. WF.msc shows application-specific firewall rules.                                                                                                      |
| The device does not respond to UDP requests by sending a [ProbeMatches](probematches-message.md) or [ResolveMatches](resolvematches-message.md) message in a timely fashion (less than 4 seconds). | [Inspecting Adapter and Firewall Settings](inspecting-adapter-and-firewall-settings.md)                                                                                                                                                         | Disabling the firewall solves the problem, and a generic host that responds in less than 4 seconds works successfully.                                                                            |
| The security context of the application is incorrect (that is, the client and host do not have adequate permissions on the network).                                                                 | [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md) or [Using a Generic Host and Client for HTTP Metadata Exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md) | The device address is not shown in WSD Debug Client output. Running the application as Administrator solves the problem.                                                                          |
| An IPSec policy is blocking messages.                                                                                                                                                                | [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md) or [Using a Generic Host and Client for HTTP Metadata Exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md) | The device address is not shown in WSD Debug Client output. The problem is not solved by disabling the firewall. The problem cannot be reproduced on a machine not subject to any IPSec policies. |



 

### Discovery traffic problems



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Problem</th>
<th>Diagnostic Procedure</th>
<th>Problem identification</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Hello](hello-message.md), [Probe](probe-message.md), or [Resolve](resolve-message.md) messages are not transmitted on the network because the application does not correctly enumerate the multicast network interfaces.</td>
<td>[Using WSD Debug Client to Verify Multicast Traffic](using-wsddebug-client-to-verify-multicast-traffic.md)</td>
<td>The Hello, Probe, or Resolve messages do not appear in WSD Debug Client output. The packets do not appear on the network. Packets are not generated for the loopback interface or for other interfaces.</td>
</tr>
<tr class="even">
<td>[Probe](probe-message.md) messages are not sent by UDP multicast to port 3702 (for applications not using directed discovery).</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md)</td>
<td>Inspection of the message shows that it was sent to the wrong port.</td>
</tr>
<tr class="odd">
<td>The [Probe](probe-message.md) message does not contain a <strong>Types</strong> element, or the <strong>Types</strong> element is empty.</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the message shows that the <strong>Types</strong> element is not present or empty.</td>
</tr>
<tr class="even">
<td>The <strong>Types</strong> element of a [Probe](probe-message.md) message does not contain the types to which a host will respond.</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the message shows that the <strong>Types</strong> element contains a malformed or incorrect value.</td>
</tr>
<tr class="odd">
<td>A [ProbeMatches](probematches-message.md) message was not sent unicast to the UDP port from which the [Probe](probe-message.md) was sent.</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the output shows that no [ProbeMatches](probematches-message.md) message was sent or that the message was sent to the wrong port.
<blockquote>
[!Note]<br />
For applications using directed discovery, the [ProbeMatches](probematches-message.md) must be sent over HTTP or HTTPS in response to the [Probe](probe-message.md) message.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>The [ProbeMatches](probematches-message.md) message does not contain a <strong>RelatesTo</strong> element, or the <strong>RelatesTo</strong> element is empty.</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the message shows that the <strong>RelatesTo</strong> element is not present or empty.</td>
</tr>
<tr class="odd">
<td>The value of the <strong>RelatesTo</strong> element in a [ProbeMatches](probematches-message.md) message does not match the value of the <strong>MessageId</strong> element from the corresponding [Probe](probe-message.md) message.</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the message shows that the <strong>RelatesTo</strong> element contains a malformed or incorrect value.</td>
</tr>
<tr class="even">
<td>The <strong>XAddrs</strong> element included in a [ProbeMatches](probematches-message.md) message does not conform to the [XAddr Validation Rules](xaddr-validation-rules.md).</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the message shows that the <strong>XAddrs</strong> are invalid.</td>
</tr>
<tr class="odd">
<td>[Resolve](resolve-message.md) messages are not sent by UDP multicast to port 3702 (for applications not using directed discovery).</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the output shows that the [Resolve](resolve-message.md) message was sent to the wrong port.</td>
</tr>
<tr class="even">
<td>A [ResolveMatches](resolvematches-message.md) message was not sent unicast to the UDP port from which a [Resolve](resolve-message.md) message was sent.</td>
<td>[Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) or [Inspecting Network Traces for Applications Using Directed Discovery](inspecting-network-traces-for-applications-using-directed-discovery.md)</td>
<td>Inspection of the output shows that no [ResolveMatches](resolvematches-message.md) message was sent or that the message was sent to the wrong port.</td>
</tr>
</tbody>
</table>



 

### Metadata exchange problems



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Problem</th>
<th>Diagnostic Procedure</th>
<th>Problem identification</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The transport address advertised by the host is wrong.</td>
<td>[Using a Generic Host and Client for HTTP Metadata Exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md)</td>
<td>Inspection of the XAddrs in the WSD Debug Client output shows that the transport address is wrong or malformed.</td>
</tr>
<tr class="even">
<td>A TCP connection could not be established for metadata exchange.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>The output from the packet analyzer does not show the following packet exchange:
<ul>
<li>A TCP SYN packet sent from the client</li>
<li>A TCP SYN/ACK packet sent from the host</li>
<li>A TCP ACK packet sent from the client</li>
</ul></td>
</tr>
<tr class="odd">
<td>The client did not send a valid HTTP GET request.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>There is no HTTP GET request in the packet analyzer output, or the request is malformed.</td>
</tr>
<tr class="even">
<td>The client did not send a valid WS-Transfer [Get](get--metadata-exchange--http-request-and-message.md) message.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>There is no WS-Transfer [Get](get--metadata-exchange--http-request-and-message.md) message in the packet analyzer output, or the message is malformed.</td>
</tr>
<tr class="odd">
<td>The host is not listening on the URL path specified in the HTTP GET request.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>There is no HTTP response in the packet analyzer output.</td>
</tr>
<tr class="even">
<td>The WS-Transfer [Get](get--metadata-exchange--http-request-and-message.md) message does not contain a <strong>To</strong> element, or the <strong>To</strong> element is empty.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>Inspection of the message shows that the <strong>To</strong> element is not present or empty.</td>
</tr>
<tr class="odd">
<td>The value of the <strong>To</strong> element of a WS-Transfer [Get](get--metadata-exchange--http-request-and-message.md) message does not match one of the host's endpoint addresses.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>Inspection of the message shows that value of the <strong>To</strong> element does not match one of the endpoint addresses advertised in the host's [ProbeMatches](probematches-message.md) or [ResolveMatches](resolvematches-message.md) message.</td>
</tr>
<tr class="even">
<td>The host did not send a valid HTTP response header.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>There is no HTTP response in the packet analyzer output, or the request is malformed.</td>
</tr>
<tr class="odd">
<td>The HTTP response header sent by the host indicates that the request cannot be completed.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>The response header has a status code other than HTTP/1.1 200.</td>
</tr>
<tr class="even">
<td>The host did not send a valid [GetResponse](getresponse--metadata-exchange--message.md) message.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>There is no [GetResponse](getresponse--metadata-exchange--message.md) message in the packet analyzer output, or the message is malformed.</td>
</tr>
<tr class="odd">
<td>The [GetResponse](getresponse--metadata-exchange--message.md) message does not contain a <strong>RelatesTo</strong> element, or the <strong>RelatesTo</strong> element is empty.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>Inspection of the message shows that the <strong>RelatesTo</strong> element is not present or empty.</td>
</tr>
<tr class="even">
<td>The value of the <strong>RelatesTo</strong> element in a [GetResponse](getresponse--metadata-exchange--message.md) message does not match the value of the <strong>MessageId</strong> element from the corresponding [Get](get--metadata-exchange--http-request-and-message.md) message.</td>
<td>[Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md)</td>
<td>Inspection of the message shows that the <strong>RelatesTo</strong> element contains a malformed or incorrect value.</td>
</tr>
</tbody>
</table>



 

### SSL/TLS negotiation problems



| Problem                                                                                                         | Diagnostic Procedure                                                                                           | Problem identification                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The operating system does not trust the server certificate presented by the device.                             | [Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md) | The WinHTTP log contains the error 0x800b0109 (CERT\_E\_UNTRUSTEDROOT).                                                                                                                                                                                                      |
| The common name (CN) of the server certificate does not match the hostname part of the device address.          | [Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md) | The WinHTTP log contains the error 0x800b010f (CERT\_E\_CN\_NO\_MATCH).                                                                                                                                                                                                      |
| Certificate revocation cannot be checked because the certificate revocation server was offline.                 | [Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md) | The WinHTTP log contains the error 0x80092013 (CRYPT\_E\_REVOCATION\_OFFLINE).                                                                                                                                                                                               |
| There is no valid certificate for client authentication to the local computer certificate store.                | [Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md) | The WinHTTP log contains the error 12044 (ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED) and SSL/TLS negotiation failed. Inspection of the certificate store using the **Certificates** MMC snap-in shows that there isn't a valid certificate.                                 |
| The process trying to issue the HTTP request does not have access to the private key of the client certificate. | [Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md) | The WinHTTP log contains the error 12044 (ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED) and SSL/TLS negotiation failed. Inspection of the ACL of the client certificate shows that the account running the process trying to issue the HTTP request does not have read access. |



 

## Related topics

<dl> <dt>

[WSDAPI Troubleshooting Guide](wsdapi-troubleshooting-guide.md)
</dt> </dl>

 

 




