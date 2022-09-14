---
title: Media.imageSourceHeight
description: The ImageSourceHeight property retrieves the height of the current media item in pixels.
ms.assetid: fa98ec62-4c58-46ab-98f3-8017096d46d8
keywords:
- Media.imageSourceHeight Windows Media Player
topic_type:
- apiref
api_name:
- Media.imageSourceHeight
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Media.imageSourceHeight

The **ImageSourceHeight** property retrieves the height of the current media item in pixels.

## Syntax

*player*.*currentMedia*.**imageSourceHeight**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

If the media item is not the current one, this property returns zero.

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Media*.imageSourceHeight to display the image size, in pixels, of the current media item. The information is printed to an HTML TEXTAREA element named VideoSize. The **Player** object was created with ID = "player".


```JScript
<!-- Create an event handler to refresh the information when the current media changes. -->
<SCRIPT LANGUAGE = "JScript"  FOR = Player  EVENT = OpenStateChange(NewState)>

// Test whether the new media item is open.
if (NewState == 13){

   // Store the height and width of the new media item.
   var Height = Player.currentMedia.imageSourceHeight;
   var Width =  Player.currentMedia.imageSourceWidth;

   // Erase the information in the text area.
   VideoSize.value = "";

   // Test whether an image is visible.
   if (Height != 0 && Width != 0)

      // Display the image size information.
      VideoSize.value = Width + " x " + Height;
}
</SCRIPT>

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

 

 





