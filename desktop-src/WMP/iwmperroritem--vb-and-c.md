---
title: IWMPErrorItem (VB and C ) interface (Wmp.h)
description: Provides access to error information.
ms.assetid: 7f1571e1-4e3a-4f06-b9fa-9add34266537
keywords:
- IWMPErrorItem (VB and C ) interface Windows Media Player
- IWMPErrorItem (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPErrorItem (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPErrorItem (VB and C#) interface

Provides access to error information.

The **IWMPErrorItem** interface exposes the following properties.



| Property                                                                             | Description                                                                                |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [customUrl](wmplibiwmperroritem-iwmperroritem-customurl--vb-and-c.md)               | Gets the URL of a website that displays specific information about codec download failure. |
| [errorCode](wmplibiwmperroritem-iwmperroritem-errorcode--vb-and-c.md)               | Gets the current error code.                                                               |
| [errorContext](wmplibiwmperroritem-iwmperroritem-errorcontext--vb-and-c.md)         | Gets a value indicating the context of the error.                                          |
| [errorDescription](wmplibiwmperroritem-iwmperroritem-errordescription--vb-and-c.md) | Gets a description of the error.                                                           |
| [remedy](wmplibiwmperroritem-iwmperroritem-remedy--vb-and-c.md)                     | Reserved for future use.                                                                   |



 

Get an **IWMPErrorItem** interface using the following property.



| Interface                            | Property                                                                   |
|--------------------------------------|----------------------------------------------------------------------------|
| [IWMPError](iwmperror--vb-and-c.md) | [Item](iwmperror-item--vb-and-c.md) (in C# use the **get\_Item** method) |



 

## Members

The **IWMPErrorItem (VB and C#)** interface does not define any members.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPErrorItem2 Interface (VB and C#)**](iwmperroritem2--vb-and-c.md)
</dt> </dl>

 

 





