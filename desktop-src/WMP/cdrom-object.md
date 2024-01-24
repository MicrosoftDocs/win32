---
title: Cdrom Object
description: The Cdrom object provides a way to access a CD or DVD in its drive.
ms.assetid: 9045b130-3e08-4880-a4e7-79b704c4c1f9
keywords:
- Cdrom Object Windows Media Player
topic_type:
- apiref
api_name:
- Cdrom Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Cdrom Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Cdrom** object provides a way to access a CD or DVD in its drive.

The **Cdrom** object supports the following properties.



| Property                                   | Description                                                                                                                                             |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [driveSpecifier](cdrom-drivespecifier.md) | Retrieves the CD or DVD drive letter.                                                                                                                   |
| [playlist](cdrom-playlist.md)             | Retrieves a [Playlist](playlist-object.md) object representing the tracks on the CD currently in the CD drive or the root-level title entries for DVD. |



 

The **Cdrom** object supports the following method.



| Method                   | Description                          |
|--------------------------|--------------------------------------|
| [eject](cdrom-eject.md) | Ejects the CD or DVD from the drive. |



 

The **Cdrom** object is accessed through the following method.



| Object                                        | Method                           |
|-----------------------------------------------|----------------------------------|
| [CdromCollection](cdromcollection-object.md) | [item](cdromcollection-item.md) |



 

For purposes of illustration, player.cdromCollection.item(*index*) is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




