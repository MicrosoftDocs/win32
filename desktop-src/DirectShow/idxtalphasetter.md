---
description: The IDxtAlphaSetter interface sets properties on the Alpha Setter effect.This interface is used internally by DirectShow Editing Services (DES) when it renders the Alpha Setter effect.
ms.assetid: 9f0439b9-55d2-4526-ae4c-64ab90e11a64
title: IDxtAlphaSetter interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtAlphaSetter
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtAlphaSetter interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IDxtAlphaSetter` interface sets properties on the [Alpha Setter](alpha-setter-effect.md) effect.

This interface is used internally by DirectShow Editing Services (DES) when it renders the Alpha Setter effect. DES applications do not have to use this interface. To set the properties on a transition in DES, use the [**IPropertySetter**](ipropertysetter.md) interface.

## Members

The **IDxtAlphaSetter** interface inherits from **IDXEffect**. **IDxtAlphaSetter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDxtAlphaSetter** interface has these methods.



| Method                                                  | Description                                                |
|:--------------------------------------------------------|:-----------------------------------------------------------|
| [**get\_Alpha**](idxtalphasetter-get-alpha.md)         | Retrieves the alpha value for the entire image.<br/> |
| [**get\_AlphaRamp**](idxtalphasetter-get-alpharamp.md) | Retrieves the alpha ramp property.<br/>              |
| [**put\_Alpha**](idxtalphasetter-put-alpha.md)         | Specifies the alpha value for the entire image.<br/> |
| [**put\_AlphaRamp**](idxtalphasetter-put-alpharamp.md) | Specifies the alpha ramp property.<br/>              |



 

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



 

 




