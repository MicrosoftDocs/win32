---
title: Channel
description: Channels encapsulate a communication context between two or more parties and are used to send and receive messages.
ms.assetid: '5a04580d-c89f-4505-a4b7-0724ffb788fd'
keywords: ["Channel Web Services for Windows", "WWSAPI", "WWS"]
---

# Channel

Channels encapsulate a communication context between two or more parties and are used to send and receive messages.

## 

On the client, use [**WsCreateChannel**](wscreatechannel.md) to create a channel. On the server, use [**WsCreateChannelForListener**](wscreatechannelforlistener.md) to create a channel that can be accepted by the client using a [listener](listener.md).

When you create a channel, you specify the following information, which determines both the local behavior of the channel and the wire protocol to be used.

-   A [**WS\_CHANNEL\_TYPE**](ws-channel-type.md), which identifies the message exchange pattern of the channel.
-   A [**WS\_CHANNEL\_BINDING**](ws-channel-binding.md), which identifies the transfer protocol to use.
-   A [**WS\_SECURITY\_DESCRIPTION**](ws-security-description.md), which specifies the security used for the channel. When creating channels for use in a server, this is specified once for all channels that will be accepted for a given listener.
-   A set [**WS\_CHANNEL\_PROPERTY**](ws-channel-property.md)s, which specify additional optional settings (for a list of these settings, see the [**WS\_CHANNEL\_PROPERTY\_ID**](ws-channel-property-id.md) enumerations).

Before you use the channel, you must open it by calling the [**WsOpenChannel**](wsopenchannel.md) function, and specifying the channel and [endpoint address](endpoint-address.md), along with other, optional information.

For information on the state transitions for a channel, see the [**Channel States**](ws-channel-state.md) topic.

For more information on channels, see the [Channel Layer Overview](channel-layer-overview.md) topic.

The following API elements are used with channels.

