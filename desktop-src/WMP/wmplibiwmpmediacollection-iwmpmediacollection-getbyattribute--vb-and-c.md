---
title: IWMPMediaCollection getByAttribute method
description: The getByAttribute method returns an IWMPPlaylist interface that corresponds to the specified attribute having the specified value.
ms.assetid: ece70a2c-38bc-4652-8319-efcde5f9720a
keywords:
- getByAttribute method Windows Media Player
- getByAttribute method Windows Media Player , IWMPMediaCollection interface
- IWMPMediaCollection interface Windows Media Player , getByAttribute method
topic_type:
- apiref
api_name:
- IWMPMediaCollection.getByAttribute
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection::getByAttribute method

The **getByAttribute** method returns an **IWMPPlaylist** interface that corresponds to the specified attribute having the specified value.

## Syntax


```CSharp
public IWMPPlaylist getByAttribute(
  System.String bstrAttribute,
  System.String bstrValue
);
```


```VB

Public Function getByAttribute( _
  ByVal bstrAttribute As System.String, _
  ByVal bstrValue As System.String _
) As IWMPPlaylist
Implements IWMPMediaCollection.getByAttribute
```





## Parameters

<dl> <dt>

*bstrAttribute* \[in\]
</dt> <dd>

The **System.String** that is the specified attribute.

</dd> <dt>

*bstrValue* \[in\]
</dt> <dd>

The **System.String** that is the specified value.

</dd> </dl>

## Return value

A **WMPLib.IWMPPlaylist** interface for the retrieved media items.

## Remarks

This method can be used to create a generic query for media items that match a value for an attribute in the library. This is useful in the case of user-defined attributes. If the attribute does not exist, an error will result.

You can use this method to retrieve all of the media items of a specific type. Use the attribute name **MediaType** and one of the following values.



| Value    | Description                                               |
|----------|-----------------------------------------------------------|
| audio    | Music and other audio-only items                          |
| other    | Other items, such as an .asf file or the URL of a stream. |
| photo    | Photo items. Requires Windows Media Player 10.            |
| playlist | Playlists represented as media items.                     |
| radio    | Radio station items. Not used by Windows Media Player 10. |
| video    | Video items.                                              |



 

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

For information about the attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md).

There are two ways you ways you can retrieve an **IWMPMediaCollection** interface, and the behavior of the **getByAttribute** method depends on which of those two ways you use. If you retrieve the interface by calling [AxWindowsMediaPlayer.mediaCollection](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md), then the **getByAttribute** method returns all the media items in the library. However, if you retrieve the interface by calling [IWMPLibrary.mediaCollection](wmplibiwmplibrary-iwmplibrary-mediacollection--vb-and-c.md), then the **getByAttribute** method returns only the audio items in the library that have the specified attribute and value.

## Examples

The following code example uses **getByAttribute** to play all content from the library by the artist named Triode 48. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Get an interface to a playlist that contains media items by a particular artist.
WMPLib.IWMPPlaylist pl = player.mediaCollection.getByAttribute("Artist", "Triode 48");

// Make the new playlist the current one.
player.currentPlaylist = pl;

// Play the media items in the current playlist. 
player.Ctlcontrols.play();
```


```VB

' Get an interface to a playlist that contains media items by a particular artist.
Dim pl As WMPLib.IWMPPlaylist = player.mediaCollection.getByAttribute(&quot;Artist&quot;, &quot;Triode 48&quot;)

&#39; Make the new playlist the current one.
player.currentPlaylist = pl

&#39; Play the media items in the current playlist. 
player.Ctlcontrols.play()
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.getAll (VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getall--vb-and-c.md)
</dt> </dl>

 

 





