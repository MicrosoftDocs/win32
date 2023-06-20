---
title: Supported Protocols and File Types
description: Supported Protocols and File Types
ms.assetid: 2672372c-0b42-437e-8b96-83b6e5200fd3
keywords:
- Windows Media Player,protocols
- Windows Media Player,file types
- Windows Media Player object model,protocols
- Windows Media Player object model,file types
- object model,protocols
- object model,file types
- Windows Media Player ActiveX control,protocols for object model
- ActiveX control,protocols for object model
- Windows Media Player Mobile ActiveX control,protocols for object model
- Windows Media Player Mobile,protocols for object model
- Windows Media Player ActiveX control,file types for object model
- ActiveX control,file types for object model
- Windows Media Player Mobile ActiveX control,file types for object model
- Windows Media Player Mobile,file types for object model
- protocols,Windows Media Player object model
- file types for Windows Media Player object model
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Supported Protocols and File Types

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player supports several protocols and many file types, all of which can be used when specifying URL values in the Player object model for properties such as *Player*.**URL** or in Windows Media metafile playlists. Additionally, the supported protocols can be used when specifying protocol values with the proxy-related methods of the **Network** object.

The following digital media file formats are currently supported for playback by Windows Media Player:

-   Advanced Systems Format (ASF)
-   AIF
-   AIFC
-   AIFF
-   AU
-   AVI
-   MID
-   MPE
-   MPEG
-   MPG
-   MPv2
-   MP2
-   MP3
-   M1V
-   SND
-   WAV
-   Windows Media files with a .wm file name extension
-   Windows Media Audio (WMA)
-   Windows Media Video (WMV)

The following protocols are currently supported by Windows Media Player.



| Protocol | Description                                                                        |
|----------|------------------------------------------------------------------------------------|
| HTTP     | Hypertext Transfer Protocol. Includes HTTP with fast cache and multicast.          |
| RTSP     | Real Time Streaming Protocol. Includes RTSP with fast cache.                       |
| RTSPU    | RTSP used with User Datagram Protocol (UDP). Includes RTSPU with fast cache        |
| RTSPT    | RTSP used with Transmission Control Protocol (TCP). Includes RTSPT with fast cache |
| MMS      | Microsoft Media Server protocol.                                                   |
| MMSU     | MMS used with UDP.                                                                 |
| MMST     | MMS used with TCP.                                                                 |
| WMPCD    | A protocol used by Windows Media Player to provide access to CDs.                  |
| WMPDVD   | A protocol used by Windows Media Player to provide access to DVDs.                 |



 

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**WMPCD Protocol**](wmpcd-protocol.md)
</dt> <dt>

[**WMPDVD Protocol**](wmpdvd-protocol.md)
</dt> </dl>

 

 