| Callback                                                                                  | Description                                                                                                                                           |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ABANDON\_MESSAGE\_CALLBACK**](ws-abandon-message-callback.md)                     | Handles the [**WsAbandonMessage**](wsabandonmessage.md) call for a channel with custom channel binding.                                              |
| [**WS\_ABORT\_CHANNEL\_CALLBACK**](ws-abort-channel-callback.md)                         | Handles the [**WsAbortChannel**](wsabortchannel.md) call for a channel with custom channel binding.                                                  |
| [**WS\_CLOSE\_CHANNEL\_CALLBACK**](ws-close-channel-callback.md)                         | Handles the [**WsCloseChannel**](wsclosechannel.md) call for a channel with custom channel binding.                                                  |
| [**WS\_CREATE\_CHANNEL\_CALLBACK**](ws-create-channel-callback.md)                       | Handles the [**WsCloseChannel**](wsclosechannel.md) call for a channel with custom channel binding.                                                  |
| [**WS\_CREATE\_DECODER\_CALLBACK**](ws-create-decoder-callback.md)                       | Handles creating a decoder instance.                                                                                                                  |
| [**WS\_CREATE\_ENCODER\_CALLBACK**](ws-create-encoder-callback.md)                       | Handles creating an encoder instance.                                                                                                                 |
| [**WS\_DECODER\_DECODE\_CALLBACK**](ws-decoder-decode-callback.md)                       | Decodes a message.                                                                                                                                    |
| [**WS\_DECODER\_END\_CALLBACK**](ws-decoder-end-callback.md)                             | Decodes the end of a message.                                                                                                                         |
| [**WS\_DECODER\_GET\_CONTENT\_TYPE\_CALLBACK**](ws-decoder-get-content-type-callback.md) | Gets the content type of the message.                                                                                                                 |
| [**WS\_DECODER\_START\_CALLBACK**](ws-decoder-start-callback.md)                         | Starts decoding a message.                                                                                                                            |
| [**WS\_ENCODER\_ENCODE\_CALLBACK**](ws-encoder-encode-callback.md)                       | Encodes a message.                                                                                                                                    |
| [**WS\_ENCODER\_END\_CALLBACK**](ws-encoder-end-callback.md)                             | Encodes the end of a message.                                                                                                                         |
| [**WS\_ENCODER\_GET\_CONTENT\_TYPE\_CALLBACK**](ws-encoder-get-content-type-callback.md) | Gets the content type of the message.                                                                                                                 |
| [**WS\_ENCODER\_START\_CALLBACK**](ws-encoder-start-callback.md)                         | Starts encoding a message.                                                                                                                            |
| [**WS\_FREE\_CHANNEL\_CALLBACK**](ws-free-channel-callback.md)                           | Handles the [**WsFreeChannel**](wsfreechannel.md) call for a channel with custom channel binding.                                                    |
| [**WS\_FREE\_DECODER\_CALLBACK**](ws-free-decoder-callback.md)                           | Handles freeing a decoder instance.                                                                                                                   |
| [**WS\_FREE\_ENCODER\_CALLBACK**](ws-free-encoder-callback.md)                           | Handles freeing an encoder instance.                                                                                                                  |
| [**WS\_GET\_CHANNEL\_PROPERTY\_CALLBACK**](ws-get-channel-property-callback.md)          | Handles the [**WsGetChannelProperty**](wsgetchannelproperty.md) call for a channel with custom channel binding.                                      |
| [**WS\_HTTP\_REDIRECT\_CALLBACK**](ws-http-redirect-callback.md)                         | Invoked when a message is about to be automatically redirected to another service utilizing HTTP auto redirect functionality as described in RFC2616. |
| [**WS\_OPEN\_CHANNEL\_CALLBACK**](ws-open-channel-callback.md)                           | Handles the [**WsOpenChannel**](wsopenchannel.md) call for a channel with custom channel binding.                                                    |
| [**WS\_READ\_MESSAGE\_END\_CALLBACK**](ws-read-message-end-callback.md)                  | Handles the [**WsReadMessageEnd**](wsreadmessageend.md) call for a channel with custom channel binding.                                              |
| [**WS\_READ\_MESSAGE\_START\_CALLBACK**](ws-read-message-start-callback.md)              | Handles the [**WsReadMessageEnd**](wsreadmessageend.md) call for a channel with custom channel binding.                                              |
| [**WS\_RESET\_CHANNEL\_CALLBACK**](ws-reset-channel-callback.md)                         | Handles the [**WsResetChannel**](wsresetchannel.md) call for a channel with custom channel binding.                                                  |
| [**WS\_SET\_CHANNEL\_PROPERTY\_CALLBACK**](ws-set-channel-property-callback.md)          | Handles the [**WsSetChannelProperty**](wssetchannelproperty.md) call for a channel with custom channel binding.                                      |
| [**WS\_SHUTDOWN\_SESSION\_CHANNEL\_CALLBACK**](ws-shutdown-session-channel-callback.md)  | Handles the [**WsShutdownSessionChannel**](wsshutdownsessionchannel.md) call for a channel with custom channel binding.                              |
| [**WS\_WRITE\_MESSAGE\_END\_CALLBACK**](ws-write-message-end-callback.md)                | Handles the [**WsWriteMessageEnd**](wswritemessageend.md) call for a channel with custom channel binding.                                            |
| [**WS\_WRITE\_MESSAGE\_START\_CALLBACK**](ws-write-message-start-callback.md)            | Handles the [**WsWriteMessageStart**](wswritemessagestart.md) call for a channel with custom channel binding.                                        |



 



| Enumeration                                                 | Description                                                                                                                               |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CHANNEL\_BINDING**](ws-channel-binding.md)          | Indicates the protocol stack to use for the channel.                                                                                      |
| [**WS\_CHANNEL\_PROPERTY\_ID**](ws-channel-property-id.md) | Identifies each channel property by an ID.                                                                                                |
| [**WS\_CHANNEL\_STATE**](ws-channel-state.md)              | The state of the channel.                                                                                                                 |
| [**WS\_CHANNEL\_TYPE**](ws-channel-type.md)                | Indicates the basic characteristics of the channel, such as whether it is sessionful, and what directions of communication are supported. |
| [**WS\_ENCODING**](ws-encoding.md)                         | The different encodings (message formats).                                                                                                |
| [**WS\_RECEIVE\_OPTION**](ws-receive-option.md)            | Specifies whether a message is required when receiving from a channel.                                                                    |
| [**WS\_TRANSFER\_MODE**](ws-transfer-mode.md)              | Specifies whether messages that are sent or received are streamed or buffered.                                                            |



 



