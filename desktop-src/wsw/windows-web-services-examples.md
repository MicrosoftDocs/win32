---
title: Windows Web Services Examples
description: The following examples show how to use Windows Web Services API.
ms.assetid: 8a557ef0-a88a-4257-a181-57f2dca9022f
ms.topic: article
ms.date: 05/31/2018
---

# Windows Web Services Examples

The following examples show how to use Windows Web Services API.

-   [Service Model Examples](service-model-examples.md)
-   [TCP Channel Layer Examples](tcp-channel-layer-examples.md)
-   [HTTP Channel Layer Examples](http-channel-layer-examples.md)
-   [UDP Channel Layer Examples](udp-channel-layer-examples.md)
-   [Named Pipe Channel Layer Examples](named-pipes-channel-layer-examples.md)
-   [Message Examples](message-examples.md)
-   [XML Examples](xml-examples.md)
-   [Async Model Examples](async-model-examples.md)
-   [Security Channel Layer Examples](security-channel-layer-examples.md)
-   [File Replication Examples](file-replication-examples.md)

## Service Model Examples

Calculator Service: Client: [HttpCalculatorClientExample](httpcalculatorclientexample.md), Server: [HttpCalculatorServiceExample](httpcalculatorserviceexample.md).

Calculator Service with SSL transport security: Client: [HttpCalculatorWithSslClientExample](httpcalculatorwithsslclientexample.md), Server: [HttpCalculatorWithSslServiceExample](httpcalculatorwithsslserviceexample.md).

Calculator Service with Username over SSL mixed-mode security: Client: [HttpCalculatorWithUsernameOverSslClientExample](httpcalculatorwithusernameoversslclientexample.md), Server: [HttpCalculatorWithUserNameOverSslServiceExample](httpcalculatorwithusernameoversslserviceexample.md).

Calculator Service with Kerberos over SSL mixed-mode security: Client: [HttpCalculatorWithKerberosOverSslClientExample](httpcalculatorwithkerberosoversslclientexample.md), Server: [HttpCalculatorWithKerberosOverSslServiceExample](httpcalculatorwithkerberosoversslserviceexample.md).

Purchase Order Service: Client: [HttpPurchaseOrderClientExample](httppurchaseorderclientexample.md), Server: [HttpPurchaseOrderServiceExample](httppurchaseorderserviceexample.md).

Purchase Order Service with SSL transport security: Client: [HttpPurchaseOrderWithSslClientExample](httppurchaseorderwithsslclientexample.md), Server: [HttpPurchaseOrderWithSslServiceExample](httppurchaseorderwithsslserviceexample.md).

Purchase Order Service with Username over SSL mixed-mode security: Client: [HttpPurchaseOrderWithUsernameOverSslClientExample](httppurchaseorderwithusernameoversslclientexample.md), Server: [HttpPurchaseOrderWithUserNameOverSslServiceExample](httppurchaseorderwithusernameoversslserviceexample.md).

Purchase Order Service with Kerberos over SSL mixed-mode security: Client: [HttpPurchaseOrderWithKerberosOverSslClientExample](httppurchaseorderwithkerberosoversslclientexample.md), Server: [HttpPurchaseOrderWithKerberosOverSslServiceExample](httppurchaseorderwithkerberosoversslserviceexample.md).

UnTyped Purchase Order Service: Server: [UnTypedServiceExample](untypedserviceexample.md). Client: [UnTypedClientExample](untypedclientexample.md)

Sessionful Calculator: Server: [SessionfullCalculatorServiceExample](sessionfullcalculatorserviceexample.md). Client:[SessionfullCalculatorClientExample](sessionfullcalculatorclientexample.md).

Calculator using a custom channel and listener implementation: Server:[HttpCalculatorWithLayeredChannelServiceExample](httpcalculatorwithlayeredchannelserviceexample.md). Client:[HttpCalculatorWithLayeredChannelClientExample](httpcalculatorwithlayeredchannelclientexample.md).

