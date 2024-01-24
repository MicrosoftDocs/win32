---
title: StringCollection.getItemInfoByType method
description: The getItemInfoByType method retrieves the value corresponding to the specified StringCollection index, name, language, and attribute index.
ms.assetid: 32a25c69-9399-4857-84c1-143c529be58f
keywords:
- getItemInfoByType method Windows Media Player
- getItemInfoByType method Windows Media Player , StringCollection class
- StringCollection class Windows Media Player , getItemInfoByType method
topic_type:
- apiref
api_name:
- StringCollection.getItemInfoByType
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# StringCollection.getItemInfoByType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getItemInfoByType** method retrieves the value corresponding to the specified **StringCollection** index, name, language, and attribute index.

## Syntax


```JScript
retVal = StringCollection.getItemInfoByType(
  index,
  name,
  language,
  attributeIndex
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the zero-based index of the **StringCollection** item from which to get the attribute.

</dd> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the attribute name.

</dd> <dt>

*language* \[in\]
</dt> <dd>

**String** containing the language. If the value is set to null or the empty string ("") the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> <dt>

*attributeIndex* \[in\]
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
| All other attributes        | String                         |



 

For attributes whose underlying value is **Boolean**, this method returns the string "true" or "false".

## Remarks

This method supports attributes with multiple values, and attributes with complex values. The **getItemInfo** method does not support attributes with multiple or complex values.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MetadataPicture Object**](metadatapicture-object.md)
</dt> <dt>

[**MetadataText Object**](metadatatext-object.md)
</dt> <dt>

[**StringCollection.getItemInfo**](stringcollection-getiteminfo.md)
</dt> <dt>

[**StringCollection Object**](stringcollection-object.md)
</dt> </dl>

 

 





