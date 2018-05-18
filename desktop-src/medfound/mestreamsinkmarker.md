---
Description: 'Raised by a stream sink after the IMFStreamSink::PlaceMarker method is called.'
ms.assetid: '40f68352-86e5-4864-9ca0-f30998857fef'
title: MEStreamSinkMarker event
---

# MEStreamSinkMarker event

Raised by a stream sink after the [**IMFStreamSink::PlaceMarker**](imfstreamsink-placemarker.md) method is called.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE            | Description                                                                                                                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| &gt;Any<br/> | The event value is a copy of the **PROPVARIANT** that the caller specified in the *pvarContextValue* parameter of the [**PlaceMarker**](imfstreamsink-placemarker.md) method.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> </dl>

 

 




