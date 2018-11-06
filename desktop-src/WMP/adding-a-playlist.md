---
title: Adding a Playlist
description: Adding a Playlist
ms.assetid: be0c2cac-245d-4435-87d9-4f17076e005a
keywords:
- creating skins,playlists
- Windows Media Player skins,playlists
- skins,playlists
- playlists,skins
- metafile playlists,skins
- Windows Media metafile playlists,skins
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Playlist

You can use playlists to choose from collections of your audio and video.

Using the artwork from your first skin, you can make a few changes to the skin definition file.

The first step is to use the shell you will use for most skins:


```C++
<THEME>
    <VIEW
        clippingColor = "#CCCC00"
        backgroundImage = "background.bmp"
        titleBar = "false">

        <BUTTONGROUP
            mappingImage = "map.bmp"
            hoverImage = "hover.bmp"> 
                
    </VIEW>


</THEME>

```



Now add a second **VIEW**, which contains a playlist. Place the following code after the </VIEW> of the shell code.


```C++
     <VIEW 
          id = "playview">
          <PLAYLIST/>
     </VIEW>

```



You will need to give this second view an ID so you can refer to it later. Add a PLAYELEMENT and a STOPELEMENT. These predefined buttons make life easier.


```C++
        <PLAYELEMENT
            mappingColor = "#00FF00" />
                          
        <STOPELEMENT
            mappingColor = "#FF0000" />

```



Finally, add an onClick event to the PLAYELEMENT to display a playlist in the second view:


```C++
            onClick = "JScript: theme.openView('playview');" />

```



You can see a similar working playlist skin in the sample section of the SDK.

## Related topics

<dl> <dt>

[**Skin Creation Guide**](skin-creation-guide.md)
</dt> </dl>

 

 




