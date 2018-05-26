---
title: Message
description: A message is an object that encapsulates data that is transmitted or received.
ms.assetid: edc810d9-7d78-4b79-8cbb-e87401f6ae41
keywords:
- Message Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Message

A message is an object that encapsulates data that is transmitted or received. The structure of a message is defined by SOAP and includes a set of headers and a body. The headers are always buffered in memory, but the body is read and written with a streaming API.

![](images/messageenvelope.png)

## 

Messages have a set of properties which can be used to specify optional settings that control the behavior of a message, and to provide a way to retrieve additional information about received messages (such as security information). See [**WS\_MESSAGE\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_message_property_id?branch=master) for a complete list of message properties.

A message is addressed to a specific [Endpoint Address](endpoint-address.md).

A [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master) is a special sort of message content used to represent failures returned from from a remote endpoint.

Messages undergo encoding that transforms the XML to a linear wire format before being transmitted.

For more information on messages, see the [Channel Layer Overview](channel-layer-overview.md) topic.

The following examples illustrate using messages in WWSAPI.

| Example                                              | Description                                  |
|------------------------------------------------------|----------------------------------------------|
| [CustomHeaderExample](customheaderexample.md)       | Illustrates using custom message headers.    |
| [MessageEncodingExample](messageencodingexample.md) | Illustrates encoding and decoding a message. |
| [ForwardMessageExample](forwardmessageexample.md)   | Illustrates forwarding a message.            |



 

The following API elements are used with messages.

| Callback                                                        | Description                                                                                                                                                                                                                              |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_MESSAGE\_DONE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_message_done_callback?branch=master) | Notifies the caller that the message has completed its use of either the WS\_XML\_READER structure that was supplied to WsReadEnvelopeStart function, or of the WS\_XML\_WRITER structure supplied to the WsWriteEnvelopeStart function. |



 



| Enumeration                                                      | Description                                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**WS\_ADDRESSING\_VERSION**](/windows/win32/WebServices/ne-webservices-ws_addressing_version?branch=master)         | The version of the specification used for the addressing headers.                                        |
| [**WS\_ENVELOPE\_VERSION**](/windows/win32/WebServices/ne-webservices-ws_envelope_version?branch=master)             | The version of the specification used for the envelope structure.                                        |
| [**WS\_HEADER\_ATTRIBUTES**](/windows/win32/WebServices/?branch=master)           | A set of flags representing the SOAP mustUnderstand and relay attributes of a header.                    |
| [**WS\_HEADER\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_header_type?branch=master)                       | The type of the header.                                                                                  |
| [**WS\_MESSAGE\_INITIALIZATION**](/windows/win32/WebServices/ne-webservices-ws_message_initialization?branch=master) | Specifies what headers the [**WsInitializeMessage**](/windows/win32/WebServices/nf-webservices-wsinitializemessage?branch=master) should add to the message. |
| [**WS\_MESSAGE\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_message_property_id?branch=master)      | The ID of each message property.                                                                         |
| [**WS\_MESSAGE\_STATE**](/windows/win32/WebServices/ne-webservices-ws_message_state?branch=master)                   | The state of the message.                                                                                |



 



