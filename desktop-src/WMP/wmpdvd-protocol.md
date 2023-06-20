---
title: WMPDVD Protocol
description: WMPDVD Protocol
ms.assetid: 01f38c9a-3ce5-4cd4-91a7-248f542eed03
keywords:
- Windows Media Player,protocols
- Windows Media Player object model,protocols
- object model,protocols
- Windows Media Player ActiveX control,protocols for object model
- ActiveX control,protocols for object model
- Windows Media Player Mobile ActiveX control,protocols for object model
- Windows Media Player Mobile,protocols for object model
- protocols,Windows Media Player object model
- protocols,WMPDVD
- WMPDVD protocol
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMPDVD Protocol

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The WMPDVD protocol enables you to specify media from a DVD using URL syntax. This is the general form of the protocol:


```C++
wmpdvd://drive/title/chapter?contentdir=path
```



The *drive* segment is the letter of the DVD drive; it does not include the colon typically used with drive specifiers. This segment is always required.

The *title* segment is the number of the title to play. It is not required unless you want to start playback at a specific title or at a specific chapter of a specific title.

The *chapter* segment is the number of the chapter to play. It is not required unless you want to start playback at a specific chapter of a specific title.

The contentdir argument is the path to a VIDEO\_TS.IFO file, which may be in local storage or on a network share. If you include this segment, then the *drive* segment is ignored although it is still required. If you also include the *title* segment or both the *title* and *chapter* segments then they are relative to the DVD content specified in the contentdir segment, not the *drive* segment.

The following example uses the WMPDVD protocol to play the DVD from the beginning, as if it were starting automatically.


```C++
player.url = "wmpdvd://F";
```



The following example uses the WMPDVD protocol to play the DVD from the beginning of the specified title.


```C++
player.url = "wmpdvd://F/2";
```



The following example uses the WMPDVD protocol to play the DVD from the specified chapter.


```C++
player.url = "wmpdvd://F/2/4";
```



The following example uses the WMPDVD protocol to play DVD content from local storage. The *path* string ends with the folder that contains the VIDEO\_TS.IFO file; it does not include the file name. In this example, the value of the *drive* segment has no effect although it is required, and playback begins in chapter 4 of title 2.


```C++
player.url = "wmpdvd://Z/2/4?contentdir="d:\sample1\video_ts";
```



Assigning a WMPDVD string to the **url** property requires Windows Media Player 9 Series or later.

## Related topics

<dl> <dt>

[**Supported Protocols and File Types**](supported-protocols-and-file-types.md)
</dt> </dl>

 

 




