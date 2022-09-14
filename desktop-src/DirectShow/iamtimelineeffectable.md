---
description: The IAMTimelineEffectable interface provides methods for adding effects to a timeline object in DirectShow Editing Services (DES), and for manipulating the effects on an object.
ms.assetid: 70f2da64-e16a-4d4d-9522-042b5fa2855c
title: IAMTimelineEffectable interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineEffectable
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineEffectable interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineEffectable` interface provides methods for adding effects to a timeline object in [DirectShow Editing Services](directshow-editing-services.md) (DES), and for manipulating the effects on an object. All objects that can have effects applied to them implement this interface; this includes sources, tracks, and compositions.

An object that implements this interface can have any number of effects. For each object, the render engine applies its effects in order of priority, starting with priority level 0.

## Members

The **IAMTimelineEffectable** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineEffectable** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineEffectable** interface has these methods.



| Method                                                                     | Description                                                                   |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**EffectGetCount**](iamtimelineeffectable-effectgetcount.md)             | Retrieves the number of effects on this object.<br/>                    |
| [**EffectInsBefore**](iamtimelineeffectable-effectinsbefore.md)           | Inserts an effect into the object at the specified priority level.<br/> |
| [**EffectSwapPriorities**](iamtimelineeffectable-effectswappriorities.md) | Switches the priority levels of two effects.<br/>                       |
| [**GetEffect**](iamtimelineeffectable-geteffect.md)                       | Retrieves the effect at the specified priority level.<br/>              |



 

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



 

 
