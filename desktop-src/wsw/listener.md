---
title: Listener
description: A listener is used by the client to accept an incoming channel from a service.
ms.assetid: fffda587-23f5-4c7a-93c5-f03d9d3fafb2
keywords:
- Listener Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Listener

A listener is used by the client to accept an incoming [channel](channel.md) from a service.

To create a listner, you specify the channel type as a [**WS\_CHANNEL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_type) enumeration value, the [binding](binding.md) information, and the [URL](url.md) to listen on.


To start listening on the URL, call the [**WsOpenListener**](/windows/desktop/api/WebServices/nf-webservices-wsopenlistener) function.

To accept incoming communications, call [**WsAcceptChannel**](/windows/desktop/api/WebServices/nf-webservices-wsacceptchannel).

To cancel pending IO for a listener, call [**WsAbortListener**](/windows/desktop/api/WebServices/nf-webservices-wsabortlistener).

For information on the state transitions for a listener, see the [**WS\_LISTENER\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_listener_state) enumeration.

The following callbacks are part of the listener:

-   [**WS\_ABORT\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_abort_listener_callback)
-   [**WS\_ACCEPT\_CHANNEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_accept_channel_callback)
-   [**WS\_CLOSE\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_close_listener_callback)
-   [**WS\_CREATE\_CHANNEL\_FOR\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_create_channel_for_listener_callback)
-   [**WS\_CREATE\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_create_listener_callback)
-   [**WS\_FREE\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_free_listener_callback)
-   [**WS\_GET\_LISTENER\_PROPERTY\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_get_listener_property_callback)
-   [**WS\_OPEN\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_open_listener_callback)
-   [**WS\_RESET\_LISTENER\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_reset_listener_callback)
-   [**WS\_SET\_LISTENER\_PROPERTY\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_set_listener_property_callback)

The following enumerations are part of the listener:

-   [**WS\_IP\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_ip_version)
-   [**WS\_LISTENER\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_listener_property_id)
-   [**WS\_LISTENER\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_listener_state)

The following functions are part of the listener:

-   [**WsAbortListener**](/windows/desktop/api/WebServices/nf-webservices-wsabortlistener)
-   [**WsAcceptChannel**](/windows/desktop/api/WebServices/nf-webservices-wsacceptchannel)
-   [**WsCloseListener**](/windows/desktop/api/WebServices/nf-webservices-wscloselistener)
-   [**WsCreateListener**](/windows/desktop/api/WebServices/nf-webservices-wscreatelistener)
-   [**WsFreeListener**](/windows/desktop/api/WebServices/nf-webservices-wsfreelistener)
-   [**WsGetListenerProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetlistenerproperty)
-   [**WsOpenListener**](/windows/desktop/api/WebServices/nf-webservices-wsopenlistener)
-   [**WsResetListener**](/windows/desktop/api/WebServices/nf-webservices-wsresetlistener)
-   [**WsSetListenerProperty**](/windows/desktop/api/WebServices/nf-webservices-wssetlistenerproperty)

The following handle is part of the listener:

-   [WS\_LISTENER](ws-listener.md)

The following structures are part of the listener:

-   [**WS\_CUSTOM\_LISTENER\_CALLBACKS**](/windows/desktop/api/WebServices/ns-webservices-ws_custom_listener_callbacks)
-   [**WS\_DISALLOWED\_USER\_AGENT\_SUBSTRINGS**](/windows/desktop/api/WebServices/ns-webservices-ws_disallowed_user_agent_substrings)
-   [**WS\_HOST\_NAMES**](/windows/desktop/api/WebServices/ns-webservices-ws_host_names)
-   [**WS\_LISTENER\_PROPERTIES**](/windows/desktop/api/WebServices/ns-webservices-ws_listener_properties)
-   [**WS\_LISTENER\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_listener_property)

 

 




