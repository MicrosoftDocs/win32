---
description: Multimedia Streaming Error and Success Codes
ms.assetid: 3b7a11d2-55b9-4505-8eb2-46be423c662b
title: Multimedia Streaming Error and Success Codes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Multimedia Streaming Error and Success Codes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This API is deprecated. New applications should not use it.

 

The following list contains error messages and success notifications for applications that use the multimedia streaming interfaces. This list does not contain all possible errors; the errors shown apply specifically to the Microsoft® DirectShow® implementation of the multimedia streaming interfaces.



| Value                       | Hexadecimal code | Description                                                                                                                                                                                |
|-----------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MS\_S\_PENDING              | 0x00040001       | Sample update is not yet complete.                                                                                                                                                         |
| MS\_S\_NOUPDATE             | 0x00040002       | Sample was not updated after forced completion.                                                                                                                                            |
| MS\_S\_ENDOFSTREAM          | 0x00040003       | End of stream. Sample not updated.                                                                                                                                                         |
| MS\_E\_SAMPLEALLOC          | 0x80040401       | An [**IMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream) object could not be removed from an [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream) object because it still contains at least one allocated sample. |
| MS\_E\_PURPOSEID            | 0x80040402       | The specified purpose ID can't be used for the call.                                                                                                                                       |
| MS\_E\_NOSTREAM             | 0x80040403       | No stream can be found with the specified attributes.                                                                                                                                      |
| MS\_E\_NOSEEKING            | 0x80040404       | Seeking not supported for this [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream) object.                                                                                                      |
| MS\_E\_INCOMPATIBLE         | 0x80040405       | The stream formats are not compatible.                                                                                                                                                     |
| MS\_E\_BUSY                 | 0x80040406       | The sample is busy.                                                                                                                                                                        |
| MS\_E\_NOTINIT              | 0x80040407       | The object can't accept the call because its initialize function or equivalent has not been called.                                                                                        |
| MS\_E\_SOURCEALREADYDEFINED | 0x80040408       | Source already defined.                                                                                                                                                                    |
| MS\_E\_INVALIDSTREAMTYPE    | 0x80040409       | The stream type is not valid for this operation.                                                                                                                                           |
| MS\_E\_NOTRUNNING           | 0x8004040A       | The [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream) object is not in running state.                                                                                                         |



 

## Related topics

<dl> <dt>

[Multimedia Streaming](multimedia-streaming.md)
</dt> </dl>

 

 



