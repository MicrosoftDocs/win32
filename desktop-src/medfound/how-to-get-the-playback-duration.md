---
Description: This topic describes how to get the playback duration of a media file using MFPlay.
ms.assetid: b1ea4f21-55d1-47b0-b6d3-8951dce79f7c
title: How to Get the Playback Duration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Get the Playback Duration

\[MFPlay is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

This topic describes how to get the playback duration of a media file using MFPlay.

**To Get the Playback Duration**

1.  Call [**IMFPMediaPlayer::CreateMediaItemFromURL**](/windows/win32/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl?branch=master) or [**IMFPMediaPlayer::CreateMediaItemFromObject**](/windows/win32/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromobject?branch=master) to create a media item for the file.
2.  Call [**IMFPMediaItem::GetDuration**](/windows/win32/mfplay/nf-mfplay-imfpmediaitem-getduration?branch=master). Specify **MFP\_POSITIONTYPE\_100NS** for the first parameter. The duration is returned as a **PROPVARIANT** that contains a **LARGE\_INTEGER** value. The duration is given in 100-nanosecond units.

The following example shows step 2:


```C++
#include <propvarutil.h>

HRESULT GetPlaybackDuration(IMFPMediaItem *pItem, ULONGLONG *phnsDuration)
{
    PROPVARIANT var;

    HRESULT hr = pItem->GetDuration(MFP_POSITIONTYPE_100NS, &amp;var);

    if (SUCCEEDED(hr))
    {
        hr = PropVariantToUInt64(var, phnsDuration);
        PropVariantClear(&amp;var);
    }

    return hr;
}
```



## Requirements

MFPlay requires Windows 7.

## Related topics

<dl> <dt>

[Using MFPlay for Audio/Video Playback](using-mfplay-for-audio-video-playback.md)
</dt> </dl>

 

 



