---
title: Managing Media Items
description: Managing Media Items
ms.assetid: fba1df60-d603-4e37-a021-8fa618144149
keywords:
- Windows Media Player,library
- Windows Media Player object model,library
- object model,library
- Windows Media Player Mobile,library for object model
- Windows Media Player ActiveX control,library for object model
- Windows Media Player Mobile ActiveX control,library for object model
- ActiveX control,library for object model
- Windows Media Player library,managing media items
- library,managing media items
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Managing Media Items

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A **Media** object represents one media item. It has properties and methods you can use to retrieve information and display it to the user, or to take different actions based on the value you retrieve.

Much of your work with **Media** objects involves metadata about the content of the media item, called the attributes. The topic [Media Item Attributes](media-item-attributes.md) describes how to read and change attribute values. In addition to this topic, see the [Windows Media Metadata Usage Guidelines](/previous-versions/ms867702(v=msdn.10)) on the Microsoft website for more information about the attributes and their use.

The **Media** object has properties and methods that retrieve some attributes directly, such as the name or duration of the item. For video items, you can retrieve the height and width of the image, and you can retrieve marker information based on the name or index of a marker. You can also determine whether a particular media item is included in a particular playlist.

## Retrieving a Media Object

You can quickly access the current media item by using the *Player*.**currentMedia** property.

Throughout this topic, the **Player** object was defined in the following manner:


```C++
AxWMPLib.AxWindowsMediaPlayer Player;
using WMPLib;

```



The following C# example retrieves a **Media** object representing the current item.


```C++
IWMPMedia media;
media = Player.currentMedia;

```



You can create a new media item from a digital media file by using the *Player*.**newMedia** method. You pass the method the URL path to a digital media file, and it returns a reference to the new **Media** object. The method does not add the new object to the library directly. However, you can pass the object to the *Playlist*.**appendItem** method or the *Playlist*.**insertItem** method.

The following C# example creates a **Media** object based on one of the digital media samples installed with the Windows Media Player SDK.


```C++
IWMPMedia media;
media = Player.newMedia("C:\\WMSDK\\WMPSDK10\\samples\\media\\laure.wma");

```



> [!Note]  
> You must include two backslash (\\) characters (or use the @ character in C#) in a string to represent one actual backslash character. This is because C# uses a single backslash character to define an escape sequence.

 

You can create a new media item from a digital media file and add it to the library in one step by using the *MediaCollection*.**add** method. Like the *Player*.**newMedia** method, the **add** method takes a path to a digital media file.

The following C# example creates a **Media** object based on one of the SDK sample files and adds that object to the library.


```C++
IWMPMedia media;
media = Player.mediaCollection.add("C:\\WMSDK\\WMPSDK10\\samples\\media\\laure.wma");

```



You can retrieve a **Media** object representing a media item in a playlist by using the *Playlist*.**item** method. The following C# example retrieves the sixth media item from the current playlist.


```C++
IWMPMedia media;
media = Player.currentPlaylist.get_Item(5);

```



## Related topics

<dl> <dt>

[**Controls.currentItem**](controls-currentitem.md)
</dt> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**MediaCollection.add**](mediacollection-add.md)
</dt> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Player.newMedia**](player-newmedia.md)
</dt> <dt>

[**Playlist.item**](playlist-item.md)
</dt> <dt>

[**Working with the Library**](working-with-the-library.md)
</dt> </dl>

 

 