| Function                                                         | Description                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**WsAbandonMessage**](wsabandonmessage.md)                     | Skips the remainder of a message for a channel.                                                              |
| [**WsAbortChannel**](wsabortchannel.md)                         | Aborts all pending I/O on a specified channel and sets the channel state to **WS\_CHANNEL\_STATE\_FAULTED**. |
| [**WsCloseChannel**](wsclosechannel.md)                         | Closes a channel when it is no longer needed.                                                                |
| [**WsCreateChannel**](wscreatechannel.md)                       | Creates a channel.                                                                                           |
| [**WsCreateChannelForListener**](wscreatechannelforlistener.md) | Creates a channel for a listener.                                                                            |
| [**WsFreeChannel**](wsfreechannel.md)                           | Releases the memory resources associated with a channel.                                                     |
| [**WsGetChannelProperty**](wsgetchannelproperty.md)             | Retrieves a property of the Channel referenced by the channel parameter.                                     |
| [**WsOpenChannel**](wsopenchannel.md)                           | Opens a channel to an endpoint.                                                                              |
| [**WsReadMessageEnd**](wsreadmessageend.md)                     | Reads the closing elements of a message from a channel.                                                      |
| [**WsReadMessageStart**](wsreadmessagestart.md)                 | Reads the headers of the next message from the channel and prepares to read the body elements.               |
| [**WsReceiveMessage**](wsreceivemessage.md)                     | Receives a message and deserializes the body of the message as a value.                                      |
| [**WsRequestReply**](wsrequestreply.md)                         | Sends a request message and receives a correlated reply message.                                             |
| [**WsResetChannel**](wsresetchannel.md)                         | Reset a channel so it can be reused.                                                                         |
| [**WsSendMessage**](wssendmessage.md)                           | Sends a message on a channel using serialization to write the body element.                                  |
| [**WsSendReplyMessage**](wssendreplymessage.md)                 | Sends a message that is a reply to a received message.                                                       |
| [**WsSetChannelProperty**](wssetchannelproperty.md)             | Sets a property of a channel.                                                                                |
| [**WsSetMessageProperty**](wssetmessageproperty.md)             | Sets a property of a message.                                                                                |
| [**WsWriteMessageEnd**](wswritemessageend.md)                   | Writes the closing elements of a message to the channel.                                                     |
| [**WsWriteMessageStart**](wswritemessagestart.md)               | Write out the headers of a message to the channel and prepares to write the body elements.                   |



 



| Handle                        | Description                                 |
|-------------------------------|---------------------------------------------|
| [WS\_CHANNEL](ws-channel.md) | An opaque type used to reference a channel. |



 



| Structure                                                                          | Description                                                                                                                                                                                      |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CHANNEL\_DECODER**](ws-channel-decoder.md)                                 | A set of callbacks that transform the content type and encoded bytes of a received message.                                                                                                      |
| [**WS\_CHANNEL\_ENCODER**](ws-channel-encoder.md)                                 | A set of callbacks that can transform the content type and encoded bytes of a sent message.                                                                                                      |
| [**WS\_CHANNEL\_PROPERTIES**](ws-channel-properties.md)                           | A set of [**WS\_CHANNEL\_PROPERTY**](ws-channel-property.md) structures.                                                                                                                        |
| [**WS\_CHANNEL\_PROPERTY**](ws-channel-property.md)                               | A channel-specific setting.                                                                                                                                                                      |
| [**WS\_CUSTOM\_CHANNEL\_CALLBACKS**](ws-custom-channel-callbacks.md)              | A set of callbacks that form the implementation of a custom channel.                                                                                                                             |
| [**WS\_CUSTOM\_HTTP\_PROXY**](ws-custom-http-proxy.md)                            | used to specify the custom proxy for the channel, using the **WS\_CHANNEL\_PROPERTY\_CUSTOM\_HTTP**\_PROXY value of the [**WS\_CHANNEL\_PROPERTY\_ID**](ws-channel-property-id.md) enumeration. |
| [**WS\_HTTP\_HEADER\_MAPPING**](ws-http-header-mapping.md)                        | Represents an individual header that is mapped as part of [**WS\_HTTP\_MESSAGE\_MAPPING**](ws-http-message-mapping.md).                                                                         |
| [**WS\_HTTP\_MESSAGE\_MAPPING**](ws-http-message-mapping.md)                      | Information about how an HTTP request or response should be represented in a message object.                                                                                                     |
| [**WS\_HTTP\_REDIRECT\_CALLBACK\_CONTEXT**](ws-http-redirect-callback-context.md) | Specifies the callback function and state for controlling the HTTP automatic redirection behavior.                                                                                               |
| [**WS\_MESSAGE\_DESCRIPTION**](ws-message-description.md)                         | The schema for the input and output [WS\_MESSAGE](ws-message.md) for a given operation description.                                                                                             |



 

 

 




