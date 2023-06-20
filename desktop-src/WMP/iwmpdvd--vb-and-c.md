---
title: IWMPDVD (VB and C ) interface (Wmp.h)
description: The IWMPDVD interface provides properties and methods for working with DVDs.The IWMPDVD interface exposes the following properties.
ms.assetid: 6bb32eed-475e-4867-8318-34578dc430a4
keywords:
- IWMPDVD (VB and C ) interface Windows Media Player
- IWMPDVD (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPDVD (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPDVD (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMPDVD** interface provides properties and methods for working with DVDs.

The **IWMPDVD** interface exposes the following properties.

## Members

The **IWMPDVD (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPDVD (VB and C#)** interface has these methods.



| Method                                                         | Description                                                                                                     |
|:---------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**back**](wmplibiwmpdvd-iwmpdvd-back--vb-and-c.md)           | Changes the display from a submenu to its parent menu.<br/>                                               |
| [**resume**](wmplibiwmpdvd-iwmpdvd-resume--vb-and-c.md)       | Changes to playback mode from menu mode, resuming at the same position as when the menu was invoked.<br/> |
| [**titleMenu**](wmplibiwmpdvd-iwmpdvd-titlemenu--vb-and-c.md) | Stops playback and displays the title menu.<br/>                                                          |
| [**topMenu**](wmplibiwmpdvd-iwmpdvd-topmenu--vb-and-c.md)     | Stops playback and displays the root menu.<br/>                                                           |



 

### Properties

The **IWMPDVD (VB and C#)** interface has these properties.



| Property                                                            | Access type          | Description                                                                                                                                                                          |
|:--------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**domain**](wmplibiwmpdvd-iwmpdvd-domain--vb-and-c.md)<br/> | Read-only<br/> | Gets the current domain of the DVD.<br/>                                                                                                                                       |
| [**isAvailable**](iwmpdvd-isavailable--vb-and-c.md)<br/>     | Read-only<br/> | Gets a value that indicates whether a specified type of information is available or a specified action can be performed. In C#, this is the **get\_isAvailable** method.<br/> |



 

Get an **IWMPDVD** interface by using the following property.



| Object                                                                   | Property                                                   |
|--------------------------------------------------------------------------|------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**dvd**](axwmplib-axwindowsmediaplayer-dvd--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> </dl>

 

 





