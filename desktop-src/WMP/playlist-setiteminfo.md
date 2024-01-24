---
title: Playlist.setItemInfo method
description: The setItemInfo method specifies the value of a playlist attribute.
ms.assetid: 'ffecb43f-343d-4a4f-9356-0e3cfa85ce77'
keywords:
- setItemInfo method Windows Media Player
- setItemInfo method Windows Media Player , Playlist class
- Playlist class Windows Media Player , setItemInfo method
topic_type:
- apiref
api_name:
- Playlist.setItemInfo
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlist.setItemInfo method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setItemInfo** method specifies the value of a playlist attribute.

## Syntax


```JScript
Playlist.setItemInfo(
  name,
  value
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the attribute to be set. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> <dt>

*value* \[in\]
</dt> <dd>

**String** containing the new value for the attribute.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A special use of the **setItemInfo** method is to sort the items in the playlist by using the SortAttribute attribute. The following JScript example sorts a playlist by the values of the UserLastPlayedTime attribute. The variable playlist is a reference to a **Playlist** object.


```JScript
playlist.setItemInfo("SortAttribute", "UserLastPlayedTime")
```



To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This method is not supported.

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

[**Playlist.getItemInfo**](playlist-getiteminfo.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





