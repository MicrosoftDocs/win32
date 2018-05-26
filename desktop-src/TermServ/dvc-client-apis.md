---
title: DVC Client APIs
description: The dynamic virtual channel (DVC) client APIs are implemented specifically for the Remote Desktop Connection (RDC) client of the connection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 976a6cc2-7bbe-4ecc-91b4-b7c659eca5ba
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DVC Client APIs

The dynamic virtual channel (DVC) client APIs are implemented specifically for the Remote Desktop Connection (RDC) client of the connection. Some of the APIs are implemented by the DVC framework, and some are implemented by the plug-in developer. Some of the APIs are used to support the Remote Desktop Connection (RDC) client plug-in, and are not directly related to data transport.

## In this section

<dl> <dt>

[**IWTSPlugin**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin?branch=master)
</dt> <dd>

Allows for the Remote Desktop Connection (RDC) client plug-in to be loaded by the Remote Desktop Connection (RDC) client.

</dd> <dt>

[**IWTSListener**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtslistener?branch=master)
</dt> <dd>

Manages configuration settings for each listener for the dynamic virtual channel (DVC) connection.

</dd> <dt>

[**IWTSListenerCallback**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtslistenercallback?branch=master)
</dt> <dd>

Used to notify the Remote Desktop Connection (RDC) client plug-in about incoming requests on a particular listener.

</dd> <dt>

[**IWTSVirtualChannelManager**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannelmanager?branch=master)
</dt> <dd>

Manages all Remote Desktop Connection (RDC) client plug-ins and dynamic virtual channel (DVC) listeners.

</dd> <dt>

[**IWTSVirtualChannel**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannel?branch=master)
</dt> <dd>

Used to control the channel state, and writes on the channel.

</dd> <dt>

[**IWTSVirtualChannelCallback**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannelcallback?branch=master)
</dt> <dd>

Receives notifications about channel state changes or data received.

</dd> <dt>

[**IWTSVirtualChannelCallback2**](iwtsvirtualchannelcallback2.md)
</dt> <dd>

This interface is not supported.

</dd> <dt>

[**VirtualChannelGetInstance**](virtualchannelgetinstance.md)
</dt> <dd>

Called to have the plug-in create an instance of the [**IWTSPlugin**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin?branch=master) interface for all plug-ins implemented by the DLL.

</dd> </dl>

 

 




