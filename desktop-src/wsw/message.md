---
title: Message
description: A message is an object that encapsulates data that is transmitted or received.
ms.assetid: 'edc810d9-7d78-4b79-8cbb-e87401f6ae41'
keywords: ["Message Web Services for Windows", "WWSAPI", "WWS"]
---

# Message

A message is an object that encapsulates data that is transmitted or received. The structure of a message is defined by SOAP and includes a set of headers and a body. The headers are always buffered in memory, but the body is read and written with a streaming API.

![](images/messageenvelope.png)

## 

Messages have a set of properties which can be used to specify optional settings that control the behavior of a message, and to provide a way to retrieve additional information about received messages (such as security information). See [**WS\_MESSAGE\_PROPERTY\_ID**](ws-message-property-id.md) for a complete list of message properties.

A message is addressed to a specific [Endpoint Address](endpoint-address.md).

A [**WS\_FAULT**](ws-fault.md) is a special sort of message content used to represent failures returned from from a remote endpoint.

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
| [**WS\_MESSAGE\_DONE\_CALLBACK**](ws-message-done-callback.md) | Notifies the caller that the message has completed its use of either the WS\_XML\_READER structure that was supplied to WsReadEnvelopeStart function, or of the WS\_XML\_WRITER structure supplied to the WsWriteEnvelopeStart function. |



 



| Enumeration                                                      | Description                                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**WS\_ADDRESSING\_VERSION**](ws-addressing-version.md)         | The version of the specification used for the addressing headers.                                        |
| [**WS\_ENVELOPE\_VERSION**](ws-envelope-version.md)             | The version of the specification used for the envelope structure.                                        |
| [**WS\_HEADER\_ATTRIBUTES**](ws-header-attributes.md)           | A set of flags representing the SOAP mustUnderstand and relay attributes of a header.                    |
| [**WS\_HEADER\_TYPE**](ws-header-type.md)                       | The type of the header.                                                                                  |
| [**WS\_MESSAGE\_INITIALIZATION**](ws-message-initialization.md) | Specifies what headers the [**WsInitializeMessage**](wsinitializemessage.md) should add to the message. |
| [**WS\_MESSAGE\_PROPERTY\_ID**](ws-message-property-id.md)      | The ID of each message property.                                                                         |
| [**WS\_MESSAGE\_STATE**](ws-message-state.md)                   | The state of the message.                                                                                |



 



| Function                                                             | Description                                                                                                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WsAddressMessage**](wsaddressmessage.md)                         | Assigns a destination address to a message.                                                                                                            |
| [**WsCheckMustUnderstandHeaders**](wscheckmustunderstandheaders.md) | Verifies that specified headers were appropriately understood by the receiver.                                                                         |
| [**WsCreateMessage**](wscreatemessage.md)                           | Creates an instance of a [WS\_MESSAGE](ws-message.md) object.                                                                                         |
| [**WsCreateMessageForChannel**](wscreatemessageforchannel.md)       | Creates a message that is appropriate for use with a specific channel.                                                                                 |
| [**WsFillBody**](wsfillbody.md)                                     | Ensures that there are a sufficient number of bytes available in a message for reading.                                                                |
| [**WsFlushBody**](wsflushbody.md)                                   | Flushes all accumulated message body data that has been written.                                                                                       |
| [**WsFreeMessage**](wsfreemessage.md)                               | Releases the memory resource associated with a message.                                                                                                |
| [**WsGetCustomHeader**](wsgetcustomheader.md)                       | Finds the application-defined header of the message and deserializes it.                                                                               |
| [**WsGetHeader**](wsgetheader.md)                                   | Finds a particular standard header in the message and deserializes it.                                                                                 |
| [**WsGetHeaderAttributes**](wsgetheaderattributes.md)               | Populates a ULONG parameter with the [**WS\_HEADER\_ATTRIBUTES**](ws-header-attributes.md) from the header element on which the reader is positioned. |
| [**WsGetMessageProperty**](wsgetmessageproperty.md)                 | Retrieves a specified Message object property.                                                                                                         |
| [**WsInitializeMessage**](wsinitializemessage.md)                   | Initializes the headers for the message in preparation for processing.                                                                                 |
| [**WsMarkHeaderAsUnderstood**](wsmarkheaderasunderstood.md)         | Marks a header as understood by the application.                                                                                                       |
| [**WsReadBody**](wsreadbody.md)                                     | Deserializes a value from the XML Reader of the message.                                                                                               |
| [**WsReadEnvelopeEnd**](wsreadenvelopeend.md)                       | Reads the closing elements of a message.                                                                                                               |
| [**WsReadEnvelopeStart**](wsreadenvelopestart.md)                   | Reads the headers of the message and prepares to read the body elements.                                                                               |
| [**WsRemoveCustomHeader**](wsremovecustomheader.md)                 | Removes a custom header from the message.                                                                                                              |
| [**WsRemoveHeader**](wsremoveheader.md)                             | Removes the standard [**WS\_HEADER\_TYPE**](ws-header-type.md) object from a message.                                                                 |
| [**WsResetMessage**](wsresetmessage.md)                             | Sets the Message state back to **WS\_MESSAGE\_STATE\_EMPTY**.                                                                                          |
| [**WsSetHeader**](wssetheader.md)                                   | Adds or replaces the specified standard header in the message.                                                                                         |
| [**WsWriteBody**](wswritebody.md)                                   | Writes a value in the body of a message.                                                                                                               |
| [**WsWriteEnvelopeEnd**](wswriteenvelopeend.md)                     | Writes the closing elements of a message.                                                                                                              |
| [**WsWriteEnvelopeStart**](wswriteenvelopestart.md)                 | Writes the start of the message including the current set of headers of the message and prepares to write the body elements.                           |



 



| Handle                        | Description                                         |
|-------------------------------|-----------------------------------------------------|
| [WS\_MESSAGE](ws-message.md) | The opaque type used to reference a message object. |



 



| Structure                                                | Description                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**WS\_FAULT**](ws-fault.md)                            | A fault value carried in the body of a message which indicates a processing failure. |
| [**WS\_FAULT\_CODE**](ws-fault-code.md)                 | Represents a fault code.                                                             |
| [**WS\_FAULT\_REASON**](ws-fault-reason.md)             | Contains an explanation of the fault.                                                |
| [**WS\_MESSAGE\_PROPERTIES**](ws-message-properties.md) | Specifies a set of [**WS\_MESSAGE\_PROPERTY**](ws-message-property.md) structures.  |
| [**WS\_MESSAGE\_PROPERTY**](ws-message-property.md)     | Specifies a message specific setting.                                                |



 

 

 




