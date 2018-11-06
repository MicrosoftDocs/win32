---
title: About the Settings Object
description: About the Settings Object
ms.assetid: 941463e6-7928-438e-824e-e5e281421a4a
keywords:
- Windows Media Player,Settings object
- Windows Media Player object model,Settings object
- object model,Settings object
- Windows Media Player ActiveX control,Settings object
- ActiveX control,Settings object
- Windows Media Player Mobile ActiveX control,Settings object
- Windows Media Player Mobile,Settings object
- Settings object
ms.topic: article
ms.date: 05/31/2018
---

# About the Settings Object

The **Settings** object governs the settings of the control such as volume, play count, mute, and so on. It is accessed only through the **Settings** property of the **Player** object. The **Settings** property returns the **Settings** object. You can only access the properties of the **Settings** object after you have created it. For example, to get the value of the **Volume** property, you must use the following code:


```C++
myvolume = player.settings.volume;

```



## Related topics

<dl> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 




