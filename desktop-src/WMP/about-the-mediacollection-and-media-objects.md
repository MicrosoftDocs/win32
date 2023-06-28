---
title: About the MediaCollection and Media Objects
description: About the MediaCollection and Media Objects
ms.assetid: e3260efd-44cc-4b4e-9f48-3441631bfa4f
keywords:
- Windows Media Player,MediaCollection object
- Windows Media Player object model,MediaCollection object
- object model,MediaCollection object
- Windows Media Player ActiveX control,MediaCollection object
- ActiveX control,MediaCollection object
- Windows Media Player Mobile ActiveX control,MediaCollection object
- Windows Media Player Mobile,MediaCollection object
- MediaCollection object
- Windows Media Player,Media object
- Windows Media Player object model,Media object
- object model,Media object
- Windows Media Player ActiveX control,Media object
- ActiveX control,Media object
- Windows Media Player Mobile ActiveX control,Media object
- Windows Media Player Mobile,Media object
- Media object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the MediaCollection and Media Objects

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **MediaCollection** and **Media** objects govern the media collection, which defines the locations of digital media files that Windows Media Player can access. You get the **MediaCollection** object from the **mediaCollection** property of the **Player** object. The **mediaCollection** property returns the **MediaCollection** object. You can only access the properties of the **MediaCollection** object after you have created it. For example, to add a **Media** object (a song), use the following code:


```C++
player.mediacollection.add('laure.wma');

```



You have added the file laure.wma to the media collection.

You can get the current **Media** object by using the **currentMedia** property of the **Player**. For example, this code gets the **duration** property of the current **Media** object:


```C++
myduration = player.currentmedia.duration;

```



There are many ways to get a **Media** object so that you can access its properties. For example, if you want to access the **duration** property of the current media, each of the following lines of code could be used.

To get the duration of the currently playing media:


```C++
player.currentMedia.duration;

```



To get the duration of the current media in a playlist:


```C++
player.controls.currentItem.duration;

```



To get the duration of the third media item in a playlist:


```C++
player.currentPlaylist.item(2).duration;

```



To get the duration of the third media item in a "Jazz" genre:


```C++
player.mediaCollection.getByGenre("jazz").item(2).duration;

```



To get the duration of the third media item in the second playlist:


```C++
player.playlistCollection.getAll.item(1).item(2).duration; 
```



## Related topics

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




