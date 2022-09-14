---
description: There are two ways to determine the diagnostic procedure to use.
ms.assetid: d6877063-6cf9-48dc-8208-0f3fc85b6d6b
title: Getting Started with WSDAPI Troubleshooting
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




| Problem | Diagnostic Procedure | Problem identification | 
|---------|----------------------|------------------------|
| <a href="hello-message.md">Hello</a>, <a href="probe-message.md">Probe</a>, or <a href="resolve-message.md">Resolve</a> messages are not transmitted on the network because the application does not correctly enumerate the multicast network interfaces. | <a href="using-wsddebug-client-to-verify-multicast-traffic.md">Using WSD Debug Client to Verify Multicast Traffic</a> | The Hello, Probe, or Resolve messages do not appear in WSD Debug Client output. The packets do not appear on the network. Packets are not generated for the loopback interface or for other interfaces. | 
| <a href="probe-message.md">Probe</a> messages are not sent by UDP multicast to port 3702 (for applications not using directed discovery). | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> | Inspection of the message shows that it was sent to the wrong port. | 
| The <a href="probe-message.md">Probe</a> message does not contain a <strong>Types</strong> element, or the <strong>Types</strong> element is empty. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the message shows that the <strong>Types</strong> element is not present or empty. | 
| The <strong>Types</strong> element of a <a href="probe-message.md">Probe</a> message does not contain the types to which a host will respond. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the message shows that the <strong>Types</strong> element contains a malformed or incorrect value. | 
| A <a href="probematches-message.md">ProbeMatches</a> message was not sent unicast to the UDP port from which the <a href="probe-message.md">Probe</a> was sent. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the output shows that no <a href="probematches-message.md">ProbeMatches</a>) message was sent or that the message was sent to the wrong port.<blockquote>[!Note]<br />For applications using directed discovery, the <a href="probematches-message.md">ProbeMatches</a> must be sent over HTTP or HTTPS in response to the <a href="probe-message.md">Probe</a> message.</blockquote><br /> | 
| The <a href="probematches-message.md">ProbeMatches</a> message does not contain a <strong>RelatesTo</strong> element, or the <strong>RelatesTo</strong> element is empty. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the message shows that the <strong>RelatesTo</strong> element is not present or empty. | 
| The value of the <strong>RelatesTo</strong> element in a <a href="probematches-message.md">ProbeMatches</a> message does not match the value of the <strong>MessageId</strong> element from the corresponding <a href="probe-message.md">Probe</a> message. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the message shows that the <strong>RelatesTo</strong> element contains a malformed or incorrect value. | 
| The <strong>XAddrs</strong> element included in a <a href="probematches-message.md">ProbeMatches</a> message does not conform to the <a href="xaddr-validation-rules.md">XAddr Validation Rules</a>. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the message shows that the <strong>XAddrs</strong> are invalid. | 
| <a href="resolve-message.md">Resolve</a> messages are not sent by UDP multicast to port 3702 (for applications not using directed discovery). | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the output shows that the <a href="resolve-message.md">Resolve</a> message was sent to the wrong port. | 
| A <a href="resolvematches-message.md">ResolveMatches</a> message was not sent unicast to the UDP port from which a <a href="resolve-message.md">Resolve</a> message was sent. | <a href="inspecting-network-traces-for-udp-ws-discovery.md">Inspecting Network Traces for UDP WS-Discovery</a> or <a href="inspecting-network-traces-for-applications-using-directed-discovery.md">Inspecting Network Traces for Applications Using Directed Discovery</a> | Inspection of the output shows that no <a href="resolvematches-message.md">ResolveMatches</a> message was sent or that the message was sent to the wrong port. | 




 

### Metadata exchange problems




| Problem | Diagnostic Procedure | Problem identification | 
|---------|----------------------|------------------------|
| The transport address advertised by the host is wrong. | <a href="using-a-generic-host-and-client-for-http-metadata-exchange.md">Using a Generic Host and Client for HTTP Metadata Exchange</a> | Inspection of the XAddrs in the WSD Debug Client output shows that the transport address is wrong or malformed. | 
| A TCP connection could not be established for metadata exchange. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | The output from the packet analyzer does not show the following packet exchange:<ul><li>A TCP SYN packet sent from the client</li><li>A TCP SYN/ACK packet sent from the host</li><li>A TCP ACK packet sent from the client</li></ul> | 
| The client did not send a valid HTTP GET request. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | There is no HTTP GET request in the packet analyzer output, or the request is malformed. | 
| The client did not send a valid WS-Transfer <a href="get--metadata-exchange--http-request-and-message.md">Get</a> message. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | There is no WS-Transfer <a href="get--metadata-exchange--http-request-and-message.md">Get</a> message in the packet analyzer output, or the message is malformed. | 
| The host is not listening on the URL path specified in the HTTP GET request. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | There is no HTTP response in the packet analyzer output. | 
| The WS-Transfer <a href="get--metadata-exchange--http-request-and-message.md">Get</a> message does not contain a <strong>To</strong> element, or the <strong>To</strong> element is empty. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | Inspection of the message shows that the <strong>To</strong> element is not present or empty. | 
| The value of the <strong>To</strong> element of a WS-Transfer <a href="get--metadata-exchange--http-request-and-message.md">Get</a> message does not match one of the host's endpoint addresses. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | Inspection of the message shows that value of the <strong>To</strong> element does not match one of the endpoint addresses advertised in the host's <a href="probematches-message.md">ProbeMatches</a> or <a href="resolvematches-message.md">ResolveMatches</a> message. | 
| The host did not send a valid HTTP response header. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | There is no HTTP response in the packet analyzer output, or the request is malformed. | 
| The HTTP response header sent by the host indicates that the request cannot be completed. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | The response header has a status code other than HTTP/1.1 200. | 
| The host did not send a valid <a href="getresponse--metadata-exchange--message.md">GetResponse</a> message. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | There is no <a href="getresponse--metadata-exchange--message.md">GetResponse</a> message in the packet analyzer output, or the message is malformed. | 
| The <a href="getresponse--metadata-exchange--message.md">GetResponse</a> message does not contain a <strong>RelatesTo</strong> element, or the <strong>RelatesTo</strong> element is empty. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | Inspection of the message shows that the <strong>RelatesTo</strong> element is not present or empty. | 
| The value of the <strong>RelatesTo</strong> element in a <a href="getresponse--metadata-exchange--message.md">GetResponse</a> message does not match the value of the <strong>MessageId</strong> element from the corresponding <a href="get--metadata-exchange--http-request-and-message.md">Get</a> message. | <a href="inspecting-network-traces-for-http-metadata-exchange.md">Inspecting Network Traces for HTTP Metadata Exchange</a> | Inspection of the message shows that the <strong>RelatesTo</strong> element contains a malformed or incorrect value. | 


## Related topics

<dl> <dt>

[WSDAPI Troubleshooting Guide](wsdapi-troubleshooting-guide.md)
</dt> </dl>
