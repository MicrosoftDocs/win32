---
title: IWMPControls3 (VB and C ) interface (Wmp.h)
description: Provides properties and methods for audio language selection and support that supplement the IWMPControls2 interface.In addition to the properties and methods inherited from IWMPControls2, the IWMPControls3 interface exposes the following properties.
ms.assetid: 1f42a352-da97-4382-9b59-a9b074aa2a5a
keywords:
- IWMPControls3 (VB and C ) interface Windows Media Player
- IWMPControls3 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPControls3 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPControls3 (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides properties and methods for audio language selection and support that supplement the **IWMPControls2** interface.

In addition to the properties and methods inherited from **IWMPControls2**, the **IWMPControls3** interface exposes the following properties.

## Members

The **IWMPControls3 (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPControls3 (VB and C#)** interface has these methods.



| Method                                                                                                         | Description                                                                                               |
|:---------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**getAudioLanguageDescription**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguagedescription--vb-and-c.md) | Returns the description for the audio language corresponding to the specified one-based index.<br/> |
| [**getAudioLanguageID**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguageid--vb-and-c.md)                   | Returns the LCID for a specified audio language index.<br/>                                         |
| [**getLanguageName**](wmplibiwmpcontrols3-iwmpcontrols3-getlanguagename--vb-and-c.md)                         | Returns the name of the audio language with the specified LCID.<br/>                                |



 

### Properties

The **IWMPControls3 (VB and C#)** interface has these properties.



| Property                                                                                                              | Access type           | Description                                                                                                                                         |
|:----------------------------------------------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**audioLanguageCount**](wmplibiwmpcontrols3-iwmpcontrols3-audiolanguagecount--vb-and-c.md)<br/>               | Read-only<br/>  | Gets the count of supported audio languages. <br/>                                                                                            |
| [**currentAudioLanguage**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguage--vb-and-c.md)<br/>           | Read/write<br/> | Gets or sets the locale identifier (LCID) of the audio language for playback. <br/>                                                           |
| [**currentAudioLanguageIndex**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguageindex--vb-and-c.md)<br/> | Read/write<br/> | Gets or sets the one-based index that corresponds to the audio language for playback. <br/>                                                   |
| [**currentPositionTimecode**](wmplibiwmpcontrols3-iwmpcontrols3-currentpositiontimecode--vb-and-c.md)<br/>     | Read/write<br/> | Gets or sets the current position in the current media item using a time code format. This property currently supports SMPTE time code. <br/> |



 

Get an **IWMPControls3** interface by casting the value returned by the [**AxWindowsMediaPlayer.Ctlcontrols**](axwmplib-axwindowsmediaplayer-ctlcontrols--vb-and-c.md) property.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPControls2 Interface (VB and C#)**](iwmpcontrols2--vb-and-c.md)
</dt> </dl>

 

 





