---
title: MSWMExt Parameter (deprecated)
description: MSWMExt Parameter (deprecated)
ms.assetid: cc52da1a-26d1-4321-b421-b0d6f44635cc
keywords:
- Windows Media metafiles,MSWMExt parameter
- metafiles,MSWMExt parameter
- MSWMExt parameter
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# MSWMExt Parameter (deprecated)

The *MSWMExt* parameter indicates to a client program the format of a referenced file.

**Syntax**


```XML

URL?MSWMExt=.
ext
```



**Example Code**


```XML
[reference]
Ref01 = https://example.com/GenerateASFFile.aspx?MSWMExt=.asf

```



## Remarks

Client programs sometimes use a file name extension or a MIME type to determine whether to render a media file as a stream, render the file after a full download, or refuse to render the file at all. If a client program cannot determine how to treat a media file based on the file name extension or the MIME type, it can determine how to treat the file by inspecting the *MSWMExt* parameter. For example, the client could treat the file as if it had an extension equal to the value of the *MSWMExt* parameter. For more information about MIME types and file name extensions, see [File Name Extensions](file-name-extensions.md).

## Related topics

<dl> <dt>

[**Previous Versions of Windows Media Metafiles (deprecated)**](previous-versions-of-windows-media-metafiles--deprecated.md)
</dt> </dl>

 

 




