---
title: CdromCollection.count
description: The count property retrieves the number of available CD and DVD drives on the system.
ms.assetid: 98d24713-6a55-409f-af9a-fc941ad6d8f5
keywords:
- CdromCollection.count Windows Media Player
topic_type:
- apiref
api_name:
- CdromCollection.count
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CdromCollection.count

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **count** property retrieves the number of available CD and DVD drives on the system.

``` syntax
player.cdromCollection.count
      
```

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

DVD-ROM drives are counted exactly like CD drives. However, the Windows Media Player control only supports DVD functionality for Windows XP or later operating systems. Typically, DVD drives can play CD media, but CD drives cannot play DVD media.

**Windows Media Player 10 Mobile:** This method always returns 0.

## Examples

The following JScript example uses *CdromCollection*.**count** to display the number of CD and DVD drives available on the user's computer. The player object was created with ID = "Player".


```JScript
// Store the count of drives found on the computer.
var numCDROMS = Player.cdromCollection.count;

// Build the string to display to the user.
var displayString = numCDROMS + " drive(s) found.";

// Show a message box with the count information.
alert(displayString);
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/>                               |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**CdromCollection Object**](cdromcollection-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





