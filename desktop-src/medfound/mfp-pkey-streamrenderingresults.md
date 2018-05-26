---
Description: Specifies which streams were connected successfully to a media sink.
ms.assetid: b5e45bfc-d91d-41b8-aaa4-72b3a23d869e
title: MFP\_PKEY\_StreamRenderingResults property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFP\_PKEY\_StreamRenderingResults property

> \[!Important\]  
> Deprecated. This API may be removed from future releases of Windows. Applications should use the [Media Session](media-session.md) for playback.

 

Specifies which streams were connected successfully to a media sink.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Array of **DWORD** values (**CAUL**)

VT\_VECTOR \| VT\_UI4

**caul**



## Remarks

This property can be sent with the **MFP\_EVENT\_TYPE\_MEDIAITEM\_SET** event.

The value of the property is an array of **HRESULT**s. The array entries correspond to streams on the current media item. Each entry in the array indicates whether the corresponding stream was connected to a media sink, as follows:

-   If the stream is connected to a media sink, the value is **S\_OK**.
-   If the stream is not selected, the value is **S\_FALSE**.
-   If an error occurred while attempting to connect the stream, the value is an error code.

If at least one stream was connected successfully, playback is possible. For example, the user might have the codec needed to play the audio stream but not to play the video stream.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Mfplay.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**MFP\_MEDIAITEM\_SET\_EVENT**](/windows/win32/mfplay/ns-mfplay-mfp_mediaitem_set_event?branch=master)
</dt> </dl>

 

 




