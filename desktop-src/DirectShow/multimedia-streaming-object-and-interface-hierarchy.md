---
Description: Multimedia Streaming Object and Interface Hierarchy
ms.assetid: dbb6dc3b-b55e-4f6c-918f-068308e2dba9
title: Multimedia Streaming Object and Interface Hierarchy
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multimedia Streaming Object and Interface Hierarchy

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

The following diagram shows the object hierarchy used in multimedia streaming.

![multimediastreaming object hierarchy](images/mmstream02.png)

The multimedia streaming architecture defines three general type of object:

-   The **AMMultimediaStream** object exposes the [**IAMMultiMediaStream**](/windows/win32/amstream/nn-amstream-iammultimediastream?branch=master) interface. Internally, this object wraps the DirectShow filter graph.
-   *Media stream* objects expose the [**IMediaStream**](/windows/win32/mmstream/nn-mmstream-imediastream?branch=master) interface and are data specific. The AMMultimediaStream object contains one or more media streams.
-   *Stream sample* objects contain the data for a particular stream.

The following media stream objects are supported:

-   Audio stream. Exposes the [**IAudioMediaStream**](/windows/win32/austream/nn-austream-iaudiomediastream?branch=master) interface.
-   DirectDraw stream. Represents a video stream that is rendered to a DirectDraw surface. Exposes the [**IDirectDrawMediaStream**](/windows/win32/ddstream/nn-ddstream-idirectdrawmediastream?branch=master) interface.
-   Media type stream. Represents arbitrary data. Exposes the [**IAMMediaTypeStream**](/windows/win32/amstream/nn-amstream-iammediatypestream?branch=master) interface.

Each media stream object creates its own kind of stream sample object:

-   Audio streams create audio samples, which expose the [**IAudioStreamSample**](/windows/win32/austream/nn-austream-iaudiostreamsample?branch=master) interface.
-   DirectDraw streams create DirectDraw samples, which expose the [**IDirectDrawStreamSample**](/windows/win32/ddstream/nn-ddstream-idirectdrawstreamsample?branch=master) interface.
-   Media type streams create media type samples, which expose the [**IAMMediaTypeSample**](/windows/win32/amstream/nn-amstream-iammediatypesample?branch=master) interface.

The following diagram shows the interface hierarchy for the interfaces listed previously:

![multimediastreaming interface hierarchy](images/mmstream01.png)

 

 



