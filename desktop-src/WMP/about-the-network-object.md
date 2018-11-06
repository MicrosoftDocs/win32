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
ms.date: 05/31/2018
---

# About the Network Object

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

 

 




