---
title: Accessing the Library Programmatically
description: Accessing the Library Programmatically
ms.assetid: f48fbb49-5b79-4a78-af72-8509c460a149
keywords:
- Windows Media Player,library
- Windows Media Player object model,library
- object model,library
- Windows Media Player ActiveX control,library for object model
- ActiveX control,library for object model
- Windows Media Player Mobile ActiveX control,library for object model
- Windows Media Player Mobile,library for object model
- Windows Media Player library,accessing programmatically
- library,accessing
- accessing Windows Media Player library programmatically
- Windows Media Player library,adding media items
- library,adding media items
- Windows Media Player library,retrieving media items
- library,retrieving media items
- Windows Media Player library,removing media items
- library,removing media items
- adding media items to Windows Media Player library
- retrieving media items from Windows Media Player library
- removing media items from Windows Media Player library
- retrieving metadata
- Windows Media Player library,retrieving metadata from media items
- library,retrieving metadata from media items
- metadata,retrieving
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Accessing the Library Programmatically

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In code, the library is represented by the **MediaCollection** object (or the **IWMPMediaCollection** interface). Media items are represented as **Media** objects (or by the **IWMPMedia** interface). Playlist items are represented as **Playlist** objects (or by the **IWMPPlaylist** interface). For simplicity, this section will simply refer to object names, when possible.

By using the **MediaCollection** object, you can work with media items and playlists. The library also exposes the **PlaylistCollection** object (or the **IWMPPlaylistCollection** interface), which provides some functionality specific to working with playlists. Most of the time, the **MediaCollection** object will provide you with the functionality you need, even when working with playlists. For more information about working with media items, see [Managing Media Items](managing-media-items.md). For more information about working with playlists, see [Managing Playlists](managing-playlists.md).

## Adding Media Items to the Library

Adding digital media content to the library is straightforward. Simply call the [MediaCollection.add](mediacollection-add.md) method, providing the path to the media file as an argument.

## Retrieving Media Items from the Library

When you retrieve media items from the library, what you really retrieve is a playlist. Even if you expect to retrieve only one media item, you will get a **Playlist** object containing a single item, which will be associated with index zero. For example, if you want to retrieve a **Media** object that represents the song named "Jeanne", you could use the following JScript code:


```C++
// Retrieve media named Jeanne from the library.
var playlist = player.mediaCollection.getByName("Jeanne");

```



The preceding code retrieves a playlist containing all the media items having the name "Jeanne" as the title. For this example, assume that you know there is only one song by that name in the library (note that the library supports multiple songs having the same name). This means you could expect the count of items in the playlist you retrieved to equal one and the media item would be represented by index zero. The following example code continues the previous example to demonstrate how you would retrieve the media item from the playlist by using the [Playlist.item](playlist-item.md) method.


```C++
// Retrieve the individual media item from the playlist.
var media = playlist.item(0);

```



For more information about retrieving media items from playlists, see [Playlists and Media Items](playlists-and-media-items.md) in the [Player Control Guide](player-control-guide.md).

## Retrieving Metadata from a Media Item

After you retrieve a **Media** object, you can read the attribute values associated with the content. In the simplest case, you might simply want to know a single value, such as the name of the artist who performed a music track. The following JScript example shows how to use the [Media.getItemInfo](media-getiteminfo.md) method to retrieve the name of the artist from the media retrieved in the previous example:


```C++
// Retrieve the artist name string.
var author = media.getItemInfo("Artist");

```



A media item can have many different attributes, and working with metadata is not always as straightforward as the simple case shown in the previous example. For instance, some attributes can contain multiple values or have values in more than one language. For more information about working with metadata, see [Media Item Attributes](media-item-attributes.md). For more information about the various attributes, their meanings, and file type support, see the [Attribute Reference](attribute-reference.md).

## Removing Media Items from the Library

Removing digital media content from the library is also straightforward. Simply call **MediaCollection.remove**, providing the **Media** object that represents the item as the first argument and the value **true** as the second. The following JScript example removes the file named Jeanne (retrieved in the previous example) from the library:


```C++
// Remove Jeanne from the library.
playst.mediaCollection.remove(media, true);

```



## Related topics

<dl> <dt>

[**About the Library**](about-the-library.md)
</dt> <dt>

[**About the MediaCollection and Media Objects**](about-the-mediacollection-and-media-objects.md)
</dt> <dt>

[**About the Playlist, PlaylistCollection, and PlaylistArray Objects**](about-the-playlist--playlistcollection--and-playlistarray-objects.md)
</dt> <dt>

[**Working with the Library**](working-with-the-library.md)
</dt> </dl>

 

 




