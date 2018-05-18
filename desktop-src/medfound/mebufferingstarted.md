---
Description: 'Signals that a media source has started to buffer data.'
ms.assetid: '8637dfcd-2e0c-4cf4-a216-4089c201bfc6'
title: MEBufferingStarted event
---

# MEBufferingStarted event

Signals that a media source has started to buffer data.

A media source can send this event if the source buffers data while the Media Session is running. When the Media Session receives this event, it pauses the presentation clock until the media source sends the [MEBufferingStopped](mebufferingstopped.md) event. The Media Session also forwards the MEBufferingStarted event to the application.

Byte streams that implement the [**IMFByteStreamBuffering**](imfbytestreambuffering.md) interface also send this event.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

If a media source sends the MEBufferingStarted event, it must send the [MEBufferingStopped](mebufferingstopped.md) event when it stops buffering data. The media source must send a matching MEBufferingStopped event for every MEBufferingStarted event. The media source should not forward these events before the source's [**IMFMediaSource::Start**](imfmediasource-start.md) method is called, or after the source's [**IMFMediaSource::Stop**](imfmediasource-stop.md) method is called.

If you are streaming from the Media Foundation network source, you can get the buffering progress by querying the **MFNETSOURCE\_BUFFERPROGRESS\_ID** statistic. For more information, see [**MFNETSOURCE\_STATISTICS\_IDS**](mfnetsource-statistics-ids.md).

## Examples


```C++
HRESULT GetBufferProgress(IMFMediaSession *pSession, DWORD *pProgress)
{
    IPropertyStore *pProp = NULL;
    PROPVARIANT var;

    // Get the property store from the media session.
    HRESULT hr = MFGetService(
        pSession, 
        MFNETSOURCE_STATISTICS_SERVICE, 
        IID_PPV_ARGS(&amp;pProp)
        );

    if (SUCCEEDED(hr))
    {
        PROPERTYKEY key;
        key.fmtid = MFNETSOURCE_STATISTICS;
        key.pid = MFNETSOURCE_BUFFERPROGRESS_ID;

        hr = pProp->GetValue(key, &amp;var);
    }

    if (SUCCEEDED(hr))
    {
        *pProgress = var.lVal;
    }

    PropVariantClear(&amp;var);
    SafeRelease(&amp;pProp);
    return hr;
}
```



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

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




