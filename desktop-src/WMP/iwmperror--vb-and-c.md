---
title: IWMPError (VB and C ) interface (Wmp.h)
description: Provides properties and methods for accessing a collection of IWMPErrorItem interfaces for retrieving error information.The IWMPError interface exposes the following properties.
ms.assetid: c7d9f834-43ed-40a2-95a3-b1633f025118
keywords:
- IWMPError (VB and C ) interface Windows Media Player
- IWMPError (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPError (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPError (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides properties and methods for accessing a collection of **IWMPErrorItem** interfaces for retrieving error information.

The **IWMPError** interface exposes the following properties.

## Members

The **IWMPError (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPError (VB and C#)** interface has these methods.



| Method                                                                         | Description                                                                                                                                   |
|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**clearErrorQueue**](wmplibiwmperror-iwmperror-clearerrorqueue--vb-and-c.md) | Clears the errors from the error queue.<br/>                                                                                            |
| [**webHelp**](wmplibiwmperror-iwmperror-webhelp--vb-and-c.md)                 | Launches the Microsoft Windows Media Player Web Help page to display further information about the first error in the error queue.<br/> |



 

### Properties

The **IWMPError (VB and C#)** interface has these properties.



| Property                                                                        | Access type           | Description                                                                                                                         |
|:--------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**errorCount**](wmplibiwmperror-iwmperror-errorcount--vb-and-c.md)<br/> | Read-only<br/>  | Gets the number of errors in the error queue.<br/>                                                                            |
| [**Item**](iwmperror-item--vb-and-c.md)<br/>                             | Read/write<br/> | Gets an **IWMPErrorItem** interface at the specified index in the error queue. In C#, this is the **get\_Item** method.<br/> |



 

Get an **IWMPError** interface by using the following property.



| Object                                                                   | Property                                                       |
|--------------------------------------------------------------------------|----------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**Error**](axwmplib-axwindowsmediaplayer-error--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> </dl>

 

 





