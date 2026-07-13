---
description: The CMediaType class manages media types. This class inherits the AM\_MEDIA\_TYPE structure. It can be cast to a variable of type AM\_MEDIA\_TYPE.
ms.assetid: ea3d03a1-cca4-4a6e-9d1d-4cebe710f913
title: CMediaType class (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaType class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cmediatype class hierarchy](images/mtype01.png)

The `CMediaType` class manages media types. This class inherits the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. It can be cast to a variable of type **AM\_MEDIA\_TYPE**.



| Public Methods                                                      | Description                                                                    |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**CMediaType**](cmediatype-cmediatype.md)                         | Constructor method.                                                            |
| [**~CMediaType**](cmediatype--cmediatype.md)                       | Destructor method.                                                             |
| [**Set**](cmediatype-set.md)                                       | Sets the media type from another media type.                                   |
| [**IsValid**](cmediatype-isvalid.md)                               | Determines whether a major type has been assigned to this object.              |
| [**Type**](cmediatype-type.md)                                     | Retrieves the major type.                                                      |
| [**SetType**](cmediatype-settype.md)                               | Specifies the major type.                                                      |
| [**Subtype**](cmediatype-subtype.md)                               | Retrieves the subtype.                                                         |
| [**SetSubtype**](cmediatype-setsubtype.md)                         | Specifies the subtype.                                                         |
| [**IsFixedSize**](cmediatype-isfixedsize.md)                       | Determines if the samples have a fixed size or a variable size.                |
| [**IsTemporalCompressed**](cmediatype-istemporalcompressed.md)     | Determines if the stream uses temporal compression.                            |
| [**GetSampleSize**](cmediatype-getsamplesize.md)                   | Retrieves the sample size.                                                     |
| [**SetSampleSize**](cmediatype-setsamplesize.md)                   | Specifies a fixed sample size, or specifies that samples have a variable size. |
| [**SetVariableSize**](cmediatype-setvariablesize.md)               | Specifies that samples do not have a fixed size.                               |
| [**SetTemporalCompression**](cmediatype-settemporalcompression.md) | Specifies whether samples are compressed using temporal compression.           |
| [**Format**](cmediatype-format.md)                                 | Retrieves a pointer to the format block.                                       |
| [**FormatLength**](cmediatype-formatlength.md)                     | Retrieves the length of the format block.                                      |
| [**SetFormatType**](cmediatype-setformattype.md)                   | Specifies the format type.                                                     |
| [**FormatType**](cmediatype-formattype.md)                         | Retrieves the format type.                                                     |
| [**SetFormat**](cmediatype-setformat.md)                           | Specifies the format block.                                                    |
| [**ResetFormatBuffer**](cmediatype-resetformatbuffer.md)           | Deletes the format block.                                                      |
| [**AllocFormatBuffer**](cmediatype-allocformatbuffer.md)           | Allocates memory for the format block.                                         |
| [**ReallocFormatBuffer**](cmediatype-reallocformatbuffer.md)       | Reallocates the format block to a new size.                                    |
| [**InitMediaType**](cmediatype-initmediatype.md)                   | Initializes the media type.                                                    |
| [**MatchesPartial**](cmediatype-matchespartial.md)                 | Determines if this media type matches a partially specified media type.        |
| [**IsPartiallySpecified**](cmediatype-ispartiallyspecified.md)     | Determines if the media type is partially defined.                             |
| Operators                                                           | Description                                                                    |
| [**operator =**](cmediatype-operator-.md)                          | Overloads the assignment operator to copy a media type.                        |
| [**operator ==**](cmediatype-operator--.md)                        | Tests for equality between `CMediaType` objects.                               |
| [**operator !=**](cmediatype-operator-neq.md)                      | Tests for inequality between `CMediaType` objects.                             |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




