---
title: IWMPControls (VB and C ) interface (Wmp.h)
description: Provides a way to manipulate the playback of a media item by representing the transport controls of Windows Media Player, such as Play, Stop, and Pause.The IWMPControls interface exposes the following properties.
ms.assetid: 46603d98-c7dd-4c20-a4ae-1472b3af8d52
keywords:
- IWMPControls (VB and C ) interface Windows Media Player
- IWMPControls (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPControls (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls (VB and C#) interface

Provides a way to manipulate the playback of a media item by representing the transport controls of Windows Media Player, such as Play, Stop, and Pause.

The **IWMPControls** interface exposes the following properties.

## Members

The **IWMPControls (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPControls (VB and C#)** interface has these methods.



| Method                                                                       | Description                                                                                 |
|:-----------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**fastForward**](wmplibiwmpcontrols-iwmpcontrols-fastforward--vb-and-c.md) | Starts fast play of the media item in the forward direction.<br/>                     |
| [**fastReverse**](wmplibiwmpcontrols-iwmpcontrols-fastreverse--vb-and-c.md) | Starts fast play of the media item in the reverse direction.<br/>                     |
| [**next**](wmplibiwmpcontrols-iwmpcontrols-next--vb-and-c.md)               | Sets the next item in the playlist as the current item.<br/>                          |
| [**pause**](wmplibiwmpcontrols-iwmpcontrols-pause--vb-and-c.md)             | Pauses playback of the media item.<br/>                                               |
| [**play**](wmplibiwmpcontrols-iwmpcontrols-play--vb-and-c.md)               | Begins playback of the current media item, or resumes playback of a paused item.<br/> |
| [**playItem**](wmplibiwmpcontrols-iwmpcontrols-playitem--vb-and-c.md)       | Plays the specified media item.<br/>                                                  |
| [**previous**](wmplibiwmpcontrols-iwmpcontrols-previous--vb-and-c.md)       | Sets the previous item in the playlist as the current item.<br/>                      |
| [**stop**](wmplibiwmpcontrols-iwmpcontrols-stop--vb-and-c.md)               | Stops playback of the media item.<br/>                                                |



 

### Properties

The **IWMPControls (VB and C#)** interface has these properties.



| Property                                                                                                    | Access type           | Description                                                                                                                                                                      |
|:------------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**currentItem**](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md)<br/>                     | Read/write<br/> | Gets or sets the current media item in a playlist.<br/>                                                                                                                    |
| [**currentMarker**](wmplibiwmpcontrols-iwmpcontrols-currentmarker--vb-and-c.md)<br/>                 | Read/write<br/> | Gets or sets the current marker number.<br/>                                                                                                                               |
| [**currentPosition**](wmplibiwmpcontrols-iwmpcontrols-currentposition--vb-and-c.md)<br/>             | Read/write<br/> | Gets or sets the current position in the media item in seconds from the beginning.<br/>                                                                                    |
| [**currentPositionString**](wmplibiwmpcontrols-iwmpcontrols-currentpositionstring--vb-and-c.md)<br/> | Read-only<br/>  | Gets the current position in the media item as a **System.String**.<br/>                                                                                                   |
| [**isAvailable**](iwmpcontrols-isavailable--vb-and-c.md)<br/>                                        | Read-only<br/>  | Gets a value indicating whether a specified type of information is available or a specified action can be performed. In C#, this is the **get\_isAvailable** method.<br/> |



 

Get an **IWMPControls** interface by using the following property.



| Object                                                                   | Property                                                                   |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**Ctlcontrols**](axwmplib-axwindowsmediaplayer-ctlcontrols--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPControls2 Interface (VB and C#)**](iwmpcontrols2--vb-and-c.md)
</dt> <dt>

[**IWMPControls3 Interface (VB and C#)**](iwmpcontrols3--vb-and-c.md)
</dt> </dl>

 

 





