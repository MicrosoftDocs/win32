---
title: Playlists
description: Playlists
ms.assetid: 'b1ac9208-33d1-448f-9e2e-920fad9c6add'
keywords:
- Windows Media Player,playlists
- Windows Media Player object model,playlists
- object model,playlists
- Windows Media Player ActiveX control,playlists
- ActiveX control,playlists
- Windows Media Player Mobile ActiveX control,playlists
- Windows Media Player Mobile,playlists
- playlists,migration
- Windows Media metafile playlists,migration
- metafile playlists,migration
- migration guide,playlists
ms.topic: article
ms.date: 05/31/2018
---

# Playlists

The Windows Media Player 6.4 ActiveX control object model includes four methods and one property for working with Windows Media metafile playlists:

-   *Player6*.**GetCurrentEntry**
-   *Player6*.**SetCurrentEntry**
-   *Player6*.**GetMediaParameter**
-   *Player6*.**GetMediaParameterName**
-   *Player6*.**EntryCount**.

Together, these provide limited functionality for navigating a playlist metafile with an .asx file name extension and retrieving information about the entries contained in the playlist.

Windows Media Player 7 introduced "Media Library." The library allows users to organize their digital media content, as well as to create custom playlists that can be managed from the Player graphical user interface. The Windows Media Player 7 or later ActiveX control object model provides support for working with library playlists, as well as playlists contained in Windows Media metafiles with an .asx file name extension.

> [!Note]  
> For security reasons, the user must grant access rights to the library before your program can manipulate its content. Access rights can only be requested and granted through the Windows Media Player 9 Series or later object model. For details about access rights, see [Library Access](library-access.md).

 

The Windows Media Player 7 or later object model includes three objects for handling playlists. The **PlaylistCollection** object provides functionality for organizing playlists; it represents the entire collection of playlists in the user's library. The **PlaylistArray** object provides a way to retrieve a specific playlist from the **PlaylistCollection** object by using an index number; two of the **PlaylistCollection** object methods retrieve a **PlaylistArray** object. The **Playlist** object provides the properties and methods necessary to manipulate media items contained in a single playlist.

As an example, since each playlist in the library has a unique name, you can retrieve a playlist from the library using the *PlaylistCollection*.**getByName** method:


```C++
// Retrieve a PlaylistArray object that contains 
// exactly one Playlist object.
var plarray = WMP9.playlistCollection.getByName("MyPlaylist");

// Get the Playlist object from the PlaylistArray object.
// The Playlist object has index number zero.
var pl = plarray.item(0);

// Make the retrieved playlist the current playlist.
WMP9.currentPlaylist = pl;

```



You will most frequently want to work with the current playlist. While it is possible to use several playlist objects, only one can be retrieved by the *Player*.**currentPlaylist** property at any given time: the one that Windows Media Player is processing at that moment.

When Windows Media Player 7 or later plays a Windows Media metafile with an .asx file name extension, it first creates a **Playlist** object. Next, it fills the object with the information from the .asx playlist, and then makes that **Playlist** object the current playlist. This means that you can use the properties and methods associated with the **Playlist** object to manipulate .asx playlists exactly as you would handle playlists in the library. For instance, to retrieve the number of entries in an .asx playlist using the version 6.4 object model, you use the *Player6*.**EntryCount** property:


```C++
var entrycount = WMP64.EntryCount;

```



When using the Windows Media Player 7 or later object model, you use the *Playlist*.**count** property:


```C++
var entrycount = WMP9.currentPlaylist.count;

```



When using the version 6.4 control, you can use the *Player6*.**GetCurrentEntry** method to retrieve the index of the current entry in an .asx playlist:


```C++
var entrynum = WMP64.GetCurrentEntry();

```



You can achieve the same result by using the Windows Media Player 7 or later object model in script. The following JScript example compares the current media object to each item in the playlist. When *Media*.**isIdentical** returns true, a message box displays the index of the current media item.


