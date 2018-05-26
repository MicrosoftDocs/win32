---
title: Web Streams
description: Web Streams
ms.assetid: 1eeb6243-5095-4dba-994c-2083beda7b78
keywords:
- Windows Media Format SDK,Web streams
- Advanced Systems Format (ASF),Web streams
- ASF (Advanced Systems Format),Web streams
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- Web streams,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Web Streams

A Web stream is like a file stream in that it contains data files. In a Web stream, these files are typically HTML pages and associated graphics in GIF or JPEG format.

Web streams can be particularly useful for ASF files that are used as presentations. Prior to the support of Web streams, presentations would have URLs in script streams within a file so that a Web page would load at a predetermined time. The difficulty was that network congestion could cause delays and create a poor viewing experience.

With Web streams, the constituent parts of Web pages can be included in the ASF file as a stream. As the files are received, they can be cached so that, when the command to display (or render) a URL is delivered, they can be instantly accessed by a browser. This enables smooth, consistent playback. The render command is delivered in the Web stream itself, not as a script command in a separate stream.

It is recommended that Web streams created by using the Windows Media Format 9 Series SDK, or later be given the version number 1. This value is specified in the [**WMT\_WEBSTREAM\_FORMAT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_webstream_format?branch=master) structure in the **wVersion** member. The SDK itself does nothing to enforce this version.

> [!Note]  
> When connecting to live broadcast streams that have Web streams, it is possible that the user may receive a render command before the specified file is actually in the local cache. Unless your application handles this condition, the browser will display a "Page not found" error.

 

## Related topics

<dl> <dt>

[**Arbitrary Streams**](arbitrary-streams.md)
</dt> <dt>

[**Configuring Web Streams**](configuring-web-streams.md)
</dt> </dl>

 

 




