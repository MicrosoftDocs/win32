---
title: Channel Binding
description: Bindings specify the wire protocol and local behavior for a channel.
ms.assetid: 82d465c5-b23d-4403-b360-8c710fbc6e1c
keywords:
- Binding Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Channel Binding

Bindings specify the wire protocol and local behavior for a channel. Bindings are made up of the following components:

-   A [**WS\_CHANNEL\_BINDING**](/windows/win32/WebServices/ne-webservices-ws_channel_binding?branch=master), which identifies the transfer protocol to use.
-   A [**WS\_SECURITY\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_security_description?branch=master), which specifies how to secure the channel.
-   A set [**WS\_CHANNEL\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_channel_property?branch=master)s, which specify additional optional settings (see also [**WS\_CHANNEL\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_channel_property_id?branch=master)).

 

 




