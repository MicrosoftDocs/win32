---
title: IWMPCdromCollection (VB and C ) interface (Wmp.h)
description: Provides a way to organize and access a collection of CD or DVD drives.The IWMPCdromCollection interface exposes the following property.
ms.assetid: 60874603-d9c8-4ed1-a92a-bd069bd0c253
keywords:
- IWMPCdromCollection (VB and C ) interface Windows Media Player
- IWMPCdromCollection (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPCdromCollection (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromCollection (VB and C#) interface

Provides a way to organize and access a collection of CD or DVD drives.

The **IWMPCdromCollection** interface exposes the following property.

## Members

The **IWMPCdromCollection (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPCdromCollection (VB and C#)** interface has these methods.



| Method                                                                                                     | Description                                                                              |
|:-----------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**getByDriveSpecifier**](wmplibiwmpcdromcollection-iwmpcdromcollection-getbydrivespecifier--vb-and-c.md) | Returns an **IWMPCdrom** interface associated with a particular drive letter.<br/> |
| [**Item**](wmplibiwmpcdromcollection-iwmpcdromcollection-item--vb-and-c.md)                               | Returns an **IWMPCdrom** interface at the given index.<br/>                        |



 

### Properties

The **IWMPCdromCollection (VB and C#)** interface has these properties.



| Property                                                                                  | Access type          | Description                                                              |
|:------------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------|
| [**count**](wmplibiwmpcdromcollection-iwmpcdromcollection-count--vb-and-c.md)<br/> | Read-only<br/> | Gets the number of available CD and DVD drives on the system.<br/> |



 

Get an **IWMPCdromCollection** interface by using the following property.



| Object                                                                   | Property                                                                           |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**cdromCollection**](axwmplib-axwindowsmediaplayer-cdromcollection--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPCdrom Interface (VB and C#)**](iwmpcdrom--vb-and-c.md)
</dt> </dl>

 

 





