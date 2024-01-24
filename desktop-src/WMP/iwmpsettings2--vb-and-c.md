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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings2 (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





