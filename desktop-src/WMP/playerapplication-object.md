---
title: PlayerApplication Object
description: The PlayerApplication object provides a way to coordinate switching between a remoted Windows Media Player control and the full mode of Windows Media Player.
ms.assetid: '904bb30c-939d-4aeb-ba4b-c27afee471ea'
keywords:
- PlayerApplication Object Windows Media Player
topic_type:
- apiref
api_name:
- PlayerApplication Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PlayerApplication Object

The **PlayerApplication** object provides a way to coordinate switching between a remoted Windows Media Player control and the full mode of Windows Media Player. This object is used only with C++ programs that implement the **IWMPRemoteMediaServices** interface and embed the Player control in remote mode. Skin files used as custom interfaces for the remoted Windows Media Player control access this object in script code through the **playerApplication** global attribute.

The **PlayerApplication** object supports the following properties.



| Property                                           | Description                                                                                              |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [hasDisplay](playerapplication-hasdisplay.md)     | Retrieves a value indicating whether video can display through the remoted Windows Media Player control. |
| [playerDocked](playerapplication-playerdocked.md) | Retrieves a value indicating whether Windows Media Player is in a docked state.                          |



 

The **PlayerApplication** object supports the following methods.



| Method                                                                       | Description                                                                     |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [switchToControl](playerapplication-switchtocontrol.md)                     | Switches a remoted Windows Media Player control to the docked state.            |
| [switchToPlayerApplication](playerapplication-switchtoplayerapplication.md) | Switches a remoted Windows Media Player control to the full mode of the Player. |



 

The **PlayerApplication** object is accessed through the following property.



| Object                      | Property                                          |
|-----------------------------|---------------------------------------------------|
| [Player](player-object.md) | [playerApplication](player-playerapplication.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 




