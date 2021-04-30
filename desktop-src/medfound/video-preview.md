---
description: This topic describes how to use MFPlay to preview video from a video camera.
ms.assetid: ecf6113f-1d8e-4680-87ab-bfd45a9663e4
title: Video Preview
ms.topic: article
ms.date: 05/31/2018
---

# Video Preview

\[MFPlay is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

This topic describes how to use MFPlay to preview video from a video camera.

MFPlay provides the simplest way in Microsoft Media Foundation to preview video from a capture device. You should use MFPlay if the following conditions are all true:

-   You do not need to capture the video to a file.
-   You do not need fine-grained control over how the video is rendered. (For example, you do not need to control the creation of the Direct3D device.)
-   You do not need to process the video data from the camera prior to rendering.

Otherwise, the [Source Reader](source-reader.md) may be a better option.

To use MFPlay with a video capture device, perform the following steps:

1.  Create a media source for the capture device. See [Enumerating Video Capture Devices](enumerating-video-capture-devices.md).
2.  Call [**MFPCreateMediaPlayer**](/windows/desktop/api/mfplay/nf-mfplay-mfpcreatemediaplayer) to create an instance of the player object.
3.  Call the [**IMFPMediaPlayer::CreateMediaItemFromObject**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromobject) method. Pass in a pointer to the IMFMediaSource interface of the media source. The method receives a pointer to the [**IMFPMediaItem**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaitem) interface.
4.  Call [**IMFPMediaPlayer::SetMediaItem**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setmediaitem).
5.  Call [**IMFPMediaPlayer::Play**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-play) to begin previewing.

The following code shows these steps:


```C++
    IMFPMediaItem *pItem = NULL;

    if (SUCCEEDED(hr))
    {
        hr = MFPCreateMediaPlayer(
            NULL,       // URL.
            FALSE,      // Do not start playback yet.
            0,          // Option flags.
            NULL,       // Callback interface.
            hwnd,
            &g_pPlayer
            );
    }

    if (SUCCEEDED(hr))
    {
        hr = g_pPlayer->CreateMediaItemFromObject(
            g_pSource,
            TRUE,       // Blocking call.
            0,          // User data.
            &pItem
            );
    }

    if (SUCCEEDED(hr))
    {
        hr = g_pPlayer->SetMediaItem(pItem);
    }

    if (SUCCEEDED(hr))
    {
        hr = g_pPlayer->Play();
    }

    SafeRelease(&pItem);
```



In a typical application, you would provide a pointer to a callback interface in the [**MFPCreateMediaPlayer**](/windows/desktop/api/mfplay/nf-mfplay-mfpcreatemediaplayer) function, and use the callback interface to get events from the player. For simplicity, the code shown here skips these steps. For more information, see [Getting Started with MFPlay](getting-started-with-mfplay.md).

### Shutting Down

Before the application exits, shut down the media source and the player object as follows:

1.  Call [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown) on the media source.
2.  Call [**IMFPMediaPlayer::Shutdown**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-shutdown) on the player object.


```C++
    if (g_pSource)
    {
        g_pSource->Shutdown();
        g_pSource->Release();
        g_pSource = NULL;
    }

    if (g_pPlayer)
    {
        g_pPlayer->Shutdown();
        g_pPlayer->Release();
        g_pPlayer = NULL;
    }
```



## Requirements

MFPlay requires Windows 7.

## Related topics

<dl> <dt>

[MFPlay](using-mfplay-for-audio-video-playback.md)
</dt> <dt>

[Video Capture](audio-video-capture.md)
</dt> </dl>

 

 



