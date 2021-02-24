---
title: Message (Windows Web Services)
description: A message is an object that encapsulates data that is transmitted or received.
ms.assetid: edc810d9-7d78-4b79-8cbb-e87401f6ae41
keywords:
- Message Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Message (Windows Web Services)

A message is an object that encapsulates data that is transmitted or received. The structure of a message is defined by SOAP and includes a set of headers and a body. The headers are always buffered in memory, but the body is read and written with a streaming API.

![Diagram showing a message with the header being buffered and the body being streamed.](images/messageenvelope.png)


Messages have a set of properties which can be used to specify optional settings that control the behavior of a message, and to provide a way to retrieve additional information about received messages (such as security information). See [**WS\_MESSAGE\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_message_property_id) for a complete list of message properties.

A message is addressed to a specific [Endpoint Address](endpoint-address.md).

A [**WS\_FAULT**](/windows/desktop/api/WebServices/ns-webservices-ws_fault) is a special sort of message content used to represent failures returned from from a remote endpoint.

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
| [**WS\_MESSAGE\_DONE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_message_done_callback) | Notifies the caller that the message has completed its use of either the WS\_XML\_READER structure that was supplied to WsReadEnvelopeStart function, or of the WS\_XML\_WRITER structure supplied to the WsWriteEnvelopeStart function. |



 



| Enumeration                                                      | Description                                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**WS\_ADDRESSING\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_addressing_version)         | The version of the specification used for the addressing headers.                                        |
| [**WS\_ENVELOPE\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_envelope_version)             | The version of the specification used for the envelope structure.                                        |
| [**WS\_HEADER\_ATTRIBUTES**](/windows/win32/api/webservices/ne-webservices-ws_xml_text_type)           | A set of flags representing the SOAP mustUnderstand and relay attributes of a header.                    |
| [**WS\_HEADER\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_header_type)                       | The type of the header.                                                                                  |
| [**WS\_MESSAGE\_INITIALIZATION**](/windows/desktop/api/WebServices/ne-webservices-ws_message_initialization) | Specifies what headers the [**WsInitializeMessage**](/windows/desktop/api/WebServices/nf-webservices-wsinitializemessage) should add to the message. |
| [**WS\_MESSAGE\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_message_property_id)      | The ID of each message property.                                                                         |
| [**WS\_MESSAGE\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_message_state)                   | The state of the message.                                                                                |



 



