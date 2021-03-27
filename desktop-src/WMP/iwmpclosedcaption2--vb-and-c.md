---
title: IWMPClosedCaption2 (VB and C ) interface (Wmp.h)
description: Provides properties and methods for closed captioning that supplement the IWMPClosedCaption interface.In addition to the properties inherited from IWMPClosedCaption, the IWMPClosedCaption2 interface exposes the following properties.
ms.assetid: e34ea819-dc1a-48f3-9e55-cf2217379ddb
keywords:
- IWMPClosedCaption2 (VB and C ) interface Windows Media Player
- IWMPClosedCaption2 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPClosedCaption2 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPClosedCaption2 (VB and C#) interface

Provides properties and methods for closed captioning that supplement the **IWMPClosedCaption** interface.

In addition to the properties inherited from **IWMPClosedCaption**, the **IWMPClosedCaption2** interface exposes the following properties.

## Members

The **IWMPClosedCaption2 (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPClosedCaption2 (VB and C#)** interface has these methods.



| Method                                                                                             | Description                                                                                       |
|:---------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**getSAMILangID**](wmplibiwmpclosedcaption2-iwmpclosedcaption2-getsamilangid--vb-and-c.md)       | Returns the locale identifier (LCID) of a language supported by the current SAMI file.<br/> |
| [**getSAMILangName**](wmplibiwmpclosedcaption2-iwmpclosedcaption2-getsamilangname--vb-and-c.md)   | Returns the name of a language supported by the current SAMI file.<br/>                     |
| [**getSAMIStyleName**](wmplibiwmpclosedcaption2-iwmpclosedcaption2-getsamistylename--vb-and-c.md) | Returns the name of a style supported by the current SAMI file.<br/>                        |



 

### Properties

The **IWMPClosedCaption2 (VB and C#)** interface has these properties.



| Property                                                                                                | Access type           | Description                                                                         |
|:--------------------------------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------|
| [**SAMILangCount**](wmplibiwmpclosedcaption2-iwmpclosedcaption2-samilangcount--vb-and-c.md)<br/> | Read/write<br/> | Gets or sets the number of languages supported by the current SAMI file.<br/> |
| [**SAMIStyleCount**](wmplibiwmpclosedcaption2-samistylecount.md)<br/>                            | Read/write<br/> | Gets or sets the number of styles supported by the current SAMI file.<br/>    |



 

Get an **IWMPClosedCaption2** interface by casting the value returned by the [**AxWindowsMediaPlayer.closedCaption**](axwmplib-axwindowsmediaplayer-closedcaption--vb-and-c.md) property.

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

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> </dl>

 

 





