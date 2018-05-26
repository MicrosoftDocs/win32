---
title: Channel
description: Channels encapsulate a communication context between two or more parties and are used to send and receive messages.
ms.assetid: 5a04580d-c89f-4505-a4b7-0724ffb788fd
keywords:
- Channel Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Channel

Channels encapsulate a communication context between two or more parties and are used to send and receive messages.

## 

On the client, use [**WsCreateChannel**](/windows/win32/WebServices/nf-webservices-wscreatechannel?branch=master) to create a channel. On the server, use [**WsCreateChannelForListener**](/windows/win32/WebServices/nf-webservices-wscreatechannelforlistener?branch=master) to create a channel that can be accepted by the client using a [listener](listener.md).

When you create a channel, you specify the following information, which determines both the local behavior of the channel and the wire protocol to be used.

-   A [**WS\_CHANNEL\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_channel_type?branch=master), which identifies the message exchange pattern of the channel.
-   A [**WS\_CHANNEL\_BINDING**](/windows/win32/WebServices/ne-webservices-ws_channel_binding?branch=master), which identifies the transfer protocol to use.
-   A [**WS\_SECURITY\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_security_description?branch=master), which specifies the security used for the channel. When creating channels for use in a server, this is specified once for all channels that will be accepted for a given listener.
-   A set [**WS\_CHANNEL\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_channel_property?branch=master)s, which specify additional optional settings (for a list of these settings, see the [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_channel_property_id?branch=master) enumerations).

Before you use the channel, you must open it by calling the [**WsOpenChannel**](/windows/win32/WebServices/nf-webservices-wsopenchannel?branch=master) function, and specifying the channel and [endpoint address](endpoint-address.md), along with other, optional information.

For information on the state transitions for a channel, see the [**Channel States**](/windows/win32/WebServices/ne-webservices-ws_channel_state?branch=master) topic.

For more information on channels, see the [Channel Layer Overview](channel-layer-overview.md) topic.

The following API elements are used with channels.

| Callback                                                                                  | Description                                                                                                                                           |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ABANDON\_MESSAGE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_abandon_message_callback?branch=master)                     | Handles the [**WsAbandonMessage**](/windows/win32/WebServices/nf-webservices-wsabandonmessage?branch=master) call for a channel with custom channel binding.                                              |
| [**WS\_ABORT\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_abort_channel_callback?branch=master)                         | Handles the [**WsAbortChannel**](/windows/win32/WebServices/nf-webservices-wsabortchannel?branch=master) call for a channel with custom channel binding.                                                  |
| [**WS\_CLOSE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_close_channel_callback?branch=master)                         | Handles the [**WsCloseChannel**](/windows/win32/WebServices/nf-webservices-wsclosechannel?branch=master) call for a channel with custom channel binding.                                                  |
| [**WS\_CREATE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_channel_callback?branch=master)                       | Handles the [**WsCloseChannel**](/windows/win32/WebServices/nf-webservices-wsclosechannel?branch=master) call for a channel with custom channel binding.                                                  |
| [**WS\_CREATE\_DECODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_decoder_callback?branch=master)                       | Handles creating a decoder instance.                                                                                                                  |
| [**WS\_CREATE\_ENCODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_encoder_callback?branch=master)                       | Handles creating an encoder instance.                                                                                                                 |
| [**WS\_DECODER\_DECODE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_decode_callback?branch=master)                       | Decodes a message.                                                                                                                                    |
| [**WS\_DECODER\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_end_callback?branch=master)                             | Decodes the end of a message.                                                                                                                         |
| [**WS\_DECODER\_GET\_CONTENT\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_get_content_type_callback?branch=master) | Gets the content type of the message.                                                                                                                 |
| [**WS\_DECODER\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_decoder_start_callback?branch=master)                         | Starts decoding a message.                                                                                                                            |
| [**WS\_ENCODER\_ENCODE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_encode_callback?branch=master)                       | Encodes a message.                                                                                                                                    |
| [**WS\_ENCODER\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_end_callback?branch=master)                             | Encodes the end of a message.                                                                                                                         |
| [**WS\_ENCODER\_GET\_CONTENT\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_get_content_type_callback?branch=master) | Gets the content type of the message.                                                                                                                 |
| [**WS\_ENCODER\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_encoder_start_callback?branch=master)                         | Starts encoding a message.                                                                                                                            |
| [**WS\_FREE\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_channel_callback?branch=master)                           | Handles the [**WsFreeChannel**](/windows/win32/WebServices/nf-webservices-wsfreechannel?branch=master) call for a channel with custom channel binding.                                                    |
| [**WS\_FREE\_DECODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_decoder_callback?branch=master)                           | Handles freeing a decoder instance.                                                                                                                   |
| [**WS\_FREE\_ENCODER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_encoder_callback?branch=master)                           | Handles freeing an encoder instance.                                                                                                                  |
| [**WS\_GET\_CHANNEL\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_get_channel_property_callback?branch=master)          | Handles the [**WsGetChannelProperty**](/windows/win32/WebServices/nf-webservices-wsgetchannelproperty?branch=master) call for a channel with custom channel binding.                                      |
| [**WS\_HTTP\_REDIRECT\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_http_redirect_callback?branch=master)                         | Invoked when a message is about to be automatically redirected to another service utilizing HTTP auto redirect functionality as described in RFC2616. |
| [**WS\_OPEN\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_open_channel_callback?branch=master)                           | Handles the [**WsOpenChannel**](/windows/win32/WebServices/nf-webservices-wsopenchannel?branch=master) call for a channel with custom channel binding.                                                    |
| [**WS\_READ\_MESSAGE\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_message_end_callback?branch=master)                  | Handles the [**WsReadMessageEnd**](/windows/win32/WebServices/nf-webservices-wsreadmessageend?branch=master) call for a channel with custom channel binding.                                              |
| [**WS\_READ\_MESSAGE\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_message_start_callback?branch=master)              | Handles the [**WsReadMessageEnd**](/windows/win32/WebServices/nf-webservices-wsreadmessageend?branch=master) call for a channel with custom channel binding.                                              |
| [**WS\_RESET\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_reset_channel_callback?branch=master)                         | Handles the [**WsResetChannel**](/windows/win32/WebServices/nf-webservices-wsresetchannel?branch=master) call for a channel with custom channel binding.                                                  |
| [**WS\_SET\_CHANNEL\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_set_channel_property_callback?branch=master)          | Handles the [**WsSetChannelProperty**](/windows/win32/WebServices/nf-webservices-wssetchannelproperty?branch=master) call for a channel with custom channel binding.                                      |
| [**WS\_SHUTDOWN\_SESSION\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_shutdown_session_channel_callback?branch=master)  | Handles the [**WsShutdownSessionChannel**](/windows/win32/WebServices/nf-webservices-wsshutdownsessionchannel?branch=master) call for a channel with custom channel binding.                              |
| [**WS\_WRITE\_MESSAGE\_END\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_message_end_callback?branch=master)                | Handles the [**WsWriteMessageEnd**](/windows/win32/WebServices/nf-webservices-wswritemessageend?branch=master) call for a channel with custom channel binding.                                            |
| [**WS\_WRITE\_MESSAGE\_START\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_message_start_callback?branch=master)            | Handles the [**WsWriteMessageStart**](/windows/win32/WebServices/nf-webservices-wswritemessagestart?branch=master) call for a channel with custom channel binding.                                        |



 



