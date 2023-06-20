---
title: Windows Media Download Packages (deprecated)
description: Windows Media Download Packages (deprecated)
ms.assetid: 'e2d55253-574e-4b18-8b69-2c7e2f6ef9c4'
keywords:
- Windows Media metafiles,Windows Media Download packages
- Windows Media Player,Windows Media Download packages
- metafiles,Windows Media Download packages
- Windows Media,Windows Media Download packages
- Windows Media Download packages,about
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Windows Media Download Packages (deprecated)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.

Windows Media Download packages combine Windows Media Player borders, playlist information, and multimedia content in a single downloadable file with a .wmd file name extension. A Windows Media Download package could include an entire album of music videos that also displays advertising in the form of graphical branding and links to an online music retailer website.

Users can download a Windows Media Download package from a website simply by clicking a link. Once the package is downloaded to the user's computer, Windows Media Player extracts the files inside the package automatically, then adds the packaged playlist to the playlists drop-down box, adds the content to the library, displays the border skin in the **Now Playing** pane of the full mode Windows Media Player, and then plays the initial item in the playlist.

Windows Media Download packages provide the following benefits:

-   A single-click downloads, extracts, and catalogues multiple files to the user's computer.
-   Content plays immediately after being downloaded.
-   Customized borders can display advertising and branding information.
-   Packaged playlists are cataloged in the library.
-   Web site redirection can occur from within Windows Media Player to a related site.
-   A variety of interactive border controls are available.
-   Multiple audio and video file types are supported for packaging.

All of these benefits can be used together. For example, a single Windows Media Download package could give users the opportunity to view the lyrics to songs as they play, display a video that accompanies the songs, view advertising information about the record distributor, view album cover art, visit a fan website, and catalog the content in the library.

The following sections provide concepts to help you understand and create Windows Media Download packages.



| Section                                                                                                                               | Description                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [How Windows Media Download Packages Work (deprecated)](how-windows-media-download-packages-work--deprecated.md)                     | Provides an overview of how a Windows Media Download file is packaged, posted to a website, downloaded, and played by Windows Media Player. |
| [Using Borders in Windows Media Download Packages (deprecated)](using-borders-in-windows-media-download-packages--deprecated.md)     | Introduces borders and explains how a border is created.                                                                                    |
| [Using Playlists in Windows Media Download Packages (deprecated)](using-playlists-in-windows-media-download-packages--deprecated.md) | Describes how a metafile playlist file is used in a Windows Media Download package, and provides sample code.                               |
| [Creating a Windows Media Download Package (deprecated)](creating-a-windows-media-download-package--deprecated.md)                   | Describes the process of putting a package together for distribution.                                                                       |



 

## Related topics

<dl> <dt>

[**About Windows Media Metafiles**](about-windows-media-metafiles.md)
</dt> <dt>

[**Borders for Windows Media Player (deprecated)**](borders-for-windows-media-player--deprecated.md)
</dt> </dl>

 

 




