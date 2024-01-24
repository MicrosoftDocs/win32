---
title: Media.isIdentical method
description: The isIdentical method retrieves a value indicating whether the supplied object is the same as the current one. | Media.isIdentical method
ms.assetid: af3266d5-4ac2-4e8c-a9f6-44f7938e9c9d
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , Media class
- Media class Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- Media.isIdentical
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.isIdentical method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isIdentical** method retrieves a value indicating whether the supplied object is the same as the current one.

## Syntax


```JScript
bRetVal = Media.isIdentical(
  media
)
```



## Parameters

<dl> <dt>

*media* \[in\]
</dt> <dd>

**Media** object to compare with the current **Media** object.

</dd> </dl>

## Return value

This method returns a **Boolean**.

## Examples

The following JScript example uses *Media*.**isIdentical** to check whether a media item named newMedia is the same as the current media item. If they are not the same, the new media item is played. Otherwise, the current media continues to play uninterrupted. The **Player** object was created with ID = "Player".


```JScript
// Check the new media item to see if it matches the current one.
if (newMedia.isIdentical(Player.currentMedia) != true){

   // Change the current media to the new media item.
   Player.currentMedia = newMedia;

   // Play the new media item.
   Player.controls.play();
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
</dt> </dl>

 

 





