---
Description: 'Raised by a media stream when the media type of the stream changes.'
ms.assetid: '14786a9b-413e-4fb4-b267-bfd0ccd4631b'
title: MEStreamFormatChanged event
---

# MEStreamFormatChanged event

Raised by a media stream when the media type of the stream changes.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFMediaType**](imfmediatype.md) interface of the new media type.<br/> <br/> |



## Remarks

Use this event to signal format changes in the stream.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




