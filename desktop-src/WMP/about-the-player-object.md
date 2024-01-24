---
title: About the Player Object
description: About the Player Object
ms.assetid: db995e75-d4e3-4f50-a34a-cc1b2f2c5db5
keywords:
- Windows Media Player,Player object
- Windows Media Player object model,Player object
- object model,Player object
- Windows Media Player ActiveX control,Player object
- ActiveX control,Player object
- Windows Media Player Mobile ActiveX control,Player object
- Windows Media Player Mobile,Player object
- Player object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Player Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Player** object is the core object for the Windows Media Player control. All other related objects are connected to this object through specific properties that return the object. For example, the **Settings** object is accessed through the **settings** property. The **Player** object provides methods, properties, and events that relate to the core functionality of Windows Media Player.

Because this reference is also to be used for skins programming, the ID of the **Player** object will be "player" for syntax examples.

Using the **player** global attribute within a skin definition file gives access to the **Player** object for use in scripting. Through the **Player** object, all other objects in the Windows Media Player control become accessible to scripts as well. The events of the **Player** object and the **URL** property can also be specified at design time using the [PLAYER](player-element.md) skin element. For more information, see [Windows Media Player Skins](windows-media-player-skins.md).

## Related topics

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




