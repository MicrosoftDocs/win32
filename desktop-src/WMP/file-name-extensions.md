---
title: File Name Extensions
description: File Name Extensions
ms.assetid: c17bf4e5-b469-45b6-bc22-2b451723d85e
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

# File Name Extensions

There are specific guidelines for the use of file name extensions for Windows Media metafiles. Windows Media metafile name extensions are used to identify the different types of Windows Media files. A file name extension provides an Independent Software Vendor (ISV) with information about the rendering requirements of an application that uses a particular extension, and enables content authors to target general types of media players.

The file name extension guidelines are listed in the following table. It is recommended that a file's MIME type, located in the file header, be used for file-type identification.



| File name extension | MIME type      | File content                                                                                                                                                                            |
|---------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .wma                | audio/x-ms-wma | Windows Media file with audio content only. Typically used to download and play files or to stream content.                                                                             |
| .wmv                | video/x-ms-wmv | Windows Media file with audio and/or video content. Typically used to download and play files or to stream content.                                                                     |
| .asf                | video/x-ms-asf | Legacy content. Typically used to download and play files or to stream content. May contain audio and/or video content. Typically used to download and play files or to stream content. |
| .wm                 | video/x-ms-wm  | Reserved                                                                                                                                                                                |
| .wax                | audio/x-ms-wax | Metafiles that reference Windows Media files with .asf, .wma, or .wax file name extensions.                                                                                             |
| .wvx                | video/x-ms-wvx | Metafiles that reference Windows Media files with .wma, .wmv, .wvx, or .wax file name extensions.                                                                                       |
| .asx                | video/x-ms-asf | Metafiles that reference Windows Media files with .wma, .wax, .wmv, .wvx, .asf, or .asx file name extensions.                                                                           |
| .wmx                | video/x-ms-wvx | Reserved.                                                                                                                                                                               |



 

## Remarks

Scripting and digital rights management (DRM) must be supported by any application that renders Windows Media files.

## Related topics

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 




