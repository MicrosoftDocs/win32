---
title: Listener
description: A listener is used by the client to accept an incoming channel from a service.
ms.assetid: 'fffda587-23f5-4c7a-93c5-f03d9d3fafb2'
keywords: ["Listener Web Services for Windows", "WWSAPI", "WWS"]
---

# Listener

A listener is used by the client to accept an incoming [channel](channel.md) from a service.

To create a listner, you specify the channel type as a [**WS\_CHANNEL\_TYPE**](ws-channel-type.md) enumeration value, the [binding](binding.md) information, and the [URL](url.md) to listen on.

## 

To start listening on the URL, call the [**WsOpenListener**](wsopenlistener.md) function.

To accept incoming communications, call [**WsAcceptChannel**](wsacceptchannel.md).

To cancel pending IO for a listener, call [**WsAbortListener**](wsabortlistener.md).

For information on the state transitions for a listener, see the [**WS\_LISTENER\_STATE**](ws-listener-state.md) enumeration.

The following callbacks are part of the listener:

-   [**WS\_ABORT\_LISTENER\_CALLBACK**](ws-abort-listener-callback.md)
-   [**WS\_ACCEPT\_CHANNEL\_CALLBACK**](ws-accept-channel-callback.md)
-   [**WS\_CLOSE\_LISTENER\_CALLBACK**](ws-close-listener-callback.md)
-   [**WS\_CREATE\_CHANNEL\_FOR\_LISTENER\_CALLBACK**](ws-create-channel-for-listener-callback.md)
-   [**WS\_CREATE\_LISTENER\_CALLBACK**](ws-create-listener-callback.md)
-   [**WS\_FREE\_LISTENER\_CALLBACK**](ws-free-listener-callback.md)
-   [**WS\_GET\_LISTENER\_PROPERTY\_CALLBACK**](ws-get-listener-property-callback.md)
-   [**WS\_OPEN\_LISTENER\_CALLBACK**](ws-open-listener-callback.md)
-   [**WS\_RESET\_LISTENER\_CALLBACK**](ws-reset-listener-callback.md)
-   [**WS\_SET\_LISTENER\_PROPERTY\_CALLBACK**](ws-set-listener-property-callback.md)

The following enumerations are part of the listener:

-   [**WS\_IP\_VERSION**](ws-ip-version.md)
-   [**WS\_LISTENER\_PROPERTY\_ID**](ws-listener-property-id.md)
-   [**WS\_LISTENER\_STATE**](ws-listener-state.md)

The following functions are part of the listener:

-   [**WsAbortListener**](wsabortlistener.md)
-   [**WsAcceptChannel**](wsacceptchannel.md)
-   [**WsCloseListener**](wscloselistener.md)
-   [**WsCreateListener**](wscreatelistener.md)
-   [**WsFreeListener**](wsfreelistener.md)
-   [**WsGetListenerProperty**](wsgetlistenerproperty.md)
-   [**WsOpenListener**](wsopenlistener.md)
-   [**WsResetListener**](wsresetlistener.md)
-   [**WsSetListenerProperty**](wssetlistenerproperty.md)

The following handle is part of the listener:

-   [WS\_LISTENER](ws-listener.md)

The following structures are part of the listener:

-   [**WS\_CUSTOM\_LISTENER\_CALLBACKS**](ws-custom-listener-callbacks.md)
-   [**WS\_DISALLOWED\_USER\_AGENT\_SUBSTRINGS**](ws-disallowed-user-agent-substrings.md)
-   [**WS\_HOST\_NAMES**](ws-host-names.md)
-   [**WS\_LISTENER\_PROPERTIES**](ws-listener-properties.md)
-   [**WS\_LISTENER\_PROPERTY**](ws-listener-property.md)

 

 




