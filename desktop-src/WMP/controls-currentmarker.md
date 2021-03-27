---
title: Controls.currentMarker
description: The currentMarker property specifies or retrieves the current marker number.
ms.assetid: 4b4eacd4-3df0-4e11-8755-1ac326fad027
keywords:
- Controls.currentMarker Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentMarker
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.currentMarker

The **currentMarker** property specifies or retrieves the current marker number.

``` syntax
player.controls.currentMarker
      
```

## Possible Values

This property is a read/write **Number** (**long**) with a default value of zero.

## Remarks

Setting **currentMarker** causes playback to start from the specified marker. Before attempting to set **currentMarker**, determine whether a file has markers and how many it has by using **markerCount**. If a file has no markers, setting **currentMarker** to anything but zero results in an error. Setting **currentMarker** to a number higher than **markerCount** also results in an error.

The **currentMarker** property always returns the current or last marker, which means the actual file position can be either at the current marker or before the next marker. Markers are numbered beginning at 1, so if a file has markers, you can set **currentMarker** to zero to change the file position to zero.

Until the current media item is set (using *Player*.**URL** or *Player*.**currentMedia**), **currentMarker** returns zero.

## Examples

The following JScript example uses **currentMarker** to start video playback from the marker that corresponds to the **selectedIndex** property of an HTML SELECT element. The **Player** object was created with ID = "Player".


```JScript
<SELECT ID = "markers"  NAME = "markers"  LANGUAGE = "JScript"

    /* Seek to the marker number that corresponds to the SELECT element
       selectedIndex value when the list selection changes. */
    onChange = "Player.controls.currentMarker = markers.selectedIndex + 1;
">

    /* Fill the SELECT element with the marker identifiers. */
    <OPTION SELECTED>Sunrise
    <OPTION>Car chase 
    <OPTION>Happy ending
</SELECT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Media.markerCount**](media-markercount.md)
</dt> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Player.URL**](player-url.md)
</dt> </dl>

 

 





