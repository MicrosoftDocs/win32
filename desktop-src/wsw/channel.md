---
title: Channel (Windows Web Services)
description: Channels encapsulate a communication context between two or more parties and are used to send and receive messages.
ms.assetid: 5a04580d-c89f-4505-a4b7-0724ffb788fd
keywords:
- Channel Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Channel (Windows Web Services)

Channels encapsulate a communication context between two or more parties and are used to send and receive messages.


On the client, use [**WsCreateChannel**](/windows/desktop/api/WebServices/nf-webservices-wscreatechannel) to create a channel. On the server, use [**WsCreateChannelForListener**](/windows/desktop/api/WebServices/nf-webservices-wscreatechannelforlistener) to create a channel that can be accepted by the client using a [listener](listener.md).

When you create a channel, you specify the following information, which determines both the local behavior of the channel and the wire protocol to be used.

-   A [**WS\_CHANNEL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_type), which identifies the message exchange pattern of the channel.
-   A [**WS\_CHANNEL\_BINDING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_binding), which identifies the transfer protocol to use.
-   A [**WS\_SECURITY\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_security_description), which specifies the security used for the channel. When creating channels for use in a server, this is specified once for all channels that will be accepted for a given listener.
-   A set [**WS\_CHANNEL\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_property)s, which specify additional optional settings (for a list of these settings, see the [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id) enumerations).

Before you use the channel, you must open it by calling the [**WsOpenChannel**](/windows/desktop/api/WebServices/nf-webservices-wsopenchannel) function, and specifying the channel and [endpoint address](endpoint-address.md), along with other, optional information.

For information on the state transitions for a channel, see the [**Channel States**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_state) topic.

For more information on channels, see the [Channel Layer Overview](channel-layer-overview.md) topic.

The following API elements are used with channels.

| Callback                                                                                  | Description                                                                                                                                           |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ABANDON\_MESSAGE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_abandon_message_callback)                     | Handles the [**WsAbandonMessage**](/windows/desktop/api/WebServices/nf-webservices-wsabandonmessage) call for a channel with custom channel binding.                                              |
| [**WS\_ABORT\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_abort_channel_callback)                         | Handles the [**WsAbortChannel**](/windows/desktop/api/WebServices/nf-webservices-wsabortchannel) call for a channel with custom channel binding.                                                  |
| [**WS\_CLOSE\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_close_channel_callback)                         | Handles the [**WsCloseChannel**](/windows/desktop/api/WebServices/nf-webservices-wsclosechannel) call for a channel with custom channel binding.                                                  |
| [**WS\_CREATE\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_create_channel_callback)                       | Handles the [**WsCloseChannel**](/windows/desktop/api/WebServices/nf-webservices-wsclosechannel) call for a channel with custom channel binding.                                                  |
| [**WS\_CREATE\_DECODER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_create_decoder_callback)                       | Handles creating a decoder instance.                                                                                                                  |
| [**WS\_CREATE\_ENCODER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_create_encoder_callback)                       | Handles creating an encoder instance.                                                                                                                 |
| [**WS\_DECODER\_DECODE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_decoder_decode_callback)                       | Decodes a message.                                                                                                                                    |
| [**WS\_DECODER\_END\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_decoder_end_callback)                             | Decodes the end of a message.                                                                                                                         |
| [**WS\_DECODER\_GET\_CONTENT\_TYPE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_decoder_get_content_type_callback) | Gets the content type of the message.                                                                                                                 |
| [**WS\_DECODER\_START\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_decoder_start_callback)                         | Starts decoding a message.                                                                                                                            |
| [**WS\_ENCODER\_ENCODE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_encoder_encode_callback)                       | Encodes a message.                                                                                                                                    |
| [**WS\_ENCODER\_END\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_encoder_end_callback)                             | Encodes the end of a message.                                                                                                                         |
| [**WS\_ENCODER\_GET\_CONTENT\_TYPE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_encoder_get_content_type_callback) | Gets the content type of the message.                                                                                                                 |
| [**WS\_ENCODER\_START\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_encoder_start_callback)                         | Starts encoding a message.                                                                                                                            |
| [**WS\_FREE\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_free_channel_callback)                           | Handles the [**WsFreeChannel**](/windows/desktop/api/WebServices/nf-webservices-wsfreechannel) call for a channel with custom channel binding.                                                    |
| [**WS\_FREE\_DECODER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_free_decoder_callback)                           | Handles freeing a decoder instance.                                                                                                                   |
| [**WS\_FREE\_ENCODER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_free_encoder_callback)                           | Handles freeing an encoder instance.                                                                                                                  |
| [**WS\_GET\_CHANNEL\_PROPERTY\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_get_channel_property_callback)          | Handles the [**WsGetChannelProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetchannelproperty) call for a channel with custom channel binding.                                      |
| [**WS\_HTTP\_REDIRECT\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_http_redirect_callback)                         | Invoked when a message is about to be automatically redirected to another service utilizing HTTP auto redirect functionality as described in RFC2616. |
| [**WS\_OPEN\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_open_channel_callback)                           | Handles the [**WsOpenChannel**](/windows/desktop/api/WebServices/nf-webservices-wsopenchannel) call for a channel with custom channel binding.                                                    |
| [**WS\_READ\_MESSAGE\_END\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_read_message_end_callback)                  | Handles the [**WsReadMessageEnd**](/windows/desktop/api/WebServices/nf-webservices-wsreadmessageend) call for a channel with custom channel binding.                                              |
| [**WS\_READ\_MESSAGE\_START\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_read_message_start_callback)              | Handles the [**WsReadMessageEnd**](/windows/desktop/api/WebServices/nf-webservices-wsreadmessageend) call for a channel with custom channel binding.                                              |
| [**WS\_RESET\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_reset_channel_callback)                         | Handles the [**WsResetChannel**](/windows/desktop/api/WebServices/nf-webservices-wsresetchannel) call for a channel with custom channel binding.                                                  |
| [**WS\_SET\_CHANNEL\_PROPERTY\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_set_channel_property_callback)          | Handles the [**WsSetChannelProperty**](/windows/desktop/api/WebServices/nf-webservices-wssetchannelproperty) call for a channel with custom channel binding.                                      |
| [**WS\_SHUTDOWN\_SESSION\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_shutdown_session_channel_callback)  | Handles the [**WsShutdownSessionChannel**](/windows/desktop/api/WebServices/nf-webservices-wsshutdownsessionchannel) call for a channel with custom channel binding.                              |
| [**WS\_WRITE\_MESSAGE\_END\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_write_message_end_callback)                | Handles the [**WsWriteMessageEnd**](/windows/desktop/api/WebServices/nf-webservices-wswritemessageend) call for a channel with custom channel binding.                                            |
| [**WS\_WRITE\_MESSAGE\_START\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_write_message_start_callback)            | Handles the [**WsWriteMessageStart**](/windows/desktop/api/WebServices/nf-webservices-wswritemessagestart) call for a channel with custom channel binding.                                        |



 



