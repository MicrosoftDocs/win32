---
title: IWMPNetwork (VB and C ) interface (Wmp.h)
description: Provides properties and methods to access statistics relating to the quality of a network connection, and to specify and retrieve the network proxy settings.The IWMPNetwork interface exposes the following properties.
ms.assetid: d385510f-11cf-4a2a-96be-b416cddc3d80
keywords:
- IWMPNetwork (VB and C ) interface Windows Media Player
- IWMPNetwork (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPNetwork (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPNetwork (VB and C#) interface

Provides properties and methods to access statistics relating to the quality of a network connection, and to specify and retrieve the network proxy settings.

The **IWMPNetwork** interface exposes the following properties.

## Members

The **IWMPNetwork (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPNetwork (VB and C#)** interface has these methods.



| Method                                                                                           | Description                                                                                                            |
|:-------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**getProxyBypassForLocal**](iwmpnetwork-getproxybypassforlocal--vb-and-c.md)                   | Returns a value indicating whether the proxy server is bypassed if the origin server is on a local network.<br/> |
| [**getProxyExceptionList**](wmplibiwmpnetwork-iwmpnetwork-getproxyexceptionlist--vb-and-c.md)   | Returns the proxy exception list.<br/>                                                                           |
| [**getProxyName**](wmplibiwmpnetwork-iwmpnetwork-getproxyname--vb-and-c.md)                     | Returns the name of the proxy server being used.<br/>                                                            |
| [**getProxyPort**](wmplibiwmpnetwork-iwmpnetwork-getproxyport--vb-and-c.md)                     | Returns the proxy port being used.<br/>                                                                          |
| [**getProxySettings**](wmplibiwmpnetwork-iwmpnetwork-getproxysettings--vb-and-c.md)             | Returns information about the proxy settings for a protocol.<br/>                                                |
| [**setProxyBypassForLocal**](wmplibiwmpnetwork-iwmpnetwork-setproxybypassforlocal--vb-and-c.md) | Specifies whether the proxy server is bypassed if the origin server is on a local network.<br/>                  |
| [**setProxyExceptionList**](wmplibiwmpnetwork-iwmpnetwork-setproxyexceptionlist--vb-and-c.md)   | Specifies the proxy exception list.<br/>                                                                         |
| [**setProxyName**](wmplibiwmpnetwork-iwmpnetwork-setproxyname--vb-and-c.md)                     | Specifies the name of the proxy server to use.<br/>                                                              |
| [**setProxyPort**](wmplibiwmpnetwork-iwmpnetwork-setproxyport--vb-and-c.md)                     | Specifies the proxy port to use.<br/>                                                                            |
| [**setProxySettings**](wmplibiwmpnetwork-iwmpnetwork-setproxysettings--vb-and-c.md)             | Specifies the proxy settings for a protocol.<br/>                                                                |



 

### Properties

The **IWMPNetwork (VB and C#)** interface has these properties.



| Property                                                                                          | Access type           | Description                                                                                  |
|:--------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------|
| [**bandWidth**](wmplibiwmpnetwork-iwmpnetwork-bandwidth--vb-and-c.md)<br/>                 | Read-only<br/>  | Gets the current bandwidth of the media item.<br/>                                     |
| [**bitRate**](wmplibiwmpnetwork-iwmpnetwork-bitrate--vb-and-c.md)<br/>                     | Read-only<br/>  | Gets the current bit rate being received.<br/>                                         |
| [**bufferingCount**](wmplibiwmpnetwork-iwmpnetwork-bufferingcount--vb-and-c.md)<br/>       | Read-only<br/>  | Gets the number of times buffering occurred during playback.<br/>                      |
| [**bufferingProgress**](wmplibiwmpnetwork-iwmpnetwork-bufferingprogress--vb-and-c.md)<br/> | Read-only<br/>  | Gets the percentage of buffering completed.<br/>                                       |
| [**bufferingTime**](wmplibiwmpnetwork-iwmpnetwork-bufferingtime--vb-and-c.md)<br/>         | Read/write<br/> | Gets or sets the amount of buffering time in milliseconds before playback begins.<br/> |
| [**downloadProgress**](wmplibiwmpnetwork-iwmpnetwork-downloadprogress--vb-and-c.md)<br/>   | Read-only<br/>  | Gets the percentage of downloading completed.<br/>                                     |
| [**encodedFrameRate**](wmplibiwmpnetwork-iwmpnetwork-encodedframerate--vb-and-c.md)<br/>   | Read-only<br/>  | Gets the video frame rate specified by the content author.<br/>                        |
| [**frameRate**](wmplibiwmpnetwork-iwmpnetwork-framerate--vb-and-c.md)<br/>                 | Read-only<br/>  | Gets the current video frame rate.<br/>                                                |
| [**framesSkipped**](wmplibiwmpnetwork-iwmpnetwork-framesskipped--vb-and-c.md)<br/>         | Read-only<br/>  | Gets the total number of frames skipped during playback.<br/>                          |
| [**lostPackets**](wmplibiwmpnetwork-iwmpnetwork-lostpackets--vb-and-c.md)<br/>             | Read-only<br/>  | Gets the number of packets lost.<br/>                                                  |
| [**maxBandwidth**](wmplibiwmpnetwork-iwmpnetwork-maxbandwidth--vb-and-c.md)<br/>           | Read/write<br/> | Gets or sets the maximum allowed bandwidth.<br/>                                       |
| [**maxBitRate**](wmplibiwmpnetwork-iwmpnetwork-maxbitrate--vb-and-c.md)<br/>               | Read-only<br/>  | Gets the maximum possible video bit rate.<br/>                                         |
| [**receivedPackets**](wmplibiwmpnetwork-iwmpnetwork-receivedpackets--vb-and-c.md)<br/>     | Read-only<br/>  | Gets the number of packets received.<br/>                                              |
| [**receptionQuality**](wmplibiwmpnetwork-iwmpnetwork-receptionquality--vb-and-c.md)<br/>   | Read-only<br/>  | Gets the percentage of packets not lost in the last 30 seconds.<br/>                   |
| [**recoveredPackets**](wmplibiwmpnetwork-iwmpnetwork-recoveredpackets--vb-and-c.md)<br/>   | Read-only<br/>  | Gets the number of recovered packets.<br/>                                             |
| [**sourceProtocol**](wmplibiwmpnetwork-iwmpnetwork-sourceprotocol--vb-and-c.md)<br/>       | Read-only<br/>  | Gets the source protocol used to receive data.<br/>                                    |



 

Get an **IWMPNetwork** interface by using the following property.



| Object                                                                   | Property                                                           |
|--------------------------------------------------------------------------|--------------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**network**](axwmplib-axwindowsmediaplayer-network--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> </dl>

 

 





