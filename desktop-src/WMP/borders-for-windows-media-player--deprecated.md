---
title: Borders for Windows Media Player (deprecated)
description: Borders for Windows Media Player (deprecated)
ms.assetid: defa461b-ffa5-4fee-bed4-aba3e733b8c4
keywords:
- Windows Media Player,borders
- Windows Media Player skins,borders
- skins,borders
- borders,compared to skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Borders for Windows Media Player (deprecated)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.

A border is similar to a skin, but instead of replacing the user interface for the compact mode of Windows Media Player, a border is embedded in the Now Playing pane of the full mode Windows Media Player.

By using a Windows Media Download package, you can include content with a border, paving the way to multimedia applications.

A sample Windows Media Download package that includes a border and embedded content is included in the samples directory of this SDK.

## Creating a Border

A border is created the same way as a skin. The only difference is that the skin is embedded inside the **Now Playing** pane. This means that the skin size cannot be calculated and that all skin elements must be relative. If the user resizes Windows Media Player, portions of the border may be clipped off and not seen.

## Loading a Border

A border is loaded when a Windows Media metafile that uses the **SKIN** element is loaded. The **HREF** attribute of the **SKIN** element must reference a skin. A typical **SKIN** element would look like this:


```C++
<SKIN HREF="myborder.wmz">

```



For more information, see [SKIN Element (deprecated)](skin-element--deprecated.md).

## Including Content with a Border

You can include content with a border by using a Windows Media Download file (with a .wmd file name extension). Follow these steps:

1.  Create the border. Take care to create it in such a way that resizing will not ruin the composition of the border. For example, do not include a background file; make the background transparent so that a visualization could run behind it.
2.  Compress the skin contents (art, JScript files, and skin definition file) into a file with a .wmz file name extension.
3.  Create a Windows Media metafile (with an .asx file name extension) that references the compressed border file (with a .wmz file name extension). The metafile can include playlist information with metadata for art and URLs for specific content.
4.  Assemble the digital media content.
5.  Compress the border, metafile, and content into one file and give it a .wmd file name extension.

## Using a Border

After you have created the Windows Media Download file, all that the user has to do is double-click on it. The file will be downloaded to the user's computer. The files inside the package will be unpacked, the playlist will be added to the playlists, the border will appear in the **Now Playing** pane of the full mode Windows Media Player, and the first item on the new playlist will begin playing.

## Related topics

<dl> <dt>

[**About Skins**](about-skins.md)
</dt> <dt>

[**Samples**](samples.md)
</dt> <dt>

[**Windows Media Download Packages (deprecated)**](windows-media-download-packages--deprecated.md)
</dt> </dl>

 

 