| Enumeration                                                 | Description                                                                                                                               |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CHANNEL\_BINDING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_binding)          | Indicates the protocol stack to use for the channel.                                                                                      |
| [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id) | Identifies each channel property by an ID.                                                                                                |
| [**WS\_CHANNEL\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_state)              | The state of the channel.                                                                                                                 |
| [**WS\_CHANNEL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_type)                | Indicates the basic characteristics of the channel, such as whether it is sessionful, and what directions of communication are supported. |
| [**WS\_ENCODING**](/windows/desktop/api/WebServices/ne-webservices-ws_encoding)                         | The different encodings (message formats).                                                                                                |
| [**WS\_RECEIVE\_OPTION**](/windows/desktop/api/WebServices/ne-webservices-ws_receive_option)            | Specifies whether a message is required when receiving from a channel.                                                                    |
| [**WS\_TRANSFER\_MODE**](/windows/desktop/api/WebServices/ne-webservices-ws_transfer_mode)              | Specifies whether messages that are sent or received are streamed or buffered.                                                            |



 



| Function                                                         | Description                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**WsAbandonMessage**](/windows/desktop/api/WebServices/nf-webservices-wsabandonmessage)                     | Skips the remainder of a message for a channel.                                                              |
| [**WsAbortChannel**](/windows/desktop/api/WebServices/nf-webservices-wsabortchannel)                         | Aborts all pending I/O on a specified channel and sets the channel state to **WS\_CHANNEL\_STATE\_FAULTED**. |
| [**WsCloseChannel**](/windows/desktop/api/WebServices/nf-webservices-wsclosechannel)                         | Closes a channel when it is no longer needed.                                                                |
| [**WsCreateChannel**](/windows/desktop/api/WebServices/nf-webservices-wscreatechannel)                       | Creates a channel.                                                                                           |
| [**WsCreateChannelForListener**](/windows/desktop/api/WebServices/nf-webservices-wscreatechannelforlistener) | Creates a channel for a listener.                                                                            |
| [**WsFreeChannel**](/windows/desktop/api/WebServices/nf-webservices-wsfreechannel)                           | Releases the memory resources associated with a channel.                                                     |
| [**WsGetChannelProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetchannelproperty)             | Retrieves a property of the Channel referenced by the channel parameter.                                     |
| [**WsOpenChannel**](/windows/desktop/api/WebServices/nf-webservices-wsopenchannel)                           | Opens a channel to an endpoint.                                                                              |
| [**WsReadMessageEnd**](/windows/desktop/api/WebServices/nf-webservices-wsreadmessageend)                     | Reads the closing elements of a message from a channel.                                                      |
| [**WsReadMessageStart**](/windows/desktop/api/WebServices/nf-webservices-wsreadmessagestart)                 | Reads the headers of the next message from the channel and prepares to read the body elements.               |
| [**WsReceiveMessage**](/windows/desktop/api/WebServices/nf-webservices-wsreceivemessage)                     | Receives a message and deserializes the body of the message as a value.                                      |
| [**WsRequestReply**](/windows/desktop/api/WebServices/nf-webservices-wsrequestreply)                         | Sends a request message and receives a correlated reply message.                                             |
| [**WsResetChannel**](/windows/desktop/api/WebServices/nf-webservices-wsresetchannel)                         | Reset a channel so it can be reused.                                                                         |
| [**WsSendMessage**](/windows/desktop/api/WebServices/nf-webservices-wssendmessage)                           | Sends a message on a channel using serialization to write the body element.                                  |
| [**WsSendReplyMessage**](/windows/desktop/api/WebServices/nf-webservices-wssendreplymessage)                 | Sends a message that is a reply to a received message.                                                       |
| [**WsSetChannelProperty**](/windows/desktop/api/WebServices/nf-webservices-wssetchannelproperty)             | Sets a property of a channel.                                                                                |
| [**WsSetMessageProperty**](/windows/desktop/api/WebServices/nf-webservices-wssetmessageproperty)             | Sets a property of a message.                                                                                |
| [**WsWriteMessageEnd**](/windows/desktop/api/WebServices/nf-webservices-wswritemessageend)                   | Writes the closing elements of a message to the channel.                                                     |
| [**WsWriteMessageStart**](/windows/desktop/api/WebServices/nf-webservices-wswritemessagestart)               | Write out the headers of a message to the channel and prepares to write the body elements.                   |



 



