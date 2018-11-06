---
title: Properties, Methods and Events
description: Properties, Methods and Events
ms.assetid: 9426d13b-42db-4a20-81f2-7a849a6e1f33
keywords:
- Windows Media Player,properties for object model
- Windows Media Player,methods for object model
- Windows Media Player,events for object model
- Windows Media Player object model,properties
- Windows Media Player object model,methods
- Windows Media Player object model,events
- object model,properties
- object model,methods
- object model,events
- Windows Media Player ActiveX control,properties for object model
- ActiveX control,properties for object model
- Windows Media Player Mobile ActiveX control,properties for object model
- Windows Media Player Mobile,properties for object model
- Windows Media Player ActiveX control,methods for object model
- ActiveX control,methods for object model
- Windows Media Player Mobile ActiveX control,methods for object model
- Windows Media Player Mobile,methods for object model
- Windows Media Player ActiveX control,events for object model
- ActiveX control,events for object model
- Windows Media Player Mobile ActiveX control,events for object model
- Windows Media Player Mobile,events for object model
- properties,Windows Media Player object model
- methods,Windows Media Player object model
- events,Windows Media Player object model
ms.topic: article
ms.date: 05/31/2018
---

# Properties, Methods and Events

Each object has methods and properties through which you can program the Windows Media Player control. A method is an action that the object can take. A property is a data value that you can read or change. For example, the **Play** method starts the content playing, and the **frameRate** property indicates the current frame rate of the content that is playing.

In addition, the **Player** object raises events that give you the opportunity to carry out actions at specific times. You write code in an event handler that will execute when Windows Media Player raises the corresponding event. For example, you can write code in a **PlayStateChange** event handler that determines whether the change in state is that the media ended and if so display a dialog box asking users if they want to play the media again.

> [!Note]  
> All of the methods in the Windows Media Player object model are asynchronous. If you call two methods in the same procedure, the second method cannot rely on the first method having completed its action.

 

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> </dl>

 

 




