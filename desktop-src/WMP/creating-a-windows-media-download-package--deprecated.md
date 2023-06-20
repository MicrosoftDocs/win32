---
title: Creating a Windows Media Download Package (deprecated)
description: Creating a Windows Media Download Package (deprecated)
ms.assetid: 95d6a214-9da6-496d-ba40-4476814b1d5a
keywords:
- Windows Media metafiles,Windows Media Download packages
- Windows Media Player,Windows Media Download packages
- metafiles,Windows Media Download packages
- Windows Media,Windows Media Download packages
- Windows Media Download packages,creating
- creating Windows Media Download packages
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Creating a Windows Media Download Package (deprecated)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.

Follow these steps to create a Windows Media Download package.

1.  **Create a border.** Use the same techniques you would use to build a skin for Windows Media Player. Design the border so that resizing Windows Media Player will not ruin the composition of the border elements. For instance, use a solid color or visualization as a background because these will scale well as Windows Media Player is resized.
2.  **Compress the border contents.** Create a compressed folder (with a .zip file name extension) that contains the border files: images, JScript files, and the skin definition file with a .wms file name extension. Rename the compressed file so that it has a .wmz file name extension.
3.  **Write a Windows Media metafile.** Windows Media Player will not load the border unless you create a Windows Media metafile with an .asx file name extension that implements the **SKIN** element. The metafile can also be used to create a playlist that describes the content included in the package.
4.  **Assemble your content.** Put all the files that you want to use into a folder. This includes audio files, video files, metafiles, and border definition files.
5.  **Create the package.** Create a compressed folder (with a .zip file name extension) that contains the border file, content files, and the metafile. Change the file name extension of this .zip file to a .wmd file name extension.
6.  **Post the package to a website.** The completed package is ready to be posted to a website and downloaded by users.

## Related topics

<dl> <dt>

[**Windows Media Download Packages (deprecated)**](windows-media-download-packages--deprecated.md)
</dt> </dl>

 

 




