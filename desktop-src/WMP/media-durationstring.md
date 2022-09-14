---
title: Media.durationString
description: The durationString property retrieves a String value indicating the duration of the current media item in HH MM SS format.
ms.assetid: dfcb4c2e-c62c-4c3e-a9f4-fd147fb5b28c
keywords:
- Media.durationString Windows Media Player
topic_type:
- apiref
api_name:
- Media.durationString
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Media.durationString

The **durationString** property retrieves a **String** value indicating the duration of the current media item in HH:MM:SS format.

## Syntax

*player*.*currentMedia*.**durationString**

## Possible Values

This property is a read-only **String**.

## Remarks

If this property is used with a media item other than the one specified in *Player*.**currentMedia**, it may not contain a valid value. If the media item is less than an hour long, the HH: portion of the return value is omitted.

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Media*.**durationString** to display the duration of the current media item as formatted text. An HTML DIV element named MediaInfo displays the duration information. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler to update the display when
 the current media item changes. -->
<SCRIPT LANGUAGE = "JScript"  FOR = Player  EVENT = OpenStateChange(NewState)>

// Test whether the new media item is open.
if (NewState == 13){

   // Write the formatted duration string to the DIV region.
   MediaInfo.innerHTML = "Duration: " + Player.currentMedia.durationString;
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

[**Media.duration**](media-duration.md)
</dt> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





