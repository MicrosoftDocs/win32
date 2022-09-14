---
title: Using URL and Server Rollover
description: Using URL and Server Rollover
ms.assetid: d0d15b1c-5631-486e-8490-b85ec51bd355
keywords:
- Windows Media metafile playlists,URL rollovers
- playlists,URL rollovers
- metafile playlists,URL rollovers
- Windows Media metafile playlists,server rollovers
- playlists,server rollovers
- metafile playlists,server rollovers
- Windows Media metafile playlists,protocol rollovers
- playlists,protocol rollovers
- metafile playlists,protocol rollovers
- Windows Media Player,URL rollovers
- Windows Media Player,server rollovers
- Windows Media Player,protocol rollovers
- URL rollovers
- server rollovers
- protocol rollovers
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using URL and Server Rollover

You can use metafile playlists to provide a means of automatically rolling over to alternate content sources when a stream cannot be accessed or played. You can use this rollover method to specify sources of the same content on different servers or different types of servers. You can, for example, specify a first alternate on a different Windows Media server. If that content fails to play, the client can roll over to a second alternate on a web server. Windows Media Player automatically tries to roll over to different protocols according to its Windows Media property settings before trying the rollover URLs in the playlist.

Set server and protocol rollover by placing multiple **REF** elements in succession within one **ENTRY** element. Each **REF** element specifies an alternate location or protocol for a media file or stream.

Example Code


```XML
<!--Server and protocol rollover is set for the file Rollover.wma.-->
<ASX version="3.0">
    <TITLE>MyServer Rollover</TITLE>
   <ENTRY>
      <REF HREF="mms://Server1.proseware.com/Path/Rollover.wma"/>
      <REF HREF="mms://Server2.proseware.com/Path/Rollover.wma"/>
      <REF HREF="mms://Server3.proseware.com/Path/Rollover.wma"/>
      <REF HREF="https://www.proseware.com/Path/Rollover.wma"/>
   </ENTRY>
</ASX>

```



## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> </dl>

 

 




