---
title: Media.getMarkerName method
description: The getMarkerName method retrieves the name of the marker at the specified index.
ms.assetid: '142438b7-88d1-4523-829f-52dafbf0a7a6'
keywords:
- getMarkerName method Windows Media Player
- getMarkerName method Windows Media Player , Media class
- Media class Windows Media Player , getMarkerName method
topic_type:
- apiref
api_name:
- Media.getMarkerName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Media.getMarkerName method

The **getMarkerName** method retrieves the name of the marker at the specified index.

## Syntax


```JScript
strRetVal = Media.getMarkerName(
  markerNum
)
```



## Parameters

<dl> <dt>

*markerNum* \[in\]
</dt> <dd>

**Number** (**long**) specifying a marker index.

</dd> </dl>

## Return value

This method returns a **String**.

## Remarks

This method returns **NULL** if the specified marker does not exist.

Some digital media items do not contain markers. Use **markerCount** to find out how many markers are in the current clip.

Marker index numbers start at 1.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Media*.**getMarkerName** to fill an HTML TEXTAREA element named MNAMES with the names of the markers in the current media item. The **Player** object was created with ID = "Player".


```JScript
// Get the number of markers in the current media item.
var mcount = Player.currentMedia.markerCount;

// Verify that at least one marker exists in the current media.
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

[**Media.getMarkerTime**](media-getmarkertime.md)
</dt> <dt>

[**Media.markerCount**](media-markercount.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





