---
description: The IAMTimelineSplittable interface splits a timeline object in DirectShow Editing Services (DES). Sources, effects, transitions, and tracks implement this interface.
ms.assetid: bb066d34-0ffd-495f-83ce-59ad054a7782
title: IAMTimelineSplittable interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSplittable
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSplittable interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineSplittable` interface splits a timeline object in [DirectShow Editing Services](directshow-editing-services.md) (DES). Sources, effects, transitions, and tracks implement this interface.

## Members

The **IAMTimelineSplittable** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineSplittable** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineSplittable** interface has these methods.



| Method                                             | Description                                                                                          |
|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**SplitAt**](iamtimelinesplittable-splitat.md)   | Splits the object at the specified time.<br/>                                                  |
| [**SplitAt2**](iamtimelinesplittable-splitat2.md) | Splits the object at the specified time, specified as a [**REFTIME**](reftime.md) value.<br/> |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 
