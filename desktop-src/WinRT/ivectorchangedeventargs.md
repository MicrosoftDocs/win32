---
description: Describes the **IVectorChangedEventArgs** interface, and documents its members, methods, and requirements.
ms.assetid: 635c0f96-5d64-436e-9186-78f9d85b6d29
title: IVectorChangedEventArgs interface (IVectorChangedEventArgs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVectorChangedEventArgs
api_type: 
- COM
api_location: 
- IVectorChangedEventArgs.h
---

# IVectorChangedEventArgs interface

Provides data for a [**VectorChanged**](/uwp/api/windows.foundation.collections.iobservablevector-1) event.

## Members

The **IVectorChangedEventArgs** interface inherits from **IInspectable**. **IVectorChangedEventArgs** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVectorChangedEventArgs** interface has these methods.



| Method                                                                        | Description                                                           |
|:------------------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**get\_CollectionChange**](ivectorchangedeventargs-get-collectionchange.md) | Gets the type of change that occurred in the vector.<br/>       |
| [**get\_Index**](ivectorchangedeventargs-get-index.md)                       | Gets the position in the vector where the change occurred.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Header<br/>                   | <dl> <dt>IVectorChangedEventArgs.h</dt> </dl> |



 

 
