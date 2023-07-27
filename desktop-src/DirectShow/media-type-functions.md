---
description: The DirectShow base classes provides helper functions for handling the AM\_MEDIA\_TYPE structure.
ms.assetid: 4dbea5b4-bf78-4253-be48-d81b77be6e77
title: Media Type Functions (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Media
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# Media Type Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DirectShow base classes provides helper functions for handling the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

The **AM\_MEDIA\_TYPE** structure contains a pointer (the **pbFormat** member) to another block of memory, which is called the *format block*. When you work with this structure, therefore, you must be careful about memory allocation in order to avoid memory leaks.

The following functions allocate memory:

-   **CreateMediaType** allocates a new **AM\_MEDIA\_TYPE** structure and the format block.
-   **CopyMediaType** copies to an existing **AM\_MEDIA\_TYPE** structure, but allocates the format block.
-   **CreateAudioMediaType** initializes an existing **AM\_MEDIA\_TYPE** structure, and optionally allocates the format block.

The following functions free memory:

-   **FreeMediaType** releases the format block.
-   **DeleteMediaType** frees an **AM\_MEDIA\_TYPE** structure, including the format block.



| Function                                             | Description                                                                                                 |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**CopyMediaType**](copymediatype.md)               | Copies a task-allocated **AM\_MEDIA\_TYPE** structure.                                                      |
| [**CreateAudioMediaType**](createaudiomediatype.md) | Initializes a media type structure given a wave format structure.                                           |
| [**CreateMediaType**](createmediatype.md)           | Allocates and initializes an **AM\_MEDIA\_TYPE** structure, from an existing **AM\_MEDIA\_TYPE** structure. |
| [**DeleteMediaType**](deletemediatype.md)           | Deletes a task-allocated **AM\_MEDIA\_TYPE** structure.                                                     |
| [**FreeMediaType**](freemediatype.md)               | Frees a task-allocated **AM\_MEDIA\_TYPE** structure from memory.                                           |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




