---
title: Playlist Attributes
description: Playlist Attributes
ms.assetid: '2f2224ad-a1de-4f88-9166-8c00137a3695'
keywords:
- Windows Media Player,playlists
- Windows Media Player object model,playlists
- object model,playlists
- Windows Media Player Mobile,playlists
- Windows Media Player ActiveX control,playlists
- Windows Media Player Mobile ActiveX control,playlists
- ActiveX control,playlists
- playlists,attributes
- metafile playlists,attributes
- Windows Media metafile playlists,attributes
- attributes,playlists
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlist Attributes

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Playlists have metadata information called attributes, just as media items have attributes. You can retrieve the names and values of playlist attributes and display them in your user interface, or your code can take actions based on the value of an attribute.

Playlists are defined in files organized in an XML format, and particular elements in the file define playlist attributes. Some attribute elements are well-known; the author of the metafile can also define arbitrary attributes. For more information about attribute elements in playlist files, see [Retrieving Metadata](retrieving-metadata.md).

The library may provide additional playlist attributes, such as **SourceURL** or **UserLastPlayedTime**. For more information about the library playlist attributes, see the Windows Media Player [Attribute Reference](attribute-reference.md).

The *Playlist*.**attributeCount** property retrieves the number of attributes associated with the playlist. The *Playlist*.**attributeName** property retrieves the name of an attribute based on its index, and the *Playlist*.**getItemInfo** method retrieves the value of an attribute based on its name.

You can modify the value of an attribute of the current playlist with the *Playlist*.**setItemInfo** method.

A special use of the **setItemInfo** method is to sort the items in the playlist, using the **SortAttribute** attribute. The following C# example sorts a playlist by the values of the **UserLastPlayedTime** attribute. The variable *Playlist* is a reference to a **Playlist** object.


```C++
Playlist.setItemInfo("SortAttribute", "UserLastPlayedTime");

```



Throughout this topic, the **Player** object was defined in the following manner:


```C++
AxWMPLib.AxWindowsMediaPlayer Player;
using WMPLib;

```



The following C# example code demonstrates retrieving playlist attributes. The first function, ShowPlaylists, populates a ListBox control with the names of the available playlists. The second part is the list box event handler. When the user clicks a playlist name, this code retrieves the attributes for that playlist and displays those attributes in a second list box.


```C++
// Member variables
IWMPPlaylistCollection PlaylistColl;
IWMPPlaylistArray PlaylistArray;

private void ShowPlaylists()
{
    // Retrieve the playlist collection
    PlaylistColl = Player.playlistCollection;
    // Store the collection in a playlist array
    PlaylistArray = PlaylistColl.getAll();

    // Retrieve the count of elements
    iCount = PlaylistArray.count;

    // Update the list box with the playlist names.
    lstPlaylist.BeginUpdate();
    for (int i=0; i<iCount; i++)
    {
        lstPlaylist.Items.Add(PlaylistArray.Item(i).name);
    }
    lstPlaylist.EndUpdate();

    // Set the selected index to zero
    lstPlaylist.SelectedIndex = 0;
}

```



The SelectedIndexChanged event for the ListBox control is called each time the user selects a playlist name. The following event handler fills a second list box with the attribute names and values corresponding to the user's selection.


```C++
private void lstPlaylist_SelectedIndexChanged(object sender, System.EventArgs e)
{
    IWMPPlaylist Playlist = PlaylistArray.Item(lstPlaylist.SelectedIndex);
    string strAttr="";
    string strItemNames="";
    int iAttribCount=0;

    iAttribCount = Playlist.attribCount;
    for (j=0; j<iAttribCount; j++)
    {
        strAttr=Playlist.get_attributeName(j) + " -- ";
        strAttr+=Playlist.getItemInfo(Playlist.get_attributeName(j));
        lstOutput.Items.Add(strAttr);
    }
}

```



## Related topics

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**Media Item Attributes**](media-item-attributes.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 




