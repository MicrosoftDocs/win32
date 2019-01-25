---
title: An Example Radio Station Playlist
description: An Example Radio Station Playlist
ms.assetid: 99b33036-6391-446c-816c-8d5d76107d37
keywords:
- Windows Media metafile playlists,playlist examples
- playlists,playlist examples
- metafile playlists,playlist examples
- Windows Media metafile playlists,example playlists
- playlists,example playlists
- metafile playlists,example playlists
- Windows Media metafile playlists,sample playlists
- playlists,sample playlists
- metafile playlists,sample playlists
- Windows Media metafile playlists,code example
- playlists,code example
- metafile playlists,code example
- Windows Media metafile playlists,radio station playlist example
- playlists,radio station playlist example
- metafile playlists,radio station playlist example
- Windows Media Player,playlist examples
- Windows Media Player,example playlists
- Windows Media Player,sample playlists
- Windows Media Player,radio station playlist example
- playlist examples
- example playlists
- sample playlists
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# An Example Radio Station Playlist

The following example code illustrates how to create a playlist to scan three rock radio stations. The fictitious company Adventure Works Radio brand is on the playlist and on all of the individual streams within the playlist. When you write your code, change all URLs and file names to valid file names that are accessible to your Windows Media Player.

A playlist is created for each of the stations. A fourth playlist scans through the first three. The playlists are created to reference dynamically generated advertisements and have Adventure Works Radio branding.

One of the playlists representing a radio station might look like this.


```XML
<ASX version = "3.0">
    <TITLE>Adventure Works Radio</TITLE>
    <MOREINFO href = "https://www.adventure-works.com" />
    <ENTRY clientSkip = "no" skipIfRef = "yes">
       <REF href = "https://www.adventure-works.com/ad.asp/" />
    </ENTRY>
    <ENTRY>
        <TITLE>MyWRCK Radio</TITLE>
        <ABSTRACT>MyTown's Best Rock 'n Roll</ABSTRACT>
        <COPYRIGHT>2000 RadioNetwork</COPYRIGHT>
        <MOREINFO href = "https://www.adventure-works.com" />
        <REF href = "https://www.adventure-works.com" />
        <REF href = "https://backup.adventure-works.com" />
    </ENTRY>
</ASX>

```



The playlist can then be constructed of references to the individual playlists.

Example Code


```XML
<ASX Version = "3.0">
    <TITLE>Adventure Works Radio Top 3 Rock Stations</TITLE>
    <MOREINFO href = "https://www.adventure-works.com/MyTop3Rocks"/>
    <REPEAT>
        <ENTRY ClientSkip = "no">
            <REF HREF = "https://www.adventure-works.com/ad.asp/">
        </ENTRY>
        <DURATION VALUE="00:00:30" />
        <ENTRYREF  HREF = "https://www.adventure-works.com/asx/RadioNetwork.wax"/>
        <DURATION VALUE="00:00:30" />
        <ENTRYREF HREF = "https://www.adventure-works.com/asx/RadioNetwork2.wax/>
        <DURATION VALUE="00:00:30" />
        <ENTRYREF HREF = "https://www.adventure-works.com/asx/RadioNetwork3.wax"/>
    </REPEAT>
</ASX>

```



This example would play an ad followed by 30 seconds of each of the three stations referenced, one after the other. This cycle will repeat indefinitely because the **COUNT** attribute of the **REPEAT** element is not defined.

-   The example companies, organizations, products, people and events depicted herein are fictitious. No association with any real company, organization, product, person or event is intended or should be inferred.

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Example Playlists**](example-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




