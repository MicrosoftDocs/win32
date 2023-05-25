---
description: The SetMediaType method specifies the media type for the connection on the input pin of the Sample Grabber.
ms.assetid: 9568832f-6666-45c9-9421-485c877affb3
title: ISampleGrabber::SetMediaType method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- ISampleGrabber.SetMediaType
api_type:
- COM
api_location:
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# ISampleGrabber::SetMediaType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetMediaType` method specifies the media type for the connection on the input pin of the Sample Grabber.

## Syntax


```C++
HRESULT SetMediaType(
   const AM_MEDIA_TYPE *pType
);
```



## Parameters

<dl> <dt>

*pType* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure specifies the required media type. It is not necessary to set all the structure members; see Remarks for details.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

By default, the Sample Grabber has no preferred media type. To ensure that the Sample Grabber connects to the correct filter, call this method before building the filter graph.

This method restricts the range of media types that the filter will accept. When the filter connects, it tries to match the media type given in *pType*. To do so, it compares the major type, subtype, and format type GUIDs, in that order. For each of these GUIDs, if *pType* has the value GUID\_NULL, the Sample Grabber accepts the media type without any further checks. If *pType* has any other value, the Sample Grabber compares it to the GUID in the connection type. Unless the two GUIDs match exactly, the Sample Grabber rejects the connection.

For video media types, the Sample Grabber ignores the format block. Therefore, it will accept any video size and frame rate. When you call `SetMediaType`, set the format block (**pbFormat**) to **NULL** and the size (**cbFormat**) to zero. For audio media types, the Sample Grabber will examine the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure and will require the other filter to connect with that format — unless the format block in *pType* is **NULL**, or the format tag is WAVE\_FORMAT\_PCM and the other structure members are zero.

Example 1:

-   Major type: MEDIATYPE\_Video
-   Subtype: GUID\_NULL
-   Format type: GUID\_NULL

The Sample Grabber will accept any video type where the major type equals MEDIATYPE\_Video. It will not check the subtype.

Example 2:

-   Major type: MEDIATYPE\_Video
-   Subtype: MEDIASUBTYPE\_RGB24
-   Format type: GUID\_NULL

Now the Sample Grabber will check the subtype, and accept only RGB 24 video.

**Limitations:** Regardless of what type you set, the Sample Grabber Filter rejects any video types with top-down orientation (negative *biHeight*), or with a format type of FORMAT\_VideoInfo2. In this case, although the `SetMediaType` method succeeds, the filter will not connect.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Using the Sample Grabber](using-the-sample-grabber.md)
</dt> <dt>

[**ISampleGrabber Interface**](isamplegrabber.md)
</dt> </dl>

 

 
