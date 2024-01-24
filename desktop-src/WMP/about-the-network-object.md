---
title: About the Network Object
description: About the Network Object
ms.assetid: 367a51d4-2db8-4c9e-82b7-85b2b631c721
keywords:
- Windows Media Player,Network object
- Windows Media Player object model,Network object
- object model,Network object
- Windows Media Player ActiveX control,Network object
- ActiveX control,Network object
- Windows Media Player Mobile ActiveX control,Network object
- Windows Media Player Mobile,Network object
- Network object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Network Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Network** object governs the properties that allow you to determine how well the content is streaming through the network. For example, you can find out whether packets are being lost and take appropriate action. The **Network** object is accessed only through the **network** property of the **Player** object. The **network** property returns the **Network** object. You can only access the properties of the **Network** object after you have created it. For example, to use the **Bandwidth** property, you must use the following code:


```C++
mybandwidth = player.network.bandwidth;

```



## Related topics

<dl> <dt>

[**Network Object**](network-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




