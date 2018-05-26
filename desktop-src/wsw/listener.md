---
title: Listener
description: A listener is used by the client to accept an incoming channel from a service.
ms.assetid: fffda587-23f5-4c7a-93c5-f03d9d3fafb2
keywords:
- Listener Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Listener

A listener is used by the client to accept an incoming [channel](channel.md) from a service.

To create a listner, you specify the channel type as a [**WS\_CHANNEL\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_channel_type?branch=master) enumeration value, the [binding](binding.md) information, and the [URL](url.md) to listen on.

## 

To start listening on the URL, call the [**WsOpenListener**](/windows/win32/WebServices/nf-webservices-wsopenlistener?branch=master) function.

To accept incoming communications, call [**WsAcceptChannel**](/windows/win32/WebServices/nf-webservices-wsacceptchannel?branch=master).

To cancel pending IO for a listener, call [**WsAbortListener**](/windows/win32/WebServices/nf-webservices-wsabortlistener?branch=master).

For information on the state transitions for a listener, see the [**WS\_LISTENER\_STATE**](/windows/win32/WebServices/ne-webservices-ws_listener_state?branch=master) enumeration.

The following callbacks are part of the listener:

-   [**WS\_ABORT\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_abort_listener_callback?branch=master)
-   [**WS\_ACCEPT\_CHANNEL\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_accept_channel_callback?branch=master)
-   [**WS\_CLOSE\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_close_listener_callback?branch=master)
-   [**WS\_CREATE\_CHANNEL\_FOR\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_channel_for_listener_callback?branch=master)
-   [**WS\_CREATE\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_create_listener_callback?branch=master)
-   [**WS\_FREE\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_free_listener_callback?branch=master)
-   [**WS\_GET\_LISTENER\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_get_listener_property_callback?branch=master)
-   [**WS\_OPEN\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_open_listener_callback?branch=master)
-   [**WS\_RESET\_LISTENER\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_reset_listener_callback?branch=master)
-   [**WS\_SET\_LISTENER\_PROPERTY\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_set_listener_property_callback?branch=master)

The following enumerations are part of the listener:

-   [**WS\_IP\_VERSION**](/windows/win32/WebServices/ne-webservices-ws_ip_version?branch=master)
-   [**WS\_LISTENER\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_listener_property_id?branch=master)
-   [**WS\_LISTENER\_STATE**](/windows/win32/WebServices/ne-webservices-ws_listener_state?branch=master)

The following functions are part of the listener:

-   [**WsAbortListener**](/windows/win32/WebServices/nf-webservices-wsabortlistener?branch=master)
-   [**WsAcceptChannel**](/windows/win32/WebServices/nf-webservices-wsacceptchannel?branch=master)
-   [**WsCloseListener**](/windows/win32/WebServices/nf-webservices-wscloselistener?branch=master)
-   [**WsCreateListener**](/windows/win32/WebServices/nf-webservices-wscreatelistener?branch=master)
-   [**WsFreeListener**](/windows/win32/WebServices/nf-webservices-wsfreelistener?branch=master)
-   [**WsGetListenerProperty**](/windows/win32/WebServices/nf-webservices-wsgetlistenerproperty?branch=master)
-   [**WsOpenListener**](/windows/win32/WebServices/nf-webservices-wsopenlistener?branch=master)
-   [**WsResetListener**](/windows/win32/WebServices/nf-webservices-wsresetlistener?branch=master)
-   [**WsSetListenerProperty**](/windows/win32/WebServices/nf-webservices-wssetlistenerproperty?branch=master)

The following handle is part of the listener:

-   [WS\_LISTENER](ws-listener.md)

The following structures are part of the listener:

-   [**WS\_CUSTOM\_LISTENER\_CALLBACKS**](/windows/win32/WebServices/ns-webservices-_ws_custom_listener_callbacks?branch=master)
-   [**WS\_DISALLOWED\_USER\_AGENT\_SUBSTRINGS**](/windows/win32/WebServices/ns-webservices-_ws_disallowed_user_agent_substrings?branch=master)
-   [**WS\_HOST\_NAMES**](/windows/win32/WebServices/ns-webservices-_ws_host_names?branch=master)
-   [**WS\_LISTENER\_PROPERTIES**](/windows/win32/WebServices/ns-webservices-_ws_listener_properties?branch=master)
-   [**WS\_LISTENER\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_listener_property?branch=master)

 

 




