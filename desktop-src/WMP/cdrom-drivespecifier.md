---
title: Cdrom.driveSpecifier
description: The driveSpecifier property retrieves the CD or DVD drive letter.
ms.assetid: f592819e-61ba-4ae1-b748-b6f29df88067
keywords:
- Cdrom.driveSpecifier Windows Media Player
topic_type:
- apiref
api_name:
- Cdrom.driveSpecifier
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Cdrom.driveSpecifier

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **driveSpecifier** property retrieves the CD or DVD drive letter.

``` syntax
player.cdromCollection.item(
        index
        ).driveSpecifier
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

Typically, DVD drives can play CD media, but CD drives cannot play DVD media. This property retrieves a drive specifier for a zero-based drive index within the range retrieved using *CdromCollection*.**count**. The value retrieved takes the form *X*:, where *X* represents the drive letter.

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This property is not supported.

## Examples

The following JScript example uses *Cdrom*.**driveSpecifier** to fill an HTML text area named myText with a comma-separated list of available CD and DVD drives. The **Player** object was created with ID = "Player".


```JScript
// Allocate an array to store the drive specifiers.
var MYdriveSpecifiers = new Array();

// Loop through the available drives using CdromCollection.count.
for (var i = 0; i < Player.cdRomCollection.count; i++){

// For each available drive, add a corresponding item 
// to the MYdriveSpecifiers array. 
    MYdriveSpecifiers[i] = Player.CDRomCollection.item(i).driveSpecifier;
}

// Write the array of drive letter specifiers to the text area.
myText.value = "Drive letters found: " + MYdriveSpecifiers;
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Version<br/>                  | Windows Media Player version 7.0 or later<br/>                               |
| DLL<br/>                      | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cdrom Object**](cdrom-object.md)
</dt> <dt>

[**CdromCollection.count**](cdromcollection-count.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





