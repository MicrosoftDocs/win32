---
title: DVD Object
description: The DVD object provides properties and methods for working with DVDs.
ms.assetid: '953f6ba5-637b-4f70-aeea-dfe9f52d8675'
keywords:
- DVD Object Windows Media Player
topic_type:
- apiref
api_name:
- DVD Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# DVD Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DVD** object provides properties and methods for working with DVDs.

The **DVD** object supports the following properties.



| Property                           | Description                                                                                        |
|------------------------------------|----------------------------------------------------------------------------------------------------|
| [domain](dvd-domain.md)           | Retrieves the current domain of the DVD.                                                           |
| [isAvailable](dvd-isavailable.md) | Retrieves whether a specified type of information is available or a given action can be performed. |



 

The **DVD** object supports the following methods.



| Method                         | Description                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------|
| [back](dvd-back.md)           | Changes the display from a submenu to its parent menu.                                               |
| [resume](dvd-resume.md)       | Changes to playback mode from menu mode, resuming at the same position as when the menu was invoked. |
| [titleMenu](dvd-titlemenu.md) | Stops playback and displays the title menu.                                                          |
| [topMenu](dvd-topmenu.md)     | Stops playback and displays the root menu.                                                           |



 

The **DVD** object is accessed through the following property.



| Object                      | Property              |
|-----------------------------|-----------------------|
| [Player](player-object.md) | [dvd](player-dvd.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




