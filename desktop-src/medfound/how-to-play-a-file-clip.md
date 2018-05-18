---
Description: 'This topic describes how to play a segment of a media file in MFPlay, by setting the start and stop times for playback.'
ms.assetid: 'cd761a4a-42ad-4994-b1b8-0946d29c3d8b'
title: How to Play a File Clip
---

# How to Play a File Clip

\[MFPlay is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

This topic describes how to play a segment of a media file in MFPlay, by setting the start and stop times for playback.

**To Play a File Clip**

1.  Call [**IMFPMediaPlayer::CreateMediaItemFromURL**](imfpmediaplayer-createmediaitemfromurl.md) or [**IMFPMediaPlayer::CreateMediaItemFromObject**](imfpmediaplayer-createmediaitemfromobject.md) to create a media item for the file.
2.  Optionally, get the total duration of the file, as described in [How to Get the Playback Duration](how-to-get-the-playback-duration.md).
3.  Call [**IMFPMediaItem::SetStartStopPosition**](imfpmediaitem-setstartstopposition.md) to set the start and stop times. The stop time must not exceed the file duration.
4.  Call [**IMFPMediaPlayer::SetMediaItem**](imfpmediaplayer-setmediaitem.md) to start playback.

The following example uses the blocking version of [**CreateMediaItemFromURL**](imfpmediaplayer-createmediaitemfromurl.md). If the non-blocking version is used, the code that appears after **CreateMediaItemFromURL** should be placed in the handler for the **MFP\_EVENT\_TYPE\_MEDIAITEM\_CREATED** event. For more information about events in MFPlay, see [Receiving Events From the Player](getting-started-with-mfplay.md#receiving-events-from-the-player).

To get the file duration, this example calls the `GetPlaybackDuration` function shown in the topic [How to Get the Playback Duration](how-to-get-the-playback-duration.md).


```C++
HRESULT PlayMediaClip(
    IMFPMediaPlayer *pPlayer,
    PCWSTR pszURL,
    LONGLONG    hnsStart,
    LONGLONG    hnsEnd
    )
{
    IMFPMediaItem *pItem = NULL;
    PROPVARIANT varStart, varEnd;

    ULONGLONG hnsDuration = 0;

    HRESULT hr = pPlayer->CreateMediaItemFromURL(pszURL, TRUE, 0, &amp;pItem);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = GetPlaybackDuration(pItem, &amp;hnsDuration);
    if (FAILED(hr))
    {
        goto done;
    }

    if ((ULONGLONG)hnsEnd > hnsDuration)
    {
        hnsEnd = hnsDuration;
    }

    hr = InitPropVariantFromInt64(hnsStart, &amp;varStart);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = InitPropVariantFromInt64(hnsEnd, &amp;varEnd);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pItem->SetStartStopPosition(
        &amp;MFP_POSITIONTYPE_100NS,
        &amp;varStart,
        &amp;MFP_POSITIONTYPE_100NS,
        &amp;varEnd
        );
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pPlayer->SetMediaItem(pItem);

done:
    SafeRelease(&amp;pItem);
    return hr;
}
```



## Requirements

MFPlay requires Windows 7.

## Related topics

<dl> <dt>

[Using MFPlay for Audio/Video Playback](using-mfplay-for-audio-video-playback.md)
</dt> </dl>

 

 



