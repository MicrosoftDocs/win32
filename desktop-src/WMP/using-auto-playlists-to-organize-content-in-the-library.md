---
title: Using Auto Playlists to Organize Content in the Library
description: Using Auto Playlists to Organize Content in the Library
ms.assetid: 118d4357-044f-4986-af51-0c344470e891
keywords:
- Windows Media Player online stores,auto playlists
- online stores,auto playlists
- type 1 online stores,auto playlists
- type 2 online stores,auto playlists
- Windows Media Player online stores,organizing library content
- online stores,organizing library content
- type 1 online stores,organizing library content
- type 2 online stores,organizing library content
- Windows Media Player online stores,library content organizing
- online stores,library content organizing
- type 1 online stores,library content organizing
- type 2 online stores,library content organizing
- library,organizing content
- organizing library content
- auto playlists
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Auto Playlists to Organize Content in the Library

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use auto playlists to organize premium content you provide. For example, you could use Windows Media Player to create an auto playlist that contains only content you provided having a user rating of at least four stars. You can then add the auto playlist to the library in Windows Media Player so that it displays in the Purchased Music node under your content distributor node.

To do this, follow these steps:

1.  Create the auto playlist.
2.  Using Windows Explorer, browse to the auto playlist and retrieve the .wpl file.
3.  Using the Windows Media Player object model, add the auto playlist to the library.
4.  Set the **WM/ContentDistributor** attribute for the playlist to your content distributor key name.
5.  Set the **SyncOnly** attribute for the playlist to true.

The following JScript example code shows a function that adds an auto playlist named "Favorite Hits" to the Proseware node in the library:


```C++
function AddWPL()
{
    var pl = Player.mediaCollection.add("c:\\media\\Favorite Hits.wpl");
    pl.setItemInfo("WM/ContentDistributor", "Proseware");
    pl.setItemInfo("SyncOnly", true);
}
```



## Related topics

<dl> <dt>

[About Library Integration](download-manager-overview.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**MediaCollection.add**](mediacollection-add.md)
</dt> <dt>

[**Playlist.setItemInfo**](playlist-setiteminfo.md)
</dt> <dt>

[**Static and Auto Playlists**](static-and-auto-playlists.md)
</dt> <dt>

[**SyncOnly Attribute**](synconly-attribute.md)
</dt> <dt>

[**WM/ContentDistributor Attribute**](wm-contentdistributor-attribute.md)
</dt> <dt>

[**Working with the Library**](working-with-the-library.md)
</dt> </dl>

 

 




