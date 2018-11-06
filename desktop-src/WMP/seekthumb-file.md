---
title: SeekThumb File
description: SeekThumb File
ms.assetid: 757aeb93-ebf0-4659-8cb0-686e54485ac4
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,SeekThumbd files
- Windows Media Player Mobile skins,SeekThumb files
- skins,SeekThumb files
- SeekThumb files in skins
- thumb,SeekThumb files
ms.topic: article
ms.date: 05/31/2018
---

# SeekThumb File

The SeekThumb file defines the image that indicates the playback location within the media item for a Seek trackbar. You can use one file and define it for use by both SeekThumb and VolumeThumb. Unlike the other art files, the thumb files are defined in the Trackbars section of the skin definition file.

The following image is a typical SeekThumb file.

![seekthumb file](images/cesdksee.gif)

These two button files look the same but are slightly different sizes. The left image is the normal view that the user sees, and the right image is the Pushed image the user sees when they tap on the button.

> [!Note]  
> SeekThumb art files created for skins used in Windows Media Player 10 Mobile or later must have the following three images (from left to right): normal, pushed, and disabled.

 

You may want to make certain areas of the thumb images transparent. This will allow you to create thumb images in shapes other than rectangular. Any region of a thumb image that you fill with the color specified by the RGB value 255, 0, 255 will appear transparent in your skin.

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




