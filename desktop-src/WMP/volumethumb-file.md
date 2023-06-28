---
title: VolumeThumb File
description: VolumeThumb File
ms.assetid: 'de6abfed-a811-44c4-8db2-f3b55ea38756'
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,VolumeThumb files
- Windows Media Player Mobile skins,VolumeThumb files
- skins,VolumeThumb files
- VolumeThumb files in skins
- thumb,VolumeThumb files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VolumeThumb File

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The VolumeThumb file defines the image that indicates the playback volume level for a Volume trackbar. You can use one file and define it for use by both SeekThumb and VolumeThumb. Unlike the other art files, the thumb files are defined in the Trackbars section of the skin definition file.

The following image is a typical VolumeThumb file.

![volumethumb file](images/cesdkvol.png)

These two button files look the same but are slightly different sizes. The left image is the normal view that the user sees, and the right image is the Pushed image the user sees when they tap on the button.

You may want to make certain areas of the thumb images transparent. This will allow you to create thumb images in shapes other than rectangular. Any region of a thumb image that you fill with the color specified by the RGB value 255, 0, 255 will appear transparent in your skin.

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




