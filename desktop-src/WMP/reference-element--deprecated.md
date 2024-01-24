---
title: reference Element (deprecated)
description: reference Element (deprecated)
ms.assetid: 0a549750-abaa-43bf-8420-8fe00eb6feff
keywords:
- Windows Media metafiles,reference element
- metafiles,reference element
- reference element
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# reference Element (deprecated)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic documents a feature that is no longer used in the current version of Windows Media Metafiles.

The **reference** element contains a list of references to URLs. Each item in the list has the form Ref *XX* = *URL*, where *XX* is an integer and *URL* is the URL of an Advanced Systems Format (ASF) file.

**Syntax**


```XML
[reference]
RefXX = URL
RefXX = URL
   
<entity type="hellip"/>
```



The integers represented by *XX* must be in ascending order. That is, the integer in each line must be greater than the integer in the preceding line.

When a client program reads a reference element, it attempts to connect to the media file represented by the first URL in the list. If that fails, the client program attempts to connect to the file represented by the next URL in the list. The client program continues down the list until it makes a successful connection or reaches the end of the list. Note that if the client program makes a successful connection, it does not read any of the subsequent URLs in the list.

**Example Code**

In the following example, the client program would first attempt to connect to the file represented by the mms URL. If that failed, the client program would attempt to connect to the file represented by the http URL.


```XML
[reference]
Ref01 = mms://example.com/MusicFile.wma
Ref02 = https://example.com/MusicFile.wma

```



## Remarks

The ASF file format encompasses a wide variety of media types including audio and video. ASF files also use several different file name extensions, including .wma and .wmv.

The integers represented by *XX* must be in ascending order. That is, the integer in each line must be greater than the integer in the preceding line.

When a client program reads a reference element, it attempts to connect to the media file represented by the first URL in the list. If that fails, the client program attempts to connect to the file represented by the next URL in the list. The client program continues down the list until it makes a successful connection or reaches the end of the list. Note that if the client program makes a successful connection, it does not read any of the subsequent URLs in the list.

## Related topics

<dl> <dt>

[**Previous Versions of Windows Media Metafiles (deprecated)**](previous-versions-of-windows-media-metafiles--deprecated.md)
</dt> </dl>

 

 