| Function                                                             | Description                                                                                                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WsAddressMessage**](/windows/desktop/api/WebServices/nf-webservices-wsaddressmessage)                         | Assigns a destination address to a message.                                                                                                            |
| [**WsCheckMustUnderstandHeaders**](/windows/desktop/api/WebServices/nf-webservices-wscheckmustunderstandheaders) | Verifies that specified headers were appropriately understood by the receiver.                                                                         |
| [**WsCreateMessage**](/windows/desktop/api/WebServices/nf-webservices-wscreatemessage)                           | Creates an instance of a [WS\_MESSAGE](ws-message.md) object.                                                                                         |
| [**WsCreateMessageForChannel**](/windows/desktop/api/WebServices/nf-webservices-wscreatemessageforchannel)       | Creates a message that is appropriate for use with a specific channel.                                                                                 |
| [**WsFillBody**](/windows/desktop/api/WebServices/nf-webservices-wsfillbody)                                     | Ensures that there are a sufficient number of bytes available in a message for reading.                                                                |
| [**WsFlushBody**](/windows/desktop/api/WebServices/nf-webservices-wsflushbody)                                   | Flushes all accumulated message body data that has been written.                                                                                       |
| [**WsFreeMessage**](/windows/desktop/api/WebServices/nf-webservices-wsfreemessage)                               | Releases the memory resource associated with a message.                                                                                                |
| [**WsGetCustomHeader**](/windows/desktop/api/WebServices/nf-webservices-wsgetcustomheader)                       | Finds the application-defined header of the message and deserializes it.                                                                               |
| [**WsGetHeader**](/windows/desktop/api/WebServices/nf-webservices-wsgetheader)                                   | Finds a particular standard header in the message and deserializes it.                                                                                 |
| [**WsGetHeaderAttributes**](/windows/desktop/api/WebServices/nf-webservices-wsgetheaderattributes)               | Populates a ULONG parameter with the [**WS\_HEADER\_ATTRIBUTES**](/windows/win32/api/webservices/ne-webservices-ws_xml_text_type) from the header element on which the reader is positioned. |
| [**WsGetMessageProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetmessageproperty)                 | Retrieves a specified Message object property.                                                                                                         |
| [**WsInitializeMessage**](/windows/desktop/api/WebServices/nf-webservices-wsinitializemessage)                   | Initializes the headers for the message in preparation for processing.                                                                                 |
| [**WsMarkHeaderAsUnderstood**](/windows/desktop/api/WebServices/nf-webservices-wsmarkheaderasunderstood)         | Marks a header as understood by the application.                                                                                                       |
| [**WsReadBody**](/windows/desktop/api/WebServices/nf-webservices-wsreadbody)                                     | Deserializes a value from the XML Reader of the message.                                                                                               |
| [**WsReadEnvelopeEnd**](/windows/desktop/api/WebServices/nf-webservices-wsreadenvelopeend)                       | Reads the closing elements of a message.                                                                                                               |
| [**WsReadEnvelopeStart**](/windows/desktop/api/WebServices/nf-webservices-wsreadenvelopestart)                   | Reads the headers of the message and prepares to read the body elements.                                                                               |
| [**WsRemoveCustomHeader**](/windows/desktop/api/WebServices/nf-webservices-wsremovecustomheader)                 | Removes a custom header from the message.                                                                                                              |
| [**WsRemoveHeader**](/windows/desktop/api/WebServices/nf-webservices-wsremoveheader)                             | Removes the standard [**WS\_HEADER\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_header_type) object from a message.                                                                 |
| [**WsResetMessage**](/windows/desktop/api/WebServices/nf-webservices-wsresetmessage)                             | Sets the Message state back to **WS\_MESSAGE\_STATE\_EMPTY**.                                                                                          |
| [**WsSetHeader**](/windows/desktop/api/WebServices/nf-webservices-wssetheader)                                   | Adds or replaces the specified standard header in the message.                                                                                         |
| [**WsWriteBody**](/windows/desktop/api/WebServices/nf-webservices-wswritebody)                                   | Writes a value in the body of a message.                                                                                                               |
| [**WsWriteEnvelopeEnd**](/windows/desktop/api/WebServices/nf-webservices-wswriteenvelopeend)                     | Writes the closing elements of a message.                                                                                                              |
| [**WsWriteEnvelopeStart**](/windows/desktop/api/WebServices/nf-webservices-wswriteenvelopestart)                 | Writes the start of the message including the current set of headers of the message and prepares to write the body elements.                           |



 



| Handle                        | Description                                         |
|-------------------------------|-----------------------------------------------------|
| [WS\_MESSAGE](ws-message.md) | The opaque type used to reference a message object. |



 



| Structure                                                | Description                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**WS\_FAULT**](/windows/desktop/api/WebServices/ns-webservices-ws_fault)                            | A fault value carried in the body of a message which indicates a processing failure. |
| [**WS\_FAULT\_CODE**](/windows/desktop/api/WebServices/ns-webservices-ws_fault_code)                 | Represents a fault code.                                                             |
| [**WS\_FAULT\_REASON**](/windows/desktop/api/WebServices/ns-webservices-ws_fault_reason)             | Contains an explanation of the fault.                                                |
| [**WS\_MESSAGE\_PROPERTIES**](/windows/desktop/api/WebServices/ns-webservices-ws_message_properties) | Specifies a set of [**WS\_MESSAGE\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_message_property) structures.  |
| [**WS\_MESSAGE\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_message_property)     | Specifies a message specific setting.                                                |



 

 

 




