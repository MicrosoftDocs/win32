---
title: About the PlayerApplication Object
description: About the PlayerApplication Object
ms.assetid: 4b77bf16-d7e1-4119-91c2-46136db13e81
keywords:
- Windows Media Player,PlayerApplication object
- Windows Media Player object model,PlayerApplication object
- object model,PlayerApplication object
- Windows Media Player ActiveX control,PlayerApplication object
- ActiveX control,PlayerApplication object
- Windows Media Player Mobile ActiveX control,PlayerApplication object
- Windows Media Player Mobile,PlayerApplication object
- PlayerApplication object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the PlayerApplication Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PlayerApplication** object is used for remoting Windows Media Player. It provides the functionality required to switch between a remoted Windows Media Player control and the full mode of the Player.

Remoting enables a Windows Media Player control embedded in a C++ application to use the same playback engine as the Player. This means that usually you will use the **PlayerApplication** object in C++ code using the COM interfaces. There is a special case, however, where you can embed the Windows Media Player control that displays a Windows Media Player skin as its user interface. In this case, **PlayerApplication** can be programmed using JScript in the skin code.

## Related topics

<dl> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> <dt>

[**PlayerApplication Object**](playerapplication-object.md)
</dt> </dl>

 

 




