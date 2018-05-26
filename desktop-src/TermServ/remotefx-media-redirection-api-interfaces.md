---
title: RemoteFX Media Redirection API interfaces
description: The RemoteFX media redirection API supports the following interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9fb19c56-67a8-40f1-b6f1-8448eb83b38c
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteFX Media Redirection API interfaces

The RemoteFX media redirection API supports the following interfaces.

## In this section

<dl> <dt>

[**IWTSBitmapRenderer**](/windows/win32/tsvirtualchannels/nn-tsvirtualchannels-iwtsbitmaprenderer?branch=master)
</dt> <dd>

Used by a dynamic virtual channel plug-in to render bitmaps.

</dd> <dt>

[**IWTSBitmapRendererCallback**](/windows/win32/tsvirtualchannels/nn-tsvirtualchannels-iwtsbitmaprenderercallback?branch=master)
</dt> <dd>

A dynamic virtual channel plug-in implements this interface to be notified when the size of the rendering area changes.

</dd> <dt>

[**IWTSBitmapRenderService**](/windows/win32/tsvirtualchannels/nn-tsvirtualchannels-iwtsbitmaprenderservice?branch=master)
</dt> <dd>

This service is used to create a visual mapping on the client corresponding to a mapped window on the server.

</dd> <dt>

[**IWTSPluginServiceProvider**](/windows/win32/tsvirtualchannels/nn-tsvirtualchannels-iwtspluginserviceprovider?branch=master)
</dt> <dd>

Provides a way for Dynamic Virtual Channel plug-ins to query various Remote Desktop Client services.

</dd> </dl>

 

 




