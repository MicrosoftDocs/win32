---
description: If the generic host and client can see each other on the network but the actual host and client cannot, it is likely that the problem is in the messages sent between the endpoints over the network.
ms.assetid: 1b0943fb-076e-4feb-9a4f-36a06bdd19ae
title: Using WSD Debug Client to Verify Multicast Traffic
ms.topic: article
ms.date: 05/31/2018
---

# Using WSD Debug Client to Verify Multicast Traffic

If the generic host and client can see each other on the network but the actual host and client cannot, it is likely that the problem is in the messages sent between the endpoints over the network. For more information about the generic host and client, see [Using a Generic Host and Client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md). Because full network traces can be difficult to collect, filter, and read, the WSD Debug Client tool can be used to print the multicast sides of WS-Discovery messages.

The WSD Debug Client in multicast mode can only inspect half of the messages, since the client cannot print unicast messages. If unicast traffic is of interest, skip directly to [Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).

This procedure shows a method that will display all multicast traffic on the network. To display only multicast traffic to and from the device, see the [Filtering WSD Debug Client Results](#filtering-wsd-debug-client-results) section below.

**To use the WSD Debug Client to verify multicast traffic**

1.  Configure the host and client to run across the network (that is, make sure that the host and client will operate on different machines).
2.  Open a command prompt and run the following command: **WSDDebug\_client.exe /mode multicast**
3.  Reproduce the failure by starting the host and client or by pressing F5 in the Network Explorer.
4.  Verify that messages are being multicast.

If the required messages are displayed in the WSD Debug Client output, then the application failure may be in the multicast message content, or in the existence or content of the corresponding unicast response messages. Continue troubleshooting by following the instructions in [Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).

If the required messages are displayed in the WSD Debug Client output, then it is likely that the source of the application problem has been identified. It is likely that the multicast traffic is not being transmitted on the network. This failure can happen when the application does not enumerate multicast adapters correctly. Applications must explicitly send multicast traffic over all network interfaces; otherwise, packets may not be generated for the loopback interface or for other interfaces. To verify that the packets are not appearing on the network, follow the instructions in [Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) and look for evidence of missing multicast messages.

## Verifying that messages are being multicast

Always verify that [Probe](probe-message.md) messages are being multicast. Optionally, verify that [Hello](hello-message.md) and [Resolve](resolve-message.md) messages are being multicast. Note that not all applications use Resolve messages. For more information about message patterns used by clients and hosts, see [Discovery and Metadata Exchange Message Patterns](discovery-and-metadata-exchange-message-patterns.md) and [Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md).

Messages must be triggered in order to be sent as described in step 3 above. The WSD Debug Client displays the raw SOAP message as output. Because all messages printed by WSD Debug Client in multicast mode are received over a multicast socket, the message destination address is not displayed.

The following sample WSD Debug Client output shows a Probe message. The \<wsa:Action> element identifies the message as a Probe message. Inspect the \<wsa:Action> field to verify that the received message was a Probe message.

``` syntax
UDP message at 05/08/07 10:06:55 from soap.udp://[127.0.0.1:49334]
<?xml version="1.0" encoding="utf-8" ?>
<soap:Envelope xmlns:soap="https://www.w3.org/2003/05/soap-envelope" xmlns:wsa="h
ttp://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="https://schemas.xmlso
ap.org/ws/2005/04/discovery" xmlns:wsdp="https://schemas.xmlsoap.org/ws/2006/02/d
evprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:T
o><wsa:Action>https://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action>
<wsa:MessageID>urn:uuid:256ad815-1576-4e59-8efc-4c1e0f15fdd2</wsa:MessageID></so
ap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types></wsd:Probe></
soap:Body></soap:Envelope>
```

The following sample WSD Debug Client output shows a Hello message. The \<wsa:Action> element identifies the message as a Hello message.

``` syntax
UDP message at 05/08/07 10:10:49 from soap.udp://[[::1]:49343]
<?xml version="1.0" encoding="utf-8" ?>
<soap:Envelope xmlns:soap="https://www.w3.org/2003/05/soap-envelope" xmlns:wsa="h
ttp://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="https://schemas.xmlso
ap.org/ws/2005/04/discovery" xmlns:wsdp="https://schemas.xmlsoap.org/ws/2006/02/d
evprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:T
o><wsa:Action>https://schemas.xmlsoap.org/ws/2005/04/discovery/Hello</wsa:Action>
<wsa:MessageID>urn:uuid:8999e29a-b056-4345-9e13-f42dbedab28a</wsa:MessageID><wsd
:AppSequence InstanceId="1" SequenceId="urn:uuid:abb0a2a1-6efc-4242-b8e7-c02484a
6eea2" MessageNumber="1"></wsd:AppSequence></soap:Header><soap:Body><wsd:Hello><
wsa:EndpointReference><wsa:Address>urn:uuid:02a76d74-82d0-43e6-ab09-16f54ab81ac6
</wsa:Address></wsa:EndpointReference><wsd:Types>wsdp:Device</wsd:Types><wsd:Met
adataVersion>1</wsd:MetadataVersion></wsd:Hello></soap:Body></soap:Envelope>
```

## Filtering WSD Debug Client Results

Filtering the WSD Debug Client results can help identify incident traffic involving the device. Filtering is only necessary on noisy networks.

There are two ways to filter results. The IP addresses to filter can be explicitly identified when starting the WSD Debug Client. Alternatively, the IP addresses can be specified after the client has started. This section describes both methods.

**To specify IP addresses to filter when starting WSD Debug Client**

1.  Configure the host and client to run across the network (that is, make sure that the host and client will operate on different machines).
2.  Collect the IP address(es) of the device. If the device has multiple addresses (for example, it has both IPv4 and IPv6 addresses) all addresses must be collected.
3.  Open a command prompt and run the following command: **WSDDebug\_client.exe /mode multicast /ip add** *\<device IP>*

*\<device IP>* is an IP address. The following list shows some sample formats for this IP address.

-   192.168.0.1
-   ::1
-   mydevice.contoso.com

The WSD Debug Client automatically resolves hostnames supplied at the command prompt.

**To filter results after starting WSD Debug Client**

1.  Configure the host and client to run across the network (that is, make sure that the host and client will operate on different machines).
2.  Collect the IP address(es) of the device. If the device has multiple addresses (for example, it has both IPv4 and IPv6 addresses) all addresses must be collected.
3.  Open a command prompt and run the following command: **WSDDebug\_client.exe /mode multicast**
4.  At the WSD Debug Client command prompt, run the following command: **ip add** *\<device IP>*
5.  Repeat step 4 until all device IP addresses have been added.

The following procedure assumes that the WSD Debug Client has been started and filtering by IP address is occurring.

**To verify that the correct IP addresses are being filtered**

-   At the WSD Debug Client command prompt, run the following command: **ip print**

    The list of IP addresses being filtered appears.

The following procedure assumes that the WSD Debug Client has been started and filtering by IP address is occurring.

**To disable filtering**

-   At the WSD Debug Client command prompt, run the following command: **ip clear**

    All multicast traffic will now be shown in the debug output.

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