```C++
function matchit(){
// Store the current playlist object in a variable.
var pl = WMP9.currentPlaylist;

// Loop through the playlist one entry at a time.
  for (var i = 0; i < pl.count; i++){

   // Test whether the current media item matches 
   // the item in the playlist at the current loop index.
   if (WMP9.currentmedia.isIdentical(pl.item(i))){

       // They match, display the index.
       var message = "Current media at index: " + i;
       alert(message);

       // Exit the function, don't continue looping!
       return;
      }
  }
}

```



To specify the index of the current entry in an .asx playlist, you use *Player6*.**SetCurrentEntry**. Playlist entry indexes in version 6.4 start with 1, so to make the second entry in a metafile playlist the current one, use the following syntax:


```C++
WMP6.SetCurrentEntry(2);

```



Playlist entry indexes are zero-based in Windows Media Player 7 or later; to make the second entry in a metafile playlist the current one, when using the Windows Media Player 7 or later object model, use the following syntax:


```C++
WMP9.controls.currentItem = WMP9.currentPlaylist.item(1);

```



The following JScript example demonstrates a function that accepts an index number as a parameter, and then makes the playlist entry that corresponds to the index the current media item:


```C++
function setindex(idx){
// Store the current playlist in a variable.
var pl = WMP9.currentPlaylist;

// Get the first playlist entry.
var firstmedia = pl.item(0);

// Start the Player to allow navigation within the playlist.
WMP9.controls.playItem(firstmedia);

// Test whether idx is within a valid range.
   if (idx < pl.count && idx >= 0){

     // Set the currentItem to the desired playlist item.
     WMP9.controls.currentItem = pl.item(idx);

     // Display the name of the media item.
     alert(WMP9.currentMedia.name);
     return true;
 }

// The index is out of range, stop the Player, alert the user.
WMP9.controls.stop();
alert("Index out of range");
return false;
}

```



Windows Media metafiles can contain custom parameter elements, which you specify by using the **&lt;PARAM&gt;** tag. When using the version 6.4 object model, you can retrieve the name of a particular parameter with the *Player6*.**GetMediaParameterName** method. The following JScript example retrieves the name of the first parameter in the first entry of an .asx playlist:


```C++
var paramname = WMP6.GetMediaParameterName(1,1);

```



Similarly, you can retrieve the value associated with the parameter using *Player6*.**GetMediaParameter**:


```C++
var paramvalue = WMP6.GetMediaParameter(1, paramname);

```



The following JScript example uses the Windows Media Player 7 or later object model to retrieve the parameter name and value from the first entry in an .asx playlist:


```C++
function getattribute(){
// Store the first playlist entry as a Media object.
var firstmedia = WMP9.currentplaylist.item(0);

// Get the name of the first parameter in the object named firstmedia.
var attname = firstmedia.getAttributeName(0);

// Get the value of the first parameter in the object named firstmedia.
var attval = firstmedia.getItemInfo(attname);

// Display the information.
alert(attname + ": " + attval);
}

```



You can use the *PlaylistCollection*.**importPlaylist** method to add an .asx playlist to the library. Once imported, the metafile playlist becomes a library playlist, so you can manipulate it using all the properties and methods at your disposal. The user must grant full access rights to the library for your application to be able to use the **importPlaylist** method.

You can use *PlaylistCollection*.**getByName** to test whether a playlist exists. This method always returns a valid **PlaylistArray** object. If the playlist array retrieved contains exactly one playlist, then there exists a playlist with that name in the library. Otherwise, the playlist array will contain no playlist object; this means there is no playlist in the library with the name passed as an argument to the **getByName** method. The following JScript example demonstrates this:


```C++
// Specify an .asx playlist file.
WMP9.URL = "https://www.microsoft.com/someplaylist.asx";

// Open the playlist and start playing the content.
WMP9.controls.play();

// Store the current playlist object.
var pl = WMP9.currentPlaylist;

// Attempt to retrieve from the library 
// a playlist having the same name as the current playlist.
var plarray = WMP9.playlistCollection.getByName(pl.name);

// Test whether the PlaylistArray object, plarray, contains
// a Playlist object.
if (!plarray.count)
   
   // If plarray contains no playlist, then import 
   // the current one.
   WMP9.playlistCollection.importPlaylist(pl);
}

```



## Related topics

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 




