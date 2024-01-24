---
title: Working with the Player
description: Working with the Player
ms.assetid: 27aff735-2142-4506-b9d0-2c0fbe60fd6b
keywords:
- Windows Media Player skins,player attribute in JScript
- skins,player attribute in JScript
- attributes,player
- player attribute
- JScript files for skins,player attribute
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with the Player

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When using Microsoft JScript to access methods and properties of Windows Media Player, you must use the name "player" for the name of the control. For example, to reference the Stop method, you must type:


```C++
player.Controls.Stop()

```



The **player** global attribute is the key to accessing the Windows Media Player control through skin scripting. Through this attribute, all the objects of the Windows Media Player control become accessible for run-time modification through their properties and methods. Additionally, the **PLAYER** element is available so that you can specify event handlers and the **url** attribute at design time.

## Related topics

<dl> <dt>

[**Using JScript**](using-jscript.md)
</dt> </dl>

 

 




