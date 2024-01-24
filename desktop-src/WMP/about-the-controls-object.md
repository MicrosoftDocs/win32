---
title: About the Controls Object
description: About the Controls Object
ms.assetid: 1678c931-af47-42c9-a8a5-b6b775aebda8
keywords:
- Windows Media Player,Controls object
- Windows Media Player object model,Controls object
- object model,Controls object
- Windows Media Player ActiveX control,Controls object
- ActiveX control,Controls object
- Windows Media Player Mobile ActiveX control,Controls object
- Windows Media Player Mobile,Controls object
- Controls object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Controls Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Controls** object governs the transport of digital media content through the control by using methods such as **Play** and **Stop**. It is accessed only through the **Controls** property of the **Player** object. The **Controls** property returns the **Controls** object. You can only access the properties of the **Controls** object after you have created it. For example, to use the **Play** method, you must use the following code:


```C++
player.controls.play();

```



## Related topics

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




