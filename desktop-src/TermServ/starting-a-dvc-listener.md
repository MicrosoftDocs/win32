---
title: Starting a DVC Listener
description: To establish a successful connection between two dynamic virtual channel (DVC) modules that are running on the Remote Desktop Connection (RDC) client and server, a DVC listener must be running and in a listening state.
ms.assetid: c9130375-eb60-4996-84f5-a1081144e130
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Starting a DVC Listener

To establish a successful connection between two dynamic virtual channel (DVC) modules that are running on the Remote Desktop Connection (RDC) client and server, a DVC listener must be running and in a listening state.

The instantiation of a listener typically occurs in the [**Initialize**](/windows/desktop/api/TsVirtualChannels/nf-tsvirtualchannels-iwtsplugin-initialize) method of the DVC plug-in. However, instantiation is not limited to the **Initialize** method, and can be started at any point of the plug-in execution. The listener is described by the [**IWTSListener**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtslistener) interface which is instantiated by the [**IWTSVirtualChannelManager**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannelmanager). An instance to the channel manager is passed to the plug-in at the initialization point. The plug-in can maintain an internal reference to the instance as long as it needs to.

A plug-in can instantiate as many listeners as it needs to. Any incoming connection will be handled by [**IWTSListenerCallback**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtslistenercallback), which is supplied in the [**CreateListener**](/windows/desktop/api/TsVirtualChannels/nf-tsvirtualchannels-iwtsvirtualchannelmanager-createlistener) method of [**IWTSVirtualChannelManager**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtsvirtualchannelmanager). For an example, see the implementation of **CDVCSamplePlugin::Initialize** in the [DVC Client Plug-in Example](dvc-client-plug-in-example.md) sample code.

 

 




