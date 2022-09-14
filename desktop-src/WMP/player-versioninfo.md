---
title: Player.versionInfo
description: The versionInfo property retrieves a String value specifying the version of the Windows Media Player.
ms.assetid: 4b644de2-fcb9-407b-9eea-3eb683a17150
keywords:
- Player.versionInfo Windows Media Player
topic_type:
- apiref
api_name:
- Player.versionInfo
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.versionInfo

The **versionInfo** property retrieves a String value specifying the version of the Windows Media Player.

## Syntax

*player* .**versionInfo**

## Possible Values

This property is a read-only **String** in the following format: "*X*.0.0.*YYYY*" where *X* represents the major version number and *YYYY* represents the build number.

## Examples

The following example creates an HTML BUTTON element that, when clicked, displays a message box containing the version information for Windows Media Player. The **Player** object was created with ID = "Player".


```
<INPUT TYPE = "BUTTON"  ID = "VERSION"  VALUE = "Show Version"
    onClick = "
        /* Build the message containing the version info. */
        var message = 'Windows Media Player Version: ';
        message += '\n';
        message += Player.versionInfo;
 
        /* Display the message box. */
        alert(message);
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





