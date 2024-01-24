---
title: MSWMExt Parameter (deprecated)
description: MSWMExt Parameter (deprecated)
ms.assetid: cc52da1a-26d1-4321-b421-b0d6f44635cc
keywords:
- Windows Media metafiles,MSWMExt parameter
- metafiles,MSWMExt parameter
- MSWMExt parameter
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# MSWMExt Parameter (deprecated)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




