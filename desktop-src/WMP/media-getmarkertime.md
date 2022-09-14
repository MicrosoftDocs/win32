---
title: Media.getMarkerTime method
description: The getMarkerTime method retrieves the time of the marker at the specified index.
ms.assetid: 'c3e6bead-2831-4d84-9d13-dcb865efe472'
keywords:
- getMarkerTime method Windows Media Player
- getMarkerTime method Windows Media Player , Media class
- Media class Windows Media Player , getMarkerTime method
topic_type:
- apiref
api_name:
- Media.getMarkerTime
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Media.getMarkerTime method

The **getMarkerTime** method retrieves the time of the marker at the specified index.

## Syntax


```JScript
retVal = Media.getMarkerTime(
  markerNum
)
```



## Parameters

<dl> <dt>

*markerNum* \[in\]
</dt> <dd>

**Number** (**long**) specifying the marker index.

</dd> </dl>

## Return value

This method returns a **Number** (**double**) specifying the location of the marker in seconds from the beginning of the clip.

## Remarks

This method returns **NULL** if the specified marker does not exist.

Some digital media items do not contain markers. Use **markerCount** to find out how many markers are in the current clip.

Marker index numbers start at 1.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Media*.**getMarkerTime** to fill an HTML TEXTAREA element named MTIMES with the location of each marker. The **Player** object was created with ID = "Player".


```JScript
// Get the number of markers in the current media item.
var mcount = Player.currentMedia.markerCount;

// Verify that at least one marker exists in the current media item.
if (mcount > 0){

// Loop through the marker list.
for (var i = 1;i < mcount + 1; i++){

   // Print the message to the text area.
   MTIMES.value += "Marker number " + i + " occurs at ";
   MTIMES.value += Player.currentMedia.getMarkerTime(i);
   MTIMES.value += " second(s).";
   MTIMES.value += "\n";
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

[**Media.getMarkerName**](media-getmarkername.md)
</dt> <dt>

[**Media.markerCount**](media-markercount.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





