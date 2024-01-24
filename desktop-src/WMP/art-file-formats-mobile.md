---
title: Art File Formats (Mobile)
description: Learn about the art file formats that Mobile recognizes for skins. These include bitmap, GIF, JPEG, and PNG.
ms.assetid: c20a8eeb-6a13-4631-bb20-df03c4a4a1d2
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,file formats
- Windows Media Player Mobile skins,file formats for art
- skins,file formats for art
- file formats for skin art
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Art File Formats (Mobile)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Art files for skins may be either bitmap (.bmp) or GIF (.gif) images. JPEG (.jpg) and PNG (.png) images are also supported. Do not include any spaces or commas in your art file name.

If you are synchronizing files to a portable device, be sure that the synchronization does not change the file name extension or convert the image files to another format.

Many drawing programs can be used to create bitmaps and GIF files, or to convert art in other formats to bitmaps or GIF files. For example, you can use Microsoft Paint, which comes with Microsoft Windows, for simple drawings.

You will want to trim the blank areas of your images around the edges to reduce file size. You can use the offsets in the Bitmaps section to compensate for removing blank spaces on the left and top sides. You can also trim the bottom and right blank edges of the images because they are not needed for measurements. The only files you should not trim are the Background, SeekThumb, and VolumeThumb images.

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




