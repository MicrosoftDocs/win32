---
title: MediaCollection.getAttributeStringCollection method
description: The getAttributeStringCollection method retrieves a StringCollection object representing the set of all values for a specified attribute within a specified media type.
ms.assetid: '75563a75-88f5-419e-983b-d105bce02511'
keywords:
- getAttributeStringCollection method Windows Media Player
- getAttributeStringCollection method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getAttributeStringCollection method
topic_type:
- apiref
api_name:
- MediaCollection.getAttributeStringCollection
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollection.getAttributeStringCollection method

The **getAttributeStringCollection** method retrieves a **StringCollection** object representing the set of all values for a specified attribute within a specified media type.

## Syntax


```JScript
retVal = MediaCollection.getAttributeStringCollection(
  attribute,
  mediaType
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** specifying the attribute.

</dd> <dt>

*mediaType* \[in\]
</dt> <dd>

**String** representing the media type. Contains one of the following values: "Audio", "Video", "Playlist", or "Other".

</dd> </dl>

## Return value

This method returns a **StringCollection** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

For information about the attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md) section.

## Examples

The following JScript example uses *MediaCollection*.**getAttributeStringCollection** to display a list of values that correspond to a particular attribute for audio items in the media collection. An HTML SELECT element, created with ID = "Attribute", allows the user to select an attribute, such as Artist, Genre, or Album. An HTML TEXTAREA element, created with ID = "AttributeVals", displays the result. The **Player** object was created with ID = "Player".


```JScript
// Clear the text in the display area.
AttributeVals.value = "";

// Store the mediaCollection object.
var library = Player.mediaCollection;

// Get the string collection for the attribute type the user selects.
var all = library.getAttributeStringCollection(Attribute.value, "Audio");

// Loop through the string collection.
for (i = 0; i < all.count; i++){

    // Display the items one line at a time.
    AttributeVals.value += all.item(i);
    AttributeVals.value += "\n";
}

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> <dt>

[**StringCollection Object**](stringcollection-object.md)
</dt> </dl>

 

 





