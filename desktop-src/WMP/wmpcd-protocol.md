---
title: WMPCD Protocol
description: WMPCD Protocol
ms.assetid: 385cfb03-88cc-400c-a2b9-174008ebd854
keywords:
- Windows Media Player,protocols
- Windows Media Player object model,protocols
- object model,protocols
- Windows Media Player ActiveX control,protocols for object model
- ActiveX control,protocols for object model
- Windows Media Player Mobile ActiveX control,protocols for object model
- Windows Media Player Mobile,protocols for object model
- protocols,Windows Media Player object model
- protocols,WMPCD
- WMPCD protocol
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMPCD Protocol

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The WMPCD protocol enables you to specify tracks on a compact disc using URL syntax. This is the general syntax of the protocol:


```C++
wmpcd://drive/track
```



The *drive* segment is the index of the CD drive. The *track* segment is the number of the track. The following example demonstrates using the WMPCD protocol.


```C++
player.url = "wmpcd://0/4";
```



The example plays the fourth track on the disc in the first CD drive (the drive whose index is 0).

## Related topics

<dl> <dt>

[**Supported Protocols and File Types**](supported-protocols-and-file-types.md)
</dt> </dl>

 

 




