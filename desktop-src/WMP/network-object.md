---
title: Network Object
description: The Network object provides properties and methods used to access statistics relating to the quality of a network connection, and to specify and retrieve the network proxy settings.
ms.assetid: '5ae6137e-22f5-4a65-8793-b6f66adb4cba'
keywords:
- Network Object Windows Media Player
topic_type:
- apiref
api_name:
- Network Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Network Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Network** object provides properties and methods used to access statistics relating to the quality of a network connection, and to specify and retrieve the network proxy settings.

The **Network** object supports the following properties.



| Property                                           | Description                                                                                 |
|----------------------------------------------------|---------------------------------------------------------------------------------------------|
| [bandWidth](network-bandwidth.md)                 | Retrieves the current bandwidth of the media item.                                          |
| [bitRate](network-bitrate.md)                     | Retrieves the current bit rate being received.                                              |
| [bufferingCount](network-bufferingcount.md)       | Retrieves the number of times buffering occurred during playback.                           |
| [bufferingProgress](network-bufferingprogress.md) | Retrieves the percentage of buffering completed.                                            |
| [bufferingTime](network-bufferingtime.md)         | Specifies or retrieves the amount of buffering time in milliseconds before playback begins. |
| [downloadProgress](network-downloadprogress.md)   | Retrieves the percentage of download completed.                                             |
| [encodedFrameRate](network-encodedframerate.md)   | Retrieves the video frame rate specified by the content author.                             |
| [frameRate](network-framerate.md)                 | Retrieves the current video frame rate.                                                     |
| [framesSkipped](network-framesskipped.md)         | Retrieves the total number of frames skipped during playback.                               |
| [lostPackets](network-lostpackets.md)             | Retrieves the number of packets lost.                                                       |
| [maxBandwidth](network-maxbandwidth.md)           | Specifies or retrieves the maximum allowed bandwidth.                                       |
| [maxBitRate](network-maxbitrate.md)               | Retrieves the maximum possible video bit rate.                                              |
| [receivedPackets](network-receivedpackets.md)     | Retrieves the number of packets received.                                                   |
| [receptionQuality](network-receptionquality.md)   | Retrieves the percentage of packets received in the last 30 seconds.                        |
| [recoveredPackets](network-recoveredpackets.md)   | Retrieves the number of recovered packets.                                                  |
| [sourceProtocol](network-sourceprotocol.md)       | Retrieves the source protocol used to receive data.                                         |



 

The **Network** object supports the following methods.



| Method                                                       | Description                                                                                                          |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [getProxyBypassForLocal](network-getproxybypassforlocal.md) | Retrieves a value indicating whether the proxy server should by bypassed if the origin server is on a local network. |
| [getProxyExceptionList](network-getproxyexceptionlist.md)   | Retrieves the proxy exception list.                                                                                  |
| [getProxyName](network-getproxyname.md)                     | Retrieves the name of a proxy server to use.                                                                         |
| [getProxyPort](network-getproxyport.md)                     | Retrieves the proxy port to use.                                                                                     |
| [getProxySettings](network-getproxysettings.md)             | Retrieves the proxy setting for a given protocol.                                                                    |
| [setProxyBypassForLocal](network-setproxybypassforlocal.md) | Specifies a value indicating whether the proxy server should by bypassed if the origin server is on a local network. |
| [setProxyExceptionList](network-setproxyexceptionlist.md)   | Specifies the proxy exception list.                                                                                  |
| [setProxyName](network-setproxyname.md)                     | Specifies the name of a proxy server to use.                                                                         |
| [setProxyPort](network-setproxyport.md)                     | Specifies the proxy port to use.                                                                                     |
| [setProxySettings](network-setproxysettings.md)             | Specifies the proxy setting for a given protocol.                                                                    |



 

The **Network** object is accessed through the following property.



| Object                      | Property                      |
|-----------------------------|-------------------------------|
| [Player](player-object.md) | [network](player-network.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




