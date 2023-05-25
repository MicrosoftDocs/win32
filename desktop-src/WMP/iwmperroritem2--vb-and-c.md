---
title: IWMPErrorItem2 (VB and C ) interface (Wmp.h)
description: Provides a property for getting an error condition code.
ms.assetid: 0393cebd-88c0-4bfd-8890-4c456ec19b57
keywords:
- IWMPErrorItem2 (VB and C ) interface Windows Media Player
- IWMPErrorItem2 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPErrorItem2 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPErrorItem2 (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a property for getting an error condition code.

In addition to the properties inherited from **IWMPErrorItem**, the **IWMPErrorItem2** interface exposes the following property.



| Property                                                                 | Description                                          |
|--------------------------------------------------------------------------|------------------------------------------------------|
| [condition](wmplibiwmperroritem2-iwmperroritem2-condition--vb-and-c.md) | Gets a value indicating the condition for the error. |



 

Get an **IWMPErrorItem2** interface by casting the value returned by the **Item** property (in C#, the **get\_Item method**) of the **IWMPErrorItem** interface.

## Members

The **IWMPErrorItem2 (VB and C#)** interface does not define any members.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmperroritem)
</dt> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> </dl>

 

 





