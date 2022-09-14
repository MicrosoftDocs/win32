---
title: Playlist.getItemInfo method
description: The getItemInfo method retrieves the value of a playlist attribute.
ms.assetid: '888c0ab7-c225-4246-b1a1-94da7e19fa1a'
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , Playlist class
- Playlist class Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- Playlist.getItemInfo
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Playlist.getItemInfo method

The **getItemInfo** method retrieves the value of a playlist attribute.

## Syntax


```JScript
strRetVal = Playlist.getItemInfo(
  name
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the attribute to be retrieved. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> </dl>

## Return value

This method returns a **String**.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

See the [attributeCount](playlist-attributecount.md) property for example code that uses this property.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**Playlist.setItemInfo**](playlist-setiteminfo.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





