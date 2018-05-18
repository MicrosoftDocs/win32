---
Description: 'Sent by a byte stream when the characteristics of the byte stream have changed.'
ms.assetid: 'EC34A7A3-BF01-4F9E-BA79-131B76D4C58F'
title: MEByteStreamCharacteristicsChanged event
---

# MEByteStreamCharacteristicsChanged event

Sent by a byte stream when the characteristics of the byte stream have changed.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event indicates that one or more of the following characteristics has changed:

-   Capability flags ([**IMFByteStream::GetCapabilities**](imfbytestream-getcapabilities.md))
-   End-of-stream flag ([**IMFByteStream::IsEndOfStream**](imfbytestream-isendofstream.md))
-   Length ([**IMFByteStream::GetLength**](imfbytestream-getlength.md))

Not all [**IMFByteStream**](imfbytestream.md) implementations support this event. To receive the event, query the byte-stream object for the [**IMFMediaEventGenerator**](imfmediaeventgenerator.md) interface.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




