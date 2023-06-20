---
description: Describes the contents of an elementary stream within an MPEG-2 transport stream. This enumeration is used in the IMPEG2PIDMap interface, which is implemented on the output pins of the MPEG-2 Demultiplexer.
ms.assetid: 989ad56b-b5af-4811-889e-c79fcd3f7f01
title: MEDIA_SAMPLE_CONTENT enumeration (Bdatypes.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MEDIA_SAMPLE_CONTENT
api_type: 
- HeaderDef
api_location: 
- bdatypes.h
ms.custom: UpdateFrequency5
---

# MEDIA\_SAMPLE\_CONTENT enumeration

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Describes the contents of an elementary stream within an MPEG-2 transport stream. This enumeration is used in the [**IMPEG2PIDMap**](/previous-versions/windows/desktop/api/Bdaiface/nn-bdaiface-impeg2pidmap) interface, which is implemented on the output pins of the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md).

## Syntax


```C++
typedef enum  { 
  MEDIA_TRANSPORT_PACKET,
  MEDIA_ELEMENTARY_STREAM,
  MEDIA_MPEG2_PSI,
  MEDIA_TRANSPORT_PAYLOAD
} MEDIA_SAMPLE_CONTENT;
```



## Constants

<dl> <dt>

<span id="MEDIA_TRANSPORT_PACKET"></span><span id="media_transport_packet"></span>**MEDIA\_TRANSPORT\_PACKET**
</dt> <dd>

Specifies a complete transport stream packet to be passed through without processing.

</dd> <dt>

<span id="MEDIA_ELEMENTARY_STREAM"></span><span id="media_elementary_stream"></span>**MEDIA\_ELEMENTARY\_STREAM**
</dt> <dd>

Specifies an audio or video PES payload.

</dd> <dt>

<span id="MEDIA_MPEG2_PSI"></span><span id="media_mpeg2_psi"></span>**MEDIA\_MPEG2\_PSI**
</dt> <dd>

Specifies a PAT, PMT, CAT, or Private data stream. These are complete PSI sections which do not need to be reassembled.

</dd> <dt>

<span id="MEDIA_TRANSPORT_PAYLOAD"></span><span id="media_transport_payload"></span>**MEDIA\_TRANSPORT\_PAYLOAD**
</dt> <dd>

Specifies gathered TS packet payloads, such as PES packets.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Enumerated Types](directshow-enumerated-types.md)
</dt> </dl>

 

 




