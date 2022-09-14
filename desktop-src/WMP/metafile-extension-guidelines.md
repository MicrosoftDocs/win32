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
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Metafile Extension Guidelines

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

 

 




