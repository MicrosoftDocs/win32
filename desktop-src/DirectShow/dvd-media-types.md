---
description: The following tables describe the media types used for DVD.
ms.assetid: 83bcce3e-4d54-463d-863e-88e8dfd0c8da
title: DVD Media Types (Ksuuids.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Media Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables describe the media types used for DVD.

## Major Types



| GUID                            | Description                               |
|---------------------------------|-------------------------------------------|
| MEDIATYPE\_DVD\_ENCRYPTED\_PACK | Encrypted DVD data                        |
| MEDIATYPE\_MPEG2\_PES           | MPEG-2 Packetized Elementary Stream (PES) |



 

## Subtypes



| GUID                          | Description                             |
|-------------------------------|-----------------------------------------|
| MEDIASUBTYPE\_DOLBY\_AC3      | Dolby AC3 audio                         |
| MEDIASUBTYPE\_DTS             | Digital Theater Systems (DTS) audio     |
| MEDIASUBTYPE\_DVD\_SUBPICTURE | DVD Subpicture                          |
| MEDIASUBTYPE\_MPEG2\_VIDEO    | MPEG-2 video                            |
| MEDIASUBTYPE\_SDDS            | Sony Dynamic Digital Sound (SDDS) audio |



 

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ksuuids.h</dt> </dl> |



 

 




