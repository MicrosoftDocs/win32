---
title: Media.getItemInfoByType method
description: The getItemInfoByType method retrieves the value of the attribute corresponding to the specified attribute name, language, and index.
ms.assetid: 9d3377c2-7ae8-48ce-a42e-9c965f6b79f9
keywords:
- getItemInfoByType method Windows Media Player
- getItemInfoByType method Windows Media Player , Media class
- Media class Windows Media Player , getItemInfoByType method
topic_type:
- apiref
api_name:
- Media.getItemInfoByType
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.getItemInfoByType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getItemInfoByType** method retrieves the value of the attribute corresponding to the specified attribute name, language, and index.

## Syntax


```JScript
retVal = Media.getItemInfoByType(
  name,
  language,
  index
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the attribute. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> <dt>

*language* \[in\]
</dt> <dd>

**String** representing the language. If the value is set to null or "" (empty string) the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) containing the zero-based index of the value to retrieve from the attribute.

</dd> </dl>

## Return value

This method returns a **Number**, **String**, **MetadataPicture** object, or **MetadataText** object as indicated in the following table.



| Attribute                   | Return value                   |
|-----------------------------|--------------------------------|
| **SyncState**               | **Number** (**unsigned long**) |
| **WM/Lyrics\_Synchronised** | **MetadataText** object        |
| **WM/Picture**              | **MetadataPicture** object     |
| **WM/UserWebURL**           | **MetadataText** object        |
| All other attributes        | **String**                     |



 

For attributes whose underlying value is **Boolean**, this method returns the string "true" or "false".

## Remarks

This method retrieves the metadata for an individual digital media item or a media item that is part of a playlist.

This method supports attributes with multiple values and attributes with complex values. The **getItemInfo** method does not support attributes with multiple values and attributes with complex values.

The **attributeCount** property contains the number of attribute names available for a given **Media** object. Index numbers can then be used with the **getAttributeName** method to determine the name of each available attribute. Individual attribute names can be passed to the *name* parameter of **getItemInfoByType**.

The **getAttributeCountByType** method returns the number of attributes that correspond to a particular attribute name for a given **Media** object. Index numbers can then be passed to the *index* parameter of **getItemInfoByType**. This is useful when a digital media item has been categorized under multiple genres, for example.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

This method can cause errors. You should include error-handling code when you call this method. For example, in JScript you can implement error handling by using the **try...catch...finally** structure.

**Windows Media Player 10 Mobile:** This method is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Media.attributeCount**](media-attributecount.md)
</dt> <dt>

[**Media.getAttributeCountByType**](media-getattributecountbytype.md)
</dt> <dt>

[**Media.getAttributeName**](media-getattributename.md)
</dt> <dt>

[**Media.getItemInfo**](media-getiteminfo.md)
</dt> <dt>

[**Media.setItemInfo**](media-setiteminfo.md)
</dt> <dt>

[**MetadataPicture Object**](metadatapicture-object.md)
</dt> <dt>

[**MetadataText Object**](metadatatext-object.md)
</dt> <dt>

[**Reading Attribute Values**](reading-attribute-values.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





