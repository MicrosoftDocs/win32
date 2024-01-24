---
title: IWMPClosedCaption (VB and C ) interface (Wmp.h)
description: Provides a way to include captions with a digital media file. The captioning text is in a Synchronized Accessible Media Interchange (SAMI) file.
ms.assetid: 927f6fe4-5847-439e-9df0-19cc910d887d
keywords:
- IWMPClosedCaption (VB and C ) interface Windows Media Player
- IWMPClosedCaption (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPClosedCaption (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPClosedCaption (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a way to include captions with a digital media file. The captioning text is in a Synchronized Accessible Media Interchange (SAMI) file.

## Members

The **IWMPClosedCaption (VB and C#)** interface does not define any members.

The **IWMPClosedCaption** interface exposes the following properties.



| Property                                                                             | Description                                                                                |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [captioningId](wmplibiwmpclosedcaption-iwmpclosedcaption-captioningid--vb-and-c.md) | Gets or sets the name of the HTML element displaying the captioning.                       |
| [SAMIFileName](wmplibiwmpclosedcaption-iwmpclosedcaption-samifilename--vb-and-c.md) | Gets or sets the name of the file containing the information needed for closed captioning. |
| [SAMILang](wmplibiwmpclosedcaption-iwmpclosedcaption-samilang--vb-and-c.md)         | Gets or sets the language displayed for closed captioning.                                 |
| [SAMIStyle](wmplibiwmpclosedcaption-iwmpclosedcaption-samistyle--vb-and-c.md)       | Gets or sets the closed captioning style.                                                  |



 

Get an **IWMPClosedCaption** interface by using the following property.



| Object                                                            | Property                                                                   |
|-------------------------------------------------------------------|----------------------------------------------------------------------------|
| [AxWindowsMediaPlayer](axwindowsmediaplayer-object--vb-and-c.md) | [closedCaption](axwmplib-axwindowsmediaplayer-closedcaption--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> </dl>

 

 





