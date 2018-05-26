---
title: Faults
description: A fault message is used to communicate error information about a failure at a remote endpoint.
ms.assetid: d2bada50-2ddd-4f7f-9b25-7bbec77b431b
keywords:
- Faults Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Faults

A fault message is used to communicate error information about a failure at a remote endpoint. A fault message is like any other message, except the format of the message body has a standard format. Faults can be used both by infrastructure protocols, such as WS-Addressing, and by higher-level application protocols.

-   [Overview](#overview)
-   [Generating faults in a Service](#generating-faults-in-a-service)
-   [Handling faults on a client](#handling-faults-on-a-client)
-   [Using faults with messages](#using-faults-with-messages)

## Overview

The contents of the body of a fault message is represented in this API using the [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master) structure. Although a fault has a fixed set of fields used to providing information about the failure (like the [**WS\_FAULT\_CODE**](/windows/win32/WebServices/ns-webservices-_ws_fault_code?branch=master) that identifies the type of fault, and the [**WS\_FAULT\_REASON**](/windows/win32/WebServices/ns-webservices-_ws_fault_reason?branch=master) that contains text describing the fault), it also contains a detail field that can be used to specify arbitrary XML content relating to the fault.

## Generating faults in a Service

A service will typically send a fault due to some error that was encountered while processing the request. The model used by this API is that the code in the service that encounters the processing error will capture the necessary fault information in the [WS\_ERROR](ws-error.md) object, and then code at a higher level in the call chain will actually send the fault using the information captured at the lower layer. This scheme allows the code that sends the fault to be insulated from how errors situations are mapped to faults while still allowing for rich fault information to be sent.

The following properties can be used with [**WsSetFaultErrorProperty**](/windows/win32/WebServices/nf-webservices-wssetfaulterrorproperty?branch=master) to capture fault information for a [WS\_ERROR](ws-error.md) object:

-   [**WS\_FAULT\_ERROR\_PROPERTY\_ACTION**](/windows/win32/WebServices/ne-webservices-ws_fault_error_property_id?branch=master). This specifies the action to use for the fault message. If this is not specified, then a default action is supplied.
-   [**WS\_FAULT\_ERROR\_PROPERTY\_FAULT**](/windows/win32/WebServices/ne-webservices-ws_fault_error_property_id?branch=master). This contains the [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master) structure that is sent in the body of the fault message.
-   [**WS\_FAULT\_ERROR\_PROPERTY\_HEADER**](/windows/win32/WebServices/ne-webservices-ws_fault_error_property_id?branch=master). Some faults include message headers which are added to the fault message to convey processing failures relating to headers of the request message. This property can be used to specify a [WS\_XML\_BUFFER](ws-xml-buffer.md) containing a header to be added to the fault message.

Any error strings that are added to the [WS\_ERROR](ws-error.md) object are used as the text in the fault that is sent. Error strings can be added to the error object using [**WsAddErrorString**](/windows/win32/WebServices/nf-webservices-wsadderrorstring?branch=master).

The [**WsSetFaultErrorProperty**](/windows/win32/WebServices/nf-webservices-wssetfaulterrorproperty?branch=master) function can be used to set these properties of the [WS\_ERROR](ws-error.md) object.

To set the detail of the fault stored in the [WS\_ERROR](ws-error.md) object, use the [**WsSetFaultErrorDetail**](/windows/win32/WebServices/nf-webservices-wssetfaulterrordetail?branch=master) function. This function can be used to associate arbitrary XML content with the fault.

The [Service Host](service-host.md) will automatically send faults by using the above information in the [WS\_ERROR](ws-error.md) object. The [**WS\_SERVICE\_PROPERTY\_FAULT\_DISCLOSURE**](/windows/win32/WebServices/ne-webservices-ws_service_property_id?branch=master) property can be used to control how detailed of a fault will be sent.

If working at the channel layer, faults can be sent for a [WS\_ERROR](ws-error.md) object using [**WsSendFaultMessageForError**](/windows/win32/WebServices/nf-webservices-wssendfaultmessageforerror?branch=master).

## Handling faults on a client

If a client receives a fault when using a [Service Proxy](service-proxy.md) or via [**WsRequestReply**](/windows/win32/WebServices/nf-webservices-wsrequestreply?branch=master) or [**WsReceiveMessage**](/windows/win32/WebServices/nf-webservices-wsreceivemessage?branch=master), the **WS\_E\_ENDPOINT\_FAULT\_RECEIVED** error will be returned. (For more information, see [Windows Web Services Return Values](windows-web-services-return-values.md).) These functions will also populate the [WS\_ERROR](ws-error.md) object supplied to the call with information about the received fault.

The following properties of an [WS\_ERROR](ws-error.md) object can be queried using [**WsGetFaultErrorProperty**](/windows/win32/WebServices/nf-webservices-wsgetfaulterrorproperty?branch=master) to obtain information about a fault that was received:

-   [**WS\_FAULT\_ERROR\_PROPERTY\_ACTION**](/windows/win32/WebServices/ne-webservices-ws_fault_error_property_id?branch=master). This specifies the action value of the fault message.
-   [**WS\_FAULT\_ERROR\_PROPERTY\_FAULT**](/windows/win32/WebServices/ne-webservices-ws_fault_error_property_id?branch=master). This contains the [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master) structure that was deserialized from the body of the fault message.

A fault may contain arbitrary additional XML content in the detail of the fault. This can be accessed using the use the [**WsGetFaultErrorDetail**](/windows/win32/WebServices/nf-webservices-wsgetfaulterrordetail?branch=master) function.

## Using faults with messages

The following section applies when dealing directly with the contents of the body of a fault message.

The contents of the body of a fault message is represented by the standard [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master) structure, which has built-in support for serialization.

For example, the following code can be used to write a fault to a message body:

``` syntax
HRESULT hr;
WS_ELEMENT_DESCRIPTION faultDescription = { NULL, WS_FAULT_TYPE, NULL, NULL };
WS_FAULT fault = { ... };
hr = WsWriteBody(message, &faultDescription, WS_WRITE_REQUIRED_VALUE, &fault, sizeof(fault), error);
```

The following code can be used to read a fault from a message body:

``` syntax
HRESULT hr;
WS_ELEMENT_DESCRIPTION faultDescription = { NULL, WS_FAULT_TYPE, NULL, NULL };
WS_FAULT fault;
hr = WsReadBody(message, &faultDescription, WS_READ_REQUIRED_VALUE, &fault, sizeof(fault), error);
```

In order to know whether a received message is a fault or not, the [**WS\_MESSAGE\_PROPERTY\_IS\_FAULT**](/windows/win32/WebServices/ne-webservices-ws_message_property_id?branch=master) can be consulted. This property is set based on whether the first element in the body is a fault element during [**WsReadMessageStart**](/windows/win32/WebServices/nf-webservices-wsreadmessagestart?branch=master) or [**WsReadEnvelopeStart**](/windows/win32/WebServices/nf-webservices-wsreadenvelopestart?branch=master).

To create a [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master) given a [WS\_ERROR](ws-error.md), use the [**WsCreateFaultFromError**](/windows/win32/WebServices/nf-webservices-wscreatefaultfromerror?branch=master) function.

The following enumerations are part of faults:

-   [**WS\_FAULT\_DISCLOSURE**](/windows/win32/WebServices/ne-webservices-ws_fault_disclosure?branch=master)
-   [**WS\_FAULT\_ERROR\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_fault_error_property_id?branch=master)

The following functions are part of faults:

-   [**WsCreateFaultFromError**](/windows/win32/WebServices/nf-webservices-wscreatefaultfromerror?branch=master)
-   [**WsGetFaultErrorDetail**](/windows/win32/WebServices/nf-webservices-wsgetfaulterrordetail?branch=master)
-   [**WsGetFaultErrorProperty**](/windows/win32/WebServices/nf-webservices-wsgetfaulterrorproperty?branch=master)
-   [**WsSetFaultErrorDetail**](/windows/win32/WebServices/nf-webservices-wssetfaulterrordetail?branch=master)
-   [**WsSetFaultErrorProperty**](/windows/win32/WebServices/nf-webservices-wssetfaulterrorproperty?branch=master)

The following structures are part of faults:

-   [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master)
-   [**WS\_FAULT\_CODE**](/windows/win32/WebServices/ns-webservices-_ws_fault_code?branch=master)
-   [**WS\_FAULT\_DETAIL\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_fault_detail_description?branch=master)
-   [**WS\_FAULT\_REASON**](/windows/win32/WebServices/ns-webservices-_ws_fault_reason?branch=master)

 

 




