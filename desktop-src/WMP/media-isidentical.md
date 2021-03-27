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
ms.date: 05/31/2018
---

# Media.isIdentical method

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

 

 