| Enumeration                                                 | Description                                                                                                                               |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CHANNEL\_BINDING**](/windows/win32/WebServices/ne-webservices-ws_channel_binding?branch=master)          | Indicates the protocol stack to use for the channel.                                                                                      |
| [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_channel_property_id?branch=master) | Identifies each channel property by an ID.                                                                                                |
| [**WS\_CHANNEL\_STATE**](/windows/win32/WebServices/ne-webservices-ws_channel_state?branch=master)              | The state of the channel.                                                                                                                 |
| [**WS\_CHANNEL\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_channel_type?branch=master)                | Indicates the basic characteristics of the channel, such as whether it is sessionful, and what directions of communication are supported. |
| [**WS\_ENCODING**](/windows/win32/WebServices/ne-webservices-ws_encoding?branch=master)                         | The different encodings (message formats).                                                                                                |
| [**WS\_RECEIVE\_OPTION**](/windows/win32/WebServices/ne-webservices-ws_receive_option?branch=master)            | Specifies whether a message is required when receiving from a channel.                                                                    |
| [**WS\_TRANSFER\_MODE**](/windows/win32/WebServices/ne-webservices-ws_transfer_mode?branch=master)              | Specifies whether messages that are sent or received are streamed or buffered.                                                            |



 



| Function                                                         | Description                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**WsAbandonMessage**](/windows/win32/WebServices/nf-webservices-wsabandonmessage?branch=master)                     | Skips the remainder of a message for a channel.                                                              |
| [**WsAbortChannel**](/windows/win32/WebServices/nf-webservices-wsabortchannel?branch=master)                         | Aborts all pending I/O on a specified channel and sets the channel state to **WS\_CHANNEL\_STATE\_FAULTED**. |
| [**WsCloseChannel**](/windows/win32/WebServices/nf-webservices-wsclosechannel?branch=master)                         | Closes a channel when it is no longer needed.                                                                |
| [**WsCreateChannel**](/windows/win32/WebServices/nf-webservices-wscreatechannel?branch=master)                       | Creates a channel.                                                                                           |
| [**WsCreateChannelForListener**](/windows/win32/WebServices/nf-webservices-wscreatechannelforlistener?branch=master) | Creates a channel for a listener.                                                                            |
| [**WsFreeChannel**](/windows/win32/WebServices/nf-webservices-wsfreechannel?branch=master)                           | Releases the memory resources associated with a channel.                                                     |
| [**WsGetChannelProperty**](/windows/win32/WebServices/nf-webservices-wsgetchannelproperty?branch=master)             | Retrieves a property of the Channel referenced by the channel parameter.                                     |
| [**WsOpenChannel**](/windows/win32/WebServices/nf-webservices-wsopenchannel?branch=master)                           | Opens a channel to an endpoint.                                                                              |
| [**WsReadMessageEnd**](/windows/win32/WebServices/nf-webservices-wsreadmessageend?branch=master)                     | Reads the closing elements of a message from a channel.                                                      |
| [**WsReadMessageStart**](/windows/win32/WebServices/nf-webservices-wsreadmessagestart?branch=master)                 | Reads the headers of the next message from the channel and prepares to read the body elements.               |
| [**WsReceiveMessage**](/windows/win32/WebServices/nf-webservices-wsreceivemessage?branch=master)                     | Receives a message and deserializes the body of the message as a value.                                      |
| [**WsRequestReply**](/windows/win32/WebServices/nf-webservices-wsrequestreply?branch=master)                         | Sends a request message and receives a correlated reply message.                                             |
| [**WsResetChannel**](/windows/win32/WebServices/nf-webservices-wsresetchannel?branch=master)                         | Reset a channel so it can be reused.                                                                         |
| [**WsSendMessage**](/windows/win32/WebServices/nf-webservices-wssendmessage?branch=master)                           | Sends a message on a channel using serialization to write the body element.                                  |
| [**WsSendReplyMessage**](/windows/win32/WebServices/nf-webservices-wssendreplymessage?branch=master)                 | Sends a message that is a reply to a received message.                                                       |
| [**WsSetChannelProperty**](/windows/win32/WebServices/nf-webservices-wssetchannelproperty?branch=master)             | Sets a property of a channel.                                                                                |
| [**WsSetMessageProperty**](/windows/win32/WebServices/nf-webservices-wssetmessageproperty?branch=master)             | Sets a property of a message.                                                                                |
| [**WsWriteMessageEnd**](/windows/win32/WebServices/nf-webservices-wswritemessageend?branch=master)                   | Writes the closing elements of a message to the channel.                                                     |
| [**WsWriteMessageStart**](/windows/win32/WebServices/nf-webservices-wswritemessagestart?branch=master)               | Write out the headers of a message to the channel and prepares to write the body elements.                   |



 



