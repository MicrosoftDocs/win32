---
Description: Important  Deprecated.
ms.assetid: bb71e792-d09c-4338-9cf4-4854e14042f9
title: MFPlayer2 Sample
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

-   [**IAudioSessionControl**](coreaudio.iaudiosessioncontrol)
-   [**IAudioSessionManager**](coreaudio.iaudiosessionmanager)
-   [**IMFPMediaItem**](/windows/win32/mfplay/nn-mfplay-imfpmediaitem?branch=master)
-   [**IMFPMediaPlayer**](/windows/win32/mfplay/nn-mfplay-imfpmediaplayer?branch=master)
-   [**IMFPMediaPlayerCallback**](/windows/win32/mfplay/nn-mfplay-imfpmediaplayercallback?branch=master)
-   [**IMMDevice**](coreaudio.immdevice)
-   [**IMMDeviceEnumerator**](coreaudio.immdeviceenumerator)
-   [**ISimpleAudioVolume**](coreaudio.isimpleaudiovolume)

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

 

 



