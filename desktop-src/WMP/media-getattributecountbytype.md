---
title: Media.getAttributeCountByType method
description: The getAttributeCountByType method retrieves the number of attributes associated with the specified attribute name and language.
ms.assetid: 5644e823-a9b1-4b02-9dd6-015e524fde64
keywords:
- getAttributeCountByType method Windows Media Player
- getAttributeCountByType method Windows Media Player , Media class
- Media class Windows Media Player , getAttributeCountByType method
topic_type:
- apiref
api_name:
- Media.getAttributeCountByType
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Media.getAttributeCountByType method

The **getAttributeCountByType** method retrieves the number of attributes associated with the specified attribute name and language.

## Syntax


```JScript
retVal = Media.getAttributeCountByType(
  name,
  language
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

**String** representing the language. If the value is set to null or "" (empty string), the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> </dl>

## Return value

This method returns a **Number** (**long**) containing the attribute count.

## Remarks

This method is used to determine the number of attributes corresponding to a particular attribute name for a given **Media** object. Index numbers can then be passed to the **getItemInfoByType** method. This is useful, for example, when a media item has been categorized under multiple genres.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This property always returns 0.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaObject**](media-object.md)
</dt> <dt>

[**Media.getItemInfoByType**](media-getiteminfobytype.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





