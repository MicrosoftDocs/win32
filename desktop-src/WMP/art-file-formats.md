---
title: Art File Formats
description: Learn about the art file formats that Windows Media Player recognizes for skins. These include bitmap, GIF, JPEG, and PNG.
ms.assetid: 803479e8-0e00-4724-80b7-9d86709c43db
keywords:
- Windows Media Player skins,art files
- skins,art files
- files for skins,art
- art files for skins,file formats
- Windows Media Player skins,file formats for art
- skins,file formats for art
- file formats for skin art
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Art File Formats

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following art file formats are recognized by Windows Media Player for skins:



| Format                                  | Extension   | Description                                                                                        |
|-----------------------------------------|-------------|----------------------------------------------------------------------------------------------------|
| Bitmap                                  | .bmp        | Bitmap images are recommended because they offer the most control over the exact image and colors. |
| Graphics Interchange Format (GIF)       | .gif        | Compressed image format used for webpages. Animated GIFs are supported.                            |
| Joint Photographic Experts Group (JPEG) | .jpeg, .jpg | Compressed image format used for webpages.                                                         |
| Portable Network Graphics (PNG)         | .png        | Compressed image format used for webpages.                                                         |



 

If you use one of the compressed file formats that defines a color as transparent to a Web browser, do not define a color as transparent in the image file. Use a visible color to represent transparent areas in your image, and then define that color as transparent in the skin definition file. For example, if you create a GIF file with some areas transparent, they will not be transparent in your final image and you will not be able to use the color you set as transparent in your gif file for the transparency color in your skin.

## Related topics

<dl> <dt>

[**Art Files**](art-files.md)
</dt> </dl>

 

 




