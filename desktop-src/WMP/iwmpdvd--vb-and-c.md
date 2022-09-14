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
ms.date: 05/31/2018
---

# IWMPDVD (VB and C#) interface

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

 

 





