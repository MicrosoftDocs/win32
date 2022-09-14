---
title: IWMPSettings (VB and C ) interface (Wmp.h)
description: Provides properties and methods that get or set the values of Windows Media Player settings.The IWMPSettings interface exposes the following properties.
ms.assetid: fb37b455-221e-4cee-a219-cacf2938a92a
keywords:
- IWMPSettings (VB and C ) interface Windows Media Player
- IWMPSettings (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPSettings (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings (VB and C#) interface

Provides properties and methods that get or set the values of Windows Media Player settings.

The **IWMPSettings** interface exposes the following properties.

## Members

The **IWMPSettings (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPSettings (VB and C#)** interface has these methods.



| Method                                                               | Description                                                                        |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**getMode**](wmplibiwmpsettings-iwmpsettings-getmode--vb-and-c.md) | Returns a value indicating whether loop mode or shuffle mode is active.<br/> |
| [**setMode**](wmplibiwmpsettings-iwmpsettings-setmode--vb-and-c.md) | Sets the loop mode or shuffle mode to active or inactive.<br/>               |



 

### Properties

The **IWMPSettings (VB and C#)** interface has these properties.



| Property                                                                                              | Access type           | Description                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**autoStart**](wmplibiwmpsettings-iwmpsettings-autostart--vb-and-c.md)<br/>                   | Read/write<br/> | Gets or sets a value indicating whether the current media item begins playing automatically. <br/>                                     |
| [**balance**](wmplibiwmpsettings-iwmpsettings-balance--vb-and-c.md)<br/>                       | Read/write<br/> | Gets or sets the current stereo balance.<br/>                                                                                          |
| [**baseURL**](wmplibiwmpsettings-iwmpsettings-baseurl--vb-and-c.md)<br/>                       | Read/write<br/> | Gets or sets the base URL used for relative path resolution with URL script commands that are embedded in digital media content. <br/> |
| [**defaultFrame**](wmplibiwmpsettings-iwmpsettings-defaultframe--vb-and-c.md)<br/>             | Read/write<br/> | Gets or sets the name of the frame used to display a URL that is received in a **scriptCommand** event. <br/>                          |
| [**enableErrorDialogs**](wmplibiwmpsettings-iwmpsettings-enableerrordialogs--vb-and-c.md)<br/> | Read/write<br/> | Gets or sets a value indicating whether error dialog boxes are displayed automatically.<br/>                                           |
| [**invokeURLs**](wmplibiwmpsettings-iwmpsettings-invokeurls--vb-and-c.md)<br/>                 | Read/write<br/> | Gets or sets a value indicating whether URL events should launch a Web browser. <br/>                                                  |
| [**isAvailable**](iwmpsettings-isavailable--vb-and-c.md)<br/>                                  | Read-only<br/>  | Gets a value indicating whether a specified action can be performed. In C#, this is the **get\_isAvailable** method.<br/>             |
| [**mute**](wmplibiwmpsettings-iwmpsettings-mute--vb-and-c.md)<br/>                             | Read/write<br/> | Gets or sets a value indicating whether audio is muted. <br/>                                                                          |
| [**playCount**](wmplibiwmpsettings-iwmpsettings-playcount--vb-and-c.md)<br/>                   | Read/write<br/> | Gets or sets the number of times a media item will play. <br/>                                                                         |
| [**rate**](wmplibiwmpsettings-iwmpsettings-rate--vb-and-c.md)<br/>                             | Read/write<br/> | Gets or sets the current playback rate for video. <br/>                                                                                |
| [**volume**](wmplibiwmpsettings-iwmpsettings-volume--vb-and-c.md)<br/>                         | Read/write<br/> | Gets or sets the current playback volume. <br/>                                                                                        |



 

Get an **IWMPSettings** interface by using the following property.



| Object                                                                   | Property                                                             |
|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**settings**](axwmplib-axwindowsmediaplayer-settings--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPSettings2 Interface (VB and C#)**](iwmpsettings2--vb-and-c.md)
</dt> </dl>

 

 