| Function                                                             | Description                                                                                                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WsAddressMessage**](/windows/win32/WebServices/nf-webservices-wsaddressmessage?branch=master)                         | Assigns a destination address to a message.                                                                                                            |
| [**WsCheckMustUnderstandHeaders**](/windows/win32/WebServices/nf-webservices-wscheckmustunderstandheaders?branch=master) | Verifies that specified headers were appropriately understood by the receiver.                                                                         |
| [**WsCreateMessage**](/windows/win32/WebServices/nf-webservices-wscreatemessage?branch=master)                           | Creates an instance of a [WS\_MESSAGE](ws-message.md) object.                                                                                         |
| [**WsCreateMessageForChannel**](/windows/win32/WebServices/nf-webservices-wscreatemessageforchannel?branch=master)       | Creates a message that is appropriate for use with a specific channel.                                                                                 |
| [**WsFillBody**](/windows/win32/WebServices/nf-webservices-wsfillbody?branch=master)                                     | Ensures that there are a sufficient number of bytes available in a message for reading.                                                                |
| [**WsFlushBody**](/windows/win32/WebServices/nf-webservices-wsflushbody?branch=master)                                   | Flushes all accumulated message body data that has been written.                                                                                       |
| [**WsFreeMessage**](/windows/win32/WebServices/nf-webservices-wsfreemessage?branch=master)                               | Releases the memory resource associated with a message.                                                                                                |
| [**WsGetCustomHeader**](/windows/win32/WebServices/nf-webservices-wsgetcustomheader?branch=master)                       | Finds the application-defined header of the message and deserializes it.                                                                               |
| [**WsGetHeader**](/windows/win32/WebServices/nf-webservices-wsgetheader?branch=master)                                   | Finds a particular standard header in the message and deserializes it.                                                                                 |
| [**WsGetHeaderAttributes**](/windows/win32/WebServices/nf-webservices-wsgetheaderattributes?branch=master)               | Populates a ULONG parameter with the [**WS\_HEADER\_ATTRIBUTES**](/windows/win32/WebServices/?branch=master) from the header element on which the reader is positioned. |
| [**WsGetMessageProperty**](/windows/win32/WebServices/nf-webservices-wsgetmessageproperty?branch=master)                 | Retrieves a specified Message object property.                                                                                                         |
| [**WsInitializeMessage**](/windows/win32/WebServices/nf-webservices-wsinitializemessage?branch=master)                   | Initializes the headers for the message in preparation for processing.                                                                                 |
| [**WsMarkHeaderAsUnderstood**](/windows/win32/WebServices/nf-webservices-wsmarkheaderasunderstood?branch=master)         | Marks a header as understood by the application.                                                                                                       |
| [**WsReadBody**](/windows/win32/WebServices/nf-webservices-wsreadbody?branch=master)                                     | Deserializes a value from the XML Reader of the message.                                                                                               |
| [**WsReadEnvelopeEnd**](/windows/win32/WebServices/nf-webservices-wsreadenvelopeend?branch=master)                       | Reads the closing elements of a message.                                                                                                               |
| [**WsReadEnvelopeStart**](/windows/win32/WebServices/nf-webservices-wsreadenvelopestart?branch=master)                   | Reads the headers of the message and prepares to read the body elements.                                                                               |
| [**WsRemoveCustomHeader**](/windows/win32/WebServices/nf-webservices-wsremovecustomheader?branch=master)                 | Removes a custom header from the message.                                                                                                              |
| [**WsRemoveHeader**](/windows/win32/WebServices/nf-webservices-wsremoveheader?branch=master)                             | Removes the standard [**WS\_HEADER\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_header_type?branch=master) object from a message.                                                                 |
| [**WsResetMessage**](/windows/win32/WebServices/nf-webservices-wsresetmessage?branch=master)                             | Sets the Message state back to **WS\_MESSAGE\_STATE\_EMPTY**.                                                                                          |
| [**WsSetHeader**](/windows/win32/WebServices/nf-webservices-wssetheader?branch=master)                                   | Adds or replaces the specified standard header in the message.                                                                                         |
| [**WsWriteBody**](/windows/win32/WebServices/nf-webservices-wswritebody?branch=master)                                   | Writes a value in the body of a message.                                                                                                               |
| [**WsWriteEnvelopeEnd**](/windows/win32/WebServices/nf-webservices-wswriteenvelopeend?branch=master)                     | Writes the closing elements of a message.                                                                                                              |
| [**WsWriteEnvelopeStart**](/windows/win32/WebServices/nf-webservices-wswriteenvelopestart?branch=master)                 | Writes the start of the message including the current set of headers of the message and prepares to write the body elements.                           |



 



| Handle                        | Description                                         |
|-------------------------------|-----------------------------------------------------|
| [WS\_MESSAGE](ws-message.md) | The opaque type used to reference a message object. |



 



| Structure                                                | Description                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**WS\_FAULT**](/windows/win32/WebServices/ns-webservices-_ws_fault?branch=master)                            | A fault value carried in the body of a message which indicates a processing failure. |
| [**WS\_FAULT\_CODE**](/windows/win32/WebServices/ns-webservices-_ws_fault_code?branch=master)                 | Represents a fault code.                                                             |
| [**WS\_FAULT\_REASON**](/windows/win32/WebServices/ns-webservices-_ws_fault_reason?branch=master)             | Contains an explanation of the fault.                                                |
| [**WS\_MESSAGE\_PROPERTIES**](/windows/win32/WebServices/ns-webservices-_ws_message_properties?branch=master) | Specifies a set of [**WS\_MESSAGE\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_message_property?branch=master) structures.  |
| [**WS\_MESSAGE\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_message_property?branch=master)     | Specifies a message specific setting.                                                |



 

 

 




