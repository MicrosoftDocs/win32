---
title: About the ClosedCaption Object
description: About the ClosedCaption Object
ms.assetid: f536c062-fcf6-4ada-b485-6deeb4dd4d9d
keywords:
- Windows Media Player,ClosedCaption object
- Windows Media Player object model,ClosedCaption object
- object model,ClosedCaption object
- Windows Media Player ActiveX control,ClosedCaption object
- ActiveX control,ClosedCaption object
- Windows Media Player Mobile ActiveX control,ClosedCaption object
- Windows Media Player Mobile,ClosedCaption object
- ClosedCaption object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the ClosedCaption Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ClosedCaption** object governs the captioning interface for Windows Media Player. The **ClosedCaption** object is obtained through the **closedCaption** property of the **Player** object. For example, to get the **SAMIFileName** property value, type the following:


```C++
myfile = player.closedcaption.SAMIFileName;

```



## Related topics

<dl> <dt>

[**ClosedCaption Object**](closedcaption-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




