---
title: IWMPSettings2 (VB and C ) interface (Wmp.h)
description: Provides properties and a method that supplement the IWMPSettings interface.In addition to the properties and methods inherited from IWMPSettings, the IWMPSettings2 interface exposes the following properties.
ms.assetid: 6bd0f6dd-df49-4c21-b47c-c8c63f85c2c0
keywords:
- IWMPSettings2 (VB and C ) interface Windows Media Player
- IWMPSettings2 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPSettings2 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings2 (VB and C#) interface

Provides properties and a method that supplement the **IWMPSettings** interface.

In addition to the properties and methods inherited from **IWMPSettings**, the **IWMPSettings2** interface exposes the following properties.

## Members

The **IWMPSettings2 (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPSettings2 (VB and C#)** interface has these methods.



| Method                                                                                                   | Description                                                     |
|:---------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| [**requestMediaAccessRights**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md) | Requests a specified level of access to the library.<br/> |



 

### Properties

The **IWMPSettings2 (VB and C#)** interface has these properties.



| Property                                                                                                    | Access type          | Description                                                                               |
|:------------------------------------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------|
| [**defaultAudioLanguage**](wmplibiwmpsettings2-iwmpsettings2-defaultaudiolanguage--vb-and-c.md)<br/> | Read-only<br/> | Gets the locale identifier (LCID) of the default audio language. <br/>              |
| [**mediaAccessRights**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)<br/>       | Read-only<br/> | Gets a value indicating the permissions currently granted for library access. <br/> |



 

Get an **IWMPSettings2** interface by casting the value returned by the **AxWindowsMediaPlayer.settings** property.



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

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





