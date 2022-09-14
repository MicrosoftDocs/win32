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
ms.date: 05/31/2018
---

# Working with the Player

When using Microsoft JScript to access methods and properties of Windows Media Player, you must use the name "player" for the name of the control. For example, to reference the Stop method, you must type:


```C++
player.Controls.Stop()

```



The **player** global attribute is the key to accessing the Windows Media Player control through skin scripting. Through this attribute, all the objects of the Windows Media Player control become accessible for run-time modification through their properties and methods. Additionally, the **PLAYER** element is available so that you can specify event handlers and the **url** attribute at design time.

## Related topics

<dl> <dt>

[**Using JScript**](using-jscript.md)
</dt> </dl>

 

 




