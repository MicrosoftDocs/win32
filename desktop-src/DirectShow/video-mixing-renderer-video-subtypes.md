---
description: The following subtypes are defined for use with the Video Mixing Renderer (VMR) filter.
ms.assetid: 74dec302-5ef7-41db-abe9-c3e9cbed17de
title: Video Mixing Renderer Video Subtypes (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Mixing Renderer Video Subtypes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following subtypes are defined for use with the Video Mixing Renderer (VMR) filter.

## VMR-7 Subtypes



| Subtype                              | Description                                      |
|--------------------------------------|--------------------------------------------------|
| MEDIASUBTYPE\_RGB32\_D3D\_DX7\_RT    | 32-bit RGB render target.                        |
| MEDIASUBTYPE\_RGB16\_D3D\_DX7\_RT    | 16-bit RGB render target.                        |
| MEDIASUBTYPE\_ARGB32\_D3D\_DX7\_RT   | 32-bit ARGB render target.                       |
| MEDIASUBTYPE\_ARGB4444\_D3D\_DX7\_RT | ARGB4444 render target. For subpicture graphics. |
| MEDIASUBTYPE\_ARGB1555\_D3D\_DX7\_RT | ARGB1555 render target. For subpicture graphics. |



 

## VMR-9 Subtypes



| Subtype                              | Description                                      |
|--------------------------------------|--------------------------------------------------|
| MEDIASUBTYPE\_RGB32\_D3D\_DX9\_RT    | 32-bit RGB render target.                        |
| MEDIASUBTYPE\_RGB16\_D3D\_DX9\_RT    | 16-bit RGB render target.                        |
| MEDIASUBTYPE\_ARGB32\_D3D\_DX9\_RT   | 32-bit ARGB render target.                       |
| MEDIASUBTYPE\_ARGB4444\_D3D\_DX9\_RT | ARGB4444 render target. For subpicture graphics. |
| MEDIASUBTYPE\_ARGB1555\_D3D\_DX9\_RT | ARGB1555 render target. For subpicture graphics. |



 

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Video Subtypes](video-subtypes.md)
</dt> <dt>

[Working with Direct3D Render Targets](working-with-direct3d-render-targets.md)
</dt> </dl>

 

 