Calculator using a encoded channel: Server:[HttpCalculatorWithEncodedChannelServiceExample](httpcalculatorwithencodedchannelserviceexample.md). Client:[HttpCalculatorWithEncodedChannelClientExample](httpcalculatorwithencodedchannelclientexample.md).

Service that handles raw (non-SOAP) HTTP requests: Client:[HttpRawClientExample](httprawclientexample.md). Server:[HttpRawServiceExample](httprawserviceexample.md).

Service Operation Abort Notification: Server: [BlockingServiceExample](blockingserviceexample.md). Client:[ServiceCancellationExample](servicecancellationexample.md).

Call Cancellation: Server: [SessionfullCalculatorServiceExample](sessionfullcalculatorserviceexample.md). Client:[CallAbandonExample](callabandonexample.md).

Manually create a policy description and use it to create a service proxy: [PolicyTemplateExample](policytemplateexample.md).

## TCP Channel Layer Examples

A TCP example that sends messages using a one-way pattern: Client: [OneWayTcpClientExample](onewaytcpclientexample.md), Server: [OneWayTcpServerExample](onewaytcpserverexample.md)

A TCP example that sends messages using a request-reply pattern: Client: [RequestReplyTcpClientExample](requestreplytcpclientexample.md), Server: [RequestReplyTcpServerExample](requestreplytcpserverexample.md)

A streaming TCP example: Client: [StreamingTcpClientExample](streamingtcpclientexample.md), Server: [StreamingTcpServerExample](streamingtcpserverexample.md)

An async streaming TCP example: Client: [AsyncStreamingTcpClientExample](asyncstreamingtcpclientexample.md), Server: [AsyncStreamingTcpServerExample](asyncstreamingtcpserverexample.md)

## HTTP Channel Layer Examples

An HTTP example: Client: [HttpClientExample](httpclientexample.md), Server: [HttpServerExample](httpserverexample.md)

An HTTP example that uses the streaming APIs: Client: [StreamingHttpClientExample](streaminghttpclientexample.md), Server: [StreamingHttpServerExample](streaminghttpserverexample.md)

## UDP Channel Layer Examples

A UDP example that sends messages using a one-way pattern: Client: [OneWayUdpClientExample](onewayudpclientexample.md), Server: [OneWayUdpServerExample](onewayudpserverexample.md)

A UDP example that sends messages using a multicast request response pattern: Client: [MulticastUdpClientExample](multicastudpclientexample.md), Server: [MulticastUdpServerExample](multicastudpserverexample.md) The following is the same example, but using IPv6 addressing: Client: [MulticastUdpClientExample6](multicastudpclientexample6.md), Server: [MulticastUdpServerExample6](multicastudpserverexample6.md)

## Named Pipes Channel Layer Examples

A named pipes example that sends messages using a request-reply pattern: Client: [RequestReplyNamedPipesClientExample](requestreplynamedpipesclientexample.md), Server: [RequestReplyNamedPipesServerExample](requestreplynamedpipesserverexample.md)

A streaming named pipes example: Client: [StreamingNamedPipesClientExample](streamingnamedpipesclientexample.md), Server: [StreamingNamedPipesServerExample](streamingnamedpipesserverexample.md)

## Message Examples

An example that uses custom message headers: [CustomHeaderExample](customheaderexample.md)

An example that encodes and decodes a message: [MessageEncodingExample](messageencodingexample.md)

An example that forwards a message: [ForwardMessageExample](forwardmessageexample.md)

## XML Examples

An example that writes and reads xml using an XML buffer [ReadWriteXmlExample](readwritexmlexample.md)

An example that writes and reads binary data using MTOM, WsWriteBytes, WsPushBytes, and WsPullBytes [ReadWriteBytesXmlExample](readwritebytesxmlexample.md)

An example that navigates an XML buffer [NavigateXmlExample](navigatexmlexample.md)

An example that reads an XML document node by node [ReadXmlExample](readxmlexample.md)

