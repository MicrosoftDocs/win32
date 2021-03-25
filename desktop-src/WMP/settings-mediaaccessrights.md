---
title: Settings.mediaAccessRights
description: The mediaAccessRights property retrieves a value indicating the rights currently granted for library access.
ms.assetid: 744e696d-29d2-44b1-a296-5b5d007b689f
keywords:
- Settings.mediaAccessRights Windows Media Player
topic_type:
- apiref
api_name:
- Settings.mediaAccessRights
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.mediaAccessRights

The **mediaAccessRights** property retrieves a value indicating the rights currently granted for library access.

## Syntax

player.settings.mediaAccessRights

## Possible Values

This property is a read-only **String**.



| Value | Description                      |
|-------|----------------------------------|
| none  | Current item access rights only. |
| read  | Read access rights only.         |
| full  | Read/Write access rights.        |



 

## Remarks

A webpage must first request permission from the user to read information from or write data to the library. This means that certain methods, properties, and events will be inaccessible from code if the appropriate access rights have not been granted. To obtain access rights, the application calls *Settings*.**requestMediaAccessRights**, passing a parameter that specifies the desired access rights level.

**Windows Media Player 10 Mobile**: This property always returns **full**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





