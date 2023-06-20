---
title: Metafile Extension Guidelines
description: Metafile Extension Guidelines
ms.assetid: 079fac31-7a6f-4775-a337-870ad25a56a0
keywords:
- Windows Media metafiles,extensions
- Windows Media metafiles,file name extensions
- metafiles,extensions
- metafiles,file name extensions
- Windows Media,metafiles
- file name extensions for Windows Media metafiles
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Metafile Extension Guidelines

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A file name extension provides an independent software vendor (ISV) with information about the rendering requirements of an application that uses the extension, and enables content authors to target general types of players.

Windows Media metafile name extensions are used to identify the format of the Windows Media files that a metafile references. Windows Media metafiles with .wax, .wvx, or .asx extensions reference files with .wma, .wmv, and .asf extensions, respectively. All metafiles, regardless of the file name extension used, have the **ASX** element tag at the beginning of the file with the **version** attribute specified.

The following table shows the media file types referenced by each type of metafile file name extension. The columns list media file name extensions, the rows list metafile name extensions. An X in a column indicates a media file type that can be referenced by a particular metafile file name extension.



| Extension | .asf | .wma | .wmv |
|-----------|------|------|------|
| .wvx      | X    | X    | X    |
| .wax      | X    | X    |      |
| .asx      | X    |      |      |



 

## Related topics

<dl> <dt>

[**File Name Extensions**](file-name-extensions.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




