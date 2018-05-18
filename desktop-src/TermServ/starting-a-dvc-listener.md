---
title: Starting a DVC Listener
description: To establish a successful connection between two dynamic virtual channel (DVC) modules that are running on the Remote Desktop Connection (RDC) client and server, a DVC listener must be running and in a listening state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c9130375-eb60-4996-84f5-a1081144e130'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Starting a DVC Listener

To establish a successful connection between two dynamic virtual channel (DVC) modules that are running on the Remote Desktop Connection (RDC) client and server, a DVC listener must be running and in a listening state.

The instantiation of a listener typically occurs in the [**Initialize**](iwtsplugin-initialize.md) method of the DVC plug-in. However, instantiation is not limited to the **Initialize** method, and can be started at any point of the plug-in execution. The listener is described by the [**IWTSListener**](iwtslistener.md) interface which is instantiated by the [**IWTSVirtualChannelManager**](iwtsvirtualchannelmanager.md). An instance to the channel manager is passed to the plug-in at the initialization point. The plug-in can maintain an internal reference to the instance as long as it needs to.

A plug-in can instantiate as many listeners as it needs to. Any incoming connection will be handled by [**IWTSListenerCallback**](iwtslistenercallback.md), which is supplied in the [**CreateListener**](iwtsvirtualchannelmanager-createlistener.md) method of [**IWTSVirtualChannelManager**](iwtsvirtualchannelmanager.md). For an example, see the implementation of **CDVCSamplePlugin::Initialize** in the [DVC Client Plug-in Example](dvc-client-plug-in-example.md) sample code.

 

 




