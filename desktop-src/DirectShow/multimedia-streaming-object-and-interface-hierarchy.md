---
Description: Multimedia Streaming Object and Interface Hierarchy
ms.assetid: 'dbb6dc3b-b55e-4f6c-918f-068308e2dba9'
title: Multimedia Streaming Object and Interface Hierarchy
---

# Multimedia Streaming Object and Interface Hierarchy

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

The following diagram shows the object hierarchy used in multimedia streaming.

![multimediastreaming object hierarchy](images/mmstream02.png)

The multimedia streaming architecture defines three general type of object:

-   The **AMMultimediaStream** object exposes the [**IAMMultiMediaStream**](iammultimediastream.md) interface. Internally, this object wraps the DirectShow filter graph.
-   *Media stream* objects expose the [**IMediaStream**](imediastream.md) interface and are data specific. The AMMultimediaStream object contains one or more media streams.
-   *Stream sample* objects contain the data for a particular stream.

The following media stream objects are supported:

-   Audio stream. Exposes the [**IAudioMediaStream**](iaudiomediastream.md) interface.
-   DirectDraw stream. Represents a video stream that is rendered to a DirectDraw surface. Exposes the [**IDirectDrawMediaStream**](idirectdrawmediastream.md) interface.
-   Media type stream. Represents arbitrary data. Exposes the [**IAMMediaTypeStream**](iammediatypestream.md) interface.

Each media stream object creates its own kind of stream sample object:

-   Audio streams create audio samples, which expose the [**IAudioStreamSample**](iaudiostreamsample.md) interface.
-   DirectDraw streams create DirectDraw samples, which expose the [**IDirectDrawStreamSample**](idirectdrawstreamsample.md) interface.
-   Media type streams create media type samples, which expose the [**IAMMediaTypeSample**](iammediatypesample.md) interface.

The following diagram shows the interface hierarchy for the interfaces listed previously:

![multimediastreaming interface hierarchy](images/mmstream01.png)

 

 



