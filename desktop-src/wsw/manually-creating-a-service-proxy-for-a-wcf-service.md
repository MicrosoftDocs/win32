---
title: Manually Creating a Service Proxy for a WCF Service
description: The easiest way to create a client service proxy for a Windows Communication Foundation (WCF) service is at the Service Model layer with the WsUtil tool, as described in the Creating a Client topic.
ms.assetid: ef545090-382b-44bd-b7ab-f5a285b6e202
ms.topic: article
ms.date: 05/31/2018
---

# Manually Creating a Service Proxy for a WCF Service

The easiest way to create a client service proxy for a Windows Communication Foundation (WCF) service is at the [Service Model](service-model-layer-overview.md) layer with the WsUtil tool, as described in the [Creating a Client](creating-a-client.md) topic. However, if necessary, you can also create a service proxy manually. This API includes a [**WsCreateServiceProxy**](/windows/desktop/api/WebServices/nf-webservices-wscreateserviceproxy) function for creating the service proxy as well as structures, enumerations, and so on for setting the properties necessary to interoperate with WCF.

WCF provides a number of standard bindings, each targeting a specific usage scenario. Which binding the service you are trying to connect to uses, in turn, determines which channel properties you need to customize for your service proxy to communicate with the service.

## Creating a Service Proxy for WCF's WSHttpBinding

WSHttpBinding is for the mainline Internet web services scenario. It uses the newer SOAP version 1.2 and WS-Addressing version 1.0 and enables a wide range of security settings over the public HTTP and HTTPS transports. WWSAPI does not have an equivalent of the WSHttpBinding (or any of the WCF standard bindings, for that matter), but since its default SOAP version, WS-Addressing version, and encoding format match those in WSHttpBinding, creating a service proxy for a service that uses the WSHttpBinding is straightforward. For example, to create a service proxy to talk to a WSHttpBinding endpoint without security, you can simply use code like following snippet (variable declaration, and heap and error creation are omitted). Notice that no channel properties or security description is specified in the call to the [**WsCreateServiceProxy**](/windows/desktop/api/WebServices/nf-webservices-wscreateserviceproxy) function.


```C++
// Create the proxy

hr = WsCreateServiceProxy(
        WS_CHANNEL_TYPE_REQUEST, 
        WS_HTTP_CHANNEL_BINDING, 
        NULL, // security description
        NULL, // proxy properties
        0, // proxy property count
        NULL, // channel properties
        0, // channel property count
        &proxy, 
        error);
```



The function creates the service proxy and returns a pointer to it in the *serviceProxy* parameter (&proxy in the function call above).

## Creating a Service Proxy for WCF's BasicHttpBinding

When you manually create a service proxy for a WCF service that uses a BasicHttpBinding binding, however, it is necessary to set the SOAP version and WS-Addressing properties of the channel. This is because WWSAPI defaults to SOAP version 1.2 and WS-Addressing 1.0. WCF's BasicHttpBinding, on the other hand, uses SOAP version 1.1 and no WS-Addressing.

To set the SOAP version and WS-Addrssing properties of the channel, declare an array of [**WS\_CHANNEL\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_property) structures to hold the channel properties and related information.


```
WS_CHANNEL_PROPERTY channelProperties[4]; // Array to hold up to 4 channel properties

ULONG channelPropertyCount = 0; // Count of properties set
 
WS_ENVELOPE_VERSION soapVersion = WS_ENVELOPE_VERSION_SOAP_1_1; // Set required SOAP version
channelProperties[channelPropertyCount].id = WS_CHANNEL_PROPERTY_ENVELOPE_VERSION; // Type of first channel property
channelProperties[channelPropertyCount].value = &soapVersion; // Address of the SOAP version value
channelProperties[channelPropertyCount].valueSize = sizeof(soapVersion); // Size of the value
channelPropertyCount++; // Increment property count
 
WS_ADDRESSING_VERSION addressingVersion = WS_ADDRESSING_VERSION_TRANSPORT; // Set required WS-Addressing value
channelProperties[channelPropertyCount].id = WS_CHANNEL_PROPERTY_ADDRESSING_VERSION; // Type of second channel property
channelProperties[channelPropertyCount].value = &addressingVersion ; // Address of the WS-Addressing value
channelProperties[channelPropertyCount].valueSize = sizeof(addressingVersion ); // Size of the value
channelPropertyCount++; // Increment property count
 
// add more channel properties here

```



Then pass the array of channel properties (channelProperties) and the count of properties (channelPropertyCount) to the [**WsCreateServiceProxy**](/windows/desktop/api/WebServices/nf-webservices-wscreateserviceproxy) (or [**WsCreateChannel**](/windows/desktop/api/WebServices/nf-webservices-wscreatechannel) if you are working at channel layer).


```
// Create the proxy

hr = WsCreateServiceProxy(
        WS_CHANNEL_TYPE_REQUEST, 
        WS_HTTP_CHANNEL_BINDING, 
        NULL, // security description
        NULL, // proxy properties
        0, // proxy property count
        channelProperties, // channel properties
        channelPropertyCount, // channel property count
        &proxy, 
        error);
```



The array you declared to hold the properties is copied in **WsCreateServiceProxy**, and as a result, you can free the memory for the property array immediately after calling the function. Also, if you allocate the memory from the stack (like the code snippet above), you can also return from the function immediately after the call.

## Other Bindings

In addition, WWSAPI provides mechanisms for creating service proxies to communicate with WCF services using other bindings, such as NetTcpBinding and WSFederationHttpBinding. Many of these binding require setting additional channel properties, such as security descriptors. For examples that illustrate using other bindings, see the [Windows Web Services Examples](windows-web-services-examples.md), section, in particular the [TCP Channel Layer Examples](tcp-channel-layer-examples.md), [HTTP Channel Layer Examples](http-channel-layer-examples.md), and [Security Channel Layer Examples](security-channel-layer-examples.md) subsections.

 

 




