---
title: Writing a Client DVC Module
description: To write a dynamic virtual channel (DVC) client module, you must first implement and register a Remote Desktop Connection (RDC) client plug-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b6f475d4-d2ad-41ce-b3b9-d844fbd23cf0
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Writing a Client DVC Module

To write a dynamic virtual channel (DVC) client module, you must first implement and register a Remote Desktop Connection (RDC) client plug-in. The DVC plug-in is an implementation of [**IWTSPlugin**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin?branch=master), registered as a Component Object Model (COM) object.

> [!Note]  
> The plug-in must be implemented in a free-threading model. Apartment-model implementation is not supported.

 

The following is a list of interfaces that are implemented by objects that are instantiated by the plug-in.



| Interface                                                        | Description                                                                                                                                                                                          |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWTSPlugin**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin?branch=master)                                 | Allows for the Remote Desktop Connection (RDC) client plug-in to be loaded by the Remote Desktop Connection (RDC) client.<br/>                                                                 |
| [**IWTSListenerCallback**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtslistenercallback?branch=master)             | Notifies the Remote Desktop Connection (RDC) client plug-in about incoming requests on a particular listener.<br/>                                                                             |
| [**IWTSVirtualChannelCallback**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannelcallback?branch=master) | Receives notifications about channel state changes or data received. Each instance of this interface is associated with one instance of [**IWTSVirtualChannel**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannel?branch=master).<br/> |



 

The following is a list of interfaces that are implemented by objects that are instantiated by the Remote Desktop Connection (RDC) client, and are part of the framework.



| Interface                                                      | Description                                                                                                        |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**IWTSVirtualChannelManager**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannelmanager?branch=master) | Manages all Remote Desktop Connection (RDC) client plug-ins, DVC listeners, or static virtual channels.<br/> |
| [**IWTSListener**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtslistener?branch=master)                           | Manages configuration settings for each listener for the DVC connection.<br/>                                |
| [**IWTSVirtualChannel**](/windows/win32/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannel?branch=master)               | Controls the channel state, as well as writes on the channel.<br/>                                           |



 

The following illustration shows the relationship between the Remote Desktop Connection (RDC) client and the Remote Desktop Connection (RDC) client plug-in.

![relationship of client and plug-in](images/tsclient.png)

 

 





