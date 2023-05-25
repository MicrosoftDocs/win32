---
title: Settings.requestMediaAccessRights method
description: The requestMediaAccessRights method requests a specified level of access to the library. | Settings.requestMediaAccessRights method
ms.assetid: 076b749b-9b25-483c-aa1f-60fc4367e4e0
keywords:
- requestMediaAccessRights method Windows Media Player
- requestMediaAccessRights method Windows Media Player , Settings class
- Settings class Windows Media Player , requestMediaAccessRights method
topic_type:
- apiref
api_name:
- Settings.requestMediaAccessRights
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.requestMediaAccessRights method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **requestMediaAccessRights** method requests a specified level of access to the library.

## Syntax


```JScript
bRetVal = Settings.requestMediaAccessRights(
  access
)
```



## Parameters

<dl> <dt>

*access* \[in\]
</dt> <dd>

**String** specifying the desired access rights level. Contains one of the following values.



| String | Description                      |
|--------|----------------------------------|
| none   | Current item access rights only. |
| read   | Read access rights only.         |
| full   | Read/Write access rights.        |



 

</dd> </dl>

## Return value

This method returns a **Boolean** value indicating whether the requested access rights were granted.

## Remarks

A webpage must first request permission from the user to read information from or write data to the library. Invoking this method prompts the user with a dialog box that requests the specified permission level. This means that certain methods, properties, and events will be inaccessible from code if the appropriate access rights have not been granted. The current access rights level can be retrieved using *Settings*.**mediaAccessRights**.

**Windows Media Player 10 Mobile**: This method always returns **true**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> </dl>

 

 