An example that find and displays an XML attribute [ReadAttributeExample](readattributeexample.md)

An example that writes and reads an array of elements [ReadWriteArrayExample](readwritearrayexample.md)

An example that inserts an element into an XML buffer [InsertElementExample](insertelementexample.md)

An example that shows the use of some XML buffer helper functions [XmlBufferExample](xmlbufferexample.md)

An example that writes and reads derived type using wsutil generated helper functions [DerivedTypeExample](derivedtypeexample.md)

## Async Model Examples

An example that illustrates the model for asynchronous functions. [AsyncModelExample](asyncmodelexample.md)

## Security Channel Layer Examples

Windows transport security over TCP: Client: [RequestReplyTcpClientWithWindowsTransportSecurityExample](requestreplytcpclientwithwindowstransportsecurityexample.md), Server: [RequestReplyTcpServerWithWindowsTransportSecurityExample](requestreplytcpserverwithwindowstransportsecurityexample.md).

Windows transport security over named pipes: Client: [RequestReplyNamedPipesClientWithWindowsTransportSecurityExample](requestreplynamedpipesclientwithwindowstransportsecurityexample.md), Server: [RequestReplyNamedPipesServerWithWindowsTransportSecurityExample](requestreplynamedpipesserverwithwindowstransportsecurityexample.md).

SSL transport security: Client: [HttpClientWithSslExample](httpclientwithsslexample.md), Server: [HttpServerWithSslExample](httpserverwithsslexample.md).

Username over SSL mixed-mode security: Client: [HttpClientWithUsernameOverSslExample](httpclientwithusernameoversslexample.md), Server: [HttpServerWithUsernameOverSslExample](httpserverwithusernameoversslexample.md).

Username over SSL mixed-mode security: Client: [HttpClientWithKerberosOverSslExample](httpclientwithkerberosoversslexample.md), Server: [HttpServerWithKerberosOverSslExample](httpserverwithkerberosoversslexample.md).

## Metadata Example

The following examples show how to process WSDL and Policy documents with the goal of extracting information about what protocol an endpoint supports.

Username over SSL mixed-mode security: [MetadataImportWithUsernameOverSslExample](metadataimportwithusernameoversslexample.md). Issued token over SSL mixed-mode security: [MetadataImportWithIssuedTokenOverSslExample](metadataimportwithissuedtokenoversslexample.md). X509 certificate over SSL mixed-mode security: [MetadataImportWithX509OverSslExample](metadataimportwithx509oversslexample.md).

## WS-Metadata Exchange Example

The following examples show how to enable WS-MetadataExchange on [WS\_SERVICE\_HOST](ws-service-host.md).

TCP service with WS-MetadataExchange enabled: [MetadataExchangeSample](metadataexchangesample.md). WCF service moniker client which calls into the TCP service with WS-MetadataExchange enabled: [ServiceMonikerSample](servicemonikersample.md).

## Custom headers and Service model

The following examples show how to use custom headers with [WS\_SERVICE\_PROXY](ws-service-proxy.md) and [WS\_SERVICE\_HOST](ws-service-host.md) respectively.

Client: [HttpCustomHeaderPurchaseOrderClientExample](httpcustomheaderpurchaseorderclientexample.md), Server: [HttpCustomHeaderPurchaseOrderServiceExample](httpcustomheaderpurchaseorderserviceexample.md).

## File Replication Sample

A comprehensive sample that demonstrates how to implement a file replication service: Tool: [FileRepToolExample](filereptoolexample.md), Service: [FileRepServiceExample](filerepserviceexample.md).

## WCF Public Service Interoperation

A Windows Web Services client communicates with a WCF service Client: [WcfPublicServiceSample](wcfpublicservicesample.md).

## Custom HTTP Proxy

A Windows Web Services client communicates with a ASMX TerraService service using custom proxy Client: [AsmxTerraServiceSampleWithCustomProxy](asmxterraservicesamplewithcustomproxy.md)

 

 




