---
title: Media.getItemInfoByAtom method
description: The getItemInfoByAtom method retrieves the value of the attribute with the specified index number.
ms.assetid: '6e2dea0c-c722-4737-9e8e-f5cb74156cea'
keywords:
- getItemInfoByAtom method Windows Media Player
- getItemInfoByAtom method Windows Media Player , Media class
- Media class Windows Media Player , getItemInfoByAtom method
topic_type:
- apiref
api_name:
- Media.getItemInfoByAtom
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Media.getItemInfoByAtom method

The **getItemInfoByAtom** method retrieves the value of the attribute with the specified index number.

## Syntax


```JScript
strRetVal = Media.getItemInfoByAtom(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the index at which a given attribute resides within the set of available attributes.

</dd> </dl>

## Return value

This method returns a **String** representing the value of the specified attribute. For attributes whose underlying value is **Boolean**, it returns the string "true" or "false".

## Remarks

This method can be used to retrieve metadata for a specific digital media item by using an attribute index number. The **attributeCount** property can be used to determine the number of attributes available for the media item.

The **getMediaAtom** method of the **MediaCollection** object can also be used to retrieve the index of a particular attribute. This technique is generally more efficient than the **getItemInfo** or **getItemInfoByType** methods when working with large playlists.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md)..

**Windows Media Player 10 Mobile:** Attributes for a media item are available only during playback unless they are retrieved from the item through the media collection.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Media.attributeCount**](media-attributecount.md)
</dt> <dt>

[**Media.getItemInfo**](media-getiteminfo.md)
</dt> <dt>

[**Media.getItemInfoByType**](media-getiteminfobytype.md)
</dt> <dt>

[**Media.setItemInfo**](media-setiteminfo.md)
</dt> <dt>

[**MediaCollection.getMediaAtom**](mediacollection-getmediaatom.md)
</dt> <dt>

[**Reading Attribute Values**](reading-attribute-values.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





