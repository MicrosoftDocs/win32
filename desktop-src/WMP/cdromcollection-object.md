---
title: CdromCollection Object
description: The CdromCollection object provides a way to organize and access a collection of CD or DVD drives.
ms.assetid: 02429ba7-a053-42bf-9ed5-c05e13c964c0
keywords:
- CdromCollection Object Windows Media Player
topic_type:
- apiref
api_name:
- CdromCollection Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# CdromCollection Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CdromCollection** object provides a way to organize and access a collection of CD or DVD drives.

The **CdromCollection** object supports the following property.



| Property                           | Description                                                        |
|------------------------------------|--------------------------------------------------------------------|
| [count](cdromcollection-count.md) | Retrieves the number of available CD and DVD drives on the system. |



 

The **CdromCollection** object supports the following methods.



| Method                                                         | Description                                                                               |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [getByDriveSpecifier](cdromcollection-getbydrivespecifier.md) | Retrieves the [Cdrom](cdrom-object.md) object associated with a particular drive letter. |
| [item](cdromcollection-item.md)                               | Retrieves the [Cdrom](cdrom-object.md) object at the given index.                        |



 

The **CdromCollection** object is accessed through the following property.



| Object                      | Property                                      |
|-----------------------------|-----------------------------------------------|
| [Player](player-object.md) | [cdromCollection](player-cdromcollection.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