| Handle                        | Description                                 |
|-------------------------------|---------------------------------------------|
| [WS\_CHANNEL](ws-channel.md) | An opaque type used to reference a channel. |



 



| Structure                                                                          | Description                                                                                                                                                                                      |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_CHANNEL\_DECODER**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_decoder)                                 | A set of callbacks that transform the content type and encoded bytes of a received message.                                                                                                      |
| [**WS\_CHANNEL\_ENCODER**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_encoder)                                 | A set of callbacks that can transform the content type and encoded bytes of a sent message.                                                                                                      |
| [**WS\_CHANNEL\_PROPERTIES**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_properties)                           | A set of [**WS\_CHANNEL\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_property) structures.                                                                                                                        |
| [**WS\_CHANNEL\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_property)                               | A channel-specific setting.                                                                                                                                                                      |
| [**WS\_CUSTOM\_CHANNEL\_CALLBACKS**](/windows/desktop/api/WebServices/ns-webservices-ws_custom_channel_callbacks)              | A set of callbacks that form the implementation of a custom channel.                                                                                                                             |
| [**WS\_CUSTOM\_HTTP\_PROXY**](/windows/desktop/api/WebServices/ns-webservices-ws_custom_http_proxy)                            | used to specify the custom proxy for the channel, using the **WS\_CHANNEL\_PROPERTY\_CUSTOM\_HTTP**\_PROXY value of the [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id) enumeration. |
| [**WS\_HTTP\_HEADER\_MAPPING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_mapping)                        | Represents an individual header that is mapped as part of [**WS\_HTTP\_MESSAGE\_MAPPING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_message_mapping).                                                                         |
| [**WS\_HTTP\_MESSAGE\_MAPPING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_message_mapping)                      | Information about how an HTTP request or response should be represented in a message object.                                                                                                     |
| [**WS\_HTTP\_REDIRECT\_CALLBACK\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_http_redirect_callback_context) | Specifies the callback function and state for controlling the HTTP automatic redirection behavior.                                                                                               |
| [**WS\_MESSAGE\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_message_description)                         | The schema for the input and output [WS\_MESSAGE](ws-message.md) for a given operation description.                                                                                             |



 

 

 




