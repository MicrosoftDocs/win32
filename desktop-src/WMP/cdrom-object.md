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
ms.date: 05/31/2018
api_location: 
---

# Cdrom Object

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

 

 




