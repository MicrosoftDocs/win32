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
ms.date: 05/31/2018
---

# Settings.requestMediaAccessRights method

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

 

 





