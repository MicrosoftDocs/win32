---
description: The KSMULTIPLE\_ITEM structure describes the size and count of variable-length properties on kernel-mode pins.
ms.assetid: aedbf7bc-393d-4ab5-afcd-d8822b925f07
title: KSMULTIPLE_ITEM structure (Ks.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KSMULTIPLE_ITEM
api_type: 
- HeaderDef
api_location: 
- ks.h
ms.custom: UpdateFrequency5
---

# KSMULTIPLE\_ITEM structure

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `KSMULTIPLE_ITEM` structure describes the size and count of variable-length properties on kernel-mode pins.

## Syntax


```C++
typedef struct {
  ULONG Size;
  ULONG Count;
} KSMULTIPLE_ITEM, *PKSMULTIPLE_ITEM;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Size of the returned memory block, in bytes. The size includes the **KSMULTIPLE\_ITEM** structure and the items that follow it.

</dd> <dt>

**Count**
</dt> <dd>

Specifies the total number of items that follow this structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ks.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Structures](directshow-structures.md)
</dt> <dt>

[**IKsPin::KsQueryMediums**](ikspin-ksquerymediums.md)
</dt> <dt>

[**REGPINMEDIUM**](/windows/desktop/api/strmif/ns-strmif-regpinmedium)
</dt> </dl>

 

 




