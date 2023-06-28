---
title: Media.isReadOnlyItem method
description: The isReadOnlyItem method returns a value indicating whether the specified attribute of the media item can be edited.
ms.assetid: '5e398e76-f64a-45b5-9b4f-679c65e5a0d1'
keywords:
- isReadOnlyItem method Windows Media Player
- isReadOnlyItem method Windows Media Player , Media class
- Media class Windows Media Player , isReadOnlyItem method
topic_type:
- apiref
api_name:
- Media.isReadOnlyItem
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.isReadOnlyItem method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isReadOnlyItem** method returns a value indicating whether the specified attribute of the media item can be edited.

## Syntax


```JScript
bRetVal = Media.isReadOnlyItem(
  attribute
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** indicating the name of the attribute to test. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md)..

</dd> </dl>

## Return value

This method returns a **Boolean**.

## Remarks

If an attribute is read-only, then it cannot be set with the **setItemInfo** method. Note that this method may return different values for a particular attribute when used with different versions of Windows Media Player.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This property always returns **true**.

## Examples

The following JScript example uses *Media*.**isReadOnlyItem** to fill an HTML TEXTAREA element named rwText with information about the current media item. The code outputs each attribute of the current media item, along with text indicating whether the attribute is read-only or read/write. The **Player** object was created with ID = "Player".


```JScript
// Store the current media item object.
var cm = Player.currentMedia;

// Create a variable to hold each attribute name.
var atName;

// Loop through the attribute list.
for(var i = 0; i < cm.attributeCount; i++){

   // Get the attribute name.
   atName = cm.getAttributeName(i);

   // Test whether the attribute is read-only.
   var test = ((cm.isReadOnlyItem(atName))?"Read-Only":"Read/Write");

// Print the attribute information to the text area.
   rwText.value += atName + " is " + test;
   rwText.value += "\n";
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

[**Media.setItemInfo**](media-setiteminfo.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





