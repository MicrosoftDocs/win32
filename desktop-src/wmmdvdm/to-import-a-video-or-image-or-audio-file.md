---
title: To Import a Video or Image or Audio File
description: To Import a Video or Image or Audio File
ms.assetid: '7c09c9bd-6b9f-45dd-8dc8-c85c65df60e2'
keywords: ["Windows Movie Maker,importing media files", "Movie Maker,importing media files", "programming reference,importing media files", "reference for Windows Movie Maker,importing media files", "command-line options for Windows Movie Maker,importing media files", "importing media files"]
---

# To Import a Video or Image or Audio File

This option specifies the path of a media file to import.

**Syntax**


```C++
moviemk 
mediafile
```



**Parameters**

*mediafile*

Specifies the path of a video, image, or audio file to import into Windows Movie Maker.

**Examples**


```C++
moviemk C:\Users\johnevans\Pictures\cake.jpg
moviemk C:\Users\chrismeyer\applause.wav
```



## Remarks

For the specified media file to be imported into Windows Movie Maker, it must be one of the file types supported by Windows Movie Maker. For a list of supported file types, see the topic "Supported File Types" in the Windows Movie Maker Help documentation. If the specified media file is an audio or video file, it must be renderable by DirectShow to uncompressed video or audio, and DirectShow must indicate that the file supports seeking.

## Related topics

<dl> <dt>

[**Command-line Options for Windows Movie Maker**](command-line-options-for-windows-movie-maker.md)
</dt> </dl>

 

 




