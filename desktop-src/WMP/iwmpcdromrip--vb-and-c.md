---
title: IWMPCdromRip (VB and C ) interface (Wmp.h)
description: Provides properties and methods to manage copying, or ripping, tracks from an audio CD.Ripping a CD by using the IWMPCdromRip interface has the same effect as ripping music by using the Windows Media Player user interface.
ms.assetid: d7fbfc68-61b5-45bf-8df5-e3125a51a4d8
keywords:
- IWMPCdromRip (VB and C ) interface Windows Media Player
- IWMPCdromRip (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPCdromRip (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromRip (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides properties and methods to manage copying, or *ripping*, tracks from an audio CD.

Ripping a CD by using the **IWMPCdromRip** interface has the same effect as ripping music by using the Windows Media Player user interface. Ripped content is automatically added to the library according to the user's preferences. For more information about user preferences for CD ripping, see "Ripping music from CDs" in Windows Media Player Help.

The **IWMPCdromRip** interface exposes the following properties.

## Members

The **IWMPCdromRip (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPCdromRip (VB and C#)** interface has these methods.



| Method                                                                 | Description                              |
|:-----------------------------------------------------------------------|:-----------------------------------------|
| [**startRip**](wmplibiwmpcdromrip-iwmpcdromrip-startrip--vb-and-c.md) | Rips the CD.<br/>                  |
| [**stopRip**](wmplibiwmpcdromrip-iwmpcdromrip-stoprip--vb-and-c.md)   | Stops the CD ripping process.<br/> |



 

### Properties

The **IWMPCdromRip (VB and C#)** interface has these properties.



| Property                                                                                | Access type          | Description                                                                                   |
|:----------------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------|
| [**ripProgress**](wmplibiwmpcdromrip-iwmpcdromrip-ripprogress--vb-and-c.md)<br/> | Read-only<br/> | Gets the CD ripping progress as percent complete.<br/>                                  |
| [**ripState**](wmplibiwmpcdromrip-iwmpcdromrip-ripstate--vb-and-c.md)<br/>       | Read-only<br/> | Gets an enumeration value that indicates the current state of the ripping process.<br/> |



 

Get an **IWMPCdromRip** interface by casting the **IWMPCdrom** interface of the CD that you wish to rip.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> </dl>

 

 





