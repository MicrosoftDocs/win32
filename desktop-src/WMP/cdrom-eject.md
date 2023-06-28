---
title: Cdrom.eject method
description: The eject method ejects the CD or DVD from the drive. | Cdrom.eject method
ms.assetid: f43c7f10-7de2-488c-833a-ecd3ac21744b
keywords:
- eject method Windows Media Player
- eject method Windows Media Player , Cdrom class
- Cdrom class Windows Media Player , eject method
topic_type:
- apiref
api_name:
- Cdrom.eject
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Cdrom.eject method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **eject** method ejects the CD or DVD from the drive.

## Syntax


```JScript
Cdrom.eject()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the drive door is open, this method closes the door.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following example creates an HTML button element that uses *Cdrom*.**eject** to open the door of the drive that has drive specifier index zero. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"
       NAME = "EJECTBUTTON"
       VALUE = "EJECT"
       OnClick =  "Player.cdromCollection.item(0).eject()"
>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Version<br/>                  | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>                      | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cdrom Object**](cdrom-object.md)
</dt> <dt>

[**Player.playState**](player-playstate.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





