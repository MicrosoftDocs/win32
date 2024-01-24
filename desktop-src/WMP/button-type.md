---
title: Button Type
description: Button Type
ms.assetid: 0c9e72d5-5cc4-4d6f-b184-2c8c8487e366
keywords:
- Windows Media Player Mobile skins,button types
- skins,button types
- reference for skins,buttons
- buttons in skins,types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Button Type

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Buttons come in two general types: location and region. Each general type has three specific types, making six button types in all.

> [!Note]  
> Buttons types are deprecated in skins for Windows Media Player 10 Mobile or later.

 

Location Button Types

Location buttons use coordinates to define their locations relative to the background. The following table shows the values that are valid for location button types. You do not need to define values for types you will not be using in your skin.



| Value  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Push   | Defines a button that triggers an event once. The button must be pushed each time to trigger further events. An example would be a button that moves to the next item in the playlist. The location of the button is defined by its coordinates.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Toggle | Defines a button that triggers an event that changes a state. The state remains until the button is pushed again. An example is a button that shuffles the playlist. Once the playlist is in a shuffled state, it will remain shuffled until the button is pushed again. The location of the button is defined by its coordinates.                                                                                                                                                                                                                                                                                                                                                           |
| 2Push  | Defines a button that triggers an event, and then changes to a state that is ready to trigger a different event. The two states are toggled every time the button is pushed. An example is a button that uses the **PlayPause** function to toggle between playing and pausing the current media item. When the button is pushed the first time, the primary Play state is triggered and a secondary image is displayed to indicate that a **Pause** event can be triggered. When the button is pushed again, the Pause state is triggered and the original image is displayed to indicate that a **Play** event can be triggered. The location of the button is defined by its coordinates. |



 

Region Button Types

Region buttons use color areas in the Region image to define where taps will be processed for a particular button. The following table shows the values that are valid for region button types. You do not need to define values for types you will not be using in your skin.



| Value     | Description                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------|
| PushHit   | Similar to the Push button value except that the hit area of the button is defined by the color value in the Region image.   |
| ToggleHit | Similar to the Toggle button value except that the hit area of the button is defined by the color value in the Region image. |
| 2PushHit  | Similar to the 2Push button value except that the hit area of the button is defined by the color value in the Region image.  |



 

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




