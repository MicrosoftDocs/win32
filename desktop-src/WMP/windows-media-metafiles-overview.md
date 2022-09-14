---
title: Windows Media Metafiles Overview
description: Windows Media Metafiles Overview
ms.assetid: 5b7742c0-f416-4bf4-ae03-9554b51fe620
keywords:
- Windows Media metafiles,about
- Windows Media Player,metafiles
- Windows Media Player,Windows Media metafiles
- metafiles,about
- Windows Media,metafiles
- Windows Media metafile playlists,about
- playlists,about
- Windows Media metafiles,syntax
- metafiles,syntax
- metafile playlists,about
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Windows Media Metafiles Overview

The most important part of successfully using Windows Media metafiles is using the correct syntax for the metafile elements. Syntax errors in a Windows Media metafile can cause anything from a single attribute being overlooked, to the metafile not being recognized as valid and failing to work.

Almost as important is the order in which the elements appear in a Windows Media metafile. The attributes of some elements temporarily override the attributes of similar elements in different sections of the metafile. There is a defined [Order of Precedence](order-of-precedence.md).

Windows Media metafile playlists are Windows Media metafiles that provide information that Windows Media Player uses to receive unicast streams, multicast streams, and other supported media from an intranet or the Internet. A metafile playlist is basically a shortcut to media content. A metafile playlist can be sent as email, used as a link reference on a webpage, created dynamically using Active Server Pages (ASP), or exist as a stand-alone file on a local disk drive. A metafile playlist can reference another metafile playlist, an ASP page, or a Windows Media station file (with an .nsc file name extension). An .nsc file is used to define a Windows Media station to Windows Media Player. The basic handling process is the same for each case.

## Related topics

<dl> <dt>

[**About Windows Media Metafiles**](about-windows-media-metafiles.md)
</dt> </dl>

 

 




