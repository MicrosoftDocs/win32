---
title: Channel Binding
description: Bindings specify the wire protocol and local behavior for a channel.
ms.assetid: 82d465c5-b23d-4403-b360-8c710fbc6e1c
keywords:
- Binding Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Channel Binding

Bindings specify the wire protocol and local behavior for a channel. Bindings are made up of the following components:

-   A [**WS\_CHANNEL\_BINDING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_binding), which identifies the transfer protocol to use.
-   A [**WS\_SECURITY\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_security_description), which specifies how to secure the channel.
-   A set [**WS\_CHANNEL\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_property)s, which specify additional optional settings (see also [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id)).

 

 




