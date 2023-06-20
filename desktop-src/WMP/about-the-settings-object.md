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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Settings Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




