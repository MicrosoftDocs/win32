---
Description: Important  Deprecated.
ms.assetid: bb71e792-d09c-4338-9cf4-4854e14042f9
title: MFPlayer2 Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPlayer2 Sample

> \[!Important\]  
> Deprecated. This API may be removed from future releases of Windows. Applications should use the [Media Session](media-session.md) for playback.

 

Demonstrates some of the playback features that are omitted from the [SimplePlay](simpleplay-sample.md) sample, such as:

-   Seeking
-   Rate control (fast forward and rewind)
-   Audio volume and mute controls
-   Video zoom

The following image shows the controls used for these features.

![screen shot of the mfplayer sample ](images/mfplayer2.png)

## APIs Demonstrated

This sample demonstrates the following APIs.

-   [**IAudioSessionControl**](https://msdn.microsoft.com/en-us/library/Dd368246(v=VS.85).aspx)
-   [**IAudioSessionManager**](https://msdn.microsoft.com/en-us/library/Dd370948(v=VS.85).aspx)
-   [**IMFPMediaItem**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaitem)
-   [**IMFPMediaPlayer**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayer)
-   [**IMFPMediaPlayerCallback**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayercallback)
-   [**IMMDevice**](https://msdn.microsoft.com/en-us/library/Dd371395(v=VS.85).aspx)
-   [**IMMDeviceEnumerator**](https://msdn.microsoft.com/en-us/library/Dd371399(v=VS.85).aspx)
-   [**ISimpleAudioVolume**](https://msdn.microsoft.com/en-us/library/Dd316531(v=VS.85).aspx)

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/MFPlayer2).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Using MFPlay for Audio/Video Playback](using-mfplay-for-audio-video-playback.md)
</dt> </dl>

 

 



