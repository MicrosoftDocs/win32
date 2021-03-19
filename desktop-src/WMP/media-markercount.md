---
title: Media.markerCount
description: The markerCount property retrieves the number of markers in the media item.
ms.assetid: 48313395-b225-4008-b0e8-82fa22d6aaef
keywords:
- Media.markerCount Windows Media Player
topic_type:
- apiref
api_name:
- Media.markerCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Media.markerCount

The **markerCount** property retrieves the number of markers in the media item.

## Syntax

*player*.*currentMedia*.**markerCount**

## Possible Values

This property is a read-only **Number** (**long**) specifying the number of markers in the file.

## Remarks

This property returns zero if a file has no markers, or if the media item is not the same as *Player*.**currentMedia**.

Marker numbers start at 1.

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Media*.**markerCount** to retrieve the number of markers in the current media item. That value is then used as the upper boundary for a looping structure, which iterates through the marker list to retrieve each marker name. An HTML TEXTAREA element named MNAMES displays the names of the markers in the current media item. The **Player** object was created with ID = "Player".


```JScript
// Get the number of markers in the current media item.
var mcount = Player.currentMedia.markerCount;

// Verify that at least one marker exists in the current media item.
if (mcount > 0){

// Loop through the marker list.
for (var i = 1; i < mcount + 1; i++){

   // Print the marker name to the text area.
   MNAMES.value += Player.currentMedia.getMarkerName(i);
   MNAMES.value += "\n";
}

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





