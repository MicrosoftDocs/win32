---
description: The IDxtKey interface sets properties on the Key transition.This interface is used internally by DirectShow Editing Services (DES) when it renders the Key transition.
ms.assetid: b929bf0c-8aaf-456e-b692-e23d88e480dd
title: IDxtKey interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtKey interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IDxtKey` interface sets properties on the [Key](key-transition.md) transition.

This interface is used internally by DirectShow Editing Services (DES) when it renders the Key transition. DES applications do not need to use this interface. To set the properties on a transition in DES, use the [**IPropertySetter**](ipropertysetter.md) interface.

## Members

The **IDxtKey** interface inherits from **IDXEffect**. **IDxtKey** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDxtKey** interface has these methods.



| Method                                            | Description                                                                            |
|:--------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**get\_Hue**](idxtkey-get-hue.md)               | Retrieves the hue value on which to key.<br/>                                    |
| [**get\_Invert**](idxtkey-get-invert.md)         | Retrieves a Boolean value indicating whether the key operation is inverted.<br/> |
| [**get\_KeyType**](idxtkey-get-keytype.md)       | Retrieves the type of key.<br/>                                                  |
| [**get\_Luminance**](idxtkey-get-luminance.md)   | Retrieves the luminance value on which to key.<br/>                              |
| [**get\_RGB**](idxtkey-get-rgb.md)               | Retrieves the RGB color on which to key.<br/>                                    |
| [**get\_Similarity**](idxtkey-get-similarity.md) | Retrieves the range of color data that becomes transparent.<br/>                 |
| [**put\_Hue**](idxtkey-put-hue.md)               | Specifies the hue value on which to key.<br/>                                    |
| [**put\_Invert**](idxtkey-put-invert.md)         | Specifies whether the key operation is inverted.<br/>                            |
| [**put\_KeyType**](idxtkey-put-keytype.md)       | Specifies the type of key.<br/>                                                  |
| [**put\_Luminance**](idxtkey-put-luminance.md)   | Specifies the luminance value on which to key.<br/>                              |
| [**put\_RGB**](idxtkey-put-rgb.md)               | Specifies the RGB color on which to key.<br/>                                    |
| [**put\_Similarity**](idxtkey-put-similarity.md) | Specifies the range of color data that becomes transparent.<br/>                 |



 

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



 

 




