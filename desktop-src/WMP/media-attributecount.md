---
title: Media.attributeCount
description: The attributeCount property retrieves the number of attributes that can be queried and/or set for the media item.
ms.assetid: d2a5286f-dde1-48b5-b486-6cee1be463f9
keywords:
- Media.attributeCount Windows Media Player
topic_type:
- apiref
api_name:
- Media.attributeCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Media.attributeCount

The **attributeCount** property retrieves the number of attributes that can be queried and/or set for the media item.

## Syntax

*player*.*currentMedia*.**attributeCount**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

**Windows Media Player 10 Mobile:** Attributes for a media item are available only during playback unless they are retrieved from the item through the media collection.

## Examples

The following JScript example uses *Media*.**attributeCount** to determine the number of attributes available in the current media item. The code uses that value to print a list of attribute names and values in an HTML text area, named myText. The **Player** object was created with ID = "Player".


```JScript
// Store the current media object.
var cm = Player.currentMedia;

// Create arrays to hold each attribute name and value.
var atNames = new Array();
var atValues = new Array();

// Loop through the attribute list.   
for(var i = 0; i < cm.attributeCount; i++){

   // Fill the arrays with the attribute info.
   atNames[i] = cm.getAttributeName(i);
   atValues[i] = cm.getItemInfo(atNames[i]);

   // Print the attribute information to the text area.
   myText.value += atNames[i] + ": " + atValues[i];
   myText.value += "\n";
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

[**Media.getAttributeName**](media-getattributename.md)
</dt> <dt>

[**Media.getItemInfo**](media-getiteminfo.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





