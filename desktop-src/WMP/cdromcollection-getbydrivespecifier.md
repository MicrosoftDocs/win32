---
title: CdromCollection.getByDriveSpecifier method
description: The getByDriveSpecifier method retrieves the Cdrom object associated with a particular drive letter.
ms.assetid: 60626ffc-3d10-435b-8827-c5d7b6e02607
keywords:
- getByDriveSpecifier method Windows Media Player
- getByDriveSpecifier method Windows Media Player , CdromCollection class
- CdromCollection class Windows Media Player , getByDriveSpecifier method
topic_type:
- apiref
api_name:
- CdromCollection.getByDriveSpecifier
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CdromCollection.getByDriveSpecifier method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getByDriveSpecifier** method retrieves the **Cdrom** object associated with a particular drive letter.

## Syntax


```JScript
retVal = CdromCollection.getByDriveSpecifier(
  driveSpecifier
)
```



## Parameters

<dl> <dt>

*driveSpecifier* \[in\]
</dt> <dd>

**String** containing the drive letter followed by a colon (":") character.

</dd> </dl>

## Return value

This method returns a **Cdrom** object.

## Remarks

Drive letters must be given in the form *X*:, where *X* represents the drive letter.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *CdromCollection*.**getByDriveSpecifier** to retrieve the **Cdrom** object that corresponds to a drive letter provided by the user. An HTML text element was created, with NAME = "MyText", for user input. The **Player** object was created with ID = "Player".


```JScript
// Store the drive letter provided by the user.
var DriveLetter = MyText.value;

// Append a colon to the drive letter to create a valid drive specifier.
DriveLetter += ":";

// Get the Cdrom object using the drive specifier.
var Drive = Player.cdRomCollection.getByDriveSpecifier(DriveLetter);

// Use the Cdrom object to open the drive door.
Drive.eject();
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cdrom Object**](cdrom-object.md)
</dt> <dt>

[**Cdrom.eject**](cdrom-eject.md)
</dt> <dt>

[**CdromCollection Object**](cdromcollection-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





