---
title: Using the Windows Media Player 7 or Later Object Model
description: Using the Windows Media Player 7 or Later Object Model
ms.assetid: e2dbe2c1-23be-499b-b754-b7e87486ecd6
keywords:
- Windows Media Player,object model
- Windows Media Player object model,version 7 or later
- object model,version 7 or later
- Windows Media Player ActiveX control,version 7 or later
- ActiveX control,version 7 or later
- Windows Media Player Mobile ActiveX control,version 7 or later
- Windows Media Player Mobile,object model
- migration guide,version 7 or later
- versions of Windows Media Player,object model
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Windows Media Player 7 or Later Object Model

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Most of the tasks you may have been performing using the Windows Media Player 6.4 ActiveX control object model will require a new approach. In many cases, the names of the properties, methods, and events have changed in the Windows Media Player 7 or later object model. For instance, to specify the file path in the version 6.4 object model, you set the **Player6.FileName** property:


```C++
WMP64.FileName = "https://www.microsoft.com/somefile.wmv";

```



When using the Windows Media Player 7 or later object model, you must set the **Player.URL** property:


```C++
WMP9.URL = "https://www.microsoft.com/somefile.wmv";

```



Alternatively, using the 10 object model, you can obtain a **Media** object from the library, and then set the **Player.currentMedia** property:


```C++
// Get the first media object in the media collection.
var MyMediaItem = WMP9.mediaCollection.getAll().item(0)

// Make the MyMediaItem object the current media.
WMP9.currentMedia = MyMediaItem;

```



Much of the functionality in the Windows Media Player 7 or later object model is accessed through the object hierarchy. As the previous example showed, you can obtain a **Playlist** object by using the **getAll** method of the **mediaCollection** object, which is accessed through the root **Player** object. You can then obtain a particular **Media** object from the **Playlist** object by using the **item** method of the **Playlist** object. There are five additional methods accessible through the **mediaCollection** object that return a **Playlist** object; each method allows you to retrieve the object based on specific criteria, like genre or album.

The hierarchical structure of the Windows Media Player 7 or later ActiveX control object model provides a more logical approach to organizing the properties, methods, and events available for your use. All the functionality for the Player controls is contained in the **Controls** object, all the functionality for the Player network connection is contained in the **Network** object, and so forth. For example, to start content playing using the version 6.4 object model, you use the **Player6.Play** method:


```C++
WMP64.Play();

```



When using the Windows Media Player 7 or later object model, you must access the **Play** method by using the **Controls** object:


```C++
WMP9.controls.play();

```



The depth of the object model, however, can lead to very long script statements:


```C++
WMP9.currentPlaylist.appendItem(WMP9.mediaCollection.getByName("MySong").item(0));

```



Statements like the preceding one can be made much simpler and more readable by working with individual named objects. The following example replaces the preceding code statement with syntax using separate object variables:


```C++
// Store the current playlist object.
var pl = WMP9.currentPlaylist;

// Get a playlist from the media collection that contains
// one media item named "MySong".
var temp = WMP9.mediaCollection.getByName("MySong");

// Get the individual media item from the temp playlist.
var song = temp.item(0);

// Append the media item to the current playlist.
pl.appendItem(song);

```



This coding style requires more lines of script, but is much easier to follow, especially with the added comments. There is another advantage: the **currentPlaylist** object is easy to reuse because it is stored in the variable pl.

Many of the properties, methods, and events in the Windows Media Player 7 or later object model set or retrieve different values, or return values of a different type or number, compared to corresponding functionality in the version 6.4 object model. For instance, when **Player6.openState** retrieves 2, that value corresponds to the Visual Basic constant **nsLoadingNSC**, meaning the Player is loading a station file with a .nsc file name extension. But when the Windows Media Player 7 or later object model property **Player.openState** retrieves 2, that value corresponds to the state PlaylistLocating, meaning Windows Media Player is attempting to locate a playlist. Additionally, the **Player6.openState** property can retrieve seven different values, while the Windows Media Player 7 or later **Player.openState** property can retrieve 22 different values. Be sure to refer to the Object Model Reference for Scripting section of the Windows Media Player SDK when revising code to use a different object model version.

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> </dl>

 

 




