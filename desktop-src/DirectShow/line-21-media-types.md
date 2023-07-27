---
description: The following tablea describe the media types used for line 21 data.
ms.assetid: ac851882-df33-4905-a507-12044c7d576d
title: Line 21 Media Types (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Line 21 Media Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tablea describe the media types used for line 21 data.

## Major Type



| GUID                     | Description  |
|--------------------------|--------------|
| MEDIATYPE\_AUXLine21Data | Line 21 data |



 

## Subtypes



| GUID                             | Description                    |
|----------------------------------|--------------------------------|
| MEDIASUBTYPE\_Line21\_BytePair   | Line 21 data as byte pairs     |
| MEDIASUBTYPE\_Line21\_GOPPacket  | Line 21 data in DVD GOP Packet |
| MEDIASUBTYPE\_Line21\_VBIRawData | Line 21 data in raw VBI format |



 

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



 

 