| Handle                        | Description                                 |
|-------------------------------|---------------------------------------------|
| [WS\_CHANNEL](ws-channel.md) | An opaque type used to reference a channel. |



 



| Structure                                                                          | Description                                                                                                                                                                                      |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CHANNEL\_DECODER**](/windows/win32/WebServices/ns-webservices-_ws_channel_decoder?branch=master)                                 | A set of callbacks that transform the content type and encoded bytes of a received message.                                                                                                      |
| [**WS\_CHANNEL\_ENCODER**](/windows/win32/WebServices/ns-webservices-_ws_channel_encoder?branch=master)                                 | A set of callbacks that can transform the content type and encoded bytes of a sent message.                                                                                                      |
| [**WS\_CHANNEL\_PROPERTIES**](/windows/win32/WebServices/ns-webservices-_ws_channel_properties?branch=master)                           | A set of [**WS\_CHANNEL\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_channel_property?branch=master) structures.                                                                                                                        |
| [**WS\_CHANNEL\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_channel_property?branch=master)                               | A channel-specific setting.                                                                                                                                                                      |
| [**WS\_CUSTOM\_CHANNEL\_CALLBACKS**](/windows/win32/WebServices/ns-webservices-_ws_custom_channel_callbacks?branch=master)              | A set of callbacks that form the implementation of a custom channel.                                                                                                                             |
| [**WS\_CUSTOM\_HTTP\_PROXY**](/windows/win32/WebServices/ns-webservices-_ws_custom_http_proxy?branch=master)                            | used to specify the custom proxy for the channel, using the **WS\_CHANNEL\_PROPERTY\_CUSTOM\_HTTP**\_PROXY value of the [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_channel_property_id?branch=master) enumeration. |
| [**WS\_HTTP\_HEADER\_MAPPING**](/windows/win32/WebServices/ns-webservices-_ws_http_header_mapping?branch=master)                        | Represents an individual header that is mapped as part of [**WS\_HTTP\_MESSAGE\_MAPPING**](/windows/win32/WebServices/ns-webservices-_ws_http_message_mapping?branch=master).                                                                         |
| [**WS\_HTTP\_MESSAGE\_MAPPING**](/windows/win32/WebServices/ns-webservices-_ws_http_message_mapping?branch=master)                      | Information about how an HTTP request or response should be represented in a message object.                                                                                                     |
| [**WS\_HTTP\_REDIRECT\_CALLBACK\_CONTEXT**](/windows/win32/WebServices/ns-webservices-_ws_http_redirect_callback_context?branch=master) | Specifies the callback function and state for controlling the HTTP automatic redirection behavior.                                                                                               |
| [**WS\_MESSAGE\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_message_description?branch=master)                         | The schema for the input and output [WS\_MESSAGE](ws-message.md) for a given operation description.                                                                                             |



 

 

 




