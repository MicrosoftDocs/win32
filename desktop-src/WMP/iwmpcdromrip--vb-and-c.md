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
ms.date: 05/31/2018
---

# IWMPCdromRip (VB and C#) interface

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

 

 





