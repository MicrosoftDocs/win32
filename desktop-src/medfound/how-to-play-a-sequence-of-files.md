---
description: This topic describes how to play a sequence of audio/video files using MFPlay.
ms.assetid: ee16eaa3-0506-4444-b139-f8a8498d6597
title: How to Play a Sequence of Files
ms.topic: article
ms.date: 05/31/2018
---

# How to Play a Sequence of Files

\[MFPlay is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

This topic describes how to play a sequence of audio/video files using MFPlay.


The topic [Getting Started with MFPlay](getting-started-with-mfplay.md) shows how to play a single media file. You can also use MFPlay to play a sequence of files.

### Synchronous (Blocking) Method

1.  Call the [**IMFPMediaPlayer::CreateMediaItemFromURL**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl) method. The method creates a media item.
2.  Call [**IMFPMediaPlayer::SetMediaItem**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setmediaitem) to queue the media item for playback.
3.  Call [**IMFPMediaPlayer::Play**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-play) to start playback.

These steps are shown in the following code.


```C++
HRESULT OpenMediaFile(IMFPMediaPlayer *pPlayer, PCWSTR pwszURL)
{
    HRESULT hr = S_OK;
    
    IMFPMediaItem *pItem = NULL;

    hr = pPlayer->CreateMediaItemFromURL(
        sURL, 
        TRUE,  // Blocking call
        0,     // User data.
        &pItem
        );

    if (SUCCEEDED(hr))
    {
        hr = pPlayer->SetMediaItem(pItem);
    }

    if (SUCCEEDED(hr))
    {
       hr = pPlayer->Play();
    }

    if (pItem)
    {
        pItem->Release();
    }
    return hr;
}
```



The [**CreateMediaItemFromURL**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl) method takes the following parameters:

-   The first parameter is the URL of the file.
-   The second parameter specifies whether the method blocks. Specifying the value **TRUE**, as shown here, causes the method to block until the media item is created.
-   The third parameter associates an arbitrary **DWORD\_PTR** value with the media item. You can get this value later by calling [**IMFPMediaItem::GetUserData**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaitem-getuserdata).
-   The fourth parameter receives a pointer to the [**IMFPMediaItem**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaitem) interface of the media item.

### Asynchronous (Non-Blocking) Method

Avoid the blocking option if you call [**CreateMediaItemFromURL**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl) from your UI thread, because it can take a noticeable amount of time to complete. The method typically opens a file or network connection and reads enough data to parse the file headers, all of which can take time. Therefore, it is generally better to set the second parameter to **FALSE**. This option causes the method to perform asynchronously. When the asynchronous option is used, the last parameter must be **NULL**:


```C++
    hr = pPlayer->CreateMediaItemFromURL(
        sURL, 
        FALSE,  // Non-blocking call.
        0,      // User data.
        NULL    // Must be NULL for the non-blocking call.
        );
```



When the media item is created, your application receives an **MFP\_EVENT\_TYPE\_MEDIAITEM\_CREATED** event. The data structure for this event contains a pointer to the media item. Pass this pointer to the [**SetMediaItem**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setmediaitem) method to queue the item for playback.


```C++
void OnMediaItemCreated(MFP_MEDIAITEM_CREATED_EVENT *pEvent)
{
    HRESULT hr = S_OK;
    if (FAILED(pEvent->header.hrEvent))
    {
        // Handle error. (Not shown.)
    }
    else
    {
        hr = g_pPlayer->SetMediaItem(pEvent->pMediaItem);
    }
}
```



## Requirements

MFPlay requires Windows 7.

## Related topics

<dl> <dt>

[Using MFPlay for Audio/Video Playback](using-mfplay-for-audio-video-playback.md)
</dt> </dl>

 

 



