---
description: Multimedia Streaming Objects
ms.assetid: 4f5460db-2670-41af-a57f-20cf706827e6
title: Multimedia Streaming Objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Multimedia Streaming Objects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This API is deprecated. New applications should not use it.

 

The following table describes the multimedia streaming objects.




| CLSID | Description | Interfaces supported | 
|-------|-------------|----------------------|
| CLSID_AMMediaTypeStream | Can create media samples for any DirectShow-supported data type | <ul><li><a href="/previous-versions/windows/desktop/api/amstream/nn-amstream-iammediastream"><strong>IAMMediaStream</strong></a></li><li><a href="/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream"><strong>IMediaStream</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a></li></ul> | 
| CLSID_AMAudioData | Implementation of <a href="/previous-versions/windows/desktop/api/austream/nn-austream-iaudiodata"><strong>IAudioData</strong></a> audio container object. | <ul><li><a href="/previous-versions/windows/desktop/api/austream/nn-austream-iaudiodata"><strong>IAudioData</strong></a></li></ul> | 
| CLSID_AMDirectDrawStream | DirectDraw media stream that can be added to a DirectShow multimedia stream. | <ul><li><a href="/previous-versions/windows/desktop/api/amstream/nn-amstream-iammediastream"><strong>IAMMediaStream</strong></a></li><li><a href="/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream"><strong>IMediaStream</strong></a></li><li><a href="/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawmediastream"><strong>IDirectDrawMediaStream</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a></li></ul> | 
| CLSID_AMMultiMediaStream | DirectShow implementation of multimedia stream. | <ul><li><a href="/previous-versions/windows/desktop/api/amstream/nn-amstream-iammultimediastream"><strong>IAMMultiMediaStream</strong></a></li><li><a href="/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream"><strong>IMultiMediaStream</strong></a></li></ul> | 
| CLSID_MediaStreamFilter | Provides multimedia streaming functionality for the CLSID_AMMultiMediaStream object through the <a href="/previous-versions/windows/desktop/api/amstream/nn-amstream-iammultimediastream"><strong>IAMMultiMediaStream</strong></a> interface. | <ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></li></ul> | 
| N/A | Samples created by the CLSID_AMMediaTypeStream object. | <ul><li><a href="/previous-versions/windows/desktop/api/mmstream/nn-mmstream-istreamsample"><strong>IStreamSample</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imediasample"><strong>IMediaSample</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imediasample2"><strong>IMediaSample2</strong></a></li></ul> | 
| N/A | Samples created by the DirectDraw stream. | <ul><li><a href="/previous-versions/windows/desktop/api/mmstream/nn-mmstream-istreamsample"><strong>IStreamSample</strong></a></li><li><a href="/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawstreamsample"><strong>IDirectDrawStreamSample</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imediasample"><strong>IMediaSample</strong></a></li></ul> | 




 

 

 



