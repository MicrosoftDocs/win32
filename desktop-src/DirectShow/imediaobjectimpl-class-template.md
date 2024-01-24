---
description: The IMediaObjectImpl class template provides a base implementation for the IMediaObject interface. For more information on using this template, see Using the DMO Class Template.
ms.assetid: 81d45b8d-8373-4e42-b768-f6126feb935d
title: IMediaObjectImpl Class Template (Dmoimpl.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IMediaObjectImpl Class Template

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `IMediaObjectImpl` class template provides a base implementation for the [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface. For more information on using this template, see [Using the DMO Class Template](using-the-dmo-class-template.md).

This `IMediaObjectImpl` template exposes the following members.



| Nested Class                              | Description                                  |
|-------------------------------------------|----------------------------------------------|
| [**LockIt**](imediaobjectimpl-lockit.md) | Helper class that locks and unlocks the DMO. |



 



| Method                                                                      | Description                                                          |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**CheckTypesSet**](/previous-versions/ms807621(v=msdn.10))                     | Determines whether all of the non-optional streams have media types. |
| [**InputType**](/previous-versions/ms807633(v=msdn.10))                             | Retrieves the current media type for a specified input stream.       |
| [**InputTypeSet**](/previous-versions/ms807638(v=msdn.10))                       | Queries whether the media type was set on an input stream.           |
| [**InternalAcceptingInput**](/previous-versions/ms809095(v=msdn.10))   | Queries whether an input stream can accept more input.               |
| [**InternalCheckInputType**](/previous-versions/ms809096(v=msdn.10))   | Queries whether an input stream can accept a given media type.       |
| [**InternalCheckOutputType**](/previous-versions/ms809098(v=msdn.10)) | Queries whether an output stream can accept a given media type.      |
| [**Lock**](/previous-versions/ms809100(v=msdn.10))                                       | Locks the DMO                                                        |
| [**OutputType**](/previous-versions/ms807644(v=msdn.10))                           | Retrieves the current media type for a specified output stream.      |
| [**OutputTypeSet**](/previous-versions/ms807649(v=msdn.10))                     | Queries whether the media type was set on an output stream.          |
| [**Unlock**](/previous-versions/ms809101(v=msdn.10))                                   | Unlocks the DMO                                                      |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dmoimpl.h</dt> </dl>                                                                     |
| Library<br/> | <dl> <dt>Dmoguids.lib; </dt> <dt>Msdmo.lib</dt> </dl> |



## See also

<dl> <dt>

[DMO Reference](dmo-reference.md)
</dt> <dt>

[Using the DMO Class Template](using-the-dmo-class-template.md)
</dt> </dl>

 

 
